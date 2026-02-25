# CLAUDE.md

## Project Overview

A simple Python GUI desktop application that displays a pixel-art banana character with googly eyes and a "Hello, World!" greeting using tkinter.

## Repository Structure

```
hello-python/
├── CLAUDE.md       # This file — guidance for AI assistants
└── hello.py        # Main application (tkinter GUI)
```

This is a single-file project with no external dependencies.

## Tech Stack

- **Language**: Python 3 (developed on 3.11)
- **GUI Framework**: tkinter (Python standard library)
- **No external packages** — no requirements.txt or pyproject.toml needed

## Running the Application

```bash
python hello.py
```

Requires a display environment (X11/Wayland) since this is a GUI app. tkinter must be available in the Python installation (it ships with standard CPython distributions).

## Code Conventions

- **Entry point**: `if __name__ == "__main__"` guard calling a `main()` function
- **Naming**: `snake_case` for variables and functions
- **Imports**: Standard library imports at the top of the file (`import tkinter as tk`)
- **Colors**: Hex color codes with inline comments describing the color name (e.g., `"#228B22"  # Forest green`)
- **Drawing**: Canvas-based pixel art using coordinate tuples and a configurable `pixel` size

## Architecture Notes

- All GUI logic lives in `main()` inside `hello.py`
- The canvas is 300x200 pixels with a forest green background
- Pixel art is rendered by iterating over coordinate tuples and drawing rectangles
- The OK button closes the application via `window.destroy`

## Development Workflow

- **Default branch**: `main`
- **Branching**: Feature branches named `feature/<description>` merged via pull requests
- No CI/CD, linting, formatting, or test infrastructure is currently configured
