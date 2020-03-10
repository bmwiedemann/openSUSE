#
# spec file for package python-rope
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


%define upname rope
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rope
Version:        0.16.0
Release:        0
Summary:        A python refactoring library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/python-rope/rope
Source:         https://files.pythonhosted.org/packages/source/r/rope/rope-%{version}.tar.gz
# PATCH-FIX-UPSTREAM isAlive_failed_test.patch gh#python-rope/rope#283 mcepl@suse.com
# Fix problems with aliased collections -> collections.abc
Patch0:         isAlive_failed_test.patch
# PATCH-FIX-UPSTREAM Python38-compatibility.patch mcepl@suse.com
# Remove Python 3.8 incompatibilities
Patch1:         Python38-compatibility.patch
# PATCH-FIX-UPSTREAM obsolete_escape_strings.patch mcepl@suse.com
# Remove weird escpaing of 's' character, which is the syntax error
# these days.
Patch2:         obsolete_escape_strings.patch
# PATCH-FIX-UPSTREAM assertEquals.patch mcepl@suse.com
# assertEquals has been deprecated for long time
Patch3:         assertEquals.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Rope is a python refactoring library.

%prep
%setup -q -n rope-%{version}
%autopatch -p1

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%{python_expand rm -rf %{buildroot}/%{$python_sitelib}/python-rope/ropetest/
%fdupes %{buildroot}/%{$python_sitelib}
}

%check
export LANG=en_US.UTF-8
%pytest -k 'not (test_textual_transformations or test_call_function_and_parameters or test_soi_on_literal_assignment)'

%files %{python_files}
%license COPYING
%doc README.rst
%doc docs/
%{python_sitelib}/

%changelog
