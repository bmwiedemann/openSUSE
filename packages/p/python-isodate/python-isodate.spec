#
# spec file for package python-isodate
#
# Copyright (c) 2023 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-isodate
Version:        0.6.1
Release:        0
Summary:        An ISO 8601 Date/Time/Duration Parser and Formatter
License:        BSD-3-Clause
URL:            https://pypi.org/project/isodate/
Source:         https://files.pythonhosted.org/packages/source/i/isodate/isodate-%{version}.tar.gz
# https://github.com/gweis/isodate/commit/07d1602048083415bc22dc72cff152c9c2e0e021
Patch0:         python-isodate-no-six.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module implements ISO 8601 date, time and duration parsing.
The implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an allowed
option.

%prep
%setup -q -n isodate-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v src/

%files %{python_files}
%doc CHANGES.txt README.rst TODO.txt
%{python_sitelib}/*

%changelog
