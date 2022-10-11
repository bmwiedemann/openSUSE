#
# spec file for package python-sphinxcontrib-blockdiag
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

%bcond_with      test
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-sphinxcontrib-blockdiag
Version:        3.0.0
Release:        0
Summary:        Sphinx "blockdiag" extension
License:        BSD-2-Clause
URL:            https://github.com/blockdiag/sphinxcontrib-blockdiag
# Use the github tag instead of the pythonhosted.org to get the tests folder
Source:         https://github.com/blockdiag/sphinxcontrib-blockdiag/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM 25.patch gh#blockdiag/sphinxcontrib-blockdiag#25
Patch0:         https://patch-diff.githubusercontent.com/raw/blockdiag/sphinxcontrib-blockdiag/pull/25.patch
Patch1:         remove-mock.patch
BuildRequires:  %{python_module Sphinx >= 2.0}
BuildRequires:  %{python_module blockdiag >= 1.5.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 2.0
Requires:       python-blockdiag >= 1.5.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Sphinx-latex}
BuildRequires:  %{python_module funcparserlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-blockdiag = %{version}}
%endif

%python_subpackages

%description
A sphinx extension for embedding block diagram using blockdiag.

%prep
%autosetup -p1 -n sphinxcontrib-blockdiag-%{version}

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
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/sphinxcontrib/blockdiag.py*
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib_blockdiag-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_blockdiag-%{version}-py*.egg-info
%endif

%changelog
