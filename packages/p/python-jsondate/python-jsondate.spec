#
# spec file for package python-jsondate
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-jsondate
Version:        0.1.2
Release:        0
Summary:        JSON with datetime support
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/rconradharris/jsondate
Source:         https://files.pythonhosted.org/packages/source/j/jsondate/jsondate-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: python3-fixes-pr-6.patch
# From https://github.com/rconradharris/jsondate/pull/6.patch#/python3-fixes-pr-6.patch with removed .gitignore file
Patch0:         python3-fixes-pr-6.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
jsondate is a drop-in replacement for Python's standard json library that
adds sensible handling of datetime and date objects.

jsondate uses ISO8601 for encoding datetime objects and the
date-specific part of ISO6801 for encoding date objects.

%prep
%setup -q -n jsondate-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests are broken upstream and need work to get fixed for 2 and 3
#%%check
#%%python_exec setup.py test

%files %{python_files}
%doc README.rst
%%license LICENSE
%{python_sitelib}/*

%changelog
