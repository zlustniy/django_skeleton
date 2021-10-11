#!/usr/bin/env python

import os
import shutil
from distutils.dir_util import copy_tree

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
ONE_DIRECTORY_UP_PATH = os.path.realpath(os.path.join(PROJECT_DIRECTORY, '..'))

if __name__ == "__main__":
    copy_tree(PROJECT_DIRECTORY, ONE_DIRECTORY_UP_PATH)
    shutil.rmtree(PROJECT_DIRECTORY)
