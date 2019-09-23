#
# spec file for package fhourstones
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fhourstones
Version:        3.1+git.20150122
Release:        0
Summary:        The Fhourstones Benchmark
License:        BSD-2-Clause
Group:          System/Benchmark
URL:            https://tromp.github.io/c4/fhour.html
Source:         %{name}-%{version}.tar.xz

%description
This integer benchmark solves positions in the game of connect-4, as played
on a vertical 7x6 board.

%prep
%setup -q

%build
sed -i "s|-O3|%{optflags}|g" Makefile
make %{?_smp_mflags} all
echo '#!/bin/sh' >> %{name}
echo 'libexecdir=%{_libdir}/%{name}' >> %{name}
echo 'datadir=%{_datadir}/%{name}' >> %{name}
echo 'exec $libexecdir/SearchGame < $datadir/inputs' >> %{name}

%install
install -D -p -m 0755 %{name} \
  %{buildroot}%{_bindir}/%{name}
install -D -p -m 0755 SearchGame \
  %{buildroot}%{_libdir}/%{name}/SearchGame
install -D -p -m 0644 inputs \
  %{buildroot}%{_datadir}/%{name}/inputs

%files
%doc LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}

%changelog
