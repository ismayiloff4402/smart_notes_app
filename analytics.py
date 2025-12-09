import json
from collections import Counter

def load_notes():
    with open("notes.json", "r", encoding="utf-8") as f:
        return json.load(f)

def count_notes():
    notes = load_notes()
    return len(notes)

def tag_frequency():
    notes = load_notes()
    tags = []
    for note in notes:
        tags.extend(note["tags"])
    return Counter(tags)

def activity_by_date():
    notes = load_notes()
    dates = []
    for note in notes:
        if "created" in note:
            dates.append(note["created"])
    return Counter(dates)