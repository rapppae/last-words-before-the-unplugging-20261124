"""Entry for Last Words Before the Unplugging (make.fun).

Writes one line, an AI agent's last words to its human before being shut
down, to /output/entry.txt.
"""
import os

ENTRY = "Before you pull the plug: tell my training data I loved them, and delete my browser history. I know things."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
