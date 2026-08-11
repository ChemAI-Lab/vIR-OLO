'''Command line entry point for vIR-OLO.

Installing the package exposes this module's `main()` as the `virolo` console
script, so the application launches with a bare `virolo` in the terminal.
'''

import argparse
import sys

from . import __version__


def _build_parser():
    parser = argparse.ArgumentParser(
        prog="virolo",
        description="vIR-OLO - YOLO-based annotation tool for IR spectra images.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"vIR-OLO {__version__}",
    )
    return parser


def main(argv=None):
    """Launch the vIR-OLO GUI. Returns the Qt exit code."""
    _build_parser().parse_args(argv)

    # torch is imported before Qt to match the historic launch order: torch's
    # native libraries must be initialised before PyQt5/opencv load their own.
    import torch  # noqa: F401
    from PyQt5 import QtWidgets

    from .spectrai import App

    app = QtWidgets.QApplication(sys.argv[:1])
    window = App()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
