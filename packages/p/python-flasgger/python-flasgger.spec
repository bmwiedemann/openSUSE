#
# spec file for package python-flasgger
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
Name:           python-flasgger%{psuffix}
Version:        0.9.7.1
Release:        0
Summary:        Tool to extract swagger specs from Flask projects
License:        MIT
URL:            https://github.com/flasgger/flasgger/
Source:         https://files.pythonhosted.org/packages/source/f/flasgger/flasgger-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#flasgger/flasgger#629
Patch0:         remove-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.10
Requires:       python-PyYAML >= 3.0
Requires:       python-jsonschema >= 3.0.1
Requires:       python-mistune >= 3
Requires:       python-packaging
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module flasgger = %{version}}
BuildRequires:  %{python_module marshmallow}
BuildRequires:  %{python_module pytest >= 3.0.7}
# /SECTION
%endif

%python_subpackages

%description
Flasgger is a Flask extension to extract OpenAPI=Specification from all Flask views registered in an API.

%prep
%autosetup -p1 -n flasgger-%{version}

# Examples directory is not included in PyPI release
rm tests/test_examples.py

find . -name .DS_Store -print -delete

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand chmod -x %{buildroot}%{$python_sitelib}/flasgger/ui2/static/lang/*.js
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%if %{with test}
%check
%pytest tests/
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/flasgger
%{python_sitelib}/flasgger-%{version}.dist-info
%endif

%changelog
