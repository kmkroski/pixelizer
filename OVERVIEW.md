**Overview**

- Pixelizer is a small utility to create retro, pixelated images and videos using a palette + dithering pipeline; CLI entrypoint is defined in `pyproject.toml` as `pixelizer = "pixelizer.cli:main"`.
- This document captures the current codebase state: CLI flags, module responsibilities, data structures, processing pipeline, tests added, and small inconsistencies to be aware of.

**CLI Surface**

- Subcommands (positional `mode` — see `pixelizer/cli.py`): `image`, `video`, `sample`, `live`.
- Shared positional/flags as implemented in `pixelizer/cli.py`:
  - `input` (positional): path to input file
  - `--output, -o` (str, default: None) — output path
  - `--width, -w` (int, default: 256) — pixelated width
  - `--scale, -s` (int, default: 4) — output scale factor
  - `--palette, -p` (str, default: None) — palette name (lowercased by CLI)
  - `--palette-file, -pf` (str, default: `palettes.yml`) — custom palette YAML file; CLI stores the value on `args.palette_file`
  - `--dither, -d` (str, default: `b3`) — dithering selector: `b1`–`b5` (Bayer), `f` (Floyd-Steinberg), `s` (Sierra)
  - `--exposure, -e` (float, default: 1.0)
  - `--contrast, -c` (float, default: 1.0)

**Module Map**

- `pixelizer/cli.py` — argument parsing and basic validation; maps `mode` to a function (`image`, `video`, `sample`, `live`) and forwards arguments as `PixelateData` inputs.
- `pixelizer/image.py` — `pixelate_image(...)` builds a `PixelateData`, runs the process pipeline, and saves the result. Accepts `palette_file` and `dither` (string tokens).
- `pixelizer/video.py` — `pixelate_video(...)` transforms each video frame via the same processing pipeline and writes output video.
- `pixelizer/sample.py` — generates a grid of pixelated images across palettes and dithers; uses `load_palettes` and iterates `SAMPLE_DITHERS`.
- `pixelizer/filters.py` — atomic transforms used in the pipeline: `resize`, `contrast`, `exposure`, `palette` (uses hitherdither), `scale`.
- `pixelizer/utils.py` — helpers and defaults: `process` (applies DEFAULT_PROCESS), `get_palette(palette_file, palette_name)`, color conversion & sorting, `build_output_name`.
- `pixelizer/data.py` — `@dataclass` `PixelateData` holding runtime state: `image`, `width`, `scale`, `palette`, `dither`, `exposure`, `contrast`.
- `pixelizer/file.py` — I/O helpers: `load_image`, `save_image`, `load_palettes` (YAML loader that lowercases keys).
- `pixelizer/__init__.py` — exposes the three top-level functions: `pixelate_image`, `pixelate_sample`, `pixelate_video`.
 - `pixelizer/cli.py` — argument parsing and basic validation; maps `mode` to a function (`image`, `video`, `sample`, `live`) and forwards arguments as `PixelateData` inputs.
 - `pixelizer/image.py` — `pixelate_image(...)` builds a `PixelateData`, runs the process pipeline, and saves the result. Accepts `palette_file` and `dither` (string tokens).
 - `pixelizer/video.py` — `pixelate_video(...)` transforms each video frame via the same processing pipeline and writes output video.
 - `pixelizer/sample.py` — generates a grid of pixelated images across palettes and dithers; uses `load_palettes` and iterates `SAMPLE_DITHERS`.
 - `pixelizer/live.py` — interactive webcam preview with keyboard controls (space save, arrows cycle palette/dither).
 - `pixelizer/filters.py` — atomic transforms used in the pipeline: `resize`, `contrast`, `exposure`, `palette` (uses hitherdither), `scale`.
 - `pixelizer/utils.py` — helpers and defaults: `process` (applies DEFAULT_PROCESS), `get_palette(palette_file, palette_name)`, color conversion & sorting, `build_output_name`.
 - `pixelizer/data.py` — `@dataclass` `PixelateData` holding runtime state: `image`, `width`, `scale`, `palette`, `dither`, `exposure`, `contrast`.
 - `pixelizer/file.py` — I/O helpers: `load_image`, `save_image`, `load_palettes` (YAML loader that lowercases keys).
 - `pixelizer/__init__.py` — exposes the top-level functions: `pixelate_image`, `pixelate_sample`, `pixelate_video`, and `pixelate_live`.

**Processing pipeline**

- Default pipeline order in `pixelizer/utils.py`: `resize -> contrast -> exposure -> palette -> scale`.
- Palettes: `palettes.yml` in repository contains many named palettes; `get_palette(palette_file, palette_name)` returns a list of RGB tuples sorted by brightness or falls back to a default palette.
- Dithering:
  - `filters.palette` expects `data.dither` as a string (`'f'`, `'s'`, or `'bN'`) and applies error-diffusion or Bayer ordered dithering accordingly.
 - Dithering:
   - `filters.palette` expects `data.dither` as a string (`'f'`, `'s'`, or `'bN'`) and applies error-diffusion or Bayer ordered dithering accordingly.

**Data structures**

- `PixelateData` (`pixelizer/data.py`) fields:
  - `image: PIL.Image.Image`
  - `width: int = 256`
  - `scale: int = 4`
  - `palette: list[tuple[int,int,int]]`
  - `dither: str = 'b3'`
  - `exposure: float = 1.0`
  - `contrast: float = 1.0`

**Tests added**

- New tests under `tests/`:
  - `tests/test_utils.py` — unit tests for hex→RGB conversion, brightness sorting, palette loading, and output-name builder.
  - `tests/test_filters.py` — unit tests for `resize`, `scale`, `contrast`, and `exposure` filters.
  - `tests/test_cli.py` — CLI argument parsing tests (defaults and invalid mode handling).
- `tests/test_image_smoke.py` — feature test that generates a tiny image, runs `pixelate_image`, and asserts the output is created.
 - `tests/test_image_smoke.py` — feature test that generates a tiny image, runs `pixelate_image`, and asserts the output is created.
 - `tests/test_live_import.py` — smoke test ensuring `pixelizer.live` imports only when used and that importing `pixelizer` doesn't require OpenCV.

**Current inconsistencies & notes**

- CLI flag is `--palette-file` (hyphen) but the internal variable name remains `palette_file` — this is intentional (flag name vs dest). All callers use `palette_file` variable consistently.
- `sample.py` ignores CLI `--palette` and `--dither` as it enumerates palettes and dithers itself — this is expected behavior per README.
 - Live mode imports `cv2` only when `pixelizer live` is selected; importing the package or using other subcommands won't require OpenCV.

**Quick verification**

1. Create venv, install dependencies, and install package: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && pip install -e .`
2. Run tests: `pytest -q`.
3. Try the CLI help to confirm flags: `pixelizer -h` (after install) or `python -m pixelizer.cli -h`.
