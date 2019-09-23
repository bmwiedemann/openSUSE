#
# spec file for package python-convertdate
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
Name:           python-convertdate
Version:        2.1.3
Release:        0
Summary:        Converts between Gregorian dates and other calendar systems
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/fitnr/convertdate
Source:         https://github.com/fitnr/convertdate/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ephem >= 3.7.5.3
Requires:       python-pytz >= 2014.10
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ephem >= 3.7.5.3}
BuildRequires:  %{python_module pytz >= 2014.10}
# /SECTION
%python_subpackages

%description
Converts between Gregorian dates and other calendar systems.Calendars included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic, ISO, Julian, Mayan and Persian.

%prep
%setup -q -n convertdate-%{version}

%build
export LANG="en_US.UTF8"
%python_build

%install
export LANG="en_US.UTF8"
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
