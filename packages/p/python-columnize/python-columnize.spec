#
# spec file for package python-columnize
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%define modname columnize
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-columnize
Version:        0.3.10
Release:        0
License:        MIT
Summary:        Format a simple (i.e. not nested) list into aligned columns
Url:            https://github.com/rocky/pycolumnize
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/c/columnize/columnize-%{version}.tar.gz
# Include test file missed from being included in source tarball
Source1:        https://raw.githubusercontent.com/rocky/pycolumnize/%{version}/test_columnize.py
# PATCH-FEATURE-OPENSUSE drop-nose-requirement.patch badshah400@gmail.com -- Drop requirement on outdated nose; we do not run tests anyway
Patch0:         drop-nose-requirement.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION For tests
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Format a simple (i.e. not nested) list into aligned columns.

%prep
%autosetup -p1 -n columnize-%{version}

cp %{SOURCE1} ./

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc NEWS.md README.rst
%license LICENSE
%{python_sitelib}/%{modname}.py*
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/
%pycache_only %{python_sitelib}/__pycache__/*

%changelog
