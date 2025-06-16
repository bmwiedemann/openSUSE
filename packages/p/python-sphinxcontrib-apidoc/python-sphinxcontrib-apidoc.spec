#
# spec file for package python-sphinxcontrib-apidoc
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
Name:           python-sphinxcontrib-apidoc%{psuffix}
Version:        0.5.0
Release:        0
Summary:        A Sphinx extension for running 'sphinx-apidoc' on each build
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://www.sphinx-doc.org/
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-apidoc/sphinxcontrib-apidoc-%{version}.tar.gz
# PATCH-FIX-UPSTREAM sphinx-82.patch gh#sphinx-contrib/apidoc#23
Patch0:         sphinx-82.patch
BuildRequires:  %{python_module pbr >= 4.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 5.0.0
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
%autosetup -p1 -n sphinxcontrib-apidoc-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
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
%dir %{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinxcontrib/apidoc
%{python_sitelib}/sphinxcontrib_apidoc-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_apidoc-%{version}.dist-info
%endif

%changelog
