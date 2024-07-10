#
# spec file for package python-dep-logic
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


%{?sle15_python_module_pythons}
Name:           python-dep-logic
Version:        0.3.0
Release:        0
Summary:        Python dependency specifications supporting logical operations
License:        Apache-2.0
URL:            https://github.com/pdm-project/dep-logic
Source:         https://files.pythonhosted.org/packages/source/d/dep-logic/dep_logic-%{version}.tar.gz
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module packaging >= 22}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-packaging >= 22
BuildArch:      noarch
%python_subpackages

%description
Python dependency specifications supporting logical operations.

This library allows logic operations on version specifiers and environment markers.

%prep
%autosetup -p1 -n dep_logic-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/dep_logic
%{python_sitelib}/dep_logic-%{version}.dist-info

%changelog
