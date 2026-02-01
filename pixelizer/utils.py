from os import name, path
from .data import PixelateData
from .file import load_palettes
from .filters import resize, contrast, exposure, palette, scale

DEFAULT_PROCESS: list = [resize, contrast, exposure, palette, scale]
DEFAULT_PALETTE: list[str] = ["#081820", "#346856", "#88c070", "#e0f8d0"]


def process(data: PixelateData) -> PixelateData:
    """Apply processing filters to the PixelateData object."""

    for filter_func in DEFAULT_PROCESS:
        data = filter_func(data)
    return data


def get_palette(palette_file: str | None, palette_name: str | None) -> list:
    """Load palette from file or return default palette.

    Parameters:
    - palette_file: path to YAML file containing palettes (or None)
    - palette_name: name of the palette (or None)
    """

    palette = DEFAULT_PALETTE
    if palette_file and palette_name:
        palettes = load_palettes(palette_file)
        if palette_name not in palettes:
            raise ValueError(
                f"Palette '{palette_name}' not found in file '{palette_file}'."
            )

        palette = palettes[palette_name]

    return sort_by_brightness([convert_hex_to_rgb(color) for color in palette])


def convert_hex_to_rgb(hex_color: str) -> tuple:
    """Convert a hex color string to an RGB tuple."""

    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def sort_by_brightness(palette: list) -> list:
    """Sort a list of RGB tuples by their perceived brightness."""

    def brightness(color: tuple) -> float:
        r, g, b = color
        return 0.299 * r + 0.587 * g + 0.114 * b

    return sorted(palette, key=brightness, reverse=True)


def build_output_name(
    input_path: str,
    extension: str,
    width: int,
    scale: int,
    palette: str | None,
    dither: str | None,
) -> str:
    """Build an output file name based on the input file name and a suffix."""
    from os import path

    name = path.splitext(input_path)[0]

    if dither is None or palette == "sample":
        return f"{name}_{palette}_{width}px_{scale}x.{extension}"

    return f"{name}_{palette}_{dither}_{width}px_{scale}x.{extension}"
