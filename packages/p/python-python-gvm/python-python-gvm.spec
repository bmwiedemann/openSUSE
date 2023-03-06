#
# spec file for package python-python-gvm
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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
%define skip_python36 1
%define skip_python39 1
Name:           python-python-gvm
Version:        23.2.0
Release:        0
Summary:        Library to communicate with remote servers over GMP or OSP
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/greenbone/python-gvm
Source:         https://files.pythonhosted.org/packages/source/p/python_gvm/python_gvm-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-defusedxml >= 0.6.0
Requires:       python-lxml >= 4.5.0
Requires:       python-paramiko >= 2.7.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module defusedxml >= 0.6.0}
BuildRequires:  %{python_module lxml >= 4.5.0}
BuildRequires:  %{python_module paramiko >= 2.7.1}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
The Greenbone Vulnerability Management Python API library python-gvm is a
collection of APIs that help with remote controlling a Greenbone Security
Manager (GSM) appliance and its underlying Greenbone Vulnerability Manager
(GVM). The library essentially abstracts accessing the communication protocols
Greenbone Management Protocol (GMP) and Open Scanner Protocol (OSP).

%prep
%setup -q -n python_gvm-%{version}

%build
%python_build

%install
%python_install
# Remove tests from sitelib
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -v tests/connections/test_unix_socket_connection.py tests/connections/test_ssh_connection.py
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/gvm
%{python_sitelib}/python_gvm*

%changelog
