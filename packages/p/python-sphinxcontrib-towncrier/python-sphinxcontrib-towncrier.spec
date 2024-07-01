#
# spec file for package python-sphinxcontrib-towncrier
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
Name:           python-sphinxcontrib-towncrier%{psuffix}
Version:        0.4.0a0
Release:        0
Summary:        An RST directive for injecting a Towncrier-generated changelog draft
License:        BSD-3-Clause
URL:            https://github.com/sphinx-contrib/sphinxcontrib-towncrier
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-towncrier/sphinxcontrib-towncrier-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-towncrier = %{version}}
BuildRequires:  %{python_module towncrier >= 19.2}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx
Requires:       python-towncrier >= 19.2
BuildArch:      noarch
%python_subpackages

%description
An RST directive for injecting a Towncrier-generated changelog draft containing fragments for the unreleased (next) project version

%prep
%setup -q -n sphinxcontrib-towncrier-%{version}
rm -v pytest.ini

%build
%python_build

%install
%if !%{with test}
%python_install
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
%dir %{python_sitelib}/sphinxcontrib/towncrier
%{python_sitelib}/sphinxcontrib/towncrier/*
%{python_sitelib}/sphinxcontrib_towncrier-*-info
%endif

%changelog
