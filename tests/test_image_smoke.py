import os
from PIL import Image

from pixelizer.image import pixelate_image


def test_pixelate_image_creates_file(tmp_path):
    # create a tiny source image in tmp_path
    src = tmp_path / "small.jpg"
    img = Image.new("RGB", (32, 32), color=(120, 150, 200))
    img.save(src)

    out = tmp_path / "out.png"

    pixelate_image(str(src), str(out), width=16, scale=2)

    assert out.exists()
    out_img = Image.open(out)
    assert out_img.size[0] >= 16
