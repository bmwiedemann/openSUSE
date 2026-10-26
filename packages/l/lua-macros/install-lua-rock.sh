#!/bin/bash
set -ex

# 1. %{lua_version}
# 2. %{buildroot}%{_prefix}
# 3. %{buildroot}%{luarocks_treedir}/%{mod_name}

SOURCE_DIR="$3"
luarocks --lua-version="$1" --tree="$2" install --deps-mode=none --no-manifest "${*:$#}"

if  [ -d "${SOURCE_DIR}" ] && [ "$(find "${SOURCE_DIR}" -type f | wc -l)" -gt 0 ]
then
  mkdir -p __rocktree
  mv -v "${SOURCE_DIR}"/*/* __rocktree
fi
