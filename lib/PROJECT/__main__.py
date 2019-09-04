#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

from {{ PROJECT }} import __version__


def main():  # pragma: no cover
    run(sys.argv[1:])


def run(argv):
    # ===========================================================
    # argparse command line argument definitions
    # ===========================================================
    parser = argparse.ArgumentParser(
        description="{{ DESCRIPTION }}"
    )
    parser.add_argument(
        "--version", action="version", version="{{ PROJECT }} v{}".format(__version__)
    )
    args = parser.parse_args(argv)
