"""macOS platform tools for Nova."""

from __future__ import annotations

import asyncio
import json
import shutil
import subprocess
from typing import Any

from nova.tools.base import Tool, ToolParameter, ToolResult


class AppleScriptTool(Tool):
    """Execute AppleScript commands on macOS."""
    
    name = "applescript"
    description = "Execute AppleScript commands to control macOS applications and system features"
    parameters = [
        ToolParameter(
            name="script",
            type="string",
            description="AppleScript code to execute",
            required=True,
        ),
        ToolParameter(
            name="application",
            type="string",
            description="Target application name (e.g., 'Finder', 'Safari')",
            required=False,
        ),
    ]
    
    async def execute(self, script: str, application: str | None = None) -> ToolResult:
        """Execute AppleScript and return the result."""
        if not shutil.which("osascript"):
            return ToolResult(
                success=False,
                error="osascript not found. This tool only works on macOS.",
            )
        
        # Wrap script with application tell block if specified
        if application:
            full_script = f'tell application "{application}"\n{script}\nend tell'
        else:
            full_script = script
        
        try:
            proc = await asyncio.create_subprocess_exec(
                "osascript", "-e", full_script,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await proc.communicate()
            
            if proc.returncode != 0:
                return ToolResult(
                    success=False,
                    error=stderr.decode().strip() or "AppleScript execution failed",
                )
            
            result = stdout.decode().strip()
            return ToolResult(success=True, result=result)
        except Exception as e:
            return ToolResult(success=False, error=str(e))


class MacOSNotifyTool(Tool):
    """Send macOS system notifications."""
    
    name = "macos_notify"
    description = "Send system notifications on macOS"
    parameters = [
        ToolParameter(
            name="title",
            type="string",
            description="Notification title",
            required=True,
        ),
        ToolParameter(
            name="message",
            type="string",
            description="Notification body text",
            required=True,
        ),
        ToolParameter(
            name="sound",
            type="string",
            description="Notification sound name (e.g., 'default', 'Glass', 'Ping')",
            required=False,
        ),
    ]
    
    async def execute(
        self, title: str, message: str, sound: str = "default"
    ) -> ToolResult:
        """Send a macOS notification."""
        script = f'''
        display notification "{message}" with title "{title}" sound name "{sound}"
        '''
        
        try:
            proc = await asyncio.create_subprocess_exec(
                "osascript", "-e", script,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await proc.communicate()
            
            if proc.returncode != 0:
                return ToolResult(
                    success=False,
                    error=stderr.decode().strip() or "Failed to send notification",
                )
            
            return ToolResult(
                success=True,
                result=f"Notification sent: {title}",
            )
        except Exception as e:
            return ToolResult(success=False, error=str(e))


class ShortcutsTool(Tool):
    """Run macOS Shortcuts."""
    
    name = "shortcuts"
    description = "Run Shortcuts.app shortcuts on macOS"
    parameters = [
        ToolParameter(
            name="name",
            type="string",
            description="Name of the shortcut to run",
            required=True,
        ),
        ToolParameter(
            name="input",
            type="string",
            description="Input string to pass to the shortcut",
            required=False,
        ),
        ToolParameter(
            name="output",
            type="boolean",
            description="Whether to capture and return the output",
            required=False,
        ),
    ]
    
    async def execute(
        self, name: str, input: str | None = None, output: bool = True
    ) -> ToolResult:
        """Run a macOS shortcut."""
        if not shutil.which("shortcuts"):
            return ToolResult(
                success=False,
                error="shortcuts CLI not found. Requires macOS Monterey or later.",
            )
        
        cmd = ["shortcuts", "run", name]
        if input:
            cmd.extend(["--input", input])
        if output:
            cmd.append("--output")
        
        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await proc.communicate()
            
            if proc.returncode != 0:
                return ToolResult(
                    success=False,
                    error=stderr.decode().strip() or f"Shortcut '{name}' failed",
                )
            
            result = stdout.decode().strip() if output else f"Shortcut '{name}' executed"
            return ToolResult(success=True, result=result)
        except Exception as e:
            return ToolResult(success=False, error=str(e))


class ImessageTool(Tool):
    """Send and manage iMessages."""
    
    name = "imessage"
    description = "Send iMessages and manage message conversations on macOS"
    parameters = [
        ToolParameter(
            name="action",
            type="string",
            description="Action to perform: send, list, search",
            required=True,
            enum=["send", "list", "search"],
        ),
        ToolParameter(
            name="recipient",
            type="string",
            description="Phone number or email for send action",
            required=False,
        ),
        ToolParameter(
            name="message",
            type="string",
            description="Message content for send action",
            required=False,
        ),
        ToolParameter(
            name="query",
            type="string",
            description="Search query for search action",
            required=False,
        ),
        ToolParameter(
            name="limit",
            type="integer",
            description="Maximum number of results for list/search",
            required=False,
        ),
    ]
    
    async def execute(
        self,
        action: str,
        recipient: str | None = None,
        message: str | None = None,
        query: str | None = None,
        limit: int = 20,
    ) -> ToolResult:
        """Execute iMessage action."""
        # Check for imsg CLI (optional, falls back to AppleScript)
        imsg_available = shutil.which("imsg")
        
        if action == "send":
            if not recipient or not message:
                return ToolResult(
                    success=False,
                    error="recipient and message required for send action",
                )
            
            if imsg_available:
                # Use imsg CLI if available
                try:
                    proc = await asyncio.create_subprocess_exec(
                        "imsg", "send", recipient, message,
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE,
                    )
                    stdout, stderr = await proc.communicate()
                    
                    if proc.returncode != 0:
                        return ToolResult(
                            success=False,
                            error=stderr.decode().strip() or "Failed to send message",
                        )
                    
                    return ToolResult(
                        success=True,
                        result=f"Message sent to {recipient}",
                    )
                except Exception as e:
                    return ToolResult(success=False, error=str(e))
            else:
                # Fall back to AppleScript
                script = f'''
                tell application "Messages"
                    send "{message}" to buddy "{recipient}"
                end tell
                '''
                tool = AppleScriptTool()
                return await tool.execute(script)
        
        elif action == "list":
            if imsg_available:
                try:
                    proc = await asyncio.create_subprocess_exec(
                        "imsg", "list", "--limit", str(limit),
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE,
                    )
                    stdout, stderr = await proc.communicate()
                    
                    if proc.returncode != 0:
                        return ToolResult(
                            success=False,
                            error=stderr.decode().strip() or "Failed to list messages",
                        )
                    
                    return ToolResult(success=True, result=stdout.decode().strip())
                except Exception as e:
                    return ToolResult(success=False, error=str(e))
            else:
                return ToolResult(
                    success=False,
                    error="imsg CLI required for list action. Install with: brew install imsg",
                )
        
        elif action == "search":
            if not query:
                return ToolResult(
                    success=False,
                    error="query required for search action",
                )
            
            if imsg_available:
                try:
                    proc = await asyncio.create_subprocess_exec(
                        "imsg", "search", query, "--limit", str(limit),
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE,
                    )
                    stdout, stderr = await proc.communicate()
                    
                    if proc.returncode != 0:
                        return ToolResult(
                            success=False,
                            error=stderr.decode().strip() or "Search failed",
                        )
                    
                    return ToolResult(success=True, result=stdout.decode().strip())
                except Exception as e:
                    return ToolResult(success=False, error=str(e))
            else:
                return ToolResult(
                    success=False,
                    error="imsg CLI required for search action",
                )
        
        return ToolResult(success=False, error=f"Unknown action: {action}")


def register_tools() -> list[type[Tool]]:
    """Register macOS tools with Nova."""
    return [
        AppleScriptTool,
        MacOSNotifyTool,
        ShortcutsTool,
        ImessageTool,
    ]