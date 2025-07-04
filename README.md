# Manimations (Manim Animations)

This repository contains all python code that generates `manim` video files for personal and educational purposes.
For now, (it may be changed later) here is the structure of the repo

```
.
├── portfolio/ # a directory for an introduction video using `manim` in my homepage
│   ├── assets/ # a directory that contains `svg` files in order `manim` to draw images
│   ├── justfile # a file for `just` a command runner (moreless like `make` but with good default settings)
│   ├── main.py # code for introduction video using `manim`
│   └── manim.cfg # configuration options for `manim`
├── pyproject.toml # `project` configuration file generated using `uv`
├── README.md # readme file
├── uv.lock # lock file generated using `uv`
└── youtube/ # code to generate `manim` videos for youtube (coming soon)
```

