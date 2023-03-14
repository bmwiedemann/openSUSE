#
# spec file for package crudini
#
# Copyright (c) 2023 SUSE LLC
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


Name:           crudini
Version:        0.9.4
Release:        0
Summary:        A utility for manipulating ini files
License:        GPL-2.0-only
Group:          System/Base
URL:            https://github.com/pixelb/crudini
Source0:        https://github.com/pixelb/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-iniparse
Requires:       python3-iniparse
BuildArch:      noarch

%description
A utility for easily handling ini files from the command line and shell
scripts.

%prep
%setup -q

sed -i 's/env python/python3/' crudini.py

%build

%install
install -m 0755 -D %{name}.py %{buildroot}%{_bindir}/%{name}
install -m 0644 -D %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
pushd tests
LC_ALL=en_US.utf8 ./test.sh
popd

%files
%license COPYING
%doc README.md EXAMPLES TODO NEWS example.ini
%{_bindir}/crudini
%{_mandir}/man1/*

%changelog
