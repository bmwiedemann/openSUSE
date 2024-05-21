#
# spec file for package python-testtools
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
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-testtools%{psuffix}
Version:        2.7.1
Release:        0
Summary:        Extensions to the Python Standard Library Unit Testing Framework
License:        MIT
URL:            https://github.com/testing-cabal/testtools
Source0:        https://files.pythonhosted.org/packages/source/t/testtools/testtools-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/testing-cabal/testtools/pull/373 Treat methodName="runTest" similar to unittest.TestCase
Patch:          pytest82.patch
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted
%if %python_version_nodots > 311
Requires:       python-setuptools
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module testresources}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools = %{version}}
%endif
Recommends:     python-fixtures >= 2.0
%python_subpackages

%description
testtools is a set of extensions to the Python standard library's unit tests
framework. These extensions have been derived from many years of experience
with unit tests in Python and come from many different sources. testtools
also ports recent unittest changes all the way back to Python 2.4.

%prep
%autosetup -p1 -n testtools-%{version}

%if !%{with test}
%build
%pyproject_wheel
%endif

%if !%{with test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%python_exec -m testtools.run testtools.tests.test_suite
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc NEWS README.rst
%{python_sitelib}/testtools
%{python_sitelib}/testtools-%{version}.dist-info
%endif

%changelog
