import os
import json

BIBLE_DATA = {
    "pl": {},
    "pb": {}
}

def load_bible_data():
    base_path = os.path.join(os.path.dirname(__file__), "..", "lib")
    for version in ["pl", "pb"]:
        version_path = os.path.join(base_path, version)
        for filename in os.listdir(version_path):
            if filename.endswith(".json"):
                filepath = os.path.join(version_path, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    book_name = data["book"].lower()
                    BIBLE_DATA[version][book_name] = data["chapters"]


# Utility function to select verses by range or single verse
def select_verses(verses, verse_range):
    """
    Given a list of verses and a verse_range string (e.g., '3' or '3-5'),
    return the selected verses as a list. Raises ValueError for bad input.
    """
    if "-" in verse_range:
        try:
            start, end = map(int, verse_range.split("-"))
        except ValueError:
            raise ValueError("Invalid verse range format. Use start-end.")
        if start > end:
            raise ValueError("Start verse cannot be greater than end verse.")
        selected = [v for v in verses if start <= v["verse"] <= end]
    else:
        try:
            verse_num = int(verse_range)
        except ValueError:
            raise ValueError("Invalid verse number.")
        selected = [v for v in verses if v["verse"] == verse_num]
    return selected

# Call this once at startup
load_bible_data()
