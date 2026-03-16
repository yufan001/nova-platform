---
name: things-mac
description: Manage Things 3 via the `things` CLI on macOS (add/update projects+todos via URL scheme; read/search/list from the local Things database).
version: 1.0.0
author: Nova Team
triggers:
  - things
  - things 3
  - todo
  - task
  - project
requirements:
  bins: [things]
os: [darwin]
---

# Things 3 CLI

Use `things` to read your local Things database (inbox/today/search/projects/areas/tags) and to add/update todos via the Things URL scheme.

## Setup

- Install: `GOBIN=/opt/homebrew/bin go install github.com/ossianhempel/things3-cli/cmd/things@latest`
- If DB reads fail: grant **Full Disk Access** to the calling app
- Optional: set `THINGSDB` to point at your ThingsData folder
- Optional: set `THINGS_AUTH_TOKEN` for update operations

## Read Operations (Database)

```bash
# View inbox
things inbox --limit 50

# View today
things today

# View upcoming
things upcoming

# Search tasks
things search "query"

# List projects/areas/tags
things projects
things areas
things tags
```

## Write Operations (URL Scheme)

```bash
# Add a basic todo
things add "Buy milk"

# Add with notes
things add "Buy milk" --notes "2% + bananas"

# Add to a project/area
things add "Book flights" --list "Travel"

# Add with tags
things add "Call dentist" --tags "health,phone"

# Add with due date
things add "Submit report" --deadline 2026-01-15

# Preview without executing
things --dry-run add "Test task"
```

## Modify Operations (Requires Auth Token)

```bash
# Get task ID first
things search "milk" --limit 5

# Update title
things update --id <UUID> --auth-token <TOKEN> "New title"

# Update notes
things update --id <UUID> --auth-token <TOKEN> --notes "New notes"

# Complete a task
things update --id <UUID> --auth-token <TOKEN> --completed
```

## Notes

- macOS-only
- Use `--dry-run` to preview URL scheme operations
- Delete not supported by CLI; use Things UI or mark as completed