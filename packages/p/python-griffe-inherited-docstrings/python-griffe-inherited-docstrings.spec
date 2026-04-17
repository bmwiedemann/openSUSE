#
# spec file for package python-griffe-inherited-docstrings
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define upname  griffe_inherited_docstrings
Name:           python-griffe-inherited-docstrings%{psuffix}
Version:        1.1.3
Release:        0
Summary:        Griffe extension for inheriting docstrings
License:        ISC
URL:            https://mkdocstrings.github.io/griffe-inherited-docstrings
Source:         https://files.pythonhosted.org/packages/source/g/griffe-inherited-docstrings/%{upname}-%{version}.tar.gz
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module griffe-inherited-docstrings = %{version}}
BuildRequires:  %{python_module griffelib >= 2.0}
BuildRequires:  %{python_module mkdocstrings}
BuildRequires:  %{python_module pytest}
# /SECTION
%endif
BuildRequires:  fdupes
Requires:       python-griffelib >= 2.0
BuildArch:      noarch
%python_subpackages

%description
Griffe extension for inheriting docstrings.

The extension will iterate on every class and their members
to set docstrings from parent classes when they are not already defined.

%prep
%autosetup -p1 -n %{upname}-%{version}

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%{python_sitelib}/%{upname}
%{python_sitelib}/%{upname}-%{version}.dist-info
%endif

%changelog
