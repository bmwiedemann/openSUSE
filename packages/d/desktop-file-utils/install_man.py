#!/usr/bin/env python3

import os

os.symlink(
    'desktop-file-install.1',
    os.getenv('MESON_INSTALL_DESTDIR_PREFIX') + '/share/man/man1/desktop-file-edit.1'
)
