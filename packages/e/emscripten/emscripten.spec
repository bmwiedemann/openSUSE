#
# spec file for package emscripten
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# emcc expects exactly this LLVM major (EXPECTED_LLVM_VERSION in tools/shared.py)
%define llvm_major 23
Name:           emscripten
Version:        6.0.3
Release:        0
Summary:        LLVM-to-WebAssembly compiler toolchain
# Legal-Review-Notice: licences of the files installed under /usr/share/emscripten
# - MIT OR NCSA: emscripten; MIT: musl, mimalloc, SIMDe, acorn npm modules
# - Apache-2.0 WITH LLVM-exception AND NCSA (legacy code, as llvm23 declares): libc++, libc++abi,
#   libunwind, compiler-rt, llvm-libc, openmp
# - Apache-2.0: Khronos platform headers, closure externs; SGI-B-2.0: GL/glu.h; HPND: X11 headers
# - MPL-2.0: third_party/WebIDL.py; BSD-2-Clause: terser; BSD-3-Clause: cmake modules, ittnotify
# - CC0-1.0: dlmalloc, wasi/api.h; Unlicense: tools/filelock.py; Zlib: SDL/GLFW headers, gl-matrix
# - public domain: websocket_to_posix_proxy sha1, musl crypt_blowfish, compat/sys/timeb.h
# - LGPL-2.1-only: tools/ports/mpg123/mpg123.h; libpng-2.0: tools/ports/libpng/pnglibconf.h
# - SDL/SDL.h names LGPL-2 in stale prose only; its licence header is Zlib
# - test/ (GPL test/third_party included), site/ and docs/ except docs/emcc.txt are not installed
License:        (MIT OR NCSA) AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND HPND AND LGPL-2.1-only AND MIT AND MPL-2.0 AND NCSA AND SGI-B-2.0 AND LicenseRef-SUSE-Public-Domain AND Unlicense AND Zlib AND libpng-2.0
URL:            https://emscripten.org
Source0:        https://github.com/emscripten-core/emscripten/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source99:       %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE emscripten-html-minifier-optional.patch -- html-minifier-terser is not packaged; skip HTML minification instead of failing
Patch0:         emscripten-html-minifier-optional.patch
# Source-Binary-Exception: emscripten-*.tar.gz:emscripten-*/test/other/*.wasm -- test-data: inputs the emsize and wasm-sourcemap tests only read; test/ is not installed
# Source-Binary-Exception: emscripten-*.tar.gz:emscripten-*/tools/pylauncher/pylauncher.exe -- other-platform: Windows launcher, not installed
BuildRequires:  binaryen >= 129
BuildRequires:  clang%{llvm_major}
BuildRequires:  fdupes
BuildRequires:  lld%{llvm_major}
BuildRequires:  llvm%{llvm_major}
BuildRequires:  local-npm-registry
BuildRequires:  nodejs >= 18.3.0
BuildRequires:  pkgconfig
BuildRequires:  python3-base >= 3.10
BuildRequires:  python3-ply
BuildRequires:  pkgconfig(stb)
Requires:       binaryen >= 129
Requires:       clang%{llvm_major}
Requires:       lld%{llvm_major}
Requires:       llvm%{llvm_major}
Requires:       nodejs >= 18.3.0
Requires:       python3-base >= 3.10
# third_party/stb_image.h includes it
Requires:       pkgconfig(stb)
Recommends:     python3-ply
Provides:       bundled(compiler-rt) = 22.1.8
Provides:       bundled(dlmalloc) = 2.8.6
Provides:       bundled(libcxx) = 21.1.8
Provides:       bundled(libcxxabi) = 21.1.8
Provides:       bundled(libunwind) = 22.1.8
Provides:       bundled(llvm-libc) = 21.1.8
Provides:       bundled(mimalloc) = 3.3.1
Provides:       bundled(musl) = 1.2.6
Provides:       bundled(openmp) = 21.1.8
Provides:       bundled(simde) = 0.8.2
Provides:       bundled(socket.io-client) = 0.9.11
Provides:       bundled(terser) = 5.18.2
BuildArch:      noarch
%include %{_sourcedir}/node_modules.spec.inc

%description
Emscripten compiles C and C++ to WebAssembly and JavaScript using LLVM
and Binaryen. It provides emcc/em++ as drop-in compiler drivers plus
wrappers for ar, ranlib, configure, make and cmake.

This package uses the system clang, lld and binaryen. The C/C++ runtime
libraries are built on first use into ~/.cache/emscripten (override with
EM_CACHE). Configuration is read from %{_datadir}/emscripten/.emscripten;
set EM_CONFIG to use another file. The Closure Compiler (--closure) is
not included.

%prep
%autosetup -p1
# only the runtime npm modules emcc needs for JS optimisation are vendored
npm pkg delete devDependencies dependencies.google-closure-compiler dependencies.html-minifier-terser
cp %{SOURCE10} package-lock.json
local-npm-registry %{_sourcedir} install --omit=dev --ignore-scripts
# expect the binaryen the smoke tests run against, so -Werror links do not fail on -Wversion-check
sed -i "s/^EXPECTED_BINARYEN_VERSION = .*/EXPECTED_BINARYEN_VERSION = $(rpm -q --qf '%%{VERSION}' binaryen)/" tools/building.py

%build
python3 tools/maint/create_entry_points.py

%install
d=%{buildroot}%{_datadir}/%{name}
install -d $d/docs
cp -a cmake html media node_modules src system third_party tools em* $d/
cp -a docs/emcc.txt $d/docs/
# not used at run time; ply comes from python3-ply
rm -r $d/tools/maint $d/tools/install.py $d/tools/pylauncher \
      $d/third_party/jni $d/third_party/ply $d/third_party/stb_image.h \
      $d/system/lib/update_*.py $d/system/lib/push_*.py $d/system/lib/libc/update_alltypes.sh \
      $d/system/lib/libc/musl/configure $d/system/lib/libcxxabi/src/demangle/cp-to-llvm.sh \
      $d/system/lib/libcxx/tags \
      $d/node_modules/.bin $d/node_modules/.package-lock.json
find $d \( -name .clang-format -o -name .clang-tidy -o -name .gitignore \) -delete
# scons tool modules, imported rather than run
sed -i '1{/^#!/d}' $d/tools/scons/site_scons/site_tools/emscripten/*.py
find $d -type f -exec sh -c 'for f; do [ "$(head -c2 "$f")" = "#!" ] && chmod 0755 "$f" || chmod 0644 "$f"; done' sh {} +
grep -rlZ '^#!%{_bindir}/env' $d | xargs -0 sed -i \
  -e '1s|^#!%{_bindir}/env python3$|#!%{_bindir}/python3|' \
  -e '1s|^#!%{_bindir}/env node$|#!%{_bindir}/node|'
cat > $d/.emscripten <<'EOF'
import os
LLVM_ROOT = '%{_bindir}'
LLVM_ADD_VERSION = '%{llvm_major}'
CLANG_ADD_VERSION = '%{llvm_major}'
BINARYEN_ROOT = '%{_prefix}'
NODE_JS = '%{_bindir}/node'
CACHE = os.path.expanduser('~/.cache/emscripten')
EOF
# upstream launchers locate their .py via $0, so /usr/bin gets exec stubs, not symlinks
install -d %{buildroot}%{_bindir}
for t in em++ em-config emar embuilder emcc emcmake emconfigure emdwp emmake emnm \
         empath-split emprofile emranlib emrun emscan-deps emscons emsize emstrip emsymbolizer; do
  printf '#!/bin/sh\nexec %{_datadir}/%{name}/%s "$@"\n' "$t" > %{buildroot}%{_bindir}/$t
  chmod 0755 %{buildroot}%{_bindir}/$t
done
printf '#include "%{_includedir}/stb/stb_image.h"\n' > $d/third_party/stb_image.h
%py3_compile %{buildroot}%{_datadir}/%{name}
%fdupes %{buildroot}%{_datadir}/%{name}

%check
em=%{buildroot}%{_datadir}/%{name}
export EM_CACHE=$PWD/em-cache
mkdir smoke
cd smoke
$em/emcc --version
cat > hello.c <<'EOF'
#include <stdio.h>
int main(void) { puts("hello, world"); return 0; }
EOF
$em/emcc hello.c -o hello.js
test "$(node hello.js)" = "hello, world"
$em/emcc -O2 hello.c -o hello.html
test -s hello.html
cat > hello.cpp <<'EOF'
#include <iostream>
#include <string>
int main() { std::string s = "hello"; std::cout << s << " c++" << std::endl; }
EOF
$em/em++ -O3 hello.cpp -o hellocpp.js
test "$(node hellocpp.js)" = "hello c++"
cat > side.c <<'EOF'
int side_add(int a, int b) { return a + b; }
EOF
cat > main.c <<'EOF'
#include <stdio.h>
int side_add(int, int);
int main(void) { printf("%%d\n", side_add(40, 2)); return 0; }
EOF
$em/emcc -O2 -sSIDE_MODULE=1 side.c -o side.wasm
$em/emcc -O2 -sMAIN_MODULE=2 main.c side.wasm -o main.js
test "$(node main.js)" = "42"
# 1x1 GIF through the system stb_image
cat > stb.c <<'EOF'
#include <stdio.h>
unsigned char *stbi_load_from_memory(const unsigned char *, int, int *, int *, int *, int);
static const unsigned char gif[] = {
  0x47, 0x49, 0x46, 0x38, 0x39, 0x61, 0x01, 0x00, 0x01, 0x00, 0x80, 0x00, 0x00, 0x00, 0x00,
  0x00, 0xff, 0xff, 0xff, 0x21, 0xf9, 0x04, 0x01, 0x00, 0x00, 0x00, 0x00, 0x2c, 0x00, 0x00,
  0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x02, 0x02, 0x44, 0x01, 0x00, 0x3b };
int main(void) {
  int w = 0, h = 0, c = 0;
  if (!stbi_load_from_memory(gif, sizeof gif, &w, &h, &c, 0)) return 1;
  printf("%%dx%%d\n", w, h);
  return 0;
}
EOF
$em/emcc -sSTB_IMAGE stb.c -o stb.js
test "$(node stb.js)" = "1x1"
printf 'interface Foo {\n  void Foo();\n  long bar();\n};\n' > foo.idl
$em/tools/webidl_binder foo.idl glue
test -s glue.cpp

%files
%license LICENSE
%doc AUTHORS ChangeLog.md README.md
%{_bindir}/em*
%{_datadir}/%{name}

%changelog
