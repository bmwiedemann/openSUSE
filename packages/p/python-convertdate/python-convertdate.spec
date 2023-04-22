#
# spec file for package python-convertdate
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
Name:           python-convertdate
Version:        2.3.2
Release:        0
Summary:        Module for date conversions from and to Gregorian calendar
License:        MIT
URL:            https://github.com/fitnr/convertdate
Source:         https://github.com/fitnr/convertdate/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyMeeus >= 0.3.6
Requires:       python-pytz >= 2014.10
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyMeeus >= 0.3.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz >= 2014.10}
# /SECTION
%python_subpackages

%description
A Python module for converting between Gregorian dates and other
calendar systems. Calendars included: Baha'i, French Republican,
Hebrew, Indian Civil, Islamic, ISO, Julian, Mayan and Persian.

%prep
%setup -q -n convertdate-%{version}
sed -i -e 's:, < 2020::g' setup.py

%build
export LC_ALL="en_US.UTF8"
%python_build

%install
export LC_ALL="en_US.UTF8"
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL="en_US.UTF8"
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
