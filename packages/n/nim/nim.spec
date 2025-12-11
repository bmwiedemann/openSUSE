#
# spec file for package nim
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


%define _atlas_version 0.9.5
%define _sat_commit d67107e94f92c4cf6f0791542f473b21329bbd97

Name:           nim
Version:        2.2.6
Release:        0
Summary:        A statically typed compiled systems programming language
License:        MIT
Group:          Development/Languages/Other
URL:            https://nim-lang.org/
Source0:        https://nim-lang.org/download/nim-%{version}.tar.xz
Source1:        https://github.com/nim-lang/atlas/archive/refs/tags/%{_atlas_version}.tar.gz#/atlas-%{_atlas_version}.tar.gz
Source2:        nim-rpmlintrc
Source3:        https://github.com/nim-lang/sat/archive/%{_sat_commit}.tar.gz#/sat-%{_sat_commit}.tar.gz
Patch0:         nim-nim-gdb_fix_interpreter.patch
Patch1:         nim-fix-tests-i586.patch
# https://github.com/nim-lang/Nim/issues/23668
# https://github.com/nim-lang/Nim/pull/24405
Patch2:         nim-2.2.2-pcre2.patch
BuildRequires:  binutils-devel
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
# required for the testsuite
BuildRequires:  gc-devel
# Nim needs support for both __builtin_saddll_overflow and
# -std=c++14, therefore gcc 6.2+ is required.
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libopenssl-devel
BuildRequires:  netcfg
BuildRequires:  sqlite3-devel
BuildRequires:  timezone
BuildRequires:  valgrind
BuildRequires:  pkgconfig(libpcre2-8)
# pull in a C compiler (required to build Nim programs)
Recommends:     clang
Recommends:     git
Recommends:     libpcre2-8-0
ExclusiveArch:  %{ix86} x86_64 armv7l armv7hl aarch64 ppc64le riscv64
# Needs node 12 for flag --unhandled-rejections=strict, but it's not
# strictly needed (it's used to test the Nim JS compiler, so we can
# skip it and run tests without this compiler target afterwards)
%if 0%{?suse_version} >= 1501 || (0%{?suse_version} >= 1501 && 0%{?is_backports})
BuildRequires:  nodejs >= 12
Recommends:     nodejs
%endif

%description
Nim is a statically typed compiled systems programming language. It
combines successful concepts from mature languages like Python, Ada
and Modula.

Efficient:
* Nim generates native dependency-free executables, not dependent on
  a virtual machine, which are small and allow easy redistribution.
* The Nim compiler and the generated executables support all major
  platforms like Windows, Linux, BSD and macOS.
* Nim's memory management is deterministic and customizable with
  destructors and move semantics, inspired by C++ and Rust. It is
  well-suited for embedded, hard-realtime systems.
* Modern concepts like zero-overhead iterators and compile-time
  evaluation of user-defined functions, in combination with the
  preference of value-based datatypes allocated on the stack, lead
  to extremely performant code.
* Support for various backends: it compiles to C, C++ or JavaScript
  so that Nim can be used for all backend and frontend needs.

Expressive:
* Nim is self-contained: the compiler and the standard library are
  implemented in Nim.
* Nim has a powerful macro system which allows direct manipulation
  of the AST, offering nearly unlimited opportunities.

Elegant:
* Macros cannot change Nim's syntax because there is no need for it
  — the syntax is flexible enough.
* Modern type system with local type inference, tuples, generics and
  sum types.
* Statements are grouped by indentation but can span multiple lines.

%prep
%setup -q -a1 -a3

mv atlas-%{_atlas_version} dist/atlas
mkdir dist/atlas/dist
mv sat-%{_sat_commit} dist/atlas/dist/sat

%patch -P 0 -p1
%ifarch i586
%patch -P 1 -p1
%endif
%patch -P 2 -p1

%build
export CFLAGS="%{optflags}"
export NIMFLAGS="$(echo '%{optflags}' | sed 's/\([^[:space:]]\+\)/--passC:\1/g')"
export NIMFLAGS="$NIMFLAGS %{?jobs:--parallelBuild:%{jobs}}"

./build.sh
# %make_build CFLAGS="%{optflags}"

./bin/nim c  $NIMFLAGS -d:release koch
./koch boot  $NIMFLAGS -d:release

# on older versions use v1 garbage collector
%if 0%{?suse_version} < 1560
echo "mm:refc" >> config/nim.cfg
%endif
./koch tools $NIMFLAGS -d:release

# TODO: build docs
# ./koch docs

%check

cat << EOT >> tests_to_skip
  # we don't care about testament itself
  tests/testament/tjoinable.nim
  tests/testament/tshould_not_work.nim
  # cannot open file: zip/zipfiles
  tests/manyloc/nake/nakefile.nim
  # cannot open file: zip/zlib
  tests/manyloc/keineschweine/keineschweine.nim
  # Temporary failure in name resolution (tries to use netcode)
  tests/stdlib/thttpclient.nim
  tests/stdlib/tnetconnect.nim
  # client: exception: error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed
  tests/stdlib/thttpclient_ssl.nim
  tests/stdlib/tssl.nim
  # cannot open file: jester
  tests/niminaction/Chapter7/Tweeter/src/tweeter.nim
  tests/cpp/tasync_cpp.nim
  # expects Nim to be in PATH...
  tests/stdlib/tosproc.nim
  # following tests are flaky
  tests/stdlib/tio.nim
  tests/arc/thard_alignment.nim
  # this one needs NodeJS althought its not required by the build
  tests/nimdoc/trunnableexamples.nim
  tests/js/tnativeexc.nim
  # broken in Leap 15.3
  tests/exception/t13115.nim
  # no SFML in plain SLE and missing in backport repos
  tests/niminaction/Chapter8/sfml/sfml_test.nim
  # GCC 14 related errors
  #tests/objects/toop1.nim
  #tests/vm/tvmmisc.nim
  #tests/cpp/tmanual_exception.nim
  #tests/objects/tobjcov.nim
  # GCC 15 related errors
  tests/stdlib/concurrency/tatomics.nim
  # exits with 1 for some reason
  tests/stdlib/tmath.nim
EOT

%ifarch i586
cat << EOT >> tests_to_skip
  # flaky test, fails in i586
  tests/async/tasyncssl.nim
  tests/realtimeGC/tmain.nim
  tests/realtimeGC/shared.nim
  tests/stdlib/tcasts.nim
  tests/stdlib/trandom.nim
  tests/stdlib/tmarshal.nim
  tests/compiler/tasm2.nim
  tests/async/tioselectors.nim
  tests/stdlib/t9754.nim
  tests/template/t13426.nim
  tests/threads/tmembug.nim
  tests/errmsgs/t22852.nim
  tests/errmsgs/t23435.nim
EOT
%endif

%ifarch aarch64 armv7l armv7hl ppc64le riscv64
cat << EOT >> tests_to_skip
  # fails because it includes immintrin.h
  tests/misc/tsizeof4.nim

  # armv7l
  tests/stdlib/tarithmetics.nim
  tests/vm/tslow_tables.nim
  tests/tuples/t12892.nim
  tests/dll/nimhcr_unit.nim
  tests/arc/tcaseobj.nim
  tests/arc/tcaseobjcopy.nim
  tests/async/tasyncssl.nim

  #aarch64 and ppc64l
  tests/range/tcompiletime_range_checks.nim
  tests/dll/nimhcr_unit.nim
  tests/coroutines/tgc.nim
  tests/coroutines/twait.nim
  tests/threads/tonthreadcreation.nim
  tests/threads/tracy_allocator.nim
  tests/threads/treusetvar.nim
  tests/threads/tthreadvars.nim
  tests/misc/ttlsemulation.nim
  tests/misc/tvcc.nim
  tests/threads/t7172.nim
  tests/dll/nimhcr_basic.nim
  tests/threads/t8535.nim
  tests/threads/threadex.nim
  tests/threads/tmanyjoin.nim
  tests/threads/tmembug.nim

  #ppc64le
  tests/arc/tasyncorc.nim
  tests/compiler/tasm.nim
  tests/compiler/tasm2.nim
EOT
%endif

%if 0%{?suse_version} < 1501
cat << EOT >> tests_to_skip
  # deactivate all tests that require node, as node version in
  # SLE and Leap 15.1 is either too old or not available at all
  tests/misc/trunner.nim
EOT
%endif

# some test fails on older compiler
%if 0%{?suse_version} <= 1560
cat << EOT >> tests_to_skip
  tests/converter/tconverter_unique_ptr.nim
  tests/destructor/t23837.nim
EOT
%endif

%if 0%{?qemu_user_space_build}
cat << EOT >> tests_to_skip
  # valgrind is not compatible with QEMU user-space emulation,
  # skip all test using it
  tests/views/tsplit_into_openarray.nim
  tests/destructor/tnewruntime_strutils.nim
  tests/destructor/tv2_raise.nim
  tests/valgrind/tleak_arc.nim
  tests/valgrind/tbasic_valgrind.nim
  tests/arc/tunref_cycle.nim
  tests/arc/tcustomtrace.nim
  tests/arc/tcaseobj.nim
  tests/arc/t14472.nim
  tests/arc/tasyncleak4.nim
  tests/arc/thavlak_orc_stress.nim
  tests/arc/torc_selfcycles.nim
  tests/arc/tfuncobj.nim
  tests/arc/tasyncleak3.nim
  tests/arc/tasyncorc.nim
  tests/arc/tcaseobjcopy.nim
EOT
%endif

# Tests as many targets as possible
NIM_COMPILER_TARGETS="c"
if rpm -q --whatprovides c++_compiler; then
    NIM_COMPILER_TARGETS="$NIM_COMPILER_TARGETS c++"
fi
if rpm -q --whatprovides nodejs; then
    NIM_COMPILER_TARGETS="$NIM_COMPILER_TARGETS js"
fi

./koch tests \
  --nim:$PWD/bin/nim \
  --failing \
  --colors:off \
  --megatest:on \
  --skipFrom:tests_to_skip \
  --targets:"$NIM_COMPILER_TARGETS" \
  all

%install
# extract everything into a staging location, as Nim devels like to
# add/remove things in an unusual way and we want to find out what
# is added/removed/modified on future versions to avoid errors
# while packaging it
TARGET="%{buildroot}/_pending"

./koch install $TARGET

# some binaries aren't installed at target location by koch
cp ./bin/* $TARGET/nim/bin/

mkdir -p \
  %{buildroot}%{_bindir}/ \
  %{buildroot}%{_libdir}/nim \
  %{buildroot}%{_sysconfdir}/nim \
  %{buildroot}%{_docdir}/nim

# remove things that aren't needed
rm $TARGET/nim/lib/pure/unidecode/gen.py

# fix endlines
sed -i 's/\r$//' $TARGET/nim/doc/nimdoc.css

# move executables to final location (or delete what isn't needed)
rm $TARGET/nim/bin/atlas
rm $TARGET/nim/bin/testament
rm $TARGET/nim/nim.nimble
mv $TARGET/nim/bin %{buildroot}%{_libdir}/nim/

# strip all symbols from binaries
strip --strip-all %{buildroot}%{_libdir}/nim/bin/nim
strip --strip-all %{buildroot}%{_libdir}/nim/bin/nimble
strip --strip-all %{buildroot}%{_libdir}/nim/bin/nim_dbg
strip --strip-all %{buildroot}%{_libdir}/nim/bin/nimgrep
strip --strip-all %{buildroot}%{_libdir}/nim/bin/nimpretty
strip --strip-all %{buildroot}%{_libdir}/nim/bin/nimsuggest

# nim requires symlinks to executables, as it looks for its
# standard library by resolving the link and then checking for
# parent paths, which is quite unusual...
ln -s %{_libdir}/nim/bin/nim        %{buildroot}%{_bindir}
ln -s %{_libdir}/nim/bin/nim-gdb    %{buildroot}%{_bindir}
ln -s %{_libdir}/nim/bin/nim_dbg    %{buildroot}%{_bindir}
ln -s %{_libdir}/nim/bin/nimble     %{buildroot}%{_bindir}
ln -s %{_libdir}/nim/bin/nimgrep    %{buildroot}%{_bindir}
ln -s %{_libdir}/nim/bin/nimpretty  %{buildroot}%{_bindir}
ln -s %{_libdir}/nim/bin/nimsuggest %{buildroot}%{_bindir}

mv $TARGET/nim/compiler* %{buildroot}%{_libdir}/nim/
mv $TARGET/nim/lib       %{buildroot}%{_libdir}/nim/
mv $TARGET/nim/doc       %{buildroot}%{_docdir}/nim/
mv $TARGET/nim/config/*  %{buildroot}%{_sysconfdir}/nim/

%files

%license copying.txt
%doc %{_docdir}/nim

%{_bindir}/nim
%{_bindir}/nim-gdb
%{_bindir}/nim_dbg
%{_bindir}/nimble
%{_bindir}/nimgrep
%{_bindir}/nimpretty
%{_bindir}/nimsuggest

%dir %{_sysconfdir}/nim
%config %{_sysconfdir}/nim/*

%{_libdir}/nim/

%changelog
