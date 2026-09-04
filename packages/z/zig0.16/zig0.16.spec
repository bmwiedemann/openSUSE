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


%global version_suffix 0.16
%global version_current 0.16.0
%global origname zig%{version_suffix}
# @BUILD_FLAVOR@ is substituted TEXTUALLY by obs-build, so it is empty for the
# default flavor - hence the %%{nil}.  The %%else branch MUST define psuffix or
# the default flavor loses its Name.
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%global debug_package %{nil}
%bcond_without  test
%else
%define psuffix %{nil}
%bcond_with     test
%endif
%global _lto_cflags %{nil}
%global __builder   ninja
# LLVM 21 is a hard requirement
%define clang_ver 21
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
Source2:        zig%{version_suffix}-rpmlintrc
# PATCH-FIX-OPENSUSE 0000-remove-lld-in-cmakelist.patch boo#1193892 -- openSUSE ships no
# lld%%{clang_ver}-devel, so LLD cannot be linked into the compiler.  Stop CMake from
# looking for it.  Patch0/1/2 exist solely to work around that missing package; drop all
# three once boo#1193892 is resolved.
Patch0:         0000-remove-lld-in-cmakelist.patch
# PATCH-FIX-OPENSUSE 0001-invoke-lld.patch boo#1193892 -- replace the in-process lld::*::link()
# calls with posix_spawn() of the versioned command line linkers, since we cannot link
# against liblld (see Patch0).
# MAINTENANCE HAZARD: the binary names ld.lld-%%{clang_ver}, lld-link-%%{clang_ver} and
# wasm-ld-%%{clang_ver} are HARDCODED in this patch with no mechanical link to clang_ver.
# A mismatch is not caught at build time - it fails when the installed zig links a program.
Patch1:         0001-invoke-lld.patch
# PATCH-FIX-OPENSUSE 0002-no-lld-libs-and-includes.patch boo#1193892 -- drop the lld include
# dir / library list from build.zig, which would otherwise assert on the empty values left
# behind by Patch0.
Patch2:         0002-no-lld-libs-and-includes.patch
# PATCH-FIX-OPENSUSE skip-localhost-test.patch -- the std "resolve DNS" test needs a working
# loopback resolver, which OBS workers do not have.  Taken from Arch:
# https://gitlab.archlinux.org/archlinux/packaging/packages/zig/-/raw/main/skip-localhost-test.patch
# NOTE: only reached by the full "zig build test" suite, not by the reduced %%check below.
Patch3:         skip-localhost-test.patch
# PATCH-FIX-OPENSUSE bump_max_rss.patch -- the CMake build drives build.zig to produce stage3,
# and upstream caps that step at 8 GB RSS, which the LLVM-enabled build exceeds here.
# Upstream discussion predates the move to Codeberg and lives on the now frozen GitHub
# mirror: https://github.com/ziglang/zig/issues/23347 (PR 23254).  Neither was carried over
# to https://codeberg.org/ziglang/zig, so there is no live upstream reference to give.
# Keep _constraints' memory request above the value set here.
Patch4:         bump_max_rss.patch
# PATCH-FIX-UPSTREAM 0003-link-Elf-support-R_X86_64_PC64.patch -- teach zig's self hosted ELF
# linker the R_X86_64_PC64 relocation; released 0.16.0 fails to link objects that use it.
# https://codeberg.org/ziglang/zig/commit/9df02121d0d87c17173f79d55692bed9cb65722c
Patch5:         0003-link-Elf-support-R_X86_64_PC64.patch
BuildRequires:  (gcc13-c++ if gcc13)
BuildRequires:  (gcc14-c++ if gcc14)
BuildRequires:  (gcc15-c++ if gcc15)
BuildRequires:  clang%{?clang_ver}
BuildRequires:  clang%{?clang_ver}-devel
BuildRequires:  cmake
BuildRequires:  elfutils
BuildRequires:  gcc-c++
BuildRequires:  glibc
BuildRequires:  glibc-devel
BuildRequires:  glibc-devel-32bit
BuildRequires:  help2man
BuildRequires:  liburing-devel
BuildRequires:  lld%{?clang_ver}
BuildRequires:  llvm%{?clang_ver}-devel
# spec-cleaner DEVIATION: it wants to relocate this block below ExclusiveArch, which would
# orphan the only conditional BuildRequires away from every other one.  Keep it here.
%if %{with mold}
BuildRequires:  mold
%endif
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(zlib)
# llvm-config is missing targets for ppc and arm architectures.
# ExcludeArch:    ppc64 ppc64le %%arm %%ix86
ExclusiveArch:  x86_64 aarch64 riscv64 %{mips64}
# The test flavor ships no binary package at all, so it must not advertise any of
# the runtime deps or the zig/zig-implementation providers - OBS reads those for
# scheduling even though rpmbuild produces nothing here.
%if %{without test}
# ld.lld-%%{clang_ver} is spawned at run time by Patch1
Requires:       lld%{?clang_ver}
# Zig needs this to work
Requires:       zig-libs%{version_suffix} = %{version}
# Zig Macros
Recommends:     zig-rpm-macros%{version_suffix} = %{version}
Conflicts:      zig-implementation < %{version}
Provides:       zig = %{version}
Provides:       zig-implementation = %{version}
%endif

%description
General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.

* Robust - behavior is correct even for edge cases such as out of memory.
* Optimal - write programs the best way they can behave and perform.
* Reusable - the same code works in many environments which have different constraints.
* Maintainable - precisely communicate intent to the compiler and other programmers.
The language imposes a low overhead to reading code and is resilient to changing requirements and environments.

# Subpackages declared with -n do NOT pick up %%{psuffix}, so they must be
# declared away entirely in the test flavor or it would advertise a second,
# competing set of zig-libs/zig-rpm-macros providers.
%if %{without test}
%package -n     zig-libs%{version_suffix}
Summary:        Zig Standard Library
# Legal-Review-Notice: this subpackage ships ALL of upstream's lib/ tree, which is far more
# than zig's own MIT code: it bundles the sources of glibc, musl, mingw-w64, FreeBSD /
# NetBSD / OpenBSD libc, the Darwin SDK headers, the sanitised Linux UAPI headers,
# wasi-libc, libcxx, libcxxabi, libunwind and libtsan, so that zig can cross compile
# against them.  The expression was derived mechanically from the tarball by the method
# below.  The SAME method is used for every zigN.NN package, so the sibling packages'
# expressions can be diffed against this one and any difference has to be a real
# difference between the two source trees:
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
#    Apache-2.0 WITH LLVM-exception - an unelected OR branch by rule 4.  NCSA is required
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
#  * APSL-2.0 (428 files) and APSL-1.1 (7) are the Darwin SDK headers in
#    lib/libc/include/any-darwin-any.
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

%if %{with macro}
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
%endif

%prep
%autosetup -n zig-%{version} -p1

%build
# TODO: why do we have this differentation for for CMAKE_BUILD_TYPE
#
# On the non-mold path: lld%%{clang_ver} only ships versioned binaries
# (/usr/bin/ld.lld-%%{clang_ver}).  The unversioned /usr/bin/ld.lld that CMake's stock
# CMAKE_LINKER_TYPE=LLD flag ("-fuse-ld=lld") resolves to comes from the unversioned lld
# package, which tracks a different LLVM major - BuildRequiring it would mean linking with
# a version skewed LLD.  Without this, aarch64 fails to configure at all with
# "clang-%%{clang_ver}: error: invalid linker name in argument '-fuse-ld=lld'"; x86_64 never
# saw it because it takes the mold path above.
#
# Overriding CMAKE_<LANG>_USING_LINKER_LLD does NOT work: Platform/Linux-GNU.cmake sets it
# with a plain set(), and a normal variable shadows the cache entry a -D would create.
# Declaring a CUSTOM linker type does work, because nothing else defines it.
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

%install
# The test flavor ships nothing, so it installs nothing: an empty buildroot is
# what lets it omit %%files without tripping the unpackaged-files check.
%if %{without test}
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr "%{buildroot}%{_bindir}/zig" --version-option=version --output=%{buildroot}%{_mandir}/man1/zig.1

%if %{with macro}
mkdir -p %{buildroot}%{_rpmmacrodir}
install -p -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}
sed -i -e "s|@@ZIG_VERSION@@|%{version}|"  %{buildroot}%{_rpmmacrodir}/macros.zig
%endif

# Collect the licences of the third party code bundled under lib/ so that
# zig-libs%%{version_suffix}, which ships all of it, can carry them as %%license.
mkdir -p bundled-licenses
cp -p LICENSE                                          bundled-licenses/LICENSE.zig
cp -p lib/libc/freebsd/COPYRIGHT                       bundled-licenses/COPYRIGHT.freebsd
cp -p lib/libc/glibc/LICENSES                          bundled-licenses/LICENSES.glibc
cp -p lib/libc/mingw/COPYING                           bundled-licenses/COPYING.mingw-w64
cp -p lib/libc/musl/COPYRIGHT                          bundled-licenses/COPYRIGHT.musl
cp -p lib/libc/wasi/LICENSE                            bundled-licenses/LICENSE.wasi-libc
cp -p lib/libc/wasi/LICENSE-APACHE                     bundled-licenses/LICENSE-APACHE.wasi-libc
cp -p lib/libc/wasi/LICENSE-APACHE-LLVM                bundled-licenses/LICENSE-APACHE-LLVM.wasi-libc
cp -p lib/libc/wasi/LICENSE-MIT                        bundled-licenses/LICENSE-MIT.wasi-libc
cp -p lib/libc/wasi/fts/musl-fts/COPYING               bundled-licenses/COPYING.musl-fts
cp -p lib/libc/wasi/libc-bottom-half/cloudlibc/LICENSE bundled-licenses/LICENSE.cloudlibc
cp -p lib/libcxx/LICENSE.TXT                           bundled-licenses/LICENSE.libcxx
cp -p lib/libcxxabi/LICENSE.TXT                        bundled-licenses/LICENSE.libcxxabi
cp -p lib/libunwind/LICENSE.TXT                        bundled-licenses/LICENSE.libunwind
%endif

%if %{with test}
%check
# Reduced test set: upstream's full "zig build test" is a multi hour, multi target matrix.
# test/behavior.zig is the compiler's own behaviour suite and is the meaningful smoke test
# that the stage3 binary we just built actually works.
# CMakeLists puts the finished compiler in ${PROJECT_BINARY_DIR}/stage3, a complete install
# prefix, so it finds its own lib/zig - we cannot use %%{buildroot} here because the test
# flavor deliberately installs nothing.
build/stage3/bin/zig test test/behavior.zig -Itest
%endif

%if %{without test}
%files
%license LICENSE
%{_bindir}/zig
%{_mandir}/man1/zig.1%{?ext_man}
%doc README.md
%doc lib/docs
%doc zig-out/doc/langref.html

%files -n zig-libs%{version_suffix}
%license bundled-licenses
%{_prefix}/lib/zig

%if %{with macro}
%files -n zig-rpm-macros%{version_suffix}
%{_rpmmacrodir}/macros.zig
%endif
%endif

%changelog
