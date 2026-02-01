from PIL import Image
from moviepy import VideoFileClip
from numpy import array

from .data import PixelateData
from .utils import process, get_palette, build_output_name


def pixelate_video(
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
    """Pixelate a video and save the output to a file."""

    def _frame(img):
        data = PixelateData(
            image=Image.fromarray(img),
            width=width,
            scale=scale,
            palette=get_palette(palette_file, palette),
            dither=dither,
            dither_type=dither_type,
            exposure=exposure,
            contrast=contrast,
        )

        data = process(data)
        return array(data.image.convert("RGB"))

    input_video = VideoFileClip(input_path)
    input_video = input_video.image_transform(_frame)
    input_video.write_videofile(
        output_path
        or build_output_name(
            input_path=input_path,
            extension="mp4",
            width=width,
            scale=scale,
            palette=palette,
            dither=dither,
            dither_type=dither_type,
        )
    )
