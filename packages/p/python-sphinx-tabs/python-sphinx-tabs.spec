#
# spec file for package python-sphinx-tabs
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


%if 0%{?sle_version} && 0%{?sle_version} <= 150300
%define pythons python3
%endif
%bcond_with      test
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-sphinx-tabs
Version:        3.4.1
Release:        0
Summary:        Tabbed views for Sphinx
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/executablebooks/sphinx-tabs
# Use the github tag instead of the pythonhosted.org to get the tests folder
Source:         https://github.com/executablebooks/sphinx-tabs/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments
Requires:       python-Sphinx
Requires:       python-docutils
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinx-tabs = %{version}}
%endif
%python_subpackages

%description
Create tabbed content in Sphinx documentation when building HTML.

%prep
%setup -q -n sphinx-tabs-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# python-rinohtype is not available
%pytest -k 'not test_rinohtype_pdf'
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/sphinx_tabs
%{python_sitelib}/sphinx_tabs-%{version}*-info
%endif

%changelog
