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


%define modname flit-core
%define mypython python
# fallback if primary_python is not available from the project configuration
%{?!primary_python:%define primary_python python3%{?!sle_version:10}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "primary"
# this one is built in Ring0
%define pprefix %{primary_python}
%define pythons %{primary_python}
%endif
%if "%{flavor}" == ""
# The rest is in Ring1
%define pprefix python
%if 0%{?suse_version} >= 1550
BuildRequires:  python3-base >= 3.6
%{expand:%%define skip_%{primary_python} 1}
%else
%define python_module() no-build-without-multibuild-flavor
# no non-primary python in <=15.5
ExclusiveArch:  do-not-build
%endif
%endif
%if "%{flavor}" == "test"
%define pprefix python
%define psuffix -test
%bcond_without test
%else
%bcond_with test
%endif
Name:           %{pprefix}-flit-core%{?psuffix}
Version:        3.8.0
Release:        0
Summary:        Distribution-building parts of Flit
License:        BSD-3-Clause AND MIT
URL:            https://github.com/pypa/flit
Source0:        https://files.pythonhosted.org/packages/source/f/flit_core/flit_core-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module flit-core = %{version}}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
%else
# SECTION boo#1186870: we are a transitive build dependency of python-packaging which is used by pythondistdeps.py normally creating this entry
#!BuildIgnore:  %{primary_python}-packaging
#!BuildIgnore:  python3-packaging
%endif
Provides:       %{mypython}%{python_version}dist(%{modname}) = %{version}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       %{mypython}3-%{modname} = %{version}-%{release}
Provides:       %{mypython}3dist(%{modname}) = %{version}
Obsoletes:      %{mypython}3-%{modname} < %{version}-%{release}
%endif
# /SECTION
%python_subpackages

%description
This provides a PEP 517 build backend for packages using Flit.
The only public interface is the API specified by PEP 517, at flit_core.buildapi.

%prep
%setup -q -n flit_core-%{version}

%if !%{with test}
%build
# https://flit.readthedocs.io/en/latest/bootstrap.html
python3 -m flit_core.wheel

%install
%{python_expand #
mkdir -p %{buildroot}%{$python_sitelib}
$python bootstrap_install.py dist/flit_core-%{version}-py3-none-any.whl -i %{buildroot}%{$python_sitelib}
# Don't package the tests
rm -r  %{buildroot}%{$python_sitelib}/flit_core/tests
}
%{?python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# make sure we do not test the sources but the package
rm flit_core/*.py pyproject.toml
%pytest -rfEs
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/flit_core
%{python_sitelib}/flit_core-%{version}*-info
%endif

%changelog
