#
# spec file for package nim
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.2.12
Release:        0
Summary:        A statically typed, imperative programming language
License:        MIT
Group:          Development/Languages/Other
URL:            https://nim-lang.org/
Source0:        https://nim-lang.org/download/nim-%{version}.tar.xz
Source1:        nim-rpmlintrc
BuildRequires:  binutils-devel
# required for the testsuite
BuildRequires:  gc-devel
BuildRequires:  libopenssl-devel
BuildRequires:  sqlite3-devel
BuildRequires:  timezone
BuildRequires:  valgrind
%if 0%{?is_opensuse} || 0%{?is_backports}
# node is not available on armv7l armv7hl
%ifnarch armv7l armv7hl
# Leap 42.3 node is too old, but SLE backports is ok
%if 0%{?suse_version} >= 1500 || 0%{?is_backports}
BuildRequires:  nodejs
%endif
%endif
BuildRequires:  sfml2-devel
%endif
%if 0%{?suse_version} >= 1500
# -std=c++14 requires gcc 5.2, SLE and old Leap do not have it
BuildRequires:  gcc-c++ >= 5.2
%endif
#
Recommends:     git
ExclusiveArch:  %{ix86} x86_64 armv7l armv7hl aarch64 ppc64le

%description
Nim is a statically typed, imperative programming language.

Beneath a infix/indentation-based syntax with a (AST-based) macro
system lies a semantic model that supports a soft realtime GC on
thread local heaps. Asynchronous message passing is used between
threads. An unsafe shared memory heap is also provided for the
increased efficiency that results from that model.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export NIMFLAGS="$(echo '%{optflags}' | sed 's/\([^[:space:]]\+\)/--passC:\1/g')"
export NIMFLAGS="$NIMFLAGS %{?jobs:--parallelBuild:%{jobs}}"

./build.sh

make %{?_smp_mflags} V=1 \
  CFLAGS="%{optflags}"
./bin/nim c $NIMFLAGS koch

./koch boot -d:release $NIMFLAGS \
  -d:useGnuReadline
./koch tools -d:release $NIMFLAGS

%check
#cat <<EOT >> skip
#tests/manyloc/keineschweine/keineschweine.nim
#tests/manyloc/keineschweine/server/sg_lobby.nim
#EOT

cat <<EOT >> skip
# FIXME list of tests that need to be reviewed and that are not passing
#
# Error: unhandled exception: No SSL/TLS CA certificates found. [IOError]
tests/stdlib/thttpclient_ssl.nim
#
# code reloading test fails
tests/dll/nimhcr_integration.nim
#
# [ 2047s] Failure: reTimeout
tests/vm/tslow_tables.nim
EOT

%ifarch aarch64 armv7l armv7hl ppc64le
cat <<EOT >> skip
# fails because it includes immintrin.h
tests/misc/tsizeof4.nim
# other
tests/dll/nimhcr_unit.nim
tests/range/tcompiletime_range_checks.nim
EOT
%endif

%if 0%{?sle_version} && 0%{?sle_version} < 150000
cat <<EOT >> skip
# compiler too old?
tests/misc/tsizeof4.nim
tests/destructor/tnewruntime_misc.nim
EOT
%endif

%if 0%{?sle_version} && !0%{?is_opensuse} && !0%{?is_backports}
cat <<EOT >> skip
# no SFML in plain SLE
tests/niminaction/Chapter8/sfml/sfml_test.nim
EOT
%endif

%ifarch i586
cat <<EOT >> skip
# crashes on i586
tests/destructor/tnewruntime_misc.nim
EOT
%endif

# Tests as many targets as possible
targets="c objc"
if rpm -q --whatprovides nodejs; then
    targets="$targets js"
fi
if rpm -q --whatprovides c++_compiler; then
    targets="$targets c++"
fi
./koch tests --nim:$PWD/bin/nim --failing --colors:off --skipFrom:skip --targets:"$targets" all

%install
./koch install %{buildroot}%{_libdir}

find . -name testament -executable -type f -delete

mkdir -p %{buildroot}%{_bindir}/ %{buildroot}%{_sysconfdir}/nim \
  %{buildroot}%{_docdir}/nim/

ls ./bin | while read f; do
    install -Dpm 0755 "./bin/$f" "%{buildroot}%{_libdir}/nim/bin/$f"
    ln -s "%{_libdir}/nim/bin/$f" "%{buildroot}%{_bindir}/$f"
done

mv -T %{buildroot}%{_libdir}/nim/config/ %{buildroot}%{_sysconfdir}/nim/

mv -T %{buildroot}%{_libdir}/nim/doc/ %{buildroot}%{_docdir}/nim/
ln -s %{_docdir}/nim/ %{buildroot}%{_libdir}/nim/doc

%files
%license copying.txt
%doc doc/advopt.txt doc/basicopt.txt
%doc %{_docdir}/nim/
%dir %{_sysconfdir}/nim
%config %{_sysconfdir}/nim/nim*.cfg
%{_bindir}/nim*
%{_libdir}/nim/

%changelog
