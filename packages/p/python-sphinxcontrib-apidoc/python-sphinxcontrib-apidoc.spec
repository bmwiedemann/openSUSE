#
# spec file for package python-sphinxcontrib-apidoc
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-sphinxcontrib-apidoc%{psuffix}
Version:        0.3.0
Release:        0
Summary:        A Sphinx extension for running 'sphinx-apidoc' on each build
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://www.sphinx-doc.org/
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-apidoc/sphinxcontrib-apidoc-%{version}.tar.gz
BuildRequires:  %{python_module pbr >= 4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.6.0
Requires:       python-pbr
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module sphinxcontrib-apidoc = %{version}}
%endif
# /SECTION
%python_subpackages

%description
*sphinx-apidoc* is a tool for automatic generation of Sphinx sources that,
using the `autodoc <sphinx_autodoc>`_ extension, documents a whole package in
the style of other automatic API documentation tools. *sphinx-apidoc* does not
actually build documentation - rather it simply generates it. As a result, it
must be run before *sphinx-build*.

%prep
%setup -q -n sphinxcontrib-apidoc-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest tests
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog README.rst
%{python_sitelib}/*
%endif

%changelog
