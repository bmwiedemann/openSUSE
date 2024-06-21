#
# spec file for package python-packaging
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


%define modname packaging
# in order to avoid rewriting for subpackage generator
%define mypython python
%global flavor @BUILD_FLAVOR@%{nil}
%if 0%{?suse_version} >= 1550
%if "%{flavor}" == "primary"
# this one is goes into Ring0:  Bootstrap for primary python stack
%define pprefix %{primary_python}
%define pythons %{primary_python}
# Avoid cycle with python-rpm-packaging requiring python3-packaging
#!BuildIgnore:  python3-packaging
%endif
%if "%{flavor}" == ""
# The rest is in Ring1
%define pprefix python
%{expand:%%define skip_%{primary_python} 1}
BuildRequires:  python3-packaging
%endif
%else
# backport and option d projects for 15.X having one or more python in the buildset don't need the Ring split for bootstrap
%if "%{flavor}" == "primary"
%define python_module() invalid-multibuild-flavor-for-15.X
ExclusiveArch:  do-not-build
%else
%define pprefix python
%endif
%{?sle15_python_module_pythons}
%endif
%if "%{flavor}" == "test"
%define pprefix python
%define psuffix -test
%bcond_without test
%else
%bcond_with test
%endif

Name:           %{pprefix}-packaging%{?psuffix}
Version:        24.1
Release:        0
Summary:        Core utilities for Python packages
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://packaging.pypa.io/
#SourceRepository: https://github.com/pypa/packaging
Source:         https://files.pythonhosted.org/packages/source/p/packaging/packaging-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
# python-flit-core is bootstrapped in Ring0 as well
BuildRequires:  %{python_module flit-core >= 3.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#!BuildIgnore:  post-build-checks-malwarescan
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module packaging = %{version}}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest >= 6.2}
%endif
%if "%{flavor}" == "primary"
# See boo#1186870, we can't provide ourselves to pythondistdeps.py
Provides:       %{mypython}%{python_version}dist(%{modname}) = %{version}-%{release}
Provides:       %{mypython}3-%{modname} = %{version}-%{release}
Provides:       %{mypython}3dist(%{modname}) = %{version}-%{release}
Obsoletes:      %{mypython}3-%{modname} < %{version}-%{release}
Requires:       %{mypython}(abi) = %{python_version}
%endif
%python_subpackages

%description
Reusable core utilities for various Python Packaging interoperability specifications.

This library provides utilities that implement the interoperability specifications
which have clearly one correct behaviour (eg: PEP 440) or benefit greatly from having
a single shared implementation (eg: PEP 425).

%prep
%autosetup -p1 -n packaging-%{version}

%if !%{with test}
%build
%{python_expand # build using pythonXX-base bundled pip with the installed flit-core backend
$python -m venv venv-%{$python_bin_suffix} --system-site-packages
venv-%{$python_bin_suffix}/bin/pip wheel %{pyproject_wheel_args} .
}
%endif

%if !%{with test}
%install
%{python_expand # install wheel (into venv sitelib) and move to buildroot system sitelib
venv-%{$python_bin_suffix}/bin/pip install %{pyproject_install_args} packaging==%{version}
venvsite=%{buildroot}${PWD}/venv-%{$python_bin_suffix}/lib/python%{$python_bin_suffix}/site-packages
mkdir -p %{buildroot}%{$python_sitelib}
mv ${venvsite}/packaging* %{buildroot}%{$python_sitelib}/
pushd %{buildroot}
rmdir -p $(realpath --relative-to ${PWD} ${venvsite})
popd
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst
%{python_sitelib}/packaging
%{python_sitelib}/packaging-%{version}.dist-info
%endif

%changelog
