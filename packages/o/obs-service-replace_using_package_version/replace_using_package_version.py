#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 SUSE Linux GmbH.  All rights reserved.
#
# This file is part of obs-service-replace_using_package_version.
#
#   obs-service-replace_using_package_version is free software: you can
#   redistribute it and/or modify it under the terms of the GNU General
#   Public License as published by the Free Software Foundation, either
#   version 3 of the License, or (at your option) any later version.
#
#   obs-service-replace_using_package_version is distributed in the hope
#   that it will be useful, but WITHOUT ANY WARRANTY; without even the
#   implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#   See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with obs-service-replace_using_package_version.  If not,
#   see <http://www.gnu.org/licenses/>.
#
"""
replace_with_package_version.py

Usage:
    replace_using_package_version.py -h
    replace_using_package_version.py --regex=REGEX --outdir=DIR
        [--file=FILE]
        (--package=PACKAGE | --replacement=REPLACEMENT)
        [--parse-version=DEPTH]

Options:
    -h,--help                   : show this help message
    --outdir=DIR                : output directory
    --file=FILE                 : file to update
                                    The default build recipe file
                                    (e.g. Dockerfile) is used when this
                                    parameter is omitted.
    --package=PACKAGE           : package to check
    --replacement=REPLACEMENT   : replacement string for any match
    --regex=REGEX               : regular expression for parsing file
    --parse-version=DEPTH       : parse the package version string to match
                                    major.minor.patch.patch_update format.
                                    It can be set to 'major', 'minor',
                                    'patch', 'patch_update' and 'offset'.
"""
from typing import Optional
import docopt
import re
import os
import subprocess
from pkg_resources import parse_version
from typing import List

version_regex = {
    'major': r'^(\d+)',
    'minor': r'^(\d+(\.\d+){0,1})',
    'patch': r'^(\d+(\.\d+){0,2})',
    'patch_update': r'^(\d+(\.\d+){0,3})',
    'offset': r'^(?:\d+(?:\.\d+){0,3})[+-.~](?:git|svn|cvs)(\d+)'
}
obsinfo_regex = r'version: (.+)'


def guess_recipe_filename_from_env() -> Optional[str]:
    """Try to infer the default build recipe file from the current build
    environment.

    The `build <https://github.com/openSUSE/obs-build>`_ script sets the
    environment variable ``BUILD_DIST`` to the location of the
    :file:`build.dist`. The same directory contains the file
    :file:`build.data`, which contains environment variables to be sourced via
    :command:`bash` or :command:`sh`. One of these is ``RECIPEFILE`` which
    contains the name of the current build recipe, with the tiny catch that it
    will be called :file:`_service:actual_name` although the build script
    already renamed the actual file to :file:`actual_name`.

    """
    build_dist = os.getenv("BUILD_DIST")
    if build_dist is None or build_dist[-5:] != ".dist":
        return None

    # Extract the variable RECIPEFILE from `build.data`
    recipefile = None
    with open(build_dist[:-5] + ".data") as data:
        for line in data:
            # lines are:
            # FOOBAR='baz'
            # => need to also remove the ' or " from the second column
            var, val = line.strip().split("=")
            if var == "RECIPEFILE":
                recipefile = val.replace("'", "").replace('"', '')

    if recipefile is None:
        return None

    # strip the leading `_service:` part
    return recipefile.split(":")[-1]


def main():
    """
    main-entry point for program, expects dict with arguments from docopt()
    """
    # TODO: probably there is a better way to set the repositories path
    rpm_dir = './repos'

    command_args = docopt.docopt(__doc__)

    src_file = command_args['--file']

    if src_file is None:
        src_file = guess_recipe_filename_from_env()
        if src_file is None:
            raise RuntimeError(
                "No file was provided and could not infer a default build file"
            )

    if not os.path.isfile(src_file):
        raise RuntimeError('File {0} not found'.format(src_file))

    if not os.path.isdir(command_args['--outdir']):
        raise Exception(
            'Output directory {0} not found'.format(command_args['--outdir'])
        )

    filecopy = os.path.join(
        command_args['--outdir'], os.path.basename(src_file)
    )

    if command_args['--package']:
        parse_version = command_args['--parse-version']
        version = find_package_version(command_args['--package'], rpm_dir)
        if parse_version and parse_version not in version_regex.keys():
            raise Exception((
                'Invalid value for this flag. Expected format is: '
                '--parse-version=[major|minor|patch|patch_update|offset]'
            ))
        elif parse_version:
            version = find_match_in_version(
                version_regex[parse_version], version
            )
        replacement = version
    else:
        replacement = command_args['--replacement']

    apply_regex_to_file(
        src_file,
        filecopy,
        command_args['--regex'],
        replacement
    )


def apply_regex_to_file(input_file, output_file, regex, replacement):
    with open(input_file, 'r') as in_file:
        contents = in_file.read()

    with open(output_file, 'w') as out_file:
        out_file.write(re.sub(regex, replacement, contents))


def find_package_version(package, rpm_dir):
    version = None
    try:
        version = get_pkg_version(package)
    except Exception:
        version = find_package_version_in_local_repos(rpm_dir, package)

    if version is None:
        version = find_package_version_in_obsinfo('.', package)

    if version is None:
        raise Exception('Package version not found')
    return str(version)


def find_package_version_in_local_repos(repo_path, package):
    version = None
    for root, _, files in os.walk(repo_path):
        packages = [
            f for f in files if f.endswith('rpm') and package in f
        ]
        for pkg in packages:
            rpm_file = os.path.join(root, pkg)
            if get_pkg_name_from_rpm(rpm_file) == package:
                rpm_ver = get_pkg_version_from_rpm(rpm_file)
                if version is None or rpm_ver >= version:
                    version = rpm_ver
    return version


def find_package_version_in_obsinfo(path, package):
    version = None
    for f in os.listdir(path):
        if f.endswith('obsinfo') and package in f:
            obsinfo_ver = get_pkg_version_from_obsinfo(f)
            if version is None or obsinfo_ver >= version:
                version = obsinfo_ver
    return version


def find_match_in_version(regexpr, version):
    search = re.search(regexpr, version)
    if search is None:
        return version
    else:
        return search.group(1)


def run_command(command: List[str]) -> str:
    return subprocess.check_output(command).decode()


def get_pkg_version_from_obsinfo(obsinfo_file):
    regex = re.compile(obsinfo_regex)
    with open(obsinfo_file) as f:
        for line in f:
            match = regex.match(line)
            if match:
                return parse_version(match[1])
    return None


def get_pkg_name_from_rpm(rpm_file):
    command = [
        'rpm', '-qp', '--queryformat', '%{NAME}', rpm_file
    ]
    return run_command(command)


def get_pkg_version_from_rpm(rpm_file):
    command = [
        'rpm', '-qp', '--queryformat', '%{VERSION}', rpm_file
    ]
    return parse_version(run_command(command))


def get_pkg_version(package):
    command = [
        'rpm', '-q', '--queryformat', '%{VERSION}', package
    ]
    return parse_version(run_command(command))


def init(__name__):
    if __name__ == '__main__':
        main()


init(__name__)
