#
# spec file for package python-apeye
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
%{?sle15_python_module_pythons}
Name:           python-apeye%{psuffix}
Version:        1.4.1
Release:        0
Summary:        Handy tools for working with URLs and APIs
License:        LGPL-3.0-or-later
URL:            https://github.com/domdfcoding/apeye
Source:         https://github.com/domdfcoding/apeye/archive/refs/tags/v%{version}.tar.gz#/apeye-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module CacheControl}
BuildRequires:  %{python_module CherryPy}
BuildRequires:  %{python_module apeye = %{version}}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module pytest-httpserver}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-apeye-core >= 1.0.0b2
Requires:       python-domdf-python-tools >= 2.6.0
Requires:       python-platformdirs >= 2.3.0
Requires:       python-requests >= 2.24.0
Suggests:       python-cachecontrol >= 0.12.6
Suggests:       python-lockfile >= 0.12.2
BuildArch:      noarch
%python_subpackages

%description
Handy tools for working with URLs and APIs.

%prep
%autosetup -p1 -n apeye-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# Requires network
%pytest --ignore tests/test_url.py -k 'not (test_http_cache or test_cache_canary)'
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/apeye
%{python_sitelib}/apeye-%{version}.dist-info
%endif

%changelog
