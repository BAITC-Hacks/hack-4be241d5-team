"""Classify an image by the share of red pixels."""

import argparse
from pathlib import Path

from PIL import Image

RED_PIXEL_SHARE_THRESHOLD = 0.30


def has_many_red_pixels(path: Path) -> bool:
    """Return True when red pixels occupy more than 30% of the image."""
    with Image.open(path) as source:
        image = source.convert("RGB")
        pixels = image.load()
        red_pixels = 0
        for y in range(image.height):
            for x in range(image.width):
                red, green, blue = pixels[x, y]
                if red > 150 and red > green * 1.25 and red > blue * 1.25:
                    red_pixels += 1
        return red_pixels / (image.width * image.height) > RED_PIXEL_SHARE_THRESHOLD


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print DEFECT for images with many red pixels, otherwise OK."
    )
    parser.add_argument("image", type=Path, help="path to an image file")
    args = parser.parse_args()

    print("DEFECT" if has_many_red_pixels(args.image) else "OK")


if __name__ == "__main__":
    main()
