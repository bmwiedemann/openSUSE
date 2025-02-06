#
# spec file for package python-zope.location
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-zope.location%{psuffix}
Version:        5.1
Release:        0
Summary:        Zope Location
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://www.python.org/pypi/zope.location
Source:         https://files.pythonhosted.org/packages/source/z/zope_location/zope_location-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.schema >= 4.2.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.interface >= 4.0.2
Requires:       python-zope.proxy >= 4.0.1
Requires:       python-zope.schema >= 4.2.2
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module zope.component >= 4.0.1}
BuildRequires:  %{python_module zope.configuration}
BuildRequires:  %{python_module zope.copy >= 4.0}
BuildRequires:  %{python_module zope.proxy}
BuildRequires:  %{python_module zope.testrunner}
%endif
%python_subpackages

%description
In Zope3, location are special objects that has a structural location.

%prep
%autosetup -p1 -n zope_location-%{version}
rm -rf src/zope.location.egg-info

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%python_expand PYTHONPATH=src %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc COPYRIGHT.txt CHANGES.rst README.rst
%{python_sitelib}/*
%endif

%changelog
