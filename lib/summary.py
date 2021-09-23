from datetime import date

import pyperclip


def generate_summary_list(entries):
    items = {}

    if len(entries) == 0:
        return "No entries - Did you not track your time today?!"

    for entry in entries:
        name = entry['description']
        duration = entry['duration']

        if name not in items:
            items[name] = duration
        else:
            items[name] = items[name] + duration

    return sorted(items.items(), key=lambda kv: kv[1], reverse=True)


def render_output(entries):

    print(f"\nGenerating daily summary for {date.today()} from Toggl Track:\n")

    final_parts = ["\N{Studio Microphone} Today"]

    for entry in entries:
        final_parts.append(f"• {entry[0]}")

    final_parts.append("\nYour daily summary has been copied to your clipboard!")

    final = "\n".join(final_parts)

    pyperclip.copy(final)

    return final
