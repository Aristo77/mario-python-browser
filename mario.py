# mario.py

def build_pyramid(height):
    """Return a right-aligned pyramid as one string (with newlines)."""
    lines = []

    for j in range(height):
        # spaces then hashes
        line = " " * (height - j - 1) + "#" * (j + 1)
        lines.append(line)

    return "\n".join(lines)


if __name__ == "__main__":
    # original terminal version
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                break
        except:
            print("", end="")

    print(build_pyramid(height))
