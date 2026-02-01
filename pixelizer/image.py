from .data import PixelateData
from .file import load_image, save_image
from .utils import process, get_palette, build_output_name


def pixelate_image(
    input_path: str,
    output_path: str | None = None,
    width: int = 256,
    scale: int = 4,
    palette: str | None = None,
    palette_file: str | None = None,
    dither: int = 3,
    dither_type: str = "floyd",
    exposure: float = 1.0,
    contrast: float = 1.0,
) -> None:
    """Pixelate an image from input_path and save to output_path."""

    data = PixelateData(
        image=load_image(input_path),
        width=width,
        scale=scale,
        palette=get_palette(palette_file, palette),
        dither=dither,
        dither_type=dither_type,
        exposure=exposure,
        contrast=contrast,
    )

    data = process(data)

    save_image(
        data.image,
        output_path
        or build_output_name(
            input_path=input_path,
            extension="png",
            width=width,
            scale=scale,
            palette=palette,
            dither=dither,
            dither_type=dither_type,
        ),
    )
