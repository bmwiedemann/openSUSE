#
# spec file for package python-inifile
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-inifile
Version:        0.4.1
Release:        0
License:        BSD-3-Clause
Summary:        A small INI library for Python
URL:            https://github.com/mitsuhiko/python-inifile
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/i/inifile/inifile-%{version}.tar.gz
# Files missing from tarball
Source1:        missing_files.tar.gz
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test.py

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
