#
# spec file for package yast2-adcommon-python
#
# Copyright (c) 2020 SUSE LLC
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


Name:           yast2-adcommon-python
Version:        1.5
Release:        0
Summary:        Common code for the yast python ad modules
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
URL:            https://github.com/dmulder/yast2-adcommon-python
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       krb5-client
Requires:       python3-keyring
Requires:       python3-ldap
Requires:       python3-ldb
Requires:       samba-ad-dc
Requires:       samba-client
Requires:       samba-dsdb-modules
Requires:       samba-python3
Requires:       yast2
Requires:       yast2-python3-bindings >= 4.0.0
BuildRequires:  python3
BuildRequires:  python3-setuptools

%description
Common code shared by the yast2-aduc, yast2-adsi, and yast2-gpmc modules.

%prep
%setup -q

%build

%install
./setup.py install --no-compile --single-version-externally-managed --root=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/adcommon-*.egg-info

%clean

%files
%defattr(-,root,root)
%dir %{python3_sitelib}/adcommon
%{python3_sitelib}/adcommon/*

%changelog
