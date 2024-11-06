#
# spec file for package python-soupsieve
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
Name:           python-soupsieve%{psuffix}
Version:        2.6
Release:        0
Summary:        A modern CSS selector implementation for BeautifulSoup
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/facelessuser/soupsieve
Source:         https://files.pythonhosted.org/packages/source/s/soupsieve/soupsieve-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4.
It aims to provide selecting, matching, and filtering using modern CSS selectors.

%prep
%setup -q -n soupsieve-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest tests
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitelib}/soupsieve
%{python_sitelib}/soupsieve-%{version}.dist-info
%endif

%changelog
