import inspect

from pixelizer import pixelate_live


def test_live_signature():
    sig = inspect.signature(pixelate_live)
    params = list(sig.parameters.keys())
    # ensure it accepts same args as other entrypoints (input_path optional)
    assert "input_path" in params or "input" in params
    assert "width" in params
    assert "scale" in params
    assert "palette_file" in params
