#
# spec file for package python-sybil
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        10.1.0
Release:        0
Summary:        Automated testing of examples in documentation
License:        MIT
URL:            https://github.com/simplistix/sybil
Source:         https://github.com/simplistix/sybil/archive/refs/tags/%{version}.tar.gz#/sybil-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/simplistix/sybil/commit/b1c31ce0818cfa7953a61b3b391a88cd5620f9dd Follow testfixtures' compare_text/compare_dict move to comparers module
Patch:          testfixtures12.patch
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest >= 8}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module sybil = %{version}}
BuildRequires:  %{python_module testfixtures >= 12}
%if 0%{?sle_version} && 0%{?sle_version} <= 150400
BuildRequires:  %{python_module dataclasses}
%endif
%if 0%{suse_version} >= 1699
BuildRequires:  %{python_module seedir}
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

%if 0%{suse_version} < 1699
# Remove seedir dependency for SLFO
sed -i '/import seedir/d' tests/helpers.py
%endif

%build
%pyproject_wheel

%if !%{with test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}

%if 0%{suse_version} < 1699
# Remove seedir build dependency
test_flags="--ignore docs/patterns.rst"
%endif

%pytest $test_flags
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst docs/changes.rst
%license docs/license.rst
%{python_sitelib}/sybil
%{python_sitelib}/sybil-%{version}.dist-info
%endif

%changelog
