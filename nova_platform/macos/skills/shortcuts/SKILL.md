---
name: shortcuts
description: Run macOS Shortcuts.app shortcuts to automate tasks on macOS.
version: 1.0.0
author: Nova Team
triggers:
  - shortcut
  - shortcuts app
  - run shortcut
  - automation
requirements:
  bins: [shortcuts]
os: [darwin]
---

# macOS Shortcuts

Run Shortcuts.app shortcuts to automate tasks on macOS (Monterey and later).

## Setup

No installation required - `shortcuts` CLI is built into macOS Monterey+.

## List Available Shortcuts

```bash
shortcuts list
```

## Run a Shortcut

```bash
# Basic execution
shortcuts run "Shortcut Name"

# With input
shortcuts run "Process Text" --input "Some text to process"

# With output capture
shortcuts run "Get Data" --output
```

## Using the shortcuts Tool

```json
// Run a shortcut
{"name": "My Shortcut", "input": "text input", "output": true}

// Without output capture
{"name": "Background Task", "output": false}
```

## Common Use Cases

- Text processing shortcuts
- File management automation
- API calls and web requests
- System automation
- Data transformation

## Notes

- macOS Monterey (12.0) or later required
- Shortcuts must be created in Shortcuts.app first
- Input/output depends on shortcut configuration
- Some shortcuts may require user interaction