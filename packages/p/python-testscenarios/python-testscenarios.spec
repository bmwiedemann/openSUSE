#
# spec file for package python-testscenarios
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-testscenarios%{psuffix}
Version:        0.5.0
Release:        0
Summary:        A pyunit extension for dependency injection
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://launchpad.net/testscenarios
Source:         https://files.pythonhosted.org/packages/source/t/testscenarios/testscenarios-%{version}.tar.gz
BuildRequires:  %{python_module pbr >= 0.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
%if %{with test}
BuildRequires:  %{python_module extras}
BuildRequires:  %{python_module testscenarios = %{version}}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pbr >= 0.11
Requires:       python-testtools
BuildArch:      noarch
%python_subpackages

%description
testscenarios provides clean dependency injection for Python unittest style
tests. This can be used for interface testing (testing many implementations via
a single test suite) or for classic dependency injection (provide tests with
dependencies externally to the test code itself, allowing easy testing in
different situations).

%prep
%setup -q -n testscenarios-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%{python_expand PYTHONPATH=%%{buildroot}%{$python_sitelib}
  $python -m testtools.run testscenarios.test_suite
}
%endif

%if !%{with test}
%files %{python_files}
%license COPYING
%doc Apache-2.0 BSD GOALS HACKING NEWS README
%{python_sitelib}/testscenarios
%{python_sitelib}/testscenarios-%{version}.dist-info
%endif

%changelog
