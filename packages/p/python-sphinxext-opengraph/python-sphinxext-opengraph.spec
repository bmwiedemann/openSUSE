#
# spec file for package python-sphinxext-opengraph
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-sphinxext-opengraph
Version:        0.13.0
Release:        0
Summary:        Sphinx Extension to enable OGP support
License:        MIT
URL:            https://github.com/wpilibsuite/sphinxext-opengraph
Source:         https://files.pythonhosted.org/packages/source/s/sphinxext-opengraph/sphinxext_opengraph-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3-Sphinx >= 5.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Sphinx >= 5.0}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxext-opengraph}
%endif
%python_subpackages

%description
Sphinx Extension to enable OGP support

%prep
%setup -q -n sphinxext_opengraph-%{version}

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
%license LICENCE.rst
%dir %{python_sitelib}/sphinxext
%{python_sitelib}/sphinxext/opengraph
%{python_sitelib}/sphinxext_opengraph-%{version}.dist-info
%endif

%changelog
