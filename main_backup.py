"""Small helper to load a book file and print its contents.

Usage:
  python main.py            # prints `books/frankenstein.txt` (default)
  python main.py path/to/book.txt
"""

from pathlib import Path
import sys


def get_book_text(path: Path) -> str:
    """Return the full text of the book at `path`.

    Raises FileNotFoundError if the file does not exist.
    """
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def main(argv=None):
    argv = argv or sys.argv[1:]
    # Default book file inside the repository
    repo_root = Path(__file__).parent
    default_book = repo_root / "books" / "frankenstein.txt"

    if len(argv) >= 1:
        book_path = Path(argv[0])
    else:
        book_path = default_book

    if not book_path.exists():
        print(f"Error: book not found: {book_path}", file=sys.stderr)
        return 2

    text = get_book_text(book_path)
    # Print the whole book; if very large, the user can pipe or redirect.
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
