import os
import sys

import pytest

from fdiff.utils import path_exists

if sys.platform.startswith("win"):
    pytest.skip("skipping Unix only tests", allow_module_level=True)


def test_path_exists_default_dirpath_toggle_succeeds():
    assert path_exists("/dev/null", include_dir_paths=True) is True
