#!/Users/james.williams/.local/share/virtualenvs/python-toggl-daily-summary-gRlFHpmu/bin/python

import datetime
import os

from lib.summary import generate_summary_list, render_output

from dotenv import load_dotenv
from datetime import datetime, date, time, timedelta

import requests

load_dotenv()

API_KEY = os.getenv('TOGGLE_KEY')
API_BASE = "https://api.track.toggl.com/api/v8/"


def run():

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
    data = response.json()

    print(generate_summary(data))


if __name__ == "__main__":
    run()
