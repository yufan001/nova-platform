---
name: imessage
description: Send and manage iMessages via CLI or AppleScript on macOS.
version: 1.0.0
author: Nova Team
triggers:
  - imessage
  - send message
  - text message
  - sms
requirements:
  bins: [imsg]
os: [darwin]
---

# iMessage

Send and manage iMessages on macOS using the `imsg` CLI or AppleScript fallback.

## Setup

### Option 1: imsg CLI (Recommended)

```bash
# Install via Homebrew
brew install imsg

# Grant Full Disk Access to Terminal (required for reading messages)
# System Settings > Privacy & Security > Full Disk Access
```

### Option 2: AppleScript (Fallback)

No installation required, but limited functionality:
- Can only send messages
- Cannot read or list messages

## Send Messages

```bash
# Using imsg CLI
imsg send "+1234567890" "Hello from Nova!"

# Using AppleScript (via applescript tool)
# tell application "Messages" to send "Hello" to buddy "+1234567890"
```

## List Conversations

```bash
# List recent chats
imsg list

# Limit results
imsg list --limit 20
```

## Search Messages

```bash
# Search by content
imsg search "keyword"

# Search with limit
imsg search "meeting" --limit 10
```

## Using the imessage Tool

The `imessage` tool provides a unified interface:

```json
// Send a message
{"action": "send", "recipient": "+1234567890", "message": "Hello!"}

// List recent messages
{"action": "list", "limit": 20}

// Search messages
{"action": "search", "query": "keyword", "limit": 10}
```

## Notes

- macOS-only
- imsg CLI requires Full Disk Access for read operations
- AppleScript fallback only supports sending
- Messages sync via iCloud to iPhone/iPad