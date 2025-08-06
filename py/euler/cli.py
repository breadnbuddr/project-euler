"""Command line interface for Project Euler problems."""

import importlib
import sys


def main():
    """Entry point for the command line interface to Project Euler problems."""
    n = int(sys.argv[1])
    mod = importlib.import_module(f"euler.problem_{n:03d}")
    print(mod.solve())


if __name__ == "__main__":
    main()
