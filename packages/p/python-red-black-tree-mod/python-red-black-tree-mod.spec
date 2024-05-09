#
# spec file for package python-red-black-tree-mod
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 LISA GmbH, Bingen, Germany.
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


Name:           python-red-black-tree-mod
Version:        1.22
Release:        0
Summary:        Flexible python implementation of red black trees
License:        MIT
URL:            https://stromberg.dnsalias.org/~strombrg/red-black-tree-mod/
Source:         https://files.pythonhosted.org/packages/source/r/red-black-tree-mod/red-black-tree-mod-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Flexible python implementation of red black trees

%prep
%autosetup -p1 -n red-black-tree-mod-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README
%license COPYING
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/red_black_*_mod.py
%{python_sitelib}/red_black_tree_mod-%{version}.dist-info

%changelog
