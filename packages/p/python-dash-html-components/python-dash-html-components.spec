#
# spec file for package python-dash-html-components-test
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
# dash packagers do not regularly tag their releases on github due to some Julia bug
# get this from the master branch (dev is the default but does not have the full package)
%define commit 422c952ed2c86f6c3dbec04150da27688d464a57
Name:           python-dash-html-components%{psuffix}
Version:        1.1.3
Release:        0
Summary:        Vanilla HTML components for Dash
License:        MIT
URL:            https://github.com/plotly/dash-html-components
# only the github archive has the tests
Source:         https://github.com/plotly/dash-html-components/archive/%{commit}.tar.gz#/dash-html-components-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module dash}
BuildRequires:  %{python_module percy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module pandas if (%python-base without python36-base)}
%endif
%python_subpackages

%description
Vanilla HTML components for Dash

%prep
%setup -q -n dash-html-components-%{commit}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# full test suite needs working nodejs (npm with network), selenium, chromedriver...
%pytest tests/test_dash_html_components.py
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/dash_html_components
%{python_sitelib}/dash_html_components-%{version}-py*.egg-info
%endif

%changelog
