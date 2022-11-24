#
# spec file for package nim
#
# Copyright (c) 2022 SUSE LLC
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


Name:           nim
Version:        1.6.10
Release:        0
Summary:        A statically typed compiled systems programming language
License:        MIT
Group:          Development/Languages/Other
URL:            https://nim-lang.org/
Source0:        https://nim-lang.org/download/nim-%{version}.tar.xz
Source1:        nim-rpmlintrc
Patch0:         nim-nim-gdb_fix_interpreter.patch
# UPSTREAM FIX: https://github.com/nim-lang/Nim/commit/8c100a37b93607806acec51733fe5e2fda392d44.patch
Patch1:         nim-fix-tests-certificate-key-too-small.patch
# UPSTREAM FIX: https://github.com/nim-lang/Nim/commit/2c73e84436a11cae1676c7da0228158ba1a885cc
Patch2:         nim-fix-tests-ip-protocol-missing.patch

# pull in a C compiler (required to build Nim programs)
Requires:       gcc
Recommends:     clang
Recommends:     pcre

BuildRequires:  binutils-devel

# required for the testsuite
BuildRequires:  gc-devel
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
BuildRequires:  git
BuildRequires:  libopenssl-devel
BuildRequires:  netcfg
BuildRequires:  pcre
BuildRequires:  sqlite3-devel
BuildRequires:  timezone
BuildRequires:  valgrind

# Nim needs support for both __builtin_saddll_overflow and
# -std=c++14, therefore gcc 6.2+ is required.
BuildRequires:  gcc-c++ >= 6.2

# Needs node 12 for flag --unhandled-rejections=strict, but it's not
# strictly needed (it's used to test the Nim JS compiler, so we can
# skip it and run tests without this compiler target afterwards)
%if 0%{?suse_version} >= 150100 || (0%{?suse_version} >= 150100 && 0%{?is_backports})
BuildRequires:  nodejs >= 12
Recommends:     nodejs
%endif

Recommends:     git
ExclusiveArch:  %{ix86} x86_64 armv7l armv7hl aarch64 ppc64le

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
%setup -q
%autopatch -p1

%build
export CFLAGS="%{optflags}"
export NIMFLAGS="$(echo '%{optflags}' | sed 's/\([^[:space:]]\+\)/--passC:\1/g')"
export NIMFLAGS="$NIMFLAGS %{?jobs:--parallelBuild:%{jobs}}"

./build.sh
make %{?_smp_mflags} V=1 CFLAGS="%{optflags}"

./bin/nim c  $NIMFLAGS -d:release koch
./koch boot  $NIMFLAGS -d:release
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
  # cannot open file: jester
  tests/niminaction/Chapter7/Tweeter/src/tweeter.nim
  tests/cpp/tasync_cpp.nim
  # # only working with megatest enabled
  # tests/misc/tjoinable.nim
  # expects Nim to be in PATH...
  tests/stdlib/tosproc.nim
  # following tests are flaky
  tests/stdlib/tio.nim
  tests/arc/thard_alignment.nim
  # this one needs NodeJS althought its not required by the build
  tests/nimdoc/trunnableexamples.nim
  # broken in Leap 15.3
  tests/exception/t13115.nim
  # no SFML in plain SLE and missing in backport repos
  tests/niminaction/Chapter8/sfml/sfml_test.nim
EOT

%ifarch i586
cat << EOT >> tests_to_skip
  # flaky test, fails in i586
  tests/async/tasyncssl.nim
EOT
%endif

%ifarch aarch64 armv7l armv7hl ppc64le
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

  #ppc64le
  tests/arc/tasyncorc.nim
EOT
%endif

%if 0%{?suse_version} < 150100
cat << EOT >> tests_to_skip
  # deactivate all tests that require node, as node version in
  # SLE and Leap 15.1 is either too old or not available at all
  tests/misc/trunner.nim
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
# add/remove things in an unusual way and we want to find out what's
# been added/removed/modified on future versions to avoid errors
# during packaging it
TARGET="%{buildroot}/_pending"

./koch install $TARGET

# some binaries aren't installed at target location by koch
cp ./bin/* $TARGET/nim/bin/

# nim-gdb requires this script under "tools" folder at final location
mkdir -p $TARGET/nim/tools
cp ./tools/nim-gdb.py $TARGET/nim/tools/

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
mv $TARGET/nim/tools     %{buildroot}%{_libdir}/nim/

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
