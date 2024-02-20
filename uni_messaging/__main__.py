from __future__ import annotations


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        pass

    return retv


if __name__ == "__main__":
    raise SystemExit(main())
