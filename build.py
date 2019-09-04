#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import toml

TEMPLATE_DIRS = os.path.join("lib", "PROJECT")

TEMPLATE_FILES = (
    "setup.py",
    "Makefile",
    ".travis.yml",
    os.path.join("lib", "PROJECT", "__main__.py"),
)

README_FILE = "README.md"

PROJECT = "{{ PROJECT }}"
DESCRIPTION = "{{ DESCRIPTION }}"
AUTHOR = "{{ AUTHOR }}"
EMAIL = "{{ EMAIL }}"
URL = "{{ URL }}"
MIN_PY = "{{ PYTHON }}"
LICENSE = "{{ LICENSE }}"

try:
    with open("project.toml") as f:
        settings = toml.load(f)
except Exception as e:
    sys.stderr.write(
        "[ERROR] Failed to read the project.toml settings file with error: {}{}".format(
            str(e), os.linesep
        )
    )
    sys.exit(1)

assert "project" in settings and settings["project"] != ""
assert "description" in settings and settings["description"] != ""
assert "author" in settings and settings["author"] != ""
assert "email" in settings and settings["email"] != ""
assert "url" in settings and settings["url"] != ""
assert "min_python" in settings and settings["min_python"] != ""
assert "license" in settings and settings["license"] != ""

# Introduction
print("Starting '{}' build...".format(settings["project"]))
# replace template strings in files with user settings
for filepath in TEMPLATE_FILES:
    with open(filepath, "r") as fr:
        file_text = fr.read()

    file_text = file_text.replace(PROJECT, settings["project"])
    file_text = file_text.replace(DESCRIPTION, settings["description"])
    file_text = file_text.replace(AUTHOR, settings["author"])
    file_text = file_text.replace(EMAIL, settings["email"])
    file_text = file_text.replace(URL, settings["url"])
    file_text = file_text.replace(MIN_PY, settings["min_python"])
    file_text = file_text.replace(LICENSE, settings["license"])

    with open(filepath, "w") as fw:
        fw.write(file_text)
    print("[*] Built template: {}".format(filepath))

# update library path name
os.rename(TEMPLATE_DIRS, os.path.join("lib", settings["project"]))
print("[*] Changed library directory name to: '{}'".format(settings["project"]))

# update README.md text
with open(README_FILE, "w") as fw:
    fw.write("## {}{}".format(settings["project"], os.linesep))
    print("[*] Updated README.md file with project name")

print("[*] Build complete!")
print("OK to remove the build.py and project.toml files")
