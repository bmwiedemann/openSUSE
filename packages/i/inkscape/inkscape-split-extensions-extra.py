#!/usr/bin/env python3
# List all files, that depend on base_extra_modules, explicitly or implicitly.
import os
import pathlib
import re
import sys

# Search all .py files that are imported by mentioned modules.
def make_deplist(inx_list, module_list):
    modules = set()
    inx_regex = re.compile(rf">(.+)\.py</(dependency|command)>")

    for entry in inx_list:
        with open(os.path.join(".", entry), encoding="utf-8") as file:
            for line in file:
                match = inx_regex.search(line)
                if (match and match.group(1)
                    and match.group(1) not in module_list):
                    modules.add(match.group(1))

    for module in module_list.union(modules):
        name = os.path.join(".", f"{module}.py")
        if os.path.isfile(name):
            with open(name, encoding="utf-8") as file:
                for line in file:
                    match = re.match(r"from (.+) import", line)
                    if not match:
                        match = re.match(r"import ([^#]+).*? *", line)

                    if match and match.group(1):
                        needle = re.sub(r"as .+", "", match.group(1)).strip()

                        if (needle not in module_list.union(modules)
                            and os.path.isfile(f"{needle}.py")):
                            modules.add(needle)

    return modules

if __name__ == "__main__":
    work_dir = pathlib.Path(os.getcwd())
    os.chdir(sys.argv[1])
    prefix = sys.argv[2]

    base_extra_modules = set(["lxml", "numpy", "scour", "xml"])
    extra_modules = set()

    prev_modules = base_extra_modules
    while True:
        prev_module_regex = rf"({'|'.join(map(re.escape, prev_modules))})"
        import_regex = re.compile(rf"(import|from).* {prev_module_regex}")

        next_modules = set()

        # Search all .py files importing one of the mentioned modules.
        for entry in pathlib.Path(".").glob("**/*.py"):
            with entry.open(encoding="utf-8") as file:
                for line in file:
                    if import_regex.search(line):
                        name = str(entry.as_posix())

                        module = name.split(os.sep, 1)[0]
                        if module.endswith(".py"):
                            module = entry.stem
                        if module not in next_modules:
                            next_modules.add(module)

        prev_modules = next_modules
        if extra_modules.issuperset(prev_modules):
            break
        extra_modules.update(prev_modules)


    std_inx = set()
    extra_inx = set()

    # We have a complete list of .py files dependent on base_extra_modules.
    # Now we need a list of .inx module descriptors.
    inx_regex = re.compile(rf'({"|".join(map(re.escape, extra_modules))})\.py')

    for entry in pathlib.Path(".").iterdir():
        if entry.is_file() and entry.suffix == ".inx":
            with entry.open(encoding="utf-8") as file:
                for line in file:
                    if inx_regex.search(line):
                        extra_inx.add(entry.name)

            # inx files that do not belong in extra_inx.
            if entry.name not in extra_inx:
                std_inx.add(entry.name)


    # Now create list of .py files that should belong in the std package.
    std_modules = make_deplist(std_inx, set())

    # Now create list of .py files that are required by extra modules
    # (If no std module needs it, then they will belong in the extra package).
    extradep_modules = make_deplist(extra_inx, extra_modules)


    # And now verify everything and generate final list.
    exclusion_regex = re.compile(r"^(cdr|fig|.*gimp|scribus)")

    std_list = work_dir / "inkscape.lst"
    extra_list = work_dir / "inkscape-extensions-extra.lst"

    with std_list.open("w", encoding="utf-8") as file:
        for inx in std_inx:
            if not exclusion_regex.match(inx):
                print(f"{prefix}{inx}", file=file)
    with extra_list.open("w", encoding="utf-8") as file:
        for inx in extra_inx:
            if not exclusion_regex.match(inx):
                print(f"{prefix}{inx}", file=file)


    with std_list.open("a", encoding="utf-8") as std_file, extra_list.open("a", encoding="utf-8") as extra_file:
        for entry in pathlib.Path(".").iterdir():
            if entry.is_file() and entry.suffix == ".py":
                name = str(entry.as_posix())
                if exclusion_regex.match(name):
                    pass
                elif entry.is_file() and entry.stem in extra_modules:
                    print(f"{prefix}{entry.name}", file=extra_file)
                elif entry.is_file() and entry.stem in std_modules:
                    print(f"{prefix}{entry.name}", file=std_file)
                elif entry.is_file() and entry.stem in extradep_modules:
                    print(f"{prefix}{entry.name}", file=extra_file)
                else:
                    print(f"ERROR: Undecided file {name}", file=sys.stderr)
            elif entry.is_dir():
                if entry.name in extra_modules:
                    print(f"{prefix}{entry.name}/", file=extra_file)
                elif entry.name in std_modules:
                    print(f"{prefix}{entry.name}/", file=std_file)
                elif entry.name in extradep_modules:
                    print(f"{prefix}{entry.name}/", file=extra_file)
