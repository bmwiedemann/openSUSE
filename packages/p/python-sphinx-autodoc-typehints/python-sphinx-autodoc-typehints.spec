#
# spec file for package python-sphinx-autodoc-typehints
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


%define modname sphinx_autodoc_typehints
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-sphinx-autodoc-typehints%{psuffix}
Version:        2.2.2
Release:        0
Summary:        Type hints (PEP 484) support for the Sphinx autodoc extension
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tox-dev/sphinx-autodoc-typehints
Source:         https://files.pythonhosted.org/packages/source/s/sphinx_autodoc_typehints/sphinx_autodoc_typehints-%{version}.tar.gz
# PATCH-FIX-OPENSUSE python-sphinx-autodoc-typehints-system-object.inv.patch gh#agronholm/sphinx-autodoc-typehints#174 mcepl@suse.com
# Don't download inventory from the Internet, but use the local one.
Patch0:         python-sphinx-autodoc-typehints-system-object.inv.patch
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.7
BuildArch:      noarch
%if %{with test}
# SECTION tests
BuildRequires:  %{python_module Sphinx >= 7.3.5}
BuildRequires:  %{python_module doc}
BuildRequires:  %{python_module nptyping >= 2.5}
BuildRequires:  %{python_module pytest >= 8.1.1}
BuildRequires:  %{python_module sphobjinv >= 2.3.1}
BuildRequires:  %{python_module typing_extensions >= 4.11}
%endif
# /SECTION
%python_subpackages

%description
This is a Sphinx extension which allows to use Python 3 annotations for documenting acceptable argument types
and return value types of functions.

%prep
%autosetup -p1 -n sphinx_autodoc_typehints-%{version}

%build
%pyproject_wheel
%python_expand sed -i -e 's/@PYTHON_VERSION@/%{$python_version}/' tests/conftest.py

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
export PYTHONPATH=./src
%if %{with test}
# test_sphinx_output -- too depenedent on sphinx version available
# gh#tox-dev/sphinx-autodoc-typehints#229
%pytest -k 'not (test_sphinx_output or test_format_annotation)'
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/%{modname}-%{version}*-info
%{python_sitelib}/%{modname}
%endif

%changelog
