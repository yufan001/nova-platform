# Nova Platform

Platform-specific tools and skills for [Nova](https://github.com/yufan001/nova) AI agent.

## Structure

```
nova-platform/
├── macos/           # macOS-specific tools and skills
│   ├── tools/       # AppleScript, iMessage, Shortcuts, etc.
│   └── skills/      # Apple Notes, Things 3, Reminders, etc.
├── windows/         # Windows-specific tools and skills
│   ├── tools/       # PowerShell, WSL, etc.
│   └── skills/      # Windows Terminal, etc.
├── linux/           # Linux-specific tools and skills
│   ├── tools/       # systemd, dbus, etc.
│   └── skills/      # Linux desktop automation
└── mobile/          # Mobile platform tools
    ├── android/     # ADB extended tools
    └── ios/         # iOS Shortcuts integration
```

## Installation

```bash
# Install with platform-specific extras
pip install nova-platform[macos]    # macOS
pip install nova-platform[windows]  # Windows
pip install nova-platform[linux]    # Linux
```

## macOS Tools

| Tool | Description |
|------|-------------|
| `applescript` | Execute AppleScript commands |
| `imessage` | Send/receive iMessages |
| `macos_notify` | System notifications |
| `shortcuts` | Run Shortcuts.app shortcuts |

## macOS Skills

| Skill | Description | Required CLI |
|-------|-------------|--------------|
| `apple-notes` | Manage Apple Notes | `memo` |
| `things-mac` | Manage Things 3 tasks | `things` |
| `apple-reminders` | Manage Apple Reminders | `remindctl` |
| `imessage` | iMessage automation | `imsg` |
| `shortcuts` | Run macOS Shortcuts | Built-in |

## Usage

Tools and skills are automatically discovered by Nova when this package is installed.

## License

MIT