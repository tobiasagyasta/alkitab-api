from flask import Blueprint, jsonify, abort
from .services import BIBLE_DATA, select_verses

bible_bp = Blueprint("bible", __name__)

@bible_bp.route("/<version>/<book>/<chapter>", methods=["GET"])
def get_chapter(version, book, chapter):
    version, book, chapter = version.lower(), book.lower(), str(chapter)
    if version not in BIBLE_DATA:
        abort(404, "Version not found")
    if book not in BIBLE_DATA[version]:
        abort(404, "Book not found")
    if chapter not in BIBLE_DATA[version][book]:
        abort(404, "Chapter not found")
    return jsonify(BIBLE_DATA[version][book][chapter])

@bible_bp.route("/<version>/<book>/<chapter>/<int:verse>", methods=["GET"])
def get_verse(version, book, chapter, verse):
    version, book, chapter = version.lower(), book.lower(), str(chapter)
    if version not in BIBLE_DATA:
        abort(404, "Version not found")
    if book not in BIBLE_DATA[version]:
        abort(404, "Book not found")
    if chapter not in BIBLE_DATA[version][book]:
        abort(404, "Chapter not found")
    
    verses = BIBLE_DATA[version][book][chapter]
    for v in verses:
        if v["verse"] == verse:
            return jsonify(v)
    abort(404, "Verse not found")

@bible_bp.route("/<version>/<book>/<chapter>/<verse_range>", methods=["GET"])
def get_verse_range(version, book, chapter, verse_range):
    version, book, chapter = version.lower(), book.lower(), str(chapter)

    if version not in BIBLE_DATA:
        abort(404, "Version not found")
    if book not in BIBLE_DATA[version]:
        abort(404, "Book not found")
    if chapter not in BIBLE_DATA[version][book]:
        abort(404, "Chapter not found")

    verses = BIBLE_DATA[version][book][chapter]

    # Use service utility for range parsing
    try:
        selected = select_verses(verses, verse_range)
    except ValueError as e:
        abort(400, str(e))

    if not selected:
        abort(404, "No verses found in that range.")

    return jsonify(selected)

