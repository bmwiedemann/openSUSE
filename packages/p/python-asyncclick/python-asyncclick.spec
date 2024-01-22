#
# spec file for package python-asyncclick
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
%define archiveversion 8.1.7.0-async
Name:           python-asyncclick
Version:        8.1.7.0+async
Release:        0
Summary:        A wrapper around optparse for command line utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-trio/asyncclick
# Upstream forgot to release on PyPI: https://github.com/python-trio/asyncclick/issues/18
#Source:         https://files.pythonhosted.org/packages/source/a/asyncclick/asyncclick-%%{version}.tar.gz
Source:         https://github.com/python-trio/asyncclick/archive/refs/tags/%{version}.tar.gz#/asyncclick-%{archiveversion}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio
# SECTION test
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trio}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
AsyncClick ist a fork of Click that works well with trio or asyncio.

Click is a Python package for creating command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit". It is configurable, and comes with
defaults out of the box.

%prep
%setup -q -n asyncclick-%{archiveversion}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest -rsfE

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/asyncclick
%{python_sitelib}/asyncclick-%{version}.dist-info/

%changelog
