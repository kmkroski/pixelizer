from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from PIL import Image


@dataclass
class PixelateData:
    """Data structure to hold image and pixelation parameters.

    Converted to a dataclass for clarity. Use `palette` as a list of RGB
    tuples. Use `field(default_factory=list)` to avoid shared mutable defaults.
    """

    image: Image.Image
    width: int = 256
    scale: int = 4
    palette: List[Tuple[int, int, int]] = field(default_factory=list)
    dither: str = "b3"
    exposure: float = 1.0
    contrast: float = 1.0
