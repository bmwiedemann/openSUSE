#
# spec file for package python-hypothesmith
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
Name:           python-hypothesmith%{psuffix}
Version:        0.3.3
Release:        0
Summary:        Hypothesis strategies for generating Python programs, something like CSmith
License:        MPL-2.0
URL:            https://github.com/Zac-HD/hypothesmith
Source:         https://files.pythonhosted.org/packages/source/h/hypothesmith/hypothesmith-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base >= 3.7
Requires:       python-hypothesis >= 6.93.0
Requires:       python-lark >= 0.10.1
Requires:       python-libcst >= 0.4.0
%if %{with test}
BuildRequires:  %{python_module exceptiongroup}
BuildRequires:  %{python_module hypothesis >= 6.93.0}
BuildRequires:  %{python_module lark >= 0.10.1}
BuildRequires:  %{python_module libcst >= 0.4.0}
BuildRequires:  %{python_module parso}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
%python_subpackages

%description
Hypothesis strategies for generating Python programs, something like CSmith.

%prep
%setup -q -n hypothesmith-%{version}
# remove pytest coverage opts
rm tox.ini

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
# multibuild: test the source dir, nothing is installed
export PYTHONPATH=$(pwd)/src
# depend on black
rm -v tests/test_cst.py tests/test_syntactic.py
%pytest -n %{?jobs}
%endif

%if !%{with test}
%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/hypothesmith
%{python_sitelib}/hypothesmith-%{version}.dist-info
%endif

%changelog
