from argparse import ArgumentParser, Namespace
from pixelizer import pixelate_image, pixelate_sample, pixelate_video


def get_function(mode: str):
    pixelate = pixelate_sample

    if mode == "image":
        pixelate = pixelate_image

    elif mode == "video":
        pixelate = pixelate_video

    elif mode == "live":
        # import here to avoid requiring cv2 for non-live usage
        from .live import pixelate_live

        pixelate = pixelate_live

    return pixelate


def get_arguments() -> Namespace:
    parser = ArgumentParser(
        prog="Pixelizer",
        description="Pixelate images, videos, or live webcam feed.",
    )

    parser.add_argument(
        "mode",
        choices=["image", "video", "sample", "live"],
        help="Image, video, sample, or live.",
    )
    parser.add_argument(
        "input",
        type=str,
        nargs="?",
        help="Path to input file (optional for live mode)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Path to output file",
    )
    parser.add_argument(
        "--width",
        "-w",
        type=int,
        default=256,
        help="Pixel width of the image",
    )
    parser.add_argument(
        "--scale",
        "-s",
        type=int,
        default=4,
        help="Output pixel scale factor",
    )
    parser.add_argument(
        "--palette",
        "-p",
        type=str,
        default=None,
        help="Palette name",
    )
    parser.add_argument(
        "--palette-file",
        "-pf",
        dest="palette_file",
        type=str,
        default="palettes.yml",
        help="Path to custom palette file",
    )
    parser.add_argument(
        "--dither",
        "-d",
        type=str,
        default="b3",
        help="Dithering amount: b1-b5 (Bayer), f (Floyd-Steinberg), s (Sierra)",
    )
    parser.add_argument(
        "--exposure",
        "-e",
        type=float,
        default=1.0,
        help="Exposure adjustment value",
    )
    parser.add_argument(
        "--contrast",
        "-c",
        type=float,
        default=1.0,
        help="Contrast adjustment value",
    )

    args = parser.parse_args()
    if args.mode in ["image", "video"] and not args.input:
        parser.error("--input is required for image and video modes.")
    elif args.mode == "live" and args.input:
        print("warning: --input is ignored in live mode.")

    args.dither = args.dither.lower()
    args.palette = args.palette.lower() if args.palette else None

    return args


def main():
    args = get_arguments()
    pixelate = get_function(args.mode)

    pixelate(
        input_path=args.input,
        output_path=args.output,
        width=args.width,
        scale=args.scale,
        palette=args.palette,
        palette_file=args.palette_file,
        dither=args.dither,
        exposure=args.exposure,
        contrast=args.contrast,
    )


if __name__ == "__main__":
    main()
