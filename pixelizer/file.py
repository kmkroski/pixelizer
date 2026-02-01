from PIL import Image
from yaml import safe_load


def load_image(path: str) -> Image.Image:
    """Load an image from the specified file path."""

    return Image.open(path)


def save_image(image: Image.Image, path: str) -> None:
    """Save an image to the specified file path."""

    image.save(path)


def load_palettes(path: str) -> dict:
    """Load color palettes from a file."""

    with open(path, "r") as file:
        palettes = safe_load(file)

    return {k.lower(): v for k, v in palettes.items()}
