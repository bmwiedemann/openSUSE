#
# spec file for package python-click-option-group
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
Name:           python-click-option-group
Version:        0.5.9
Release:        0
Summary:        Option groups missing in Click
License:        BSD-3-Clause
URL:            https://github.com/click-contrib/click-option-group
Source:         https://files.pythonhosted.org/packages/source/c/click-option-group/click_option_group-%{version}.tar.gz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module click >= 7.0}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  dos2unix
Requires:       python-click >= 7.0
BuildArch:      noarch
%python_subpackages

%description
Option groups missing in Click

%prep
%setup -q -n click_option_group-%{version}

%build
%pyproject_wheel
dos2unix README.md CHANGELOG.md

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/click_option_group
%{python_sitelib}/click_option_group-%{version}.dist-info/

%changelog
