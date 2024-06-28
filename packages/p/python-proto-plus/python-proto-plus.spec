#
# spec file for package python-proto-plus
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
%define modname proto-plus
%{?sle15_python_module_pythons}
Name:           python-proto-plus%{psuffix}
Version:        1.24.0
Release:        0
Summary:        Pythonic Protocol Buffers
License:        Apache-2.0
URL:            https://github.com/googleapis/proto-plus-python
Source0:        https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pytest-staticmethod.patch gh#pytest-dev/pytest#9637 mcepl@suse.com
# workaround for the problem with pytest 7.0
Patch0:         pytest-staticmethod.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module protobuf >= 3.19.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module google-api-core >= 1.31.5}
BuildRequires:  %{python_module proto-plus}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-protobuf >= 3.19.0
BuildArch:      noarch
%python_subpackages

%description
This is a wrapper around protocol buffers. Protocol buffers is
a specification format for APIs, such as those inside Google.
This library provides protocol buffer message classes and objects
that largely behave like native Python types.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# gh#googleapis/proto-plus-python#311
%pytest -k 'not (test_fields_mitigate_collision or test_dir or test_dir_message_base)'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/proto
%{python_sitelib}/proto_plus-%{version}.dist-info
%endif

%changelog
