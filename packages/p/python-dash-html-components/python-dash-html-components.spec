#
# spec file for package python-dash-html-components
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
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-dash-html-components%{psuffix}
Version:        1.0.2
Release:        0
Summary:        Vanilla HTML components for Dash
License:        MIT
URL:            https://github.com/plotly/dash-html-components
Source:         https://github.com/plotly/dash-html-components/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dash
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module dash}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module percy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
%endif
%python_subpackages

%description
Vanilla HTML components for Dash

%prep
%setup -q -n dash-html-components-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest tests/test_dash_html_components.py
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*
%endif

%changelog
