# Nova Platform

Platform-specific skills for [Nova](https://github.com/yufan001/nova) AI agent framework.

## Structure

```
nova-platform/
├── macos/           # macOS-specific skills
│   └── skills/      # 12 skills for Apple ecosystem
├── windows/         # Windows-specific (coming soon)
├── linux/           # Linux-specific (coming soon)
└── mobile/          # Mobile platforms (coming soon)
```

## Installation

```bash
pip install git+https://github.com/yufan001/nova-platform.git
```

## macOS Skills (12 total)

| Skill | Description | Requirements |
|-------|-------------|--------------|
| `apple-notes` | Manage Apple Notes app | `memo` CLI or AppleScript |
| `apple-reminders` | Manage Apple Reminders | `remindctl` CLI or AppleScript |
| `things-mac` | Manage Things 3 tasks | `things3-cli` |
| `imessage` | iMessage automation | `imsg` CLI or BlueBubbles |
| `bluebubbles` | BlueBubbles iMessage extension | BlueBubbles server |
| `bear-notes` | Bear notes management | Bear app |
| `shortcuts` | Run macOS Shortcuts | Built-in Shortcuts.app |
| `canvas` | Canvas control for Nova | Nova desktop app |
| `spotify-player` | Spotify control | `spotify` CLI |
| `sonoscli` | Sonos speaker control | `sonoscli` |
| `camsnap` | Camera capture | macOS camera access |
| `peekaboo` | Screen peek/monitor | Screen recording permission |

### Requirements

Most macOS skills require:

1. **Full Disk Access** - Grant to Terminal/your app
2. **AppleScript permissions** - Granted automatically on first use
3. **CLI tools** - Install via Homebrew:

```bash
# Apple Notes
brew install memo

# Things 3
brew install things3-cli

# Apple Reminders
brew install remindctl

# iMessage (alternative: BlueBubbles)
brew install imsg

# Sonos
brew install sonoscli

# Spotify
brew install spotify-tui
```

### BlueBubbles Setup (Recommended for iMessage)

BlueBubbles provides a more robust iMessage integration:

1. Install BlueBubbles server on your Mac
2. Configure the server URL and password
3. The `bluebubbles` skill supports:
   - Send/receive messages
   - Reactions (tapbacks)
   - Edit/unsend messages
   - Reply to specific messages

## Configuration

Nova automatically discovers platform skills via Python entry points. No manual configuration required!

To verify skills are loaded:

```python
from nova_platform.macos.skills import register_skills
print(f"Loaded {len(register_skills())} macOS skills")
```

## Windows & Linux

Coming soon! Contributions welcome.

## License

MIT License - see [LICENSE](LICENSE)