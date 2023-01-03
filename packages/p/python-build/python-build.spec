#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%define skip_python2 1
Name:           python-build%{psuffix}
Version:        0.9.0
Release:        0
Summary:        Simple PEP517 package builder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pypa/build
Source0:        https://github.com/pypa/build/archive/%{version}.tar.gz#/build-%{version}.tar.gz
# Needs the wheels for wheel, flit-core (<3), pytoml, and tomli for testing
Source10:       https://files.pythonhosted.org/packages/py2.py3/w/wheel/wheel-0.37.1-py2.py3-none-any.whl
Source11:       https://files.pythonhosted.org/packages/py2.py3/f/flit-core/flit_core-2.3.0-py2.py3-none-any.whl
Source12:       https://files.pythonhosted.org/packages/py2.py3/p/pytoml/pytoml-0.1.21-py2.py3-none-any.whl
Source13:       https://files.pythonhosted.org/packages/py3/t/tomli/tomli-2.0.1-py3-none-any.whl
# PATCH-FIX-UPSTREAM build-pr550-packaging22.patch gh#pypa/build#550
Patch1:         https://github.com/pypa/build/pull/550.patch#/build-pr550-packaging22.patch
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module importlib-metadata >= 0.22 if %python-base < 3.8}
BuildRequires:  %{python_module packaging >= 19.0}
BuildRequires:  %{python_module pep517 >= 0.9.1}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module tomli >= 1.0.0 if %python-base < 3.11}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 0.19.0
Requires:       python-pep517 >= 0.9.1
Requires:       (python-importlib-metadata >= 0.22 if python-base < 3.8)
Requires:       (python-tomli if python-base < 3.11)
Recommends:     python-virtualenv >= 20.0.35
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module build = %{version}}
BuildRequires:  %{python_module filelock >= 3}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module pytest-mock >= 2}
BuildRequires:  %{python_module pytest-rerunfailures >= 9.1}
BuildRequires:  %{python_module pytest-xdist >= 1.34}
BuildRequires:  %{python_module toml >= 0.10.0}
BuildRequires:  %{python_module wheel >= 0.36}
BuildRequires:  python3-setuptools-wheel
%endif
%python_subpackages

%description
Build will invoke the PEP 517 hooks to build a distribution package.
It is a simple build tool and does not perform any dependency management.

%prep
%autosetup -p1 -n build-%{version}

%if !%{with test}
%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyproject-build
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
mkdir -p wheels
cp %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} wheels/
export PIP_FIND_LINKS="%{python3_sitelib}/../wheels $PWD/wheels"
%pytest tests -n auto
%endif

%if !%{with test}
%post
%python_install_alternative pyproject-build

%postun
%python_uninstall_alternative pyproject-build

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pyproject-build
%{python_sitelib}/build
%{python_sitelib}/build-%{version}*-info
%endif

%changelog
