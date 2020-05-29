#
# spec file for package python-booleanOperations
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-booleanOperations%{psuffix}
Version:        0.8.2
Release:        0
Summary:        Boolean operations on paths
License:        MIT
URL:            https://github.com/typemytype/booleanOperations
Source:         https://files.pythonhosted.org/packages/source/b/booleanOperations/booleanOperations-%{version}.zip
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 3.32.0
Requires:       python-pyclipper >= 1.0.5
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module FontTools >= 3.32.0}
BuildRequires:  %{python_module defcon}
BuildRequires:  %{python_module fontPens}
BuildRequires:  %{python_module pyclipper >= 1.0.5}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Boolean operations on paths.

%prep
%setup -q -n booleanOperations-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
