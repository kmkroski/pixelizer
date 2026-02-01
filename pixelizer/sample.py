from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

from .data import PixelateData
from .file import load_image, save_image, load_palettes
from .filters import resize
from .utils import process, get_palette, build_output_name

SAMPLE_DITHERS: list[str] = ["f", "s", "b1", "b2", "b3", "b4", "b5"]


def pixelate_sample(
    input_path: str,
    output_path: str = "output.png",
    width: int = 256,
    scale: int = 4,
    palette: str | None = None,
    palette_file: str | None = None,
    dither: str = "b3",
    exposure: float = 1.0,
    contrast: float = 1.0,
) -> None:
    """Create a sample of pixelated images showing different palettes and dithering levels."""

    source_image = load_image(input_path)
    data = PixelateData(
        image=source_image.copy(),
        width=width,
        scale=scale,
        palette=get_palette(palette_file, palette),
        dither=dither,
        exposure=exposure,
        contrast=contrast,
    )
    data = resize(data)

    dithers = SAMPLE_DITHERS
    palettes = load_palettes(palette_file) if palette_file else {}

    print(f"{len(palettes)} palettes - {len(dithers)} dithers")

    output_width = data.image.width * scale
    output_height = data.image.height * scale
    border = 8

    image = Image.new(
        "RGB",
        (
            output_width * len(dithers),
            output_height * len(palettes),
        ),
    )
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=width * scale // 12)

    with tqdm(total=len(dithers) * len(palettes)) as pbar:
        for row, palette in enumerate(palettes.keys()):
            for col, dither in enumerate(dithers):
                pbar.update(1)

                data.image = source_image.copy()
                data.palette = get_palette(palette_file, palette)
                data.dither = dither

                new_data = process(data)
                # new_data.image.save(
                #     build_output_name(
                #         input_path=input_path,
                #         extension="png",
                #         width=width,
                #         scale=scale,
                #         palette=palette,
                #         dither=dither,
                #     )
                # )

                image.paste(
                    new_data.image,
                    (col * output_width, row * output_height),
                )

                draw.text(
                    (
                        col * output_width + border,
                        row * output_height + border,
                    ),
                    f"{(palette or 'default').upper()}  {dither.upper()}  {width}px",
                    font=font,
                    fill="white",
                    stroke_fill="#333",
                    stroke_width=2,
                )

    save_image(
        image,
        output_path
        or build_output_name(
            input_path=input_path,
            extension="png",
            width=width,
            scale=scale,
            palette="sample",
            dither=None,
        ),
    )
