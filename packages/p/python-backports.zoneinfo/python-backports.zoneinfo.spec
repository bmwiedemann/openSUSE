#
# spec file for package python-backports.zoneinfo
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python39 1
%define skip_python310 1
%define skip_python311 1
Name:           python-backports.zoneinfo
Version:        0.2.1
Release:        0
Summary:        Backport of new features in Python's zoneinfo module
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pganssle/zoneinfo
Source:         https://github.com/pganssle/zoneinfo/archive/refs/tags/%{version}.tar.gz#/backports.zoneinfo-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM zoneinfo-0.2.1-santiago-tz2022a.patch -- gh#pganssle/zoneinfo#114, gh#pganssle/zoneinfo#115 (+ gh#pganssle/zoneinfo#101)
Patch1:         zoneinfo-0.2.1-santiago-tz2022a.patch
Patch2:         zoneinfo-remove-dublin-check.patch
BuildRequires:  %{python_module devel < 3.9}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module dataclasses if %python-base < 3.7}
BuildRequires:  %{python_module hypothesis >= 5.7.0}
BuildRequires:  %{python_module importlib_metadata if %python-base < 3.8}
BuildRequires:  %{python_module importlib_resources if %python-base < 3.7}
BuildRequires:  %{python_module pytest-subtests}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
BuildRequires:  timezone >= 2022a
# /SECTION
%if 0%{?python_version_nodots} < 37
Requires:       python-importlib_resources
%endif
%python_subpackages

%description
This package provides backports of new features in Python's zoneinfo module
under the backports namespace.

%prep
%autosetup -p1 -n zoneinfo-%{version}

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitearch}/backports/__init__.py*
%python_expand rm -f %{buildroot}%{$python_sitearch}/backports/__pycache__/__init__*.py*
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# no "bad" timezone in system data, possibly related: https://github.com/pganssle/zoneinfo/issues/78
donttest="((ZoneInfoDatetimeSubclassTest or ZoneInfoSubclassTest or ZoneInfoTest or ZoneInfoV1Test) and test_bad_keys)"
# free() error: https://github.com/pganssle/zoneinfo/issues/116
donttest="$donttest or (CZoneInfoDatetimeSubclassTest and test_folds_from_utc)"
%pytest_arch -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitearch}/backports
%{python_sitearch}/backports/zoneinfo
%{python_sitearch}/backports.zoneinfo-%{version}*-info

%changelog
