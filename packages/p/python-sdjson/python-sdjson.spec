#
# spec file for package python-sdjson
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
Name:           python-sdjson%{psuffix}
Version:        0.5.0
Release:        0
Summary:        Custom JSON Encoder utilising functools.singledispatch
License:        MIT
URL:            https://github.com/domdfcoding/singledispatch-json
Source:         https://github.com/domdfcoding/singledispatch-json/archive/refs/tags/v%{version}.tar.gz#/sdjson-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module whey}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module sdjson = %{version}}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-domdf-python-tools >= 2.5.2
Requires:       python-typing-extensions >= 3.7.4.3
BuildArch:      noarch
%python_subpackages

%description
Custom JSON Encoder for Python utilising functools.singledispatch to support
custom encoders for both Python's built-in classes and user-created classes,
without as much legwork.

%prep
%autosetup -p1 -n singledispatch-json-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# skip because of gh#domdfcoding/singledispatch-json#55
%pytest -k 'not test_unexpected_data'
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/sdjson
%{python_sitelib}/sdjson-%{version}.dist-info
%endif

%changelog
