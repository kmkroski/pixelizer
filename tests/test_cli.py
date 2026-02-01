import sys
from argparse import Namespace

import pytest

from pixelizer import cli


def test_get_arguments_defaults(monkeypatch, tmp_path):
    src = tmp_path / "in.jpg"
    src.write_text("x")
    monkeypatch.setattr(sys, "argv", ["pixelizer", "image", str(src)])
    args = cli.get_arguments()
    assert args.mode == "image"
    assert args.width == 256
    assert args.scale == 4


def test_invalid_mode(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["pixelizer", "unknown", "in.jpg"])
    with pytest.raises(SystemExit):
        cli.get_arguments()
