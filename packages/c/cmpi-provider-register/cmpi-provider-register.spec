#
# spec file for package cmpi-provider-register
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cmpi-provider-register
Version:        1.1.0
Release:        0
Summary:        CIMOM neutral provider registration utility
License:        BSD-3-Clause
Group:          System/Management
Requires:       cim-schema
%if 0%{?suse_version} >= 1500
Requires:       python3-pywbem
%else
Requires:       python-pywbem
%endif
BuildArch:      noarch
Source0:        cmpi-provider-register.py
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A utility allowing CMPI provider packages to register with various
CIMOM(s) present on the system.

%prep

%build
# For older SUSE distros and others, use whatever default python.
%if 0%{?suse_version} < 1500
sed -i -e 's,^#!/usr/bin/python3,#!/usr/bin/python,' %{S:0}
%endif

%install
mkdir -p %{buildroot}/usr/sbin
install -m 755 %{S:0} %{buildroot}/usr/sbin/cmpi-provider-register

%files
%defattr(-,root,root)
/usr/sbin/cmpi-provider-register

%changelog
