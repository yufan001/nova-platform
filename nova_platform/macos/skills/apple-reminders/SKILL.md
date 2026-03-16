---
name: apple-reminders
description: Manage Apple Reminders via remindctl CLI (list, add, edit, complete, delete). Supports lists, date filters, and JSON/plain output.
version: 1.0.0
author: Nova Team
triggers:
  - reminder
  - reminders app
  - remindctl
  - add reminder
requirements:
  bins: [remindctl]
os: [darwin]
---

# Apple Reminders CLI (remindctl)

Use `remindctl` to manage Apple Reminders directly from the terminal.

## When to Use

✅ **USE this skill when:**
- User explicitly mentions "reminder" or "Reminders app"
- Creating personal to-dos with due dates that sync to iOS
- Managing Apple Reminders lists

❌ **DON'T use this skill when:**
- Scheduling Nova tasks or alerts → use `cron` tool
- Calendar events → use Apple Calendar
- Project/work task management → use Notion or GitHub Issues

## Setup

- Install: `brew install steipete/tap/remindctl`
- Check status: `remindctl status`
- Request access: `remindctl authorize`

## View Reminders

```bash
remindctl                    # Today's reminders
remindctl today              # Today
remindctl tomorrow           # Tomorrow
remindctl week               # This week
remindctl overdue            # Past due
remindctl all                # Everything
remindctl 2026-01-04         # Specific date
```

## Manage Lists

```bash
remindctl list               # List all lists
remindctl list Work          # Show specific list
remindctl list Projects --create    # Create list
remindctl list Work --delete        # Delete list
```

## Create Reminders

```bash
remindctl add "Buy milk"
remindctl add --title "Call mom" --list Personal --due tomorrow
remindctl add --title "Meeting prep" --due "2026-02-15 09:00"
```

## Complete/Delete

```bash
remindctl complete 1 2 3     # Complete by ID
remindctl delete 4A83 --force  # Delete by ID
```

## Output Formats

```bash
remindctl today --json       # JSON for scripting
remindctl today --plain      # TSV format
remindctl today --quiet      # Counts only
```

## Notes

- macOS-only
- Grants Reminders permission when prompted
- Syncs with iPhone/iPad via iCloud