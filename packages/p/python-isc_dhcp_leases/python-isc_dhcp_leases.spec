#
# spec file for package python-isc_dhcp_leases
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


Name:           python-isc_dhcp_leases
Version:        0.9.1
Release:        0
Summary:        Python module for reading dhcpd.leases from ISC DHCP server
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/MartijnBraam/python-isc-dhcp-leases
Source:         https://github.com/MartijnBraam/python-isc-dhcp-leases/archive/%{version}.tar.gz#/isc_dhcp_leases-%{version}.tar.gz
# https://github.com/MartijnBraam/python-isc-dhcp-leases/issues/38
Patch0:         python-isc_dhcp_leases-remove-unused-code.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module freezegun}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Python module for reading dhcpd.leases from ISC DHCP server.
This module also supports reading lease files from the ISC DHCP daemon
running in IPv6 mode.

%prep
%setup -q -n python-isc-dhcp-leases-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%{python_sitelib}/isc_dhcp_leases*

%changelog
