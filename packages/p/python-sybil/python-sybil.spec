#
# spec file for package python-sybil
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
Name:           python-sybil%{psuffix}
Version:        6.1.1
Release:        0
Summary:        Automated testing of examples in documentation
License:        MIT
URL:            https://github.com/simplistix/sybil
Source:         https://github.com/simplistix/sybil/archive/refs/tags/%{version}.tar.gz#/sybil-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest >= 7.1}
BuildRequires:  %{python_module seedir}
BuildRequires:  %{python_module sybil = %{version}}
BuildRequires:  %{python_module testfixtures}
%if 0%{?sle_version} && 0%{?sle_version} <= 150400
BuildRequires:  %{python_module dataclasses}
%endif
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-pytest
BuildArch:      noarch
%python_subpackages

%description
python-sybil provides a way to test examples in one's documentation by parsing
them from the documentation source and evaluating the parsed examples as part
of the normal test run. Integration is provided for the main Python test runners.

%prep
%autosetup -p1 -n sybil-%{version}
sed -i '/pytest-cov/ d'  setup.py

%build
%pyproject_wheel

%if !%{with test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst docs/changes.rst
%license docs/license.rst
%{python_sitelib}/sybil
%{python_sitelib}/sybil-%{version}.dist-info
%endif

%changelog
