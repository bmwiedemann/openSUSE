#
# spec file for package python-fontPens
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


Name:           python-fontPens
Version:        0.2.4
Release:        0
Summary:        A collection of classes implementing the pen protocol for manipulating glyphs
License:        BSD-3-Clause
URL:            https://github.com/robotools/fontPens
Source:         https://files.pythonhosted.org/packages/source/f/fontPens/fontPens-%{version}.zip
Patch0:         fix-fp-issue.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 3.32.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 3.32.0}
BuildRequires:  %{python_module fontParts >= 0.8.1}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A collection of classes implementing the pen protocol for manipulating glyphs.

%prep
%autosetup -p1 -n fontPens-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/fontPens
%{python_sitelib}/fontPens-%{version}.dist-info

%changelog
