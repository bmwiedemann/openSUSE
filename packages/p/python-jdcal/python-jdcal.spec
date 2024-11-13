#
# spec file for package python-jdcal
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?sle15_python_module_pythons}
Name:           python-jdcal
Version:        1.4.1
Release:        0
Summary:        Julian dates from proleptic Gregorian and Julian calendars
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://github.com/phn/jdcal
Source:         https://files.pythonhosted.org/packages/source/j/jdcal/jdcal-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
This module contains functions for converting between Julian dates and
calendar dates.

A function for converting Gregorian calendar dates to Julian dates, and
another function for converting Julian calendar dates to Julian dates
are defined. Two functions for the reverse calculations are also
defined.

%prep
%setup -q -n jdcal-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
