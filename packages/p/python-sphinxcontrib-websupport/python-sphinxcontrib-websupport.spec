#
# spec file for package python-sphinxcontrib-websupport
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
Name:           python-sphinxcontrib-websupport%{psuffix}
Version:        2.0.0
Release:        0
Summary:        Sphinx API for Web Apps
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-websupport
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-websupport/sphinxcontrib_websupport-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#sphinx-doc/sphinxcontrib-websupport#78
Patch0:         fix-testsuite.patch
# PATCH-FIX-UPSTREAM gh#sphinx-doc/sphinxcontrib-websupport#91
Patch1:         support-sphinx-9.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module flit-core >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-Sphinx >= 5.0
Requires:       python-sphinxcontrib-serializinghtml
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module Whoosh}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-websupport >= %{version}}
%endif
%python_subpackages

%description
sphinxcontrib-webuspport provides a Python API to integrate Sphinx
documentation into your Web application.

%prep
%autosetup -p1 -n sphinxcontrib_websupport-%{version}

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
%license LICENCE.rst
%doc CHANGES.rst README.rst
%dir %{python_sitelib}/sphinxcontrib/
%{python_sitelib}/sphinxcontrib/websupport
%{python_sitelib}/sphinxcontrib_websupport-%{version}.dist-info
%endif

%changelog
