#
# spec file for package python-sphinxcontrib-towncrier
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
Name:           python-sphinxcontrib-towncrier%{psuffix}
Version:        0.5.0a0
Release:        0
Summary:        An RST directive for injecting a Towncrier-generated changelog draft
License:        BSD-3-Clause
URL:            https://github.com/sphinx-contrib/sphinxcontrib-towncrier
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-towncrier/sphinxcontrib_towncrier-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#sphinx-contrib/sphinxcontrib-towncrier#ab800bcd251a4c7ca558999faa740eb9586b91f5
Patch0:         support-towncrier-25.8.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-towncrier = %{version}}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx
Requires:       python-towncrier >= 23
BuildArch:      noarch
%python_subpackages

%description
An RST directive for injecting a Towncrier-generated changelog draft containing fragments for the unreleased (next) project version

%prep
%autosetup -p1 -n sphinxcontrib_towncrier-%{version}
rm -v pytest.ini

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinxcontrib/towncrier
%{python_sitelib}/sphinxcontrib_towncrier-%{version}.dist-info
%endif

%changelog
