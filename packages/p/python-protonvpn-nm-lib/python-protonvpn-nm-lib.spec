#
# spec file for package python-protonvpn-nm-lib
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-protonvpn-nm-lib
Version:        3.3.2
Release:        0
Summary:        ProtonVPN NetworkManager library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ProtonVPN/protonvpn-nm-lib
Source:         https://github.com/ProtonVPN/protonvpn-nm-lib/archive/refs/tags/%{version}.tar.gz#/protonvpn-nm-lib-%{version}.tar.gz
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       NetworkManager
Requires:       NetworkManager-openvpn
Requires:       gtk3
Requires:       openvpn
Requires:       python-dbus-python
Requires:       python-distro
Requires:       python-jinja2
Requires:       python-keyring
Requires:       python-proton-client < 0.6.0
Requires:       python-proton-client >= 0.5.0
Requires:       python-pyxdg
Requires:       python-systemd
Requires:       xdg-utils
BuildArch:      noarch
%python_subpackages

%description
The ProtonVPN NetworkManager library

%prep
%setup -q -n protonvpn-nm-lib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/protonvpn_nm_lib

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/protonvpn_nm_lib
%{python_sitelib}/protonvpn_nm_lib-*-py*.*-info

%changelog
