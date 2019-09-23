#
# spec file for package python-statistics
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         skip_python3 1
Name:           python-statistics
Version:        3.4.0b3
Release:        0
Summary:        Python 2.* port of 3.4 Statistics Module
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/digitalemagine/py-statistics
Source:         https://files.pythonhosted.org/packages/source/s/statistics/statistics-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils >= 0.3
BuildArch:      noarch
BuildRequires:  %{python_module docutils >= 0.3}
%python_subpackages

%description
A port of Python 3.4 statistics module to Python 2.*, initially done
through the 3to2 tool.

This module provides functions for calculating mathematical statistics
of numeric (Real-valued) data.

%prep
%setup -q -n statistics-%{version}

%build
%python_build

%check
# no testsuite found

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
