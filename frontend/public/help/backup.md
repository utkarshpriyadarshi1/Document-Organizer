### System Backup & Sync

System backup packages organized document stores and relational database states into compressed directories.

#### Workstation Cold Backup:
- Pack archives: Copies files in organized directory and indices to a backup package.
- Path layout: `backups/backup_[timestamp]`

#### WebSocket Progress:
- A live WebSocket tunnel at `ws://localhost:8080/progress` handles telemetry stream sync during packaging.
- Check the logger panel for real-time log messages from the backing broker thread.
- Review past backup packages and status logs in the Backup Registry History panel.
