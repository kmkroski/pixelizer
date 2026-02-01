from __future__ import annotations

import os
from time import time
from typing import Optional

import cv2
import numpy as np
from PIL import Image

from .data import PixelateData
from .file import load_palettes
from .utils import process, get_palette, build_output_name, DEFAULT_PALETTE


WINDOW_NAME: str = "Pixelizer"
LIVE_DITHERS: list[str] = ["b5", "b4", "b3", "b2", "b1", "f", "s"]


def _get_window_name(
    palette_name: str,
    dither: str,
    width: int,
) -> str:
    return " | ".join([palette_name.upper(), dither.upper(), f"{width}px"])


def _ensure_output_dir(path: Optional[str]) -> Optional[str]:
    if not path:
        return None

    # if path looks like a directory or ends with a separator, ensure directory
    if (
        path.endswith(os.sep)
        or path.endswith("/")
        or path.endswith("\\")
        or os.path.isdir(path)
    ):
        os.makedirs(path, exist_ok=True)
        return path

    # path appears to be a file; ensure parent dir
    parent = os.path.dirname(path) or "."
    os.makedirs(parent, exist_ok=True)
    return path


def pixelate_live(
    input_path: str | None = None,
    output_path: str | None = None,
    width: int = 256,
    scale: int = 4,
    palette: str | None = None,
    palette_file: str | None = None,
    dither: str = "b3",
    exposure: float = 1.0,
    contrast: float = 1.0,
) -> None:
    """Open webcam and run an interactive pixelation preview.

    Controls:
    - Space: capture/save current processed frame
    - Left/Right: cycle palettes (from palette_file)
    - Up/Down: cycle dither tokens
    - q or ESC: quit
    """

    # Prepare palettes
    palettes = load_palettes(palette_file or "")
    palette_names = list(palettes.keys()) or ["default"]

    # start indexes
    palette_idx = 0
    if palette and palette in palette_names:
        palette_idx = palette_names.index(palette)

    dither_idx = (
        LIVE_DITHERS.index(dither)
        if dither in LIVE_DITHERS
        else LIVE_DITHERS.index("b3")
    )

    out_path = _ensure_output_dir(output_path)

    # Template PixelateData (image replaced each frame)
    data = PixelateData(
        image=Image.new("RGB", (width, width)),
        width=width,
        scale=scale,
        palette=palettes[palette_names[palette_idx]],
        dither=LIVE_DITHERS[dither_idx],
        exposure=exposure,
        contrast=contrast,
    )

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam (cv2.VideoCapture(0)).")

    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Setup window
            status = _get_window_name(
                palette_names[palette_idx], LIVE_DITHERS[dither_idx], width
            )
            window_name = f"{WINDOW_NAME} | {status}"
            cv2.setWindowTitle(WINDOW_NAME, window_name)

            # Setup data
            data.palette = palettes[palette_names[palette_idx]]
            data.dither = LIVE_DITHERS[dither_idx]
            data.image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Processing may be slow; measure but keep simple
            start = time()
            out = process(data)

            out_pil = out.image
            out_np = cv2.cvtColor(np.array(out_pil.convert("RGB")), cv2.COLOR_RGB2BGR)

            # Add text and show
            cv2.putText(
                out_np,
                f"{status} | t={(time() - start):.2f}s",
                (8, 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1,
                cv2.LINE_AA,
            )
            cv2.imshow(WINDOW_NAME, out_np)

            key = cv2.waitKey(1)
            if key == -1:
                continue

            # Spacebar
            if key in (ord(" "), 32):
                output_path = build_output_name(
                    input_path=f"{time():.0f}",
                    extension="png",
                    width=width,
                    scale=scale,
                    palette=palette_names[palette_idx],
                    dither=LIVE_DITHERS[dither_idx],
                )
                out_pil.save(output_path)

            # Left arrow
            elif key in (2, 81, 2424832):
                palette_idx = (palette_idx - 1) % len(palette_names)

            # Right arrow
            elif key in (3, 83, 2555904):
                palette_idx = (palette_idx + 1) % len(palette_names)

            # Up arrow
            elif key in (0, 82, 2490368):
                dither_idx = (dither_idx - 1) % len(LIVE_DITHERS)

            # Down arrow
            elif key in (1, 84, 2621440):
                dither_idx = (dither_idx + 1) % len(LIVE_DITHERS)

            # q or ESC
            elif key in (ord("q"), 27):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
