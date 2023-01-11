#
# spec file for package protonvpn-gui
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


%define pythons python3
Name:           protonvpn-cli
Version:        3.13.0
Release:        0
Summary:        Official Proton VPN CLI
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://github.com/ProtonVPN/linux-cli
Source:         https://github.com/ProtonVPN/linux-cli/archive/refs/tags/%{version}.tar.gz#/linux-cli-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools
Requires:       python3-protonvpn-nm-lib >= 3.4.0
Requires:       python3-pythondialog
Provides:       protonvpn-cli = %{version}
BuildArch:      noarch

%description
The Proton VPN CLI is intended for every Proton VPN service user.

%prep
%setup -q -n linux-cli-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}/

%check
%pytest

%files
%doc README.md
%license LICENSE COPYING.md
%{python3_sitelib}/protonvpn_cli
%{python3_sitelib}/protonvpn_cli-%{version}*-info
%{_bindir}/protonvpn-cli

%changelog
