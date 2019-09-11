#
# spec file for package python-pytz
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytz
Version:        2019.2
Release:        0
Summary:        World timezone definitions, modern and historical
License:        MIT
Group:          Development/Languages/Python
URL:            https://pythonhosted.org/pytz/
Source:         https://files.pythonhosted.org/packages/source/p/pytz/pytz-%{version}.tar.gz
Source2:        https://files.pythonhosted.org/packages/source/p/pytz/pytz-%{version}.tar.gz.asc
Source90:       %{name}.keyring
# PATCH-FIX-UPSTREAM fix-tests.patch -- Remote tests which are known to be broken
Patch0:         fix-tests.patch
# PATCH-FEATURE-OPENSUSE -- Use system tz database (Olson database)
Patch1:         system_zoneinfo.patch
# PATCH-FIX-UPSTREAM 0001-Fix-tests-for-older-timezone-versions.patch -- https://code.launchpad.net/~toabctl/pytz/+git/pytz/+merge/326419
Patch2:         0001-Fix-tests-for-older-timezone-versions.patch
BuildRequires:  %{python_module setuptools}
# pytest is required only because of 2.7 stdlib test runner, python3
# unittest runner is sufficient.
BuildRequires:  %{python_module pytest}
# Test requirements
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  timezone
Requires:       python-base
Requires:       timezone
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-tz = %{version}
Obsoletes:      %{oldpython}-tz < %{version}
%endif
%python_subpackages

%description
pytz - World Timezone Definitions for Python
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.4
or higher. It also solves the issue of ambiguous times at the end
of daylight savings, which you can read more about in the Python
Library Reference (``datetime.tzinfo``).

Amost all of the Olson timezones are supported.

%prep
%setup -q -n pytz-%{version}
%autopatch -p1

# For rpmlint warning: remove shebang from python library:
sed -i '/^#!/d' ./pytz/tzfile.py

%build
%python_build

%install
%python_install
%python_expand rm -fr %{buildroot}%{$python_sitelib}/pytz/zoneinfo
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=. py.test-%{$python_bin_suffix} -v pytz/tests

%files %{python_files}
%license LICENSE.txt
%doc README.txt
%{python_sitelib}/*

%changelog
