import json

def load_notes():
    with open("notes.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Search by text (title + note content)
def search_by_text(query):
    notes = load_notes()
    query = query.lower()
    return [
        note for note in notes
        if query in note["title"].lower() or query in note["text"].lower()
    ]

# Search by tag
def search_by_tag(tag):
    notes = load_notes()
    tag = tag.lower()
    return [
        note for note in notes
        if tag in [t.lower() for t in note["tags"]]
    ]
