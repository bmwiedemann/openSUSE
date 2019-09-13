#
# spec file for package python-pyquery
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pyquery%{psuffix}
Version:        1.4.0
Release:        0
Summary:        A jQuery-like library for python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://pypi.python.org/pypi/pyquery
Source:         https://files.pythonhosted.org/packages/source/p/pyquery/pyquery-%{version}.tar.gz
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module cssselect > 0.7.9}
BuildRequires:  %{python_module lxml >= 2.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cssselect > 0.7.9
Requires:       python-lxml >= 2.1
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module WebOb > 1.1.9}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module requests}
%endif
%python_subpackages

%description
Pyquery allows you to make jQuery queries on XML documents. The API is
as much as possible the similar to jQuery. Pyquery uses lxml for fast
XML and HTML manipulation.

%prep
%setup -q -n pyquery-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# Disable tests which perform live fetch
%python_exec -m nose tests -e test_get
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python_sitelib}/*
%endif

%changelog
