#
# spec file for package python-holidays
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

%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname hijri-converter
Name:           python-hijri-converter
Version:        2.1.1
Release:        0
Summary:        Python package to convert accurately between Hijri and Gregorian dates
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dralshehri/hijri-converter
Source:         https://github.com/dralshehri/%{modname}/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python package to convert accurately between Hijri and Gregorian dates using the Umm al-Qura calendar of Saudi Arabia.


%prep
%setup -q -n hijri-converter-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/*

%changelog
