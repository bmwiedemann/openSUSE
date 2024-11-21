#
# spec file for package python-shippinglabel
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
Name:           python-shippinglabel%{psuffix}
Version:        2.1.0
Release:        0
Summary:        Utilities for handling packages
License:        MIT
URL:            https://github.com/domdfcoding/shippinglabel
Source:         https://github.com/domdfcoding/shippinglabel/archive/refs/tags/v%{version}.tar.gz#/shippinglabel-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.6.0}
BuildRequires:  %{python_module wheel >= 0.34.2}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module apeye}
BuildRequires:  %{python_module betamax}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module consolekit}
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module shippinglabel = %{version}}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-dist-meta >= 0.1.2
Requires:       python-dom-toml >= 0.2.2
Requires:       python-domdf-python-tools >= 3.1.0
Requires:       python-packaging >= 20.9
Requires:       python-typing-extensions >= 3.7.4.3
BuildArch:      noarch
%python_subpackages

%description
Utilities for handling packages.

%prep
%autosetup -p1 -n shippinglabel-%{version}

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
%pytest -k 'not (test_get_sha256_hash or test_get_md5_hash or test_check_sha256_hash or test_get_record_entry or test_list_requirements)'
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/shippinglabel
%{python_sitelib}/shippinglabel-%{version}.dist-info
%endif

%changelog
