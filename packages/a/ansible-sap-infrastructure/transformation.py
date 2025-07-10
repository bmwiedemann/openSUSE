# This Python script updates upstream with downstream customizations before packaging.
# All customizations are defined in separate yaml file.
# List of available customizations:
# - remove_paths - Removes the specified files or directories.
# - remove_lines - Removes lines matching the patterns from the files matching specified glob patterns.
# - replace_text - Replaces text in files matching specified glob patterns.
# - update_yaml_key - Updates a specific key's value in the specified YAML files matching specified glob patterns.
# - append_yaml_list - Appends a new item to a list in the specified YAML files matching specified glob patterns.
# - set_yaml_value - Sets or replaces a specific key's value in the specified YAML files matching specified glob patterns.
# - remove_yaml_list_items - Removes specific items from a list in the specified YAML files matching specified glob patterns.

# Intended use: Executed by spec file during %prep

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
    """Removes the specified files or directories.

    This function iterates through a list of path patterns, finds all matching
    files and directories using glob, and removes them. This is useful for
    cleaning up a build directory by removing unnecessary files or directories
    before packaging.

    Args:
        build_dir (str): The absolute path to the base directory from which
            paths will be removed.
        paths (list[str]): A list of path patterns to remove. These paths are
            relative to `build_dir` and can include glob patterns (e.g., '*.txt',
            'temp/**').

    Example:
        ```yaml
        changes:
          - type: remove_paths
            paths:
              - "roles/*/meta/main.yml"
        ```
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
    """Removes lines matching the patterns from the files matching specified glob patterns.

    This function finds files matching the given glob patterns and then reads
    each file to remove any lines that match any of the specified regular
    expression patterns. This is useful for cleaning up documentation or
    configuration files by removing obsolete or unwanted content.

    Args:
        build_dir (str): The absolute path to the base directory where the
            files are located.
        files_patterns (list[str]): A list of file path patterns to process.
            These paths are relative to `build_dir` and support glob
            patterns (e.g., 'docs/*.md', 'roles/**/tasks/main.yml').
        patterns (list[str]): A list of regular expression patterns. Any line
            in the target files that matches one of these patterns will be
            removed.

    Example:
        ```yaml
        changes:
            - type: remove_lines
                files:
                - "README.md"
                - "roles/*/README.md"
                patterns:
                - "\\[Ansible Lint"
        ```
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
    """Replaces text in files matching specified glob patterns.

    
    This function finds all files matching the given patterns and performs a
    series of find-and-replace operations on their content. The 'find'
    patterns are treated as regular expressions, allowing for powerful and
    flexible text manipulation. This is useful for updating project-wide
    values like namespaces, repository URLs, or other boilerplate text.
    
    Args:
        build_dir (str): The absolute path to the base directory where the
            files are located.
        files_patterns (list[str]): A list of file path patterns to process.
            These paths are relative to `build_dir` and support glob
            patterns (e.g., 'README.md', 'roles/**/*.yml').
        replacements (list[dict[str, str]]): A list of replacement rules.
            Each rule is a dictionary with two keys:
            - 'find': The regular expression pattern to search for.
            - 'replace': The string to substitute for each match.

    Example:
        ```yaml
        changes:
            - type: replace_text
                files:
                - "galaxy.yml"
                replacements:
                - { find: "namespace: community", replace: "namespace: suse" }
        ```        
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


def update_yaml_key(build_dir, files_patterns, key_path, value):
    """Updates a specific key's value in the specified YAML files, preserving the header.

    This function finds all YAML files matching the given patterns and updates
    the value of a specified key. The key can be nested, using dot notation
    for the path (e.g., 'parent.child.key'). If the key or any part of its
    path does not exist, it will be created.

    The function is designed to preserve YAML formatting, including comments
    and indentation, by using `ruamel.yaml` and by explicitly handling
    non-YAML headers (lines before the first '---').

    Args:
        build_dir (str): The absolute path to the base directory where the
            YAML files are located.
        files_patterns (list[str]): A list of file path patterns to process,
            relative to `build_dir`. Supports glob patterns (e.g., 'galaxy.yml',
            'roles/**/meta.yml').
        key_path (str): The dot-separated path to the key to update
            (e.g., 'info.version', 'authors').
        value (any): The new value to assign to the key. This can be any
            YAML-compatible type (string, list, dictionary, etc.).

    Example:
        ```yaml
        changes:
            - type: update_yaml_key
                files:
                - "galaxy.yml"
                key: "build_ignore"
                value:
                - "tests"
        ```
    """

    for file_pattern in files_patterns:
        full_pattern = os.path.join(build_dir, file_pattern)
        for file_path in glob.glob(full_pattern):
            if os.path.exists(file_path):
                try:
                    relative_path = os.path.relpath(file_path, build_dir)
                    header_lines = read_yaml_header(file_path)
                    with open(file_path, 'r') as f:
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

                    with open(file_path, 'w') as f:
                        f.writelines(header_lines)
                        yaml.dump(data, f)

                except Exception as e:
                    print(f"Error processing YAML in {relative_path}: {e}")


def append_yaml_list(build_dir, files_patterns, list_key_path, new_item):
    """Appends a new item to a list in the specified YAML files, preserving the header.

    This function finds all YAML files matching the given patterns and appends
    a new item to a specified list. The list is identified by a dot-separated
    key path. If the list or any part of its path does not exist, it will be
    created. The function ensures the item is not added if it already exists
    in the list, preventing duplicates.

    Like other YAML modification functions in this script, it preserves
    comments and formatting by using `ruamel.yaml` and handling file headers.
    
    Args:
        build_dir (str): The absolute path to the base directory where the
            YAML files are located.
        files_patterns (list[str]): A list of file path patterns to process,
            relative to `build_dir`. Supports glob patterns.
        list_key_path (str): The dot-separated path to the list to which the
            item will be appended (e.g., 'galaxy_info.platforms').
        new_item (any): The item to append to the list. This can be a simple
            string or a more complex dictionary.

    Example:
        ```yaml
        changes:
          - type: append_yaml_list
            files:
              - "roles/*/meta/main.yml"
            list_key: "galaxy_info.platforms"
            new_item:
              name: "SLES"
              versions:
                - "15"
        ```
    """

    for file_pattern in files_patterns:
        full_pattern = os.path.join(build_dir, file_pattern)
        for file_path in glob.glob(full_pattern):
            if os.path.exists(file_path):
                try:
                    relative_path = os.path.relpath(file_path, build_dir)
                    header_lines = read_yaml_header(file_path)
                    with open(file_path, 'r') as f:
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

                    with open(file_path, 'w') as f:
                        f.writelines(header_lines)
                        yaml.dump(data, f)

                except Exception as e:
                    print(f"Error processing YAML in {relative_path}: {e}")


def set_yaml_value(build_dir, files_patterns, key_path, value):
    """Sets or replaces a specific key's value in the specified YAML files, preserving the header.

    This function finds all YAML files matching the given patterns and sets a
    specified key to a new value. The key can be nested, using dot notation
    for the path (e.g., 'parent.child.key').

    Unlike `update_yaml_key`, this function will always set the value. If the
    key or any part of its path does not exist, it will be created. This is
    useful for overwriting existing values or ensuring a key is present with
    a specific value.

    Args:
        build_dir (str): The absolute path to the base directory where the
            YAML files are located.
        files_patterns (list[str]): A list of file path patterns to process,
            relative to `build_dir`. Supports glob patterns.
        key_path (str): The dot-separated path to the key to set or create
            (e.g., 'collections', 'info.version').
        value (any): The new value to assign to the key. This can be any
            YAML-compatible type (string, list, dictionary, etc.).

    Example:
        ```yaml
        changes:
          - type: set_yaml_value
            files:
              - "special_actions/*/ansible_requirements.yml"
            key: "collections"
            value: []
        ```
    """

    for file_pattern in files_patterns:
        full_pattern = os.path.join(build_dir, file_pattern)
        for file_path in glob.glob(full_pattern):
            if os.path.exists(file_path):
                relative_path = os.path.relpath(file_path, build_dir)
                try:
                    header_lines = read_yaml_header(file_path)
                    with open(file_path, 'r') as f:
                        # Skip header lines when loading
                        for _ in header_lines:
                            next(f, None)
                        data = yaml.load(f)

                    keys = key_path.split('.')
                    current_level = data
                    for i, key in enumerate(keys):
                        if i == len(keys) - 1:
                            current_level[key] = value
                            print(f"Set key '{key_path}' in: {relative_path}")
                        else:
                            if key not in current_level:
                                current_level[key] = {}
                                print(
                                    f"Created missing key '{key}' in path '{key_path}' in: {relative_path}"
                                )
                            current_level = current_level[key]

                    with open(file_path, 'w') as f:
                        f.writelines(header_lines)
                        yaml.dump(data, f)

                except Exception as e:
                    print(f"Error processing YAML in {relative_path}: {e}")


def remove_yaml_list_items(build_dir, files_patterns, list_key_path, items_to_remove):
    """Removes specific items from a list in the specified YAML files.

    This function finds all YAML files matching the given glob patterns and
    removes specified items from a list within those files. The list is
    identified by a dot-separated key path.

    Args:
        build_dir (str): The absolute path to the base directory where the
            YAML files are located.
        files_patterns (list[str]): A list of file path patterns to process,
            relative to `build_dir`. Supports glob patterns.
        list_key_path (str): The dot-separated path to the list from which
            items will be removed (e.g., 'collections').
        items_to_remove (list[any]): A list of specification items. Any item
            in the target list that matches one of these specifications will
            be removed.

    Example:
        ```yaml
        changes:
          - type: remove_yaml_list_items
            files:
              - "deploy_scenarios/*/ansible_requirements.yml"
            list_key: "collections"
            items_to_remove:
              - name: "community.sap_install"
        ```
    """

    def item_matches(list_item, spec_item):
        """Check if a list item matches a specification item."""
        if isinstance(list_item, dict) and isinstance(spec_item, dict):
            # For dicts, check if list_item contains all key-value pairs from spec_item.
            return all(k in list_item and list_item[k] == v for k, v in spec_item.items())
        # For other types (like strings), use simple equality.
        return list_item == spec_item

    for file_pattern in files_patterns:
        full_pattern = os.path.join(build_dir, file_pattern)
        for file_path in glob.glob(full_pattern):
            if os.path.isfile(file_path):
                relative_path = os.path.relpath(file_path, build_dir)
                try:
                    header_lines = read_yaml_header(file_path)
                    with open(file_path, 'r') as f:
                        for _ in header_lines:
                            next(f, None)
                        data = yaml.load(f)

                    # Skip if there is nothing to update.
                    if data is None:
                        continue

                    keys = list_key_path.split('.')
                    current_level = data
                    modified = False
                    path_exists = True

                    for i, key in enumerate(keys):
                        if not (isinstance(current_level, dict) and key in current_level):
                            path_exists = False
                            break
                        if i < len(keys) - 1:
                            current_level = current_level[key]

                    if not path_exists:
                        print(f"Warning: Path '{list_key_path}' not found in {relative_path}. Skipping.")
                        continue

                    list_key = keys[-1]
                    if isinstance(current_level[list_key], list):
                        target_list = current_level[list_key]
                        initial_len = len(target_list)
                        new_list = [item for item in target_list if not any(item_matches(item, rem_spec) for rem_spec in items_to_remove)]
                        if len(new_list) < initial_len:
                            current_level[list_key] = new_list
                            print(f"Removed {initial_len - len(new_list)} item(s) from list '{list_key_path}' in: {relative_path}")
                            modified = True

                    if modified:
                        with open(file_path, 'w') as f:
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
        elif change_type == 'set_yaml_value':
            set_yaml_value(build_dir, change.get('files', []), change.get('key'), change.get('value'))
        elif change_type == 'remove_yaml_list_items':
            remove_yaml_list_items(build_dir, change.get('files', []), change.get('list_key'), change.get('items_to_remove'))
        else:
            print(f"Unknown changes type: {change['type']}")


if __name__ == "__main__":
    main()
