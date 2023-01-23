#
# spec file for package python-merge3
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-merge3
Version:        0.0.12
Release:        0
Summary:        Python implementation of 3-way merge
License:        GPL-2.0-or-later
URL:            https://www.breezy-vcs.org/
Source:         https://files.pythonhosted.org/packages/source/m/merge3/merge3-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python implementation of 3-way merge

%prep
%autosetup -p1 -n merge3-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v merge3.test_merge3

%files %{python_files}
%doc AUTHORS README.rst
%license COPYING
%{python_sitelib}/merge3
%{python_sitelib}/merge3-%{version}*-info

%changelog
