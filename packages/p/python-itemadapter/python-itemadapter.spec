#
# spec file for package python-itemadapter
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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
Name:           python-itemadapter%{psuffix}
Version:        0.11.0
Release:        0
Summary:        Wrapper for data container objects
License:        BSD-3-Clause
URL:            https://github.com/scrapy/itemadapter
Source:         https://github.com/scrapy/itemadapter/archive/v%{version}.tar.gz#/itemadapter-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.5.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Scrapy >= 2.0}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module itemadapter >= %{version}}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest >= 5.4}
%endif
BuildArch:      noarch
%python_subpackages

%description
The ItemAdapter class is a wrapper for data container objects, providing
a common interface to handle objects of different types in an uniform
manner, regardless of their underlying implementation.

%prep
%autosetup -p1 -n itemadapter-%{version}

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
%doc README.md
%{python_sitelib}/itemadapter
%{python_sitelib}/itemadapter-%{version}.dist-info
%endif

%changelog
