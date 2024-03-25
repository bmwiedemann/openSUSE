#!/usr/bin/python3
# SPDX-License-Identifier: GPL-2.0
# SPDX-FileCopyrightText: 2024 Björn Bidar

"""Generate compile commands by reading binding.gyp"""

# pylint: disable=invalid-name
# pylint: disable=too-many-branches

import argparse
from pathlib import Path
from typing import List, Dict, Optional
import ast
from copy import copy

parser = argparse.ArgumentParser(prog = Path(__file__).name,
                                 description = "Generate compile commands by reading binding.gyp")
parser.add_argument('-b', '--binding', dest = "binding",
                    action="store", help="Path to binding file")
parser.add_argument('-g', '--grammar', dest = "grammars",
                    action= "append",
                    required = False,
                    help="Specify grammars in case binding file contains more than one grammar")

args = parser.parse_args()

if args.binding:
    binding_gyp = Path(args.binding)
else:
    binding_gyp = Path("binding.gyp")

if not binding_gyp.exists():
    raise FileNotFoundError(f"bindings {binding_gyp.absolute()} not found")


with open(binding_gyp, 'r', encoding='utf8') as binding_raw:
    binding = ast.literal_eval(binding_raw.read())

targets = binding['targets'][0]

def buildCompileCommand(target: Dict, grammars: Optional[List[str]] = None) -> Dict[
        str,
        List
]:
    """Generate compile commands from TARGET supplied found in GRAMMARS or src"""
    cc = 'cc'
    cflags_c = []
    cflags_cc = []
    commands = {}
    base_command = [ cc, '-shared', '-fPIC']
    suffixes_cc = ['cc', 'cxx', 'cpp']
    if 'cflags_c' in target:
        cflags_c = target['cflags_c']
    if 'clfags_cc' in target:
        cflags_cc = target['cflags_cc']

    include_dirs = []
    for include_dir in target['include_dirs']:
        # Don't include any node commands
        if not include_dir.startswith('<!'):
            include_dirs+=[ include_dir ]

    if not grammars:
        grammars = { "src" }
    for _grammar in grammars:
        command = copy(base_command)
        for include_dir in include_dirs:
            command += '-I', include_dir
        for source in target['sources']:
            source = Path(source)
            # We don't need node bindings
            if source.parts[0] == "node":
                continue
            if not source.parts[0] == _grammar:
                continue
            for suffix_cc in suffixes_cc:
                if source.name.endswith(suffix_cc):
                    command+= '-xc++', source
                    break
            if source.name.endswith('.c'):
                command+= '-xc', source
        for flag in cflags_c, cflags_cc:
            if flag:
                command += flag
        commands[_grammar] = command
    return commands

if not args.grammars:
    args.grammars = ["src"]

cc_cmd = buildCompileCommand(targets, args.grammars)
for grammar in args.grammars:
    print(*cc_cmd[grammar])
