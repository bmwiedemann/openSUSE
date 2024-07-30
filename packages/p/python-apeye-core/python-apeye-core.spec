#
# spec file for package python-apeye-core
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
Name:           python-apeye-core%{psuffix}
Version:        1.1.5
Release:        0
Summary:        Core (offline) functionality for the apeye library
License:        MIT
URL:            https://github.com/domdfcoding/apeye-core
Source:         https://github.com/domdfcoding/apeye-core/archive/refs/tags/v%{version}.tar.gz#/apeye_core-%{version}.tar.gz
BuildRequires:  %{python_module hatch-requirements-txt}
BuildRequires:  %{python_module pip}
%if %{with test}
BuildRequires:  %{python_module apeye-core = %{version}}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module pytest}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-domdf-python-tools >= 2.6
Requires:       python-idna >= 2.5
BuildArch:      noarch
%python_subpackages

%description
Core (offline) functionality for the apeye library.

%prep
%autosetup -p1 -n apeye-core-%{version}

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
%license LICENSE
%doc README.rst
%{python_sitelib}/apeye_core
%{python_sitelib}/apeye_core-%{version}.dist-info
%endif

%changelog
