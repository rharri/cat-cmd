import argparse
from collections import namedtuple


Options = namedtuple("Options", ["n", "b", "file"])


def decorate_lines(lines: list[str], options: Options):
    if options.b:
        out = []
        line_number = 1
        for line in lines:
            if line.strip():
                out.append(f"     {line_number}  {line}")
                line_number += 1
            else:
                out.append(f"     {line}")
        return out
    elif options.n:
        return [f"     {line_number}  {line}" for line_number, line in enumerate(lines, start=1)]
    else:
        return [f"     {line}" for line in lines]


def main() -> int:
    """Entry point for cat_cmd."""
    parser = argparse.ArgumentParser(prog="cat", description="concatenate and print files")
    parser.add_argument(
        "-b",
        help="Number the non-blank output lines, starting at 1.",
        action="store_true",
        required=False)
    parser.add_argument(
        "-n",
        help="Number the output lines, starting at 1.",
        action="store_true",
        required=False)
    parser.add_argument("file", nargs="*")

    options = Options(**vars(parser.parse_args()))

    for file_name in options.file:
        try:
            with open(file_name, mode="r") as f:
                print("".join(decorate_lines(f.readlines(), options)), end="")
        except FileNotFoundError:
            print(f"cat: {file_name}: No such file or directory")
    return 0
