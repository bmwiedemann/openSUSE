#
# spec file for package python-sphinxcontrib-autoprogram
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
%define psuffix       %{nil}
%if "%{flavor}" != ""
%define psuffix      -%{flavor}
%endif
%global short_name autoprogram
%{?sle15_python_module_pythons}
Name:           python-sphinxcontrib-%{short_name}%{psuffix}
Version:        0.1.9
Release:        0
%if "%{flavor}" == "" || "%{flavor}" == "test"
Summary:        Sphinx extension to document CLI programs
%endif
%if "%{flavor}" == "doc"
Summary:        Documentation for sphinxcontrib-autoprogram
%endif
License:        BSD-2-Clause
URL:            https://github.com/sphinx-contrib/%{short_name}
Source0:        %{URL}/archive/%{version}/python-sphinxcontrib-%{short_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip-failing-test.patch gh#sphinx-contrib/autoprogram#54 mcepl@suse.com
# Switch off failing tests by the environmental variable SKIPTESTS
Patch1:         skip-failing-test.patch
BuildRequires:  %{python_module Sphinx >= 1.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.2
BuildArch:      noarch
%if "%{flavor}" == "test"
BuildRequires:  %{python_module sphinxcontrib-autoprogram == %{version}}
BuildRequires:  %{python_module sphinxcontrib-websupport >= 1.0.1}
%endif
%if "%{flavor}" == "doc"
BuildRequires:  %{python_module sphinxcontrib-autoprogram == %{version}}
BuildRequires:  %{python_module sphinxcontrib-websupport}
%endif
%python_subpackages

%if "%{flavor}" == "doc"
%description
This package contains the documentation for the package
python-sphinxcontrib-autoprogram.
%endif
%if "%{flavor}" == "" || "%{flavor}" == "test"
%description
This contrib extension, sphinxcontrib.autoprogram, provides an automated way to
document CLI programs. It scans arparser.ArgumentParser object, and then expands
it into a set of .. program:: and .. option:: directives.
%endif

%prep
%autosetup -p1 -n %{short_name}-%{version} -p1

%build
%if "%{flavor}" == ""
%pyproject_wheel
%endif
%if "%{flavor}" == "doc"
sphinx-build -b html -d doc/_build/doctrees doc doc/_build/html
rm doc/_build/html/objects.inv
%endif

%install
%if "%{flavor}" == ""
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if "%{flavor}" == "test"
export SKIPTESTS=1
%pyunittest -v sphinxcontrib.autoprogram.suite
%endif

%if "%{flavor}" == ""
%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitelib}/sphinxcontrib
%dir %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib/autoprogram.py
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__/autoprogram.*.pyc
%{python_sitelib}/sphinxcontrib_autoprogram-%{version}.dist-info
%{python_sitelib}/sphinxcontrib_autoprogram-%{version}*-nspkg.pth
%endif

%if "%{flavor}" == "doc"
%files %{python_files}
%license LICENSE
%doc doc/_build/html/*
%endif

%changelog
