#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-build%{psuffix}
Version:        0.7.0
Release:        0
Summary:        Simple PEP517 package builder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pypa/build
Source0:        https://github.com/pypa/build/archive/%{version}.tar.gz#/build-%{version}.tar.gz
BuildRequires:  %{python_module importlib-metadata >= 0.22 if %python-base < 3.8}
BuildRequires:  %{python_module packaging >= 19.0}
BuildRequires:  %{python_module pep517 >= 0.9.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli >= 1.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 0.19.0
Requires:       python-pep517 >= 0.9.1
Requires:       python-tomli
Requires:       (python-importlib-metadata >= 0.22 if python-base < 3.8)
Recommends:     python-virtualenv >= 20.0.35
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module build = %{version}}
BuildRequires:  %{python_module filelock >= 3}
BuildRequires:  %{python_module pytest-mock >= 2}
BuildRequires:  %{python_module pytest-rerunfailures >= 9.1}
BuildRequires:  %{python_module pytest-xdist >= 1.34}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml >= 0.10.0}
BuildRequires:  %{python_module wheel >= 0.36}
%endif
%python_subpackages

%description
Build will invoke the PEP 517 hooks to build a distribution package.
It is a simple build tool and does not perform any dependency management.

%prep
%autosetup -p1 -n build-%{version}

%build
%python_build

%if !%{with test}
%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyproject-build
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# obs can't download packages into "isolated" envs
donttest="test_build_package"
donttest+=" or (test_wheel_metadata and True)"
donttest+=" or test_with_get_requires"
donttest+=" or test_wheel_metadata_isolation"
donttest+=" or test_output and (via-sdist-isolation or wheel-direct-isolation)"
%pytest tests -n auto -k "not ($donttest)"
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
