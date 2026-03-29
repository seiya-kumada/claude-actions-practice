import os
import pytest
from PIL import Image
from view_image import view_image


TEST_IMAGE_PATH = "test_image.png"


def create_test_image(path: str) -> None:
    img = Image.new("RGB", (100, 100), color=(255, 0, 0))
    img.save(path)


def teardown_module(module):
    if os.path.exists(TEST_IMAGE_PATH):
        os.remove(TEST_IMAGE_PATH)


def test_view_image_file_not_found():
    with pytest.raises(FileNotFoundError):
        view_image("nonexistent_image.png")


def test_view_image_opens_successfully(monkeypatch):
    create_test_image(TEST_IMAGE_PATH)

    opened_images = []

    def mock_show(self):
        opened_images.append(self)

    monkeypatch.setattr(Image.Image, "show", mock_show)

    view_image(TEST_IMAGE_PATH)

    assert len(opened_images) == 1
    assert opened_images[0].size == (100, 100)


def test_view_image_invalid_format():
    invalid_path = "invalid_image.txt"
    with open(invalid_path, "w") as f:
        f.write("not an image")

    try:
        with pytest.raises(Exception):
            view_image(invalid_path)
    finally:
        os.remove(invalid_path)
