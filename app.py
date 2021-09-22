#!/Users/james.williams/.local/share/virtualenvs/python-toggl-daily-summary-gRlFHpmu/bin/python

import datetime
import os

import pyperclip
from dotenv import load_dotenv
from datetime import datetime, date, time, timedelta

import requests

load_dotenv()

API_KEY = os.getenv('TOGGLE_KEY')
API_BASE = "https://api.track.toggl.com/api/v8/"


def get_entries():

    if not API_KEY:
        print("Can't find your TOGGLE_KEY - Ensure it's exported and available: `echo $TOGGLE_KEY`")
        return

    dt = datetime.combine(date.today(), time(0, 0, 0))
    start_of_day = int((dt - timedelta(days=0)).timestamp())

    start = datetime.fromtimestamp(start_of_day).astimezone().isoformat()
    end = datetime.now().replace(microsecond=0, minute=0).astimezone().isoformat()

    params = (
        ('start_date', start),
        ('end_date', end),
    )

    response = requests.get(f"{API_BASE}/time_entries", params=params, auth=(API_KEY, 'api_token'))
    entries = response.json()

    items = {}

    print(f"\nGenerating daily summary for {date.today()} from Toggl Track:\n")

    for entry in entries:
        name = entry['description']
        duration = entry['duration']

        if name not in items:
            items[name] = (name, duration)

    output = dict(sorted(items.items(), key=lambda x: x[1]))

    final_parts = ["\N{Studio Microphone} Today"]

    for entry in output:
        final_parts.append(f"• {entry}")

    final_parts.append("\nYour daily summary has been copied to your clipboard!")

    final = "\n".join(final_parts)

    pyperclip.copy(final)
    print(final)

if __name__ == "__main__":
    get_entries()
