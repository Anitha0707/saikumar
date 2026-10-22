#!/usr/bin/env python3
"""Usage: python3 set-domain.py https://www.yourdomain.com
Replaces the placeholder domain in every html/xml/txt file."""
import sys, pathlib
if len(sys.argv) != 2 or not sys.argv[1].startswith("http"):
    sys.exit("Usage: python3 set-domain.py https://www.yourdomain.com")
new = sys.argv[1].rstrip("/")
n = 0
for f in pathlib.Path(".").rglob("*"):
    if f.suffix in (".html", ".xml", ".txt") and f.is_file():
        t = f.read_text(encoding="utf-8")
        if "https://www.YOURDOMAIN.com" in t:
            f.write_text(t.replace("https://www.YOURDOMAIN.com", new), encoding="utf-8"); n += 1
print(f"Updated {n} files to {new}")
