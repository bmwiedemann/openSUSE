#
# spec file for package python-sphinxcontrib-devhelp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sphinxcontrib-devhelp%{psuffix}
Version:        1.0.1
Release:        0
Summary:        Sphinx extension which outputs Devhelp documents
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sphinx-doc/sphinxcontrib-devhelp
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-devhelp/sphinxcontrib-devhelp-%{version}.tar.gz
%if %{with test}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-devhelp >= %{version}}
%endif
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.

%prep
%setup -q -n sphinxcontrib-devhelp-%{version}

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
%doc README.rst CHANGES
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
