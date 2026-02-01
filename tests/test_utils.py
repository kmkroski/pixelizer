import yaml

from pixelizer.utils import (
    convert_hex_to_rgb,
    sort_by_brightness,
    build_output_name,
    get_palette,
    DEFAULT_PALETTE,
)


def test_convert_hex_to_rgb():
    assert convert_hex_to_rgb("#ff00ff") == (255, 0, 255)


def test_sort_by_brightness():
    colors = [(0, 0, 0), (255, 255, 255), (128, 0, 0)]
    sorted_colors = sort_by_brightness(colors)
    assert sorted_colors[0] == (255, 255, 255)


def test_build_output_name():
    name = build_output_name("in.jpg", "png", 128, 4, "default", "b3")
    assert "in_default_b3_128px_4x.png" in name


def test_get_palette_with_file(tmp_path):
    palettes = {"test": ["#000000", "#ffffff"]}
    pfile = tmp_path / "palettes.yml"
    pfile.write_text(yaml.safe_dump(palettes))

    palette = get_palette(str(pfile), "test")
    # brightest first -> white then black
    assert palette[0] == (255, 255, 255)
