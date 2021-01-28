import sys
from zlib import *
if len(sys.argv) != 2:
    print("Usage: zlib.py <zlib-compressed-file>")
    print("Produces decompressed file with \".out\" filename suffix.")
    sys.exit(0)
indata=open(sys.argv[1], "rb").read()
outdata=decompress(indata)
with open(sys.argv[1] + ".out", "wb") as f:
    f.write(outdata)
    f.close()