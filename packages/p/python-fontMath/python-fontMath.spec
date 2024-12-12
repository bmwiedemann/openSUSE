#
# spec file for package python-fontMath
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
Name:           python-fontMath
Version:        0.9.4
Release:        0
Summary:        A set of objects for performing math operations on font data
License:        MIT
URL:            https://github.com/robotools/fontMath
Source:         https://files.pythonhosted.org/packages/source/f/fontmath/fontmath-%{version}.zip
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 4.28.5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 4.28.5}
BuildRequires:  %{python_module pytest >= 3.0.3}
# /SECTION
%python_subpackages

%description
A set of objects for performing math operations on font data.

%prep
%setup -q -n fontmath-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license License.txt
%{python_sitelib}/fontMath
%{python_sitelib}/fontMath-%{version}*-info

%changelog
