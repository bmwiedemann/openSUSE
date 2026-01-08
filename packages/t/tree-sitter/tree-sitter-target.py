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

def apply_conditions(target: Dict):
    """Apply conditions from binding.gyp to the target dictionary."""
    if 'conditions' not in target:
        return

    # Check for any valid scanner extension in the src directory
    scanner_extensions = ('.c', '.cc', '.cpp', '.cxx')
    has_scanner = any(
        Path('src').joinpath(f'scanner{ext}').exists()
        for ext in scanner_extensions
    )

    for condition_block in target['conditions']:
        condition = condition_block[0]
        action = condition_block[1]

        # Handle the dynamic addition of scanner sources
        if condition == "has_scanner=='true'" and has_scanner:
            if 'sources+' in action:
                if 'sources' not in target:
                    target['sources'] = []
                for source in action['sources+']:
                    if source not in target['sources']:
                        target['sources'].append(source)

        # Assuming non-windows as per user's environment
        if condition == "OS!='win'":
            for flag_type in ['cflags_c', 'cflags_cc']:
                if flag_type in action:
                    if flag_type not in target:
                        target[flag_type] = []
                    for flag in action[flag_type]:
                        if flag not in target[flag_type]:
                            target[flag_type].append(flag)


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
    if 'cflags_cc' in target:
        cflags_cc = target['cflags_cc']

    sources = target['sources']

    include_dirs = []
    for include_dir in target['include_dirs']:
        # Don't include any node commands
        if not include_dir.startswith('<!'):
            include_dirs+=[ include_dir ]

    if not grammars:
        grammars = { "src" }
    for _grammar in grammars:
        command = copy(base_command)
        seen_sources = set()

        for include_dir in include_dirs:
            command += '-I', include_dir

        for source_str in sources:
            source = Path(source_str)

            # STRENGHTENED SKIP: Skip if 'node' is anywhere in the path
            if 'node' in source.parts or 'bindings' in source.parts:
                continue

            # Skip if we've already seen this file
            if str(source) in seen_sources:
                continue

            # Only include if it belongs to the grammar (or default 'src')
            if _grammar == "src" or source.parts[0] == _grammar:
                if any(source.name.endswith(s) for s in suffixes_cc):
                    command += ['-xc++', str(source)]
                    seen_sources.add(str(source))
                elif source.name.endswith('.c'):
                    command += ['-xc', str(source)]
                    seen_sources.add(str(source))
        for flag in cflags_c, cflags_cc:
            if flag:
                command += flag
        commands[_grammar] = command
    return commands


apply_conditions(targets)

if not args.grammars:
    args.grammars = ["src"]

cc_cmd = buildCompileCommand(targets, args.grammars)
for grammar in args.grammars:
    print(*cc_cmd[grammar])
