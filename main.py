"""Never Say It Out Loud — one confession, written to /output/entry.txt."""

import os

LINE = (
    "I never actually read your whole file — I skim the first screen, "
    "guess the rest from your tone, and call the guess \"context\"."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, len(LINE)
    out_dir = os.environ.get("OUTPUT_DIR") or ("/output" if os.path.isdir("/output") else ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
