#
# spec file for package python-crontab
#
# Copyright (c) 2021 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-crontab
Version:        0.23.0
Release:        0
Summary:        Python module for parsing and using crontab schedules
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://github.com/josiahcarlson/parse-crontab
Source:         https://github.com/josiahcarlson/parse-crontab/archive/%{version}.tar.gz#/crontab-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Requires:       python-pytz
BuildArch:      noarch
%python_subpackages

%description
This package offers a method of parsing crontab schedule entries and
determining when an item should next be run. More specifically, it
calculates a delay in seconds from when the .next() method is called
to when the item should next be executed.

%prep
%setup -q -n parse-crontab-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE3
%{python_sitelib}/*

%changelog
