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
Version:        2.4.0
Release:        0
Summary:        Module for date conversions from and to Gregorian calendar
License:        MIT
URL:            https://github.com/fitnr/convertdate
Source:         https://github.com/fitnr/convertdate/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyMeeus >= 0.3.6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyMeeus >= 0.3.6}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%pyproject_wheel

%install
export LC_ALL="en_US.UTF8"
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/censusgeocode

%check
export LC_ALL="en_US.UTF8"
%pytest %{?jobs:-n %jobs}

%post
%python_install_alternative censusgeocode

%postun
%python_uninstall_alternative censusgeocode

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/censusgeocode
%{python_sitelib}/convertdate
%{python_sitelib}/convertdate-%{version}.dist-info

%changelog
