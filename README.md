# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a small command-line tool that analyzes text files (like books) and reports simple stats.

## Features
- Count words, characters, and lines
- List the frequency of each letter (case-insensitive)
- Report the most common words

## Getting Started

### Prerequisites
- Python 3.10+ (or your target language/runtime)
- Git

### Setup
```bash
git clone https://github.com/axp-knickei/bookbot
cd bookbot
```

# Usage
```
# Example: analyze a local text file
python main.py path/to/book.txt
```

# Example Output:
```
Lines: 1234
Words: 21045
Characters: 125678

Top letters:
e: 12.3%
t: 9.8%
a: 8.9%
...

Top words:
the (1450)
and (980)
to (875)
...
```

# Project Structure
```
bookbot/
├─ main.py          # CLI entry point
├─ bookbot/         # Library code (parsers, analyzers)
│  ├─ __init__.py
│  ├─ analyzer.py
│  └─ utils.py
├─ tests/           # Unit tests
│  └─ test_analyzer.py
├─ data/            # Sample texts (optional, gitignored if large)
└─ README.md

```

# Development
```
# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dev dependencies
pip install -r requirements.txt  # if you add one

# Run tests
pytest
```

# Roadmap
- Add CSV/JSON export of stats
- Ignore stopwords for common-word ranking
- Support multiple files and aggregate reports

# Contributing
Issues and PRs welcome. Please open an issue before major changes.

#License
MIT