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
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-apipkg%{psuffix}
Version:        3.0.2
Release:        0
Summary:        Namespace control and lazy-import mechanism
License:        MIT
URL:            https://github.com/pytest-dev/apipkg/
Source:         https://github.com/pytest-dev/apipkg/archive/refs/tags/v%{version}.tar.gz#/apipkg-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/pytest-dev/apipkg/pull/58
Patch0:         support-pytest-9.patch
%if %{with test}
BuildRequires:  %{python_module apipkg = %{version}}
BuildRequires:  %{python_module pytest >= 7}
# Assumes setuptools is installed, Python 3.12+
BuildRequires:  %{python_module setuptools}
%endif
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
With apipkg you can control the exported namespace of a
python package and greatly reduce the number of imports for your users.
It is a small pure python module that works on CPython 2.7 and 3.4+,
Jython and PyPy.  It co-operates well with Python's help() system,
custom importers (PEP302) and common command line completion tools.

Usage is very simple: you can require 'apipkg' as a dependency or you
can copy paste the ~200 lines of code into your project.

%prep
%autosetup -p1 -n apipkg-%{version}
# Set the package version static, not dynamic, to build without the .git folder
sed -i ':a;N;$!ba;s/dynamic = \[[^]]*\]/version = "%{version}"/g' pyproject.toml
# Remove hatch-vcs dep to avoid cycles
rm .gitignore
sed -i '/tool.hatch.build.hooks.vcs/d' pyproject.toml
cat << EOF > src/apipkg/_version.py
version = "%{version}"
version_tuple = tuple(map(int, version.split(".")))
EOF

%build
%pyproject_wheel

%install
%if ! %{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# Do not test distribution version, it's broken because pytest doesn't require
# python-py anymore
%pytest -k 'not test_get_distribution_version'
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/apipkg
%{python_sitelib}/apipkg-%{version}.dist-info
%endif

%changelog
