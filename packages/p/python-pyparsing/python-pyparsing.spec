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


%define modname pyparsing
# in order to avoid rewriting for subpackage generator
%define mypython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "primary"
# this one is built in Ring0
%define pprefix %{primary_python}
%define pythons %{primary_python}
%endif
%if "%{flavor}" == ""
# The rest is in Ring1
%define pprefix python
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} == 150500
BuildRequires:  python3-base >= 3.6
%{expand:%%define skip_%{primary_python} 1}
%else
%define python_module() no-build-without-multibuild-flavor
# no non-primary python in <=15.4
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
%{?!python_module:%define python_module() python3-%{**}}
Name:           %{pprefix}-pyparsing%{?psuffix}
Version:        3.0.9
Release:        0
Summary:        Grammar Parser Library for Python
License:        GPL-2.0-or-later AND MIT AND GPL-3.0-or-later
URL:            https://github.com/pyparsing/pyparsing/
Source:         https://files.pythonhosted.org/packages/source/p/pyparsing/pyparsing-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module flit-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jinja2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module railroad-diagrams}
%endif
# SECTION boo#1186870: we are a dependency of python-packaging which is used by pythondistdeps.py normally creating this entry
#!BuildIgnore:  python3-packaging
Provides:       %{mypython}%{python_version}dist(%{modname}) = %{version}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       %{mypython}3-%{modname} = %{version}-%{release}
Provides:       %{mypython}3dist(%{modname}) = %{version}
Obsoletes:      %{mypython}3-%{modname} < %{version}-%{release}
%endif
# /SECTION
%python_subpackages

%description
The pyparsing module is an alternative approach to creating and executing
simple grammars, vs. the traditional lex/yacc approach, or the use of regular
expressions. The pyparsing module provides a library of classes that client
code uses to construct the grammar directly in Python code.

%prep
%setup -q -n %{modname}-%{version}

%if !%{with test}
%build
%{python_expand # use pythonXX-base bundled pip as PEP517 frontend for flit-core for every flavor to install
mkdir -p build
$python -m venv build/buildenv --system-site-packages
}
# building pure wheel once is enough
export PATH=$PWD/build/buildenv/bin:$PATH
python -mpip wheel --verbose --progress-bar off \
  --disable-pip-version-check --use-pep517 --no-build-isolation \
  --no-deps --wheel-dir ./dist .

%install
export PATH=$PWD/build/buildenv/bin:$PATH
%{python_expand # install into every active flavored sitelib
python -mpip install \
  --verbose --progress-bar off --disable-pip-version-check \
  --root %{buildroot} \
  --ignore-installed --no-deps \
  --no-index --find-links ./dist pyparsing==%{version}
}
# fix venv install path
mv %{buildroot}/$PWD/build/buildenv %{buildroot}%{_prefix}
rm -r %{buildroot}/home
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/pyparsing
%{python_sitelib}/pyparsing-%{version}*-info
%endif

%changelog
