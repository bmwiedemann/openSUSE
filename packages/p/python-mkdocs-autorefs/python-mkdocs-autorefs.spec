#
# spec file for package python-mkdocs-autorefs
#
# Copyright (c) 2026 SUSE LLC
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
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-mkdocs-autorefs%{psuffix}
Version:        1.4.4
Release:        0
Summary:        Automatically link across pages in MkDocs
License:        ISC
URL:            https://mkdocstrings.github.io/autorefs
Source:         https://files.pythonhosted.org/packages/source/m/mkdocs_autorefs/mkdocs_autorefs-%{version}.tar.gz
BuildRequires:  %{python_module Markdown >= 3.3}
BuildRequires:  %{python_module MarkupSafe >= 2.0.1}
BuildRequires:  %{python_module mkdocs >= 1.1}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pymdown-extensions >= 10.14}
BuildRequires:  %{python_module tomli >= 2.0 if %python-base < 3.11}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Markdown >= 3.3
Requires:       python-MarkupSafe >= 2.0.1
Requires:       python-mkdocs >= 1.1
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module mkdocstrings}
BuildRequires:  %{python_module mkdocs-autorefs = %{version}}
BuildRequires:  %{python_module mkdocs-material}
BuildRequires:  %{python_module griffe}
BuildRequires:  %{python_module pytest-randomly}
BuildRequires:  %{python_module pytest}
# /SECTION
%endif
%python_subpackages

%description
Automatically link across pages in MkDocs.

%prep
%autosetup -p1 -n mkdocs_autorefs-%{version}

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%{python_sitelib}/mkdocs_autorefs
%{python_sitelib}/mkdocs_autorefs-%{version}.dist-info
%endif


%changelog
