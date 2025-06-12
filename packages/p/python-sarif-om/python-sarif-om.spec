#
# spec file for package python-sarif-om
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


%{?sle15_python_module_pythons}
Name:           python-sarif-om
Version:        1.0.4
Release:        0
Summary:        Classes implementing the SARIF 2.1.0 object model
License:        MIT
URL:            https://github.com/microsoft/sarif-python-om
Source:         https://files.pythonhosted.org/packages/source/s/sarif_om/sarif_om-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Requires:       python-pbr
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module pbr}
# /SECTION
%python_subpackages

%description
Classes implementing the SARIF 2.1.0 object model.

%prep
%setup -q -n sarif_om-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream testsuite

%files %{python_files}
%{python_sitelib}/sarif[-_]om
%{python_sitelib}/sarif[-_]om-%{version}*-info

%changelog
