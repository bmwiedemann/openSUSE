#
# spec file for package python-python-dateutil
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


%define oldpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-python-dateutil%{psuffix}
Version:        2.9.0.post0
Release:        0
Summary:        A Python Datetime Library
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://dateutil.readthedocs.org/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/p/python-dateutil/python-dateutil-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove-six.patch gh#dateutil/dateutil!1403 mcepl@suse.com
# remove dependency on the six module
Patch0:         remove-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 24.3}
# Don't pin to <8 like upstream does: gh#dateutil/dateutil#1346
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      python-dateutil < %{version}-%{release}
Provides:       python-dateutil = %{version}-%{release}
Provides:       python-python_dateutil = %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  timezone
%endif
%ifpython2
Obsoletes:      %{oldpython}-dateutil < %{version}
Provides:       %{oldpython}-dateutil = %{version}
%endif
%python_subpackages

%description
The python dateutil module provides powerful extensions to the standard
datetime module.

* Computing of relative deltas (next month, next year, next monday,
   last week of month, etc.)

* Computing of relative deltas between two given dates and/or
   datetime objects

* Computing of dates based on very flexible recurrence rules, using
   a superset of the iCalendar specification. Parsing of RFC strings
   is supported as well.

* Generic parsing of dates in almost any string format.

* Timezone (tzinfo) implementations for tzfile(5) format files
   (%{_sysconfdir}/localtime, %{_datadir}/zoneinfo, etc.), TZ environment
   string (in all known formats), iCalendar format files, given
   ranges (with help from relative deltas), local machine timezone,
   fixed offset timezone, UTC timezone, and Windows registry-based
   time zones.

* Internal up-to-date world timezone information based on Olson's
   database.

* Computing of Easter Sunday dates for any given year, using Western,
Orthodox or Julian algorithms.

%prep
%autosetup -p1 -n python-dateutil-%{version}
#cleanup and MSdos style end of line separators
dos2unix LICENSE NEWS PKG-INFO README.rst

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
rm setup.cfg
export LANG=en_US.UTF-8
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc NEWS PKG-INFO README.rst
%license LICENSE
%{python_sitelib}/dateutil
%{python_sitelib}/python_dateutil-%{version}.dist-info
%endif

%changelog
