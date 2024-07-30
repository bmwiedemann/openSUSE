#
# spec file for package python-deprecation-alias
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-deprecation-alias%{psuffix}
Version:        0.3.3
Release:        0
Summary:        A wrapper around 'deprecation' providing support for deprecated aliases
License:        Apache-2.0
URL:            https://github.com/domdfcoding/deprecation-alias
Source:         https://github.com/domdfcoding/deprecation-alias/archive/refs/tags/v%{version}.tar.gz#/deprecation-alias-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.6.0}
BuildRequires:  %{python_module wheel >= 0.34.2}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module deprecation-alias = %{version}}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-deprecation >= 2.1.0
Requires:       python-packaging >= 20.4
BuildArch:      noarch
%python_subpackages

%description
A wrapper around 'deprecation' providing support for deprecated aliases.

%prep
%autosetup -p1 -n deprecation-alias-%{version}

%build
%pyproject_wheel

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
%doc README.rst
%license LICENSE
%{python_sitelib}/deprecation_alias
%{python_sitelib}/deprecation_alias-%{version}.dist-info
%endif

%changelog
