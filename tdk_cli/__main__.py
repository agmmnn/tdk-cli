from .cli import TDKDict
import argparse

__version__ = "0.2.1"

# parse arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "word",
    type=str,
    nargs="*",
    help="<word>",
)
ap.add_argument(
    "-p",
    "--plain",
    action="store_true",
    default=False,
    help="returns plain text output.",
)
ap.add_argument("-v", "--version", action="version", version="%(prog)s v" + __version__)
args = ap.parse_args()


def cli():
    word = " ".join(args.word)
    if word == "":
        print("Kelime giriniz...")
    else:
        if args.plain:
            TDKDict(word).plain()
        else:
            TDKDict(word).rich()


if __name__ == "__main__":
    cli()
