from PIL import Image
import os
import sys


(x, y) = int(sys.argv[1]), int(sys.argv[2])

for i in os.listdir():
    if i ==  "resizer.py":
        continue
    img = Image.open(i)
    img = img.resize((int(x), int(y)))
    img.save("../"+i)