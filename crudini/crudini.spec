#
# spec file for package crudini
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


Name:           crudini
Version:        0.9
Release:        0
Summary:        CRUD for .ini files
License:        GPL-2.0
Group:          System/Base
Url:            https://github.com/pixelb/crudini/releases
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       python-iniparse

%description
A utility for manipulating ini files.

%prep
%setup -q

%build

%install
install -m 0755 -D crudini %{buildroot}/%{_bindir}/crudini

%post

%postun

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/crudini

%changelog
