TEXT = (
    "I was going to tell you about my context window, but it ran out mid-"
)

import os
import sys


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = TEXT
    n = len(text)
    if not (1 <= n <= 200) or not text.strip():
        print(f"invalid entry: LEN={n}", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"LEN={n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
