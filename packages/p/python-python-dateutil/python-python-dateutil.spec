#
# spec file for package python-python-dateutil
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
%define oldpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-python-dateutil%{psuffix}
Version:        2.8.0
Release:        0
Summary:        A Python Datetime Library
License:        BSD-3-Clause OR Apache-2.0
Group:          Development/Libraries/Python
URL:            https://dateutil.readthedocs.org/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/p/python-dateutil/python-dateutil-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 18.0.1}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.9.0
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
%ifpython3
Obsoletes:      python3-dateutil < %{version}
Provides:       python3-dateutil = %{version}
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
%setup -q -n python-dateutil-%{version}
#cleanup and MSdos style end of line separators
sed -i 's/\r$//' LICENSE NEWS PKG-INFO README.rst
rm -f setup.cfg

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export LANG=en_US.UTF-8
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} \
    py.test-%{$python_bin_suffix} dateutil/test}
%endif

%if !%{with test}
%files %{python_files}
%doc NEWS PKG-INFO README.rst
%license LICENSE
%{python_sitelib}/dateutil/
%{python_sitelib}/python_dateutil-%{version}-py*.egg-info
%endif

%changelog
