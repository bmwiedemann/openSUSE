#
# spec file for package nim
#
# Copyright (c) 2019 SUSE LLC
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
Version:        1.0.2
Release:        0
Summary:        A statically typed, imperative programming language
License:        MIT
Group:          Development/Languages/Other
URL:            https://nim-lang.org/
Source0:        https://nim-lang.org/download/nim-%{version}.tar.xz
Source1:        nim-rpmlintrc
BuildRequires:  binutils-devel
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
