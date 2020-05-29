#
# spec file for package python-fontMath
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-fontMath
Version:        0.6.0
Release:        0
Summary:        A set of objects for performing math operations on font data
License:        MIT
URL:            https://github.com/robotools/fontMath
Source:         https://files.pythonhosted.org/packages/source/f/fontMath/fontMath-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 3.32.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 3.32.0}
BuildRequires:  %{python_module pytest >= 3.0.3}
# /SECTION
%python_subpackages

%description
A set of objects for performing math operations on font data.

%prep
%setup -q -n fontMath-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license License.txt
%{python_sitelib}/*

%changelog
