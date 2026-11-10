import sys
from pathlib import Path
from PIL import Image

for p in Path(sys.argv[1]).glob('*.jpg'):
    im = Image.open(p)
    im.thumbnail((1280, 1280))
    im.save(p)
