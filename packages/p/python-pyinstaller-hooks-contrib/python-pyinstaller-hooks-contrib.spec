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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pyinstaller-hooks-contrib%{psuffix}
Version:        2022.13
Release:        0
Summary:        Community maintained hooks for PyInstaller
License:        Apache-2.0 OR GPL-2.0-only
URL:            https://github.com/pyinstaller/pyinstaller-hooks-contrib
Source:         https://files.pythonhosted.org/packages/source/p/pyinstaller-hooks-contrib/pyinstaller-hooks-contrib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyInstaller}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyinstaller-hooks-contrib = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  timezone
# SECTION optional, the depending tests would be skipped without these
# most of the libraries enable only two tests, so adding just scikit-learn to run at least any tests
BuildRequires:  %{python_module scikit-learn}
# /SECTION
%endif
%python_subpackages

%description
Community maintained hooks for PyInstaller

%prep
%setup -q -n pyinstaller-hooks-contrib-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest src/_pyinstaller_hooks_contrib/tests
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE LICENSE.APL.txt LICENSE.GPL.txt
%{python_sitelib}/*
%endif

%changelog
