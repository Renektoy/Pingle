import json
import os
from datetime import datetime

LOG_FILE = "logs.json"

def _load_logs():
    """Load logs from the JSON file. If file doesn't exist, return an empty list."""
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def _save_logs(logs):
    """Save the given list of logs to the JSON file."""
    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

def log_event(log_type, message, **kwargs):
    """
    Add a new log entry.
    
    log_type: 'device_event', 'security_event', etc.
    message: Brief description of the event.
    kwargs: Optional metadata (device_id, file_path, etc.)
    """
    logs = _load_logs()

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "type": log_type,
        "message": message
    }

    # Include any additional metadata (like device_id, file_path, etc.)
    log_entry.update(kwargs)

    logs.append(log_entry)
    _save_logs(logs)

    print(f"[{log_type.upper()}] {message}")
