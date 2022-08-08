#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
# fallback if primary_python is not available from the project configuration
%{?!primary_python:%define primary_python python3%{?!sle_version:10}}
# in order to avoid rewriting for subpackage generator
%define mypython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "primary"
# this one is goes into Ring0
%define pprefix %{primary_python}
%define pythons %{primary_python}
# Avoid cycle with python-rpm-packaging requiring python3-packaging
#!BuildIgnore:  python3-packaging
%endif
%if "%{flavor}" == ""
# The rest is in Ring1
%define pprefix python
%if 0%{suse_version} >= 1550 || 0%{?sle_version} == 150500
%{expand:%%define skip_%{primary_python} 1}
BuildRequires:  python3-packaging
%else
# no non-primary python in <=15.4
ExclusiveArch:  do-not-build
%define python_module() no-build-without-multibuild-flavor
%endif
%endif
%if "%{flavor}" == "test"
%define pprefix python
%define psuffix -test
%bcond_without test
%else
%bcond_with test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           %{pprefix}-packaging%{?psuffix}
Version:        21.3
Release:        0
Summary:        Core utilities for Python packages
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://github.com/pypa/packaging
Source:         https://files.pythonhosted.org/packages/source/p/packaging/packaging-%{version}.tar.gz
# Fix testsuite on big-endian systems
# see: https://github.com/pypa/packaging/pull/538
Patch2:         fix-big-endian-build.patch
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#!BuildIgnore:  post-build-checks-malwarescan
# ! Do not add setuptools build dependency here, so that the primary package can be in Ring0 !
# ! Also make sure all runtime dependencies don't require setuptools. !
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module packaging = %{version}}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest}
%endif
%if "%{flavor}" == "primary"
# See boo#1186870, we can't provide ourselves to pythondistdeps.py
Provides:       %{mypython}%{python_version}dist(%{modname}) = %{version}-%{release}
Provides:       %{mypython}3-%{modname} = %{version}-%{release}
Provides:       %{mypython}3dist(%{modname}) = %{version}-%{release}
Obsoletes:      %{mypython}3-%{modname} < %{version}-%{release}
Requires:       %{primary_python}-pyparsing >= 2.0.2
Requires:       %{mypython}(abi) = %{python_version}
%else
Requires:       python-pyparsing >= 2.0.2
%endif
%python_subpackages

%description
Core utilities for Python packages

%prep
%autosetup -p1 -n packaging-%{version}

%if !%{with test}
%build
%{python_expand # build using pythonXX-base bundled setuptools
$python -m venv venv-%{$python_bin_suffix}
venv-%{$python_bin_suffix}/bin/python setup.py build
}
%endif

%if !%{with test}
%install
%{python_expand # install using pythonXX-base bundled setuptools.
# This will work until deprecated support of setup.py install is removed from the bundled setuptools.
# Hopefully upstream packaging comes up with a better bootstrapping process by then.
# (https://github.com/pypa/packaging/pull/536, https://github.com/pypa/packaging/pull/546)
venv-%{$python_bin_suffix}/bin/python setup.py install \
 -O1 --skip-build --force --root %{buildroot} --prefix %{_prefix}
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
%doc CHANGELOG.rst README.rst
%{python_sitelib}/packaging
%{python_sitelib}/packaging-%{version}*-info
%endif

%changelog
