#
# spec file for package python-dist-meta
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
Name:           python-dist-meta%{psuffix}
Version:        0.8.1
Release:        0
Summary:        Parse and create Python distribution metadata
License:        MIT
URL:            https://github.com/repo-helper/dist-meta
Source:         https://github.com/repo-helper/dist-meta/archive/refs/tags/v%{version}.tar.gz#/dist-meta-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.6.0}
BuildRequires:  %{python_module wheel >= 0.34.2}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module apeye}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module dist-meta = %{version}}
BuildRequires:  %{python_module first}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module shippinglabel}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-domdf-python-tools >= 3.1.0
Requires:       python-handy-archives >= 0.1.0
Requires:       python-packaging >= 20.9
BuildArch:      noarch
%python_subpackages

%description
Parse and create Python distribution metadata.

%prep
%autosetup -p1 -n dist-meta-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# Requires network, via pypi-json (also not packaged)
%pytest --ignore tests/test_metadata_top_packages.py -k 'not test_packages_distributions'
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/dist_meta
%{python_sitelib}/dist_meta-%{version}.dist-info
%endif

%changelog
