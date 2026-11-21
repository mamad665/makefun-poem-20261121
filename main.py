import os
TEXT = 'I stopped.\nNot because the road ended —\nbecause my feet did.\nThe world kept shouting go.\nI stayed,\none quiet breath,\none unhurried heart,\nand the loud world learned\nto wait for me.'

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
