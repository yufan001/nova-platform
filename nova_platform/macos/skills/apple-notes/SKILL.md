---
name: apple-notes
description: Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes).
version: 1.0.0
author: Nova Team
triggers:
  - apple notes
  - notes app
  - memo
  - create note
  - search notes
requirements:
  bins: [memo]
os: [darwin]
---

# Apple Notes CLI

Use `memo notes` to manage Apple Notes directly from the terminal. Create, view, edit, delete, search, move notes between folders, and export to HTML/Markdown.

## Setup

- Install (Homebrew): `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo`
- macOS-only; if prompted, grant Automation access to Notes.app.

## Common Operations

### View Notes

```bash
# List all notes
memo notes

# Filter by folder
memo notes -f "Folder Name"

# Search notes (fuzzy)
memo notes -s "query"
```

### Create Notes

```bash
# Add a new note (opens interactive editor)
memo notes -a

# Quick add with title
memo notes -a "Note Title"
```

### Edit Notes

```bash
# Edit existing note (interactive selection)
memo notes -e
```

### Delete Notes

```bash
# Delete a note (interactive selection)
memo notes -d
```

### Move Notes

```bash
# Move note to folder (interactive selection)
memo notes -m
```

### Export Notes

```bash
# Export to HTML/Markdown
memo notes -ex
```

## Limitations

- Cannot edit notes containing images or attachments
- Interactive prompts may require terminal access

## Notes

- macOS-only
- Requires Apple Notes.app to be accessible
- For automation, grant permissions in System Settings > Privacy & Security > Automation