#
# spec file for package python-soupsieve
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
%define skip_python2 1
Name:           python-soupsieve%{psuffix}
Version:        2.0.1
Release:        0
Summary:        A modern CSS selector implementation for BeautifulSoup
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/facelessuser/soupsieve
Source:         https://files.pythonhosted.org/packages/source/s/soupsieve/soupsieve-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
A modern CSS selector implementation for BeautifulSoup

%prep
%setup -q -n soupsieve-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
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
%{python_sitelib}/soupsieve*
%endif

%changelog
