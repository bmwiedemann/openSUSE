#
# spec file for package python-simple-websocket
#
# Copyright (c) 2024 SUSE LLC
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

%{?sle15_python_module_pythons}
Name:           python-simple-websocket
Version:        1.0.0
Release:        0
Summary:        Simple WebSocket server and client for Python
License:        MIT
URL:            https://github.com/miguelgrinberg/simple-websocket
Source:         https://files.pythonhosted.org/packages/source/s/simple-websocket/simple-websocket-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module wsproto}
# /SECTION
BuildRequires:  fdupes
Requires:       python-wsproto
Suggests:       python-sphinx
BuildArch:      noarch
%python_subpackages

%description
Simple WebSocket server and client for Python

%prep
%autosetup -p1 -n simple-websocket-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# FIXME: Disable check for now as the upstream tarball test files are incomplete. i.e. helpers.py
# is needed by excluded from the release tarball for whatever reason. Hence, the tests will
# inevitably failed without it.

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/simple_websocket
%{python_sitelib}/simple_websocket-%{version}.dist-info

%changelog
