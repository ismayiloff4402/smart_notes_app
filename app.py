import json
from datetime import datetime

# Load notes
def load_notes():
    try:
        with open("notes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save notes
def save_notes(notes):
    with open("notes.json", "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

# Add a new note
def add_note(title, text, tags):
    notes = load_notes()
    notes.append({
        "title": title,
        "text": text,
        "tags": tags,
        "created": datetime.now().strftime("%Y-%m-%d")
    })
    save_notes(notes)

# Debug preview (optional)
if __name__ == "__main__":
    print("Total notes:", len(load_notes()))
