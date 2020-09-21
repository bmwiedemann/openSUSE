#
# spec file for package python-python-jsonrpc-server
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname python-jsonrpc-server
%bcond_without python2
Name:           python-python-jsonrpc-server
Version:        0.4.0
Release:        0
Summary:        JSON RPC 2.0 server library
License:        MIT
URL:            https://github.com/palantir/python-jsonrpc-server
Source:         https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module ujson}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python2-future >= 0.14.0
BuildRequires:  python2-futures
%endif
Requires:       python-ujson
%ifpython2
Requires:       python2-future >= 0.14.0
Requires:       python2-futures
%endif

%python_subpackages

%description
A Python 2.7 and 3.4+ server implementation of the JSON RPC 2.0 protocol.
This library has been pulled out of the Python Language Server project.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Remove pytest addopts
rm setup.cfg
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pyls_jsonrpc
%{python_sitelib}/python_jsonrpc_server-%{version}-*.egg-info

%changelog
