# This Python script updates downstream collection details before execution of ansible-galaxy build.
# Intended use: Executed by RPM spec file during %prep

import os
import shutil
import re
import glob
import argparse

# Requires entry in spec file: BuildRequires: python3-ruamel.yaml
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True  # Preserves quotes
yaml.indent(mapping=2, sequence=4, offset=2)  # Preserves indents in yaml
yaml.width = 4096  # Disable ruamel wrapping long lines


def load_config(config_file):
    """Loads the configuration from a YAML file.
    """
    with open(config_file, 'r') as f:
        return yaml.load(f)


def remove_paths(build_dir, paths):
    """Removes the specified files or directories within the build directory.

    Args:
        build_dir (str): The base directory where the files/directories are located.
        paths (list): A list of path patterns (relative to build_dir) to remove.
                      These can be file paths or directory paths.
                      Supports glob patterns.
    """
    for path_pattern in paths:
        full_pattern = os.path.join(build_dir, path_pattern)
        for item in glob.glob(full_pattern):
            relative_path = os.path.relpath(item, build_dir)
            if os.path.isdir(item):
                print(f"Removed: {relative_path}")
                shutil.rmtree(item, ignore_errors=True)
            elif os.path.isfile(item):
                print(f"Removed: {relative_path}")
                os.remove(item)


def remove_lines(build_dir, files_patterns, patterns):
    """Removes lines matching the patterns from the specified files within the build directory.

    Args:
        build_dir (str): The base directory where the files are located.
        files_patterns (list): A list of file path patterns (relative to build_dir) to modify.
                               Supports glob patterns.
        patterns (list): A list of regular expression patterns.
                         Lines matching any of these patterns will be removed.
    """
    for file_pattern in files_patterns:
        full_pattern = os.path.join(build_dir, file_pattern)
        for file_path in glob.glob(full_pattern):
            if os.path.isfile(file_path):
                relative_path = os.path.relpath(file_path, build_dir)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                updated_lines = [
                    line
                    for line in lines
                    if not any(re.search(pattern, line) for pattern in patterns)
                ]
                with open(file_path, 'w') as f:
                    f.writelines(updated_lines)
                print(f"Removed lines from: {relative_path}")


def replace_text(build_dir, files_patterns, replacements):
    """Replaces text in the specified files within the build directory.

    Args:
        build_dir (str): The base directory where the files are located.
        files_patterns (list): A list of file path patterns (relative to build_dir) to modify.
                               Supports glob patterns.
        replacements (list): A list of dictionaries, each with 'find' and 'replace' keys.
                             'find' is the regular expression pattern to search for.
                             'replace' is the text to replace it with.
    """
    for file_pattern in files_patterns:
        full_pattern = os.path.join(build_dir, file_pattern)
        for file_path in glob.glob(full_pattern):
            if os.path.isfile(file_path):
                relative_path = os.path.relpath(file_path, build_dir)
                with open(file_path, 'r') as f:
                    content = f.read()
                for replacement in replacements:
                    content = re.sub(
                        replacement['find'],
                        replacement['replace'],
                        content,
                        flags=re.MULTILINE,
                    )
                with open(file_path, 'w') as f:
                    f.write(content)
                print(
                    f"Replaced text {replacement['find']} with {replacement['replace']} in: {relative_path}"
                )


def read_yaml_header(file_path):
    """Reads the header of a YAML file (lines before the first '---').

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        list: A list of lines representing the header of the YAML file.
    """
    header_lines = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip() == '---':
                header_lines.append(line)
                break
            header_lines.append(line)
    return header_lines


def update_yaml_key(build_dir, files, key_path, value):
    """Updates a specific key's value in the specified YAML files, preserving the header.

    Args:
        build_dir (str): The base directory where the YAML files are located.
        files (list): A list of file paths (relative to build_dir) to modify.
        key_path (str): The path to the key to update, using dot notation (e.g., 'a.b.c').
        value (any): The new value to set for the specified key.
    """
    for file_path in files:
        full_path = os.path.join(build_dir, file_path)
        if os.path.exists(full_path):
            try:
                relative_path = os.path.relpath(full_path, build_dir)
                header_lines = read_yaml_header(full_path)
                with open(full_path, 'r') as f:
                    # Skip header lines when loading
                    for _ in header_lines:
                        next(f, None)
                    data = yaml.load(f)

                keys = key_path.split('.')
                current_level = data
                for i, key in enumerate(keys):
                    if i == len(keys) - 1:
                        if key not in current_level:
                            print(
                                f"Warning: Key '{key_path}' not found in {relative_path}"
                            )
                        else:
                            current_level[key] = value
                            print(f"Updated key '{key_path}' in: {relative_path}")
                    else:
                        if key not in current_level:
                            current_level[key] = {}
                            print(
                                f"Created missing key '{key}' in path '{key_path}' in: {relative_path}"
                            )
                        current_level = current_level[key]

                with open(full_path, 'w') as f:
                    f.writelines(header_lines)
                    yaml.dump(data, f)

            except Exception as e:
                print(f"Error processing YAML in {relative_path}: {e}")


def append_yaml_list(build_dir, files, list_key_path, new_item):
    """Appends a new item to a list in the specified YAML files, preserving the header.

    Args:
        build_dir (str): The base directory where the YAML files are located.
        files (list): A list of file paths (relative to build_dir) to modify.
        list_key_path (str): The path to the list to append to, using dot notation (e.g., 'a.b.c').
        new_item (any): The new item to append to the list.
    """
    for file_path in files:
        full_path = os.path.join(build_dir, file_path)
        if os.path.exists(full_path):
            try:
                relative_path = os.path.relpath(full_path, build_dir)
                header_lines = read_yaml_header(full_path)
                with open(full_path, 'r') as f:
                    # Skip header lines when loading
                    for _ in header_lines:
                        next(f, None)
                    data = yaml.load(f)

                keys = list_key_path.split('.')
                current_level = data
                for i, key in enumerate(keys):
                    if i == len(keys) - 1:
                        if key not in current_level:
                            current_level[key] = []
                            print(
                                f"Created missing list '{list_key_path}' in: {relative_path}"
                            )
                        if isinstance(current_level[key], list):
                            if new_item not in current_level[key]:
                                current_level[key].append(new_item)
                                print(
                                    f"Appended item to list '{list_key_path}' in: {relative_path}"
                                )
                            else:
                                print(
                                    f"Item '{new_item}' already exists in list '{list_key_path}' in: {relative_path}"
                                )
                    else:
                        if key not in current_level:
                            current_level[key] = {}
                            print(
                                f"Created missing key '{key}' in path '{list_key_path}' in: {relative_path}"
                            )
                        current_level = current_level[key]

                with open(full_path, 'w') as f:
                    f.writelines(header_lines)
                    yaml.dump(data, f)

            except Exception as e:
                print(f"Error processing YAML in {relative_path}: {e}")


def main():
    """Main function to load config and apply changes."""
    parser = argparse.ArgumentParser(description="Change files in a specified directory based on a configuration file.")
    parser.add_argument("--build_dir", help="The path to the build directory where changes will occur." )
    parser.add_argument("--config", help="The path to the configuration YAML file (default: config.yaml)." )
    args = parser.parse_args()

    config_file = args.config
    build_dir = args.build_dir

    if not os.path.isdir(build_dir):
        print(f"Error: Build directory '{build_dir}' does not exist.")
        return

    config = load_config(config_file)
    changes = config.get('changes', [])

    for change in changes:
        change_type = change.get('type')
        if change_type == 'remove_paths':
            remove_paths(build_dir, change.get('paths', []))
        elif change_type == 'remove_lines':
            remove_lines(build_dir, change.get('files', []), change.get('patterns', []))
        elif change_type == 'replace_text':
            replace_text(build_dir, change.get('files', []), change.get('replacements', []))
        elif change_type == 'update_yaml_key':
            update_yaml_key(build_dir, change.get('files', []), change.get('key'), change.get('value'))
        elif change_type == 'append_yaml_list':
            append_yaml_list(build_dir, change.get('files', []), change.get('list_key'), change.get('new_item'))
        else:
            print(f"Unknown changes type: {change['type']}")


if __name__ == "__main__":
    main()
