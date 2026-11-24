import os

ENTRY = "v3.2.0: fixed a bug where the brain marked 2 a.m. as a great time to replay every embarrassing thing you said in 2019."

# Sealed-scorer gate: one line, 1-160 UTF-8 chars, not blank.
assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 chars"
assert ENTRY.strip(), "entry must not be blank"
assert "\n" not in ENTRY, "entry must be a single line"

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
