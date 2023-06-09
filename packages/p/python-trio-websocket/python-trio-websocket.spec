#
# spec file for package python-trio-websocket
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


Name:           python-trio-websocket
Version:        0.10.3
Release:        0
Summary:        WebSocket library for Trio
License:        MIT
URL:            https://github.com/HyperionGray/trio-websocket
Source0:        https://files.pythonhosted.org/packages/source/t/trio-websocket/trio-websocket-%{version}.tar.gz
# Not included in sdist
Source1:        https://raw.githubusercontent.com/HyperionGray/trio-websocket/master/pytest.ini
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module exceptiongroup}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trio >= 0.11}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module wsproto >= 0.14}
# /SECTION
BuildRequires:  fdupes
Requires:       python-exceptiongroup
Requires:       python-trio >= 0.11
Requires:       python-wsproto >= 0.14
BuildArch:      noarch
%python_subpackages

%description
WebSocket library for Trio

%prep
%autosetup -p1 -n trio-websocket-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/trio_websocket
%{python_sitelib}/trio_websocket-%{version}.dist-info

%changelog
