#
# spec file for package python-flit-core
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


%define modname flit-core
%global flavor @BUILD_FLAVOR@%{nil}
%define plainpython python
%if 0%{?suse_version} >= 1550
# The primary python flavor is built in Factory Ring0
%if "%{flavor}" == "primary"
%define pprefix %{primary_python}
%define pythons %{primary_python}
%endif
# Additional flavors are built in Factory Ring1
%if "%{flavor}" == ""
%define pprefix python
%{expand:%%define skip_%{primary_python} 1}
%if "%{shrink:%{pythons}}" == ""
# Exclude for local osc build: unresolvable
%define python_module() empty-python-buildset
# Exclude for obs server
ExclusiveArch:  do-not-build
%endif
%endif
%else
# backport and option d projects for 15.X having one or more python in the buildset don't need the Ring split for bootstrap
%if "%{flavor}" == "primary"
%define python_module() invalid-multibuild-flavor-for-15.X
ExclusiveArch:  do-not-build
%else
%define pprefix python
%endif
%endif
# test everything in the buildset by standard python flavor expansion: primary and non-primary, if any.
%if "%{flavor}" == "test"
%define pprefix python
%define psuffix -test
%endif
%{?sle15_python_module_pythons}
Name:           %{pprefix}-flit-core%{?psuffix}
Version:        3.9.0
Release:        0
Summary:        Distribution-building parts of Flit
License:        BSD-3-Clause AND MIT
URL:            https://github.com/pypa/flit
Source0:        https://files.pythonhosted.org/packages/source/f/flit_core/flit_core-%{version}.tar.gz
Patch1:         https://github.com/pypa/flit/commit/915fa612e227fb4bf67f8484af5c8a399f108526.patch#/py312-avoid-using-utcfromtimestamp.patch
Patch2:         https://github.com/pypa/flit/commit/6ab62c91d0db451b5e9ab000f0dba5471550b442.patch#/py314-avoid-using-ast-str.patch
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if "%{flavor}" == "test"
BuildRequires:  %{python_module flit-core = %{version}}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
%endif
# SECTION boo#1186870
# We are a transitive build dependency of python-packaging
# which is used by pythondistdeps.py normally creating these entries
#!BuildIgnore:  %{primary_python}-packaging
#!BuildIgnore:  python3-packaging
Requires:       %{plainpython}(abi) = %{python_version}
Provides:       %{plainpython}%{python_version}dist(%{modname}) = %{version}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       %{plainpython}3-%{modname} = %{version}-%{release}
Provides:       %{plainpython}3dist(%{modname}) = %{version}
Obsoletes:      %{plainpython}3-%{modname} < %{version}-%{release}
%endif
# /SECTION
%python_subpackages

%description
This provides a PEP 517 build backend for packages using Flit.
The only public interface is the API specified by PEP 517, at flit_core.buildapi.

%prep
%autosetup -p2 -n flit_core-%{version}

%if "%{flavor}" != "test"
%build
# https://flit.readthedocs.io/en/latest/bootstrap.html, take the first available python in the build set
mypython=%{expand:%%__%(echo %{pythons} | cut -d " " -f 1)}
$mypython -m flit_core.wheel

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

%if "%{flavor}" == "test"
%check
# make sure we do not test the sources but the package
rm flit_core/*.py pyproject.toml
%pytest -rfEs
%endif

%if "%{flavor}" != "test"
%files %{python_files}
%{python_sitelib}/flit_core
%{python_sitelib}/flit_core-%{version}*-info
%endif

%changelog
