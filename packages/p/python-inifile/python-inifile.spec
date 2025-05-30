#
# spec file for package python-inifile
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-inifile
Version:        0.4.1
Release:        0
Summary:        A small INI library for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mitsuhiko/python-inifile
Source0:        https://files.pythonhosted.org/packages/source/i/inifile/inifile-%{version}.tar.gz
# Files missing from tarball
Source1:        missing_files.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A small INI library for Python.

%prep
%setup -q -a1 -n inifile-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test.py

%files %{python_files}
%license LICENSE
%{python_sitelib}/inifile.py
%{python_sitelib}/inifile-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/inifile*

%changelog
