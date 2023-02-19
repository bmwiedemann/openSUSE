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


%define modname pyparsing
# in order to avoid rewriting for subpackage generator
%define mypython python
%global flavor @BUILD_FLAVOR@%{nil}
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
# ... unless the build set is empty. (We can't use shrink server-side and any skips here or on project level may have left spaces)
%if "%{pythons}" == "" || "%{pythons}" == " " || "%{pythons}" == "  " || "%{pythons}" == "   " || "%{pythons}" == "    "
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
%if "%{flavor}" == "test"
%define pprefix python
%define psuffix -test
%bcond_without test
%else
%bcond_with test
%endif
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
