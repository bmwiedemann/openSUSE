#
# spec file for package python-asyncclick
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


%define oldpython python
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-asyncclick
Version:        8.1.3.4
Release:        0
Summary:        A wrapper around optparse for command line utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-trio/asyncclick
Source:         https://files.pythonhosted.org/packages/source/a/asyncclick/asyncclick-%{version}.tar.gz
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
AsyncClick ist a fork of Click that works well with trio or asyncio.

Click is a Python package for creating command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit". It is configurable, and comes with
defaults out of the box.

%prep
%setup -q -n asyncclick-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest -rs --tb=short

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/asyncclick
%{python_sitelib}/asyncclick-*.dist-info/

%changelog
