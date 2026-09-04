#
# spec file for package zig
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%global version_suffix 0.15
%global version_current 0.15.2
%global _lto_cflags %{nil}
%global __builder   ninja
%define origname zig%{version_suffix}
# LLVM 20 is a hard requirement
%define clang_ver 20
# The test suite runs in a separate _multibuild "test" flavour rather than
# inline. It is risk isolation, not latency: %%check is only a few percent of
# this build, but it had never executed in this package's history, and zig has
# six consumers in Factory (ghostty, minizign, opentui, river, waylock, zls).
# Inline, one flaky or arch-specific test failure blocks all of them; in a
# flavour it does not. The price is that total build compute nearly doubles,
# because the test flavour has to repeat the whole compile before it can test.
%if "%{flavor}" == "test"
%define psuffix -test
%global debug_package %{nil}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with    test
%endif
%if 0%{?suse_version} >= 1600
%ifnarch aarch64
%bcond_without mold
%else
%bcond_with    mold
%endif
%endif
%if 0%{?suse_version} >= 1699
%bcond_without has_linker_type
%else
%bcond_with    has_linker_type
%endif
%bcond_without  macro
Name:           %{origname}%{psuffix}
Version:        %{version_current}
Release:        0
Summary:        Compiler for the Zig language
License:        MIT
URL:            https://ziglang.org/
Source0:        https://ziglang.org/download/%{version}/zig-%{version}.tar.xz
Source1:        macros.zig
Source2:        %{origname}-rpmlintrc
# PATCH-FIX-OPENSUSE 0000-remove-lld-in-cmakelist.patch boo#1193892 -- openSUSE ships no lldNN-devel package, so LLD cannot be linked into zig; stop cmake from looking for it
Patch0:         0000-remove-lld-in-cmakelist.patch
# PATCH-FIX-OPENSUSE 0001-invoke-lld.patch boo#1193892 -- companion to the above: spawn the ld.lld-NN/lld-link-NN/wasm-ld-NN binaries instead of calling into the LLD library. NOTE the tool names are hardcoded and must be kept in sync with %%{clang_ver} by hand -- a mismatch only fails at zig runtime, not at build time
Patch1:         0001-invoke-lld.patch
# PATCH-FIX-OPENSUSE 0002-no-lld-libs-and-includes.patch boo#1193892 -- companion to the above: drop the LLD library and include lists from zig's own build description
Patch2:         0002-no-lld-libs-and-includes.patch
# PATCH-FIX-OPENSUSE skip-localhost-test.patch -- skip the std.net test that resolves "localhost"; build workers have no usable resolver. Taken from Arch Linux (https://gitlab.archlinux.org/archlinux/packaging/packages/zig), which has since dropped it
Patch3:         skip-localhost-test.patch
# PATCH-FIX-UPSTREAM bump_max_rss.patch -- raise the compiler step's max_rss so the build is not killed on big workers; https://github.com/ziglang/zig/issues/23347 and https://github.com/ziglang/zig/pull/23254 (GitHub is a frozen mirror since upstream moved to codeberg.org/ziglang/zig)
Patch4:         bump_max_rss.patch
BuildRequires:  (gcc13-c++ if gcc13)
BuildRequires:  (gcc14-c++ if gcc14)
BuildRequires:  (gcc15-c++ if gcc15)
BuildRequires:  clang%{?clang_ver}
BuildRequires:  clang%{?clang_ver}-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  glibc-devel-32bit
BuildRequires:  help2man
BuildRequires:  lld%{?clang_ver}
BuildRequires:  llvm%{?clang_ver}-devel
# spec-cleaner deviation: spec-cleaner wants to relocate this block -- and the
# "%%if %%{with macro}" Recommends below -- past ExclusiveArch:, which orphans a
# BuildRequires from the rest of the dependency block. Kept here on purpose.
%if %{with mold}
BuildRequires:  mold
%endif
BuildRequires:  ninja
# Everything below is package identity: the test flavour must not advertise it,
# because OBS reads these provides for scheduling even though the flavour
# builds no binary package at all.
%if %{without test}
Requires:       lld%{?clang_ver}
# Zig needs this to work
Requires:       zig-libs%{version_suffix} = %{version}
Conflicts:      zig-implementation < %{version}
Provides:       zig = %{version}
Provides:       zig-implementation = %{version}
%endif
%if %{with macro} && %{without test}
# Zig Macros
Recommends:     zig-rpm-macros%{version_suffix} = %{version}
%endif
# llvm-config is missing targets for ppc and arm architectures.
# ExcludeArch:    ppc64 ppc64le %%arm %%ix86
ExclusiveArch:  x86_64 aarch64 riscv64 %{mips64}

%description
General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.

* Robust - behavior is correct even for edge cases such as out of memory.
* Optimal - write programs the best way they can behave and perform.
* Reusable - the same code works in many environments which have different constraints.
* Maintainable - precisely communicate intent to the compiler and other programmers.
The language imposes a low overhead to reading code and is resilient to changing requirements and environments.

%if %{without test}
%package -n     zig-libs%{version_suffix}
Summary:        Zig Standard Library
# Legal-Review-Notice: this subpackage ships ALL of upstream's lib/ tree, which is far more
# than zig's own MIT code: it bundles the sources of glibc, musl, mingw-w64, FreeBSD /
# NetBSD libc, the Darwin SDK headers, the sanitised Linux UAPI headers, wasi-libc, libcxx,
# libcxxabi, libunwind and libtsan, so that zig can cross compile against them.  The
# expression was derived mechanically from the tarball by the method below.  The SAME
# method is used for every zigN.NN package, so the sibling packages' expressions can be
# diffed against this one and any difference has to be a real difference between the two
# source trees:
#  1. Scope is exactly what lands in %%{_prefix}/lib/zig, i.e. upstream's lib/ tree.
#  2. A file's licence is its own SPDX-License-Identifier tag where it has one, else the
#     grant written in the file, else the licence file governing its directory (LICENSE /
#     LICENSE.TXT / COPYING / COPYRIGHT / LICENSES).
#  3. Tags are normalised to current SPDX ids (GPL-2.0 -> GPL-2.0-only, LGPL-2.1+ ->
#     LGPL-2.1-or-later, ...).  A WITH exception is part of the grant and is kept.
#  4. An OR is a choice offered to us: only the branch we elect is declared, never the
#     branch we do not.
#  5. A public domain dedication is declared SUSE-Public-Domain, openSUSE's spelling.
#  6. A grant that cannot be mapped to an id rpmlint accepts is omitted, never replaced by
#     a near match.
#  7. The surviving ids are AND-joined in case insensitive alphabetical order.
# Findings worth recording, because every one of them is easy to get wrong:
#  * NCSA is declared, but NOT on account of lib/lib{cxx,cxxabi,unwind}.  There it appears
#    only in the "Legacy LLVM License" section, which says in terms that a user "may choose
#    to use it under either license", while every shipped source file tags itself
#    Apache-2.0 WITH LLVM-exception - an unelected OR branch by rule 4.  The same goes for
#    lib/libc/wasi/emmalloc, offered as MIT or NCSA, where we elect MIT.  NCSA is required
#    by exactly one file carrying it as a standalone grant:
#    lib/libc/include/any-windows-any/dxcapi.h, "distributed under the University of
#    Illinois Open Source License".
#  * Plain Apache-2.0 is NOT declared.  No file in lib/ carries it as a standalone tag; it
#    occurs only as one of the three branches wasi-libc offers ("multi-licensed under the
#    Apache License v2.0 with LLVM Exceptions, the Apache License v2.0, and the MIT
#    License"), and we elect the first.  BSL-1.0 is out for the same reason: the ryu copy
#    bundled in lib/libcxx tags itself Apache-2.0 WITH LLVM-exception.
#  * The Linux UAPI headers under lib/libc/include/*-linux-any carry the syscall note on
#    every GPL/LGPL variant they use (~1200 files), so it is part of each of those five
#    terms.  A bare GPL-2.0-only would misstate the grant those headers actually give.
#  * There is NO GCC-exception-2.0 here.  lib/libc/glibc/csu holds 5 files and no start
#    files at all; nothing under lib/libc/glibc contains "unlimited permission to link",
#    "GCC Runtime Library Exception" or even "As a special exception", and no file there
#    cites the GPL rather than the LGPL.  The only GCC exception present is 3.1, on
#    lib/libc/include/generic-netbsd/unwind.h.
#  * MIT-CMU is required by 11 FreeBSD headers under lib/libc/include (the sys/vm/*.h set
#    and machine/profile.h) and by the CMU section of lib/libc/glibc/LICENSES.
#  * APSL-2.0 (418 files) and APSL-1.1 (7) are the Darwin SDK headers in
#    lib/libc/include/any-macos-any.
#  * lib/libc/include/generic-netbsd/sys/acl.h still tags itself BSD-2-Clause-FreeBSD, a
#    retired id.  The "views and conclusions" paragraph that used to distinguish it is not
#    in the file, so it counts as BSD-2-Clause and no new term is needed.
License:        Apache-2.0 WITH LLVM-exception AND APSL-1.1 AND APSL-2.0 AND Beerware AND BSD-1-Clause AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND CDDL-1.0 AND GFDL-1.1-or-later AND GPL-1.0-or-later WITH Linux-syscall-note AND GPL-2.0-only WITH Linux-syscall-note AND GPL-2.0-or-later WITH Linux-syscall-note AND GPL-3.0-or-later WITH GCC-exception-3.1 AND Inner-Net-2.0 AND ISC AND LGPL-2.0-or-later WITH Linux-syscall-note AND LGPL-2.1-only WITH Linux-syscall-note AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH Linux-syscall-note AND MIT AND MIT-CMU AND NCSA AND RSA-MD AND SUSE-Public-Domain AND ZPL-2.1
Conflicts:      zig-libs < %{version_current}
Provides:       zig-libs = %{version_current}
Provides:       zig-libs-implementation = %{version_current}
BuildArch:      noarch

%description -n zig-libs%{version_suffix}
Zig %{version_current} Standard Library
%endif

%if %{with macro} && %{without test}
%package    -n  zig-rpm-macros%{version_suffix}
Summary:        Common RPM macros for %{origname}
License:        MIT
Requires:       rpm
Conflicts:      zig-rpm-macros < %{version_current}
Provides:       zig-rpm-macros = %{version_current}
Provides:       zig-rpm-macros-implementation = %{version_current}
BuildArch:      noarch

%description    -n zig-rpm-macros%{version_suffix}
This package contains common RPM macros for zig in version %{version_current}.
%endif

%prep
%autosetup -n zig-%{version} -p1

%build
# TODO: why do we have this differentation for for CMAKE_BUILD_TYPE
#
# Linker selection: mold where we have it, otherwise LLD. lldNN only ships
# versioned binaries (/usr/bin/ld.lld-NN) and carries
# "Provides: lldNN-update-alternatives-removed", so the unversioned
# /usr/bin/ld.lld that plain "-fuse-ld=lld" needs does not exist and
# -DCMAKE_LINKER_TYPE=LLD fails the compiler check. Overriding
# CMAKE_<LANG>_USING_LINKER_LLD does not help either: cmake's own
# Platform/Linux-GNU.cmake set()s that variable unconditionally after our
# cache entry, so the plain -fuse-ld=lld wins. Declaring a *custom* linker
# type instead is not shadowed by cmake and pins the version-matched linker.
%cmake \
  -DCMAKE_C_COMPILER="clang-%{clang_ver}" \
  -DCMAKE_CXX_COMPILER="clang++-%{clang_ver}" \
%if %{with has_linker_type}
%if %{with mold}
  -DCMAKE_LINKER_TYPE=MOLD \
%else
  -DCMAKE_LINKER_TYPE=LLD%{clang_ver} \
  -DCMAKE_C_USING_LINKER_LLD%{clang_ver}="-fuse-ld=lld-%{clang_ver}" \
  -DCMAKE_CXX_USING_LINKER_LLD%{clang_ver}="-fuse-ld=lld-%{clang_ver}" \
%endif
%endif
  -DZIG_SHARED_LLVM=On \
  -DZIG_USE_LLVM_CONFIG=ON \
  -DZIG_PIE:BOOL=true \
  -DZIG_TARGET_MCPU="baseline" \
  -DZIG_VERSION:STRING="%{version}"

# Workaround since CMAKE on Leap does not have
# the CMAKE_LINKER_TYPE option
%if %{without has_linker_type} && %{with mold}
mold -run %cmake_build
%else
%cmake_build
%endif

# %%cmake left us in the build directory
cd ..
%if %{without test}
# doc/langref.html.in is upstream's docgen *template*, not the rendered manual: it is full
# of literal {#syntax#} markers. The CMake path can never render it, because CMakeLists.txt
# hardcodes -Dno-langref -- which is precisely why upstream also exposes a standalone
# "langref" build step. Run that step against the freshly built stage3 compiler so the
# package ships the real language reference. The test flavour skips it: it installs
# nothing, and rendering costs a full docgen run over every doc code sample.
./%{__builddir}/stage3/bin/zig build langref \
  --prefix zig-out \
  --zig-lib-dir lib \
  --cache-dir "$PWD/.zig-cache" \
  --global-cache-dir "$PWD/.zig-cache"
%endif

%if %{without test}
%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr "%{buildroot}%{_bindir}/zig" --version-option=version --output=%{buildroot}%{_mandir}/man1/zig.1

%if %{with macro}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.zig
sed -i -e "s|@@ZIG_VERSION@@|%{version}|" %{buildroot}%{_rpmmacrodir}/macros.zig
%endif

# Collect the licence texts of the third-party sources bundled in lib/ so the
# zig-libs subpackage can expose them via %%license (their basenames collide,
# hence the renames).
mkdir -p bundled-licenses
cp -p LICENSE bundled-licenses/LICENSE.zig
cp -p lib/libc/freebsd/COPYRIGHT bundled-licenses/COPYRIGHT.freebsd
cp -p lib/libc/glibc/LICENSES bundled-licenses/LICENSES.glibc
cp -p lib/libc/mingw/COPYING bundled-licenses/COPYING.mingw-w64
cp -p lib/libc/musl/COPYRIGHT bundled-licenses/COPYRIGHT.musl
cp -p lib/libc/wasi/LICENSE bundled-licenses/LICENSE.wasi
cp -p lib/libc/wasi/LICENSE-APACHE bundled-licenses/LICENSE-APACHE.wasi
cp -p lib/libc/wasi/LICENSE-APACHE-LLVM bundled-licenses/LICENSE-APACHE-LLVM.wasi
cp -p lib/libc/wasi/LICENSE-MIT bundled-licenses/LICENSE-MIT.wasi
cp -p lib/libcxx/LICENSE.TXT bundled-licenses/LICENSE.libcxx
cp -p lib/libcxxabi/LICENSE.TXT bundled-licenses/LICENSE.libcxxabi
cp -p lib/libunwind/LICENSE.TXT bundled-licenses/LICENSE.libunwind
%endif

%if %{with test}
%check
# Reduced test set, following upstream's own CI (a full "zig build test"
# rebuilds the compiler several times over). Run against the freshly built
# stage3 compiler in the build tree: the test flavour deliberately skips
# %%install, because a populated buildroot with no %%files aborts rpmbuild
# with "Installed (but unpackaged) file(s) found".
./%{__builddir}/stage3/bin/zig test test/behavior.zig -Itest --zig-lib-dir lib
%endif

%if %{without test}
%files
%license LICENSE
%doc README.md
%doc zig-out/doc/langref.html
%{_bindir}/zig
%{_mandir}/man1/zig.1%{?ext_man}

%files -n zig-libs%{version_suffix}
%license bundled-licenses/*
%{_prefix}/lib/zig

%if %{with macro}
%files -n zig-rpm-macros%{version_suffix}
%{_rpmmacrodir}/macros.zig
%endif
%endif

%changelog
