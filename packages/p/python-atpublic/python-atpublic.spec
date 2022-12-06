#
# spec file for package python-atpublic
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-atpublic
Version:        3.1.1
Release:        0
Summary:        @public decorator for populating __all__
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://public.readthedocs.io/
Source:         https://gitlab.com/warsaw/public/-/archive/%{version}/public-%{version}.tar.gz#/atpublic-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pdm-pep517 >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sybil}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
%endif
%python_subpackages

%description
public -- @public for populating __all__.

%prep
%setup -q -n atpublic-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%else

%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc docs/NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/public
%{python_sitelib}/atpublic-%{version}*-info
%endif

%changelog
