#
# spec file for package python-dom-toml
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
Name:           python-dom-toml%{psuffix}
Version:        2.0.1
Release:        0
Summary:        Dom's tools for Tom's Obvious, Minimal Language
License:        MIT
URL:            https://github.com/domdfcoding/dom_toml
Source:         https://github.com/domdfcoding/dom_toml/archive/refs/tags/v%{version}.tar.gz#/dom_toml-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module dom-toml = %{version}}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-domdf-python-tools >= 2.8.0
Requires:       python-tomli >= 1.2.3
BuildArch:      noarch
%python_subpackages

%description
Dom's tools for Tom's Obvious, Minimal Language.

%prep
%autosetup -p1 -n dom_toml-%{version}
find . -name *.py -exec sed -i '/#\!\/usr\/bin\/env\ python3/d' {} \;

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
%license LICENSE
%doc README.rst
%{python_sitelib}/dom_toml
%{python_sitelib}/dom_toml-%{version}.dist-info
%endif

%changelog
