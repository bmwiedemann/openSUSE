#!/usr/bin/env python3

import argparse
import subprocess
from pathlib import Path

PREFIX = '/usr/share/libreoffice'
DATADIR = '/usr/share'
LIBDIRS = (
    Path('/usr/lib/'),
    Path('/usr/lib64/'),
    Path('/usr/lib32/'),
)
LEFTOVER_DIRS = (
    Path('/usr/share/libreoffice/help'),
    Path('/usr/share/libreoffice/program'),
    Path('/usr/share/libreoffice/share'),
    Path('/usr/share/libreoffice'),
)

parser = argparse.ArgumentParser(description='This script (un)links or unlinks the given to/from libreoffice home')
parser.add_argument('filelist', help='List of files')
parser.add_argument('--unlink', action='store_true', help='Unlink the files during package removal')
args = parser.parse_args()

files = sorted([Path(x) for x in open(args.filelist).read().splitlines() if x.startswith(PREFIX)])


def get_relative_folder(file, libdir):
    try:
        return libdir / file.relative_to(DATADIR)
    except ValueError:
        return None


for libdir in LIBDIRS:
    # for each dir verify there is libreoffice folder, otherwise skip
    lodir = libdir / 'libreoffice'
    if not lodir.is_dir():
        continue

    # Decide if we are linking or wiping first
    if args.unlink:
        for file in files:
            link = get_relative_folder(file, libdir)
            if link:
                # first just remove the symlinks
                if link.is_symlink() and not link.is_dir():
                    link.unlink()

                # continue by wiping out all EMPTY dirs
                # we have to be sure it is not owned by anything else
                # doing in 2nd run to ensure avoiding collisions
                if link.is_dir() and not any(link.iterdir()):
                    r = subprocess.run(f'rpm -qf {file}', shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                    if not r.stdout:
                        link.rmdir()
    else:
        for file in files:
            # if we get ourselves folder then just create it
            # it might not be around so lets be safe
            link = get_relative_folder(file, libdir)
            if link:
                if file.is_dir():
                    if not link.exists():
                        link.mkdir(parents=True)
                        link.chmod(file.stat().st_mode)
                else:
                    # if the file is already there, skip it
                    # this is true when the parent folder is link
                    if not link.exists():
                        link.symlink_to(file)

    for leftover in LEFTOVER_DIRS:
        if leftover.is_dir() and not any(leftover.iterdir()):
            leftover.rmdir()

    # remove dangling links as they might happen when migratin from older
    # libreoffice versions
    # Run find directly as it's faster than os.walk run and a os.path.islink!
    subprocess.run(f'find {str(lodir)} -type l -xtype l -delete',
                   shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
