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
Name:           python-editables%{psuffix}
Version:        0.5
Release:        0
Summary:        Editable installations
License:        MIT
URL:            https://github.com/pfmoore/editables
Source:         https://files.pythonhosted.org/packages/source/e/editables/editables-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core >= 3.3}
BuildRequires:  %{python_module pip}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module editables = %{version}}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
%python_subpackages

%description
A Python library for creating "editable wheels"

This library supports the building of wheels which, when installed, will expose
packages in a local directory on sys.path in "editable mode". In other words,
changes to the package source will be reflected in the package visible to
Python, without needing a reinstall.

%prep
%setup -q -n editables-%{version}

# fix end of lines for the readme
dos2unix -c ascii README.md

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/editables
%{python_sitelib}/editables-%{version}*-info
%endif

%changelog
