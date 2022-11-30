#
# spec file for package python-protonvpn-nm-lib
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
# test suite requires network connection, you can test locally with `rpmbuild --with test`
%bcond_with test
Name:           python-protonvpn-nm-lib
Version:        3.14.0
Release:        0
Summary:        Proton VPN NetworkManager library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ProtonVPN/protonvpn-nm-lib
Source:         https://github.com/ProtonVPN/protonvpn-nm-lib/archive/refs/tags/%{version}.tar.gz#/protonvpn-nm-lib-%{version}.tar.gz
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  python-rpm-macros
# SECTION check that all runtime requirements are available
BuildRequires:  NetworkManager-openvpn
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module keyring}
BuildRequires:  %{python_module proton-client >= 0.5.0}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module systemd}
BuildRequires:  dbus-1-x11
# /SECTION
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
Requires:       NetworkManager-openvpn
Requires:       dbus-1-x11
Requires:       python-Jinja2
Requires:       python-dbus-python
Requires:       python-distro
Requires:       python-gobject
Requires:       python-keyring
Requires:       python-proton-client >= 0.5.0
Requires:       python-pyxdg
Requires:       python-systemd
BuildArch:      noarch
%python_subpackages

%description
The Proton VPN NetworkManager library

%prep
%setup -q -n protonvpn-nm-lib-%{version}
sed -i '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pytest
%endif

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/protonvpn_nm_lib
%{python_sitelib}/protonvpn_nm_lib-%{version}*-info

%changelog
