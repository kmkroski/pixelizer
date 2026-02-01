from PIL import Image

from pixelizer.data import PixelateData
from pixelizer.filters import resize, scale, contrast, exposure


def make_image(width=64, height=32):
    return Image.new("RGB", (width, height), color=(128, 128, 128))


def test_resize():
    data = PixelateData(image=make_image(64, 32), width=32)
    resized = resize(data)
    assert resized.image.width == 32


def test_scale():
    data = PixelateData(image=make_image(16, 8), scale=2)
    scaled = scale(data)
    assert scaled.image.width == 32


def test_contrast_exposure_no_errors():
    data = PixelateData(image=make_image(), contrast=1.2, exposure=0.8)
    data = contrast(data)
    data = exposure(data)
    # just ensure functions run and return PixelateData
    assert data.image is not None
