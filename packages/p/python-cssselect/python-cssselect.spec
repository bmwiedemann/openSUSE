#
# spec file for package python-cssselect
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-cssselect%{psuffix}
Version:        1.3.0
Release:        0
Summary:        CSS3 selectors for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/scrapy/cssselect
Source:         https://github.com/scrapy/cssselect/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
cssselect parses CSS3 Selectors and translates them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath engine to
find the matching elements in an XML or HTML document.

This module used to live inside of lxml as lxml.cssselect before it was
extracted as a stand-alone project.

%prep
%setup -q -n cssselect-%{version}

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
%{python_sitelib}/cssselect
%{python_sitelib}/cssselect-%{version}.dist-info
%license LICENSE
%doc README.rst CHANGES AUTHORS
%endif

%changelog
