#
# spec file for package python-sphinx-autodoc-typehints
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           python-sphinx-autodoc-typehints%{psuffix}
Version:        3.13.0
Release:        0
Summary:        Type hints (PEP 484) support for the Sphinx autodoc extension
License:        MIT
URL:            https://github.com/tox-dev/sphinx-autodoc-typehints
Source:         https://files.pythonhosted.org/packages/source/s/sphinx_autodoc_typehints/sphinx_autodoc_typehints-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 9.1
BuildArch:      noarch
%if %{with test}
# SECTION tests
BuildRequires:  %{python_module doc}
BuildRequires:  %{python_module pytest >= 8.1.1}
BuildRequires:  %{python_module sphinx-autodoc-typehints = %{version}}
BuildRequires:  %{python_module sphobjinv >= 2.3.1}
BuildRequires:  %{python_module typing_extensions >= 4.15}

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
%if %{with test}
# test_sphinx_output -- too depenedent on sphinx version available
# gh#tox-dev/sphinx-autodoc-typehints#229
# test_sphinx_build_stub_types_produce_crossrefs -- requires intersphinx, which
# requires network
donttest="test_sphinx_output or test_format_annotation"
donttest+=" or test_sphinx_build_stub_types_produce_crossrefs"
%python_exec -B -m pytest -k "not ($donttest)"
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info
%endif

%changelog
