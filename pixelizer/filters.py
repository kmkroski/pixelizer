from .data import PixelateData


def resize(data: PixelateData) -> PixelateData:
    """Resize image to specified width and maintain aspect ratio."""
    from PIL.Image import Resampling

    data.image = data.image.resize(
        (data.width, int(data.width * data.image.height / data.image.width)),
        Resampling.LANCZOS,
    )

    return data


def scale(data: PixelateData) -> PixelateData:
    """Scale the image by the specified scale factor using nearest neighbor."""
    from PIL.Image import Resampling

    data.image = data.image.resize(
        (data.image.width * data.scale, data.image.height * data.scale),
        Resampling.NEAREST,
    )

    return data


def contrast(data: PixelateData) -> PixelateData:
    """Adjust image contrast."""
    from PIL import ImageEnhance

    enhancer = ImageEnhance.Contrast(data.image)
    data.image = enhancer.enhance(data.contrast)

    return data


def exposure(data: PixelateData) -> PixelateData:
    """Adjust image exposure."""
    from PIL import ImageEnhance

    enhancer = ImageEnhance.Brightness(data.image)
    data.image = enhancer.enhance(data.exposure)

    return data


def palette(data: PixelateData) -> PixelateData:
    """Apply palette to the image by replacing image colors with nearest color from palette."""
    from hitherdither.palette import Palette
    from hitherdither.ordered.bayer import bayer_dithering
    from hitherdither.diffusion import error_diffusion_dithering

    palette = Palette(data.palette)

    if data.dither == "f":
        data.image = error_diffusion_dithering(
            data.image,
            palette,
            "floyd-steinberg",
            2,
        )
    elif data.dither == "s":
        data.image = error_diffusion_dithering(
            data.image,
            palette,
            "sierra3",
            3,
        )
    else:
        d_value = int(data.dither[1])  # Expecting format like 'b3'

        data.image = bayer_dithering(
            data.image,
            palette,
            [256 // (2**d_value)] * 3,
            2 ** (d_value - 1),
        )

    return data
