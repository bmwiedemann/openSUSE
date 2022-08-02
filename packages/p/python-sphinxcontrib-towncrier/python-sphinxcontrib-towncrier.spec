#
# spec file for package python-sphinxcontrib-towncrier
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sphinxcontrib-towncrier%{psuffix}
Version:        0.2.1a0
Release:        0
Summary:        An RST directive for injecting a Towncrier-generated changelog draft
License:        BSD-3-Clause
URL:            https://github.com/sphinx-contrib/sphinxcontrib-towncrier
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-towncrier/sphinxcontrib-towncrier-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module towncrier >= 19.2}
BuildRequires:  %{python_module sphinxcontrib-towncrier}
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
