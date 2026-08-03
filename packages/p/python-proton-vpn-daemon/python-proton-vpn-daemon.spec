#
# spec file for package python-proton-vpn-daemon
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         _name proton_vpn_daemon
Name:           python-proton-vpn-daemon
Version:        0.13.6
Release:        0
Summary:        ProtonVPN daemon package 
License:        GPL-3.0-only
URL:            https://github.com/ProtonVPN/proton-vpn-daemon
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module dbus_fast}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proton-vpn-api-core}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module systemd}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
%{name} ontains all daemons that are required for the CLI and GUI App of ProtonVPN

%prep
%autosetup -n proton-vpn-daemon-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc README.md
%{python_sitelib}/proton
%{python_sitelib}/%{_name}-%{version}.dist-info

%changelog
