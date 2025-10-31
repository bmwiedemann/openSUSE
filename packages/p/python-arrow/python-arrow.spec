#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-arrow%{?psuffix}
Version:        1.4.0
Release:        0
Summary:        Better dates and times for Python
License:        Apache-2.0
URL:            https://github.com/arrow-py/arrow
Source:         https://files.pythonhosted.org/packages/source/a/arrow/arrow-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.7.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module arrow == %{version}}
BuildRequires:  %{python_module dateparser}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz >= 2025.02}
BuildRequires:  %{python_module simplejson}
%endif
%python_subpackages

%description
Arrow is a Python library that offers a sensible, human-friendly
approach to creating, manipulating, formatting and converting dates,
times, and timestamps.  It implements and updates the datetime type,
plugging gaps in functionality, and provides an intelligent module
API that supports many common creation scenarios.  Simply put, it
helps you work with dates and times with fewer imports and a lot
less code.

Arrow is heavily inspired by moment.js and requests.

%prep
%setup -q -n arrow-%{version}
rm -rf arrow.egg-info
# typing stubs not required for runtime gh#arrow-py/arrow#1169
sed -i '/dependencies = /,/]/ {/types-python-dateutil/d}' pyproject.toml

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
rm tox.ini
%pytest
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/arrow
%{python_sitelib}/arrow-%{version}*-info
%endif

%changelog
