from PIL import Image
import os


def view_image(path: str) -> None:
    """
    画像ファイルのパスを受け取り、画像を表示する。

    Args:
        path: 表示する画像ファイルのパス
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"画像ファイルが見つかりません: {path}")

    img = Image.open(path)
    img.show()


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("使い方: python view_image.py <画像ファイルのパス>")
        sys.exit(1)

    view_image(sys.argv[1])
