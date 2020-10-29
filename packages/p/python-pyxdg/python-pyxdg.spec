#
# spec file for package python-pyxdg
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
%define oldpython python
Name:           python-pyxdg
Version:        0.26
Release:        0
Summary:        Implementations of freedesktop.org standards in python
License:        LGPL-2.1-only
URL:            https://freedesktop.org/wiki/Software/pyxdg
Source:         https://files.pythonhosted.org/packages/source/p/pyxdg/pyxdg-%{version}.tar.gz
Patch0:         resource_leak.patch
Patch1:         https://gitlab.freedesktop.org/tcallawa/pyxdg/-/commit/b8d3d7b337adeb2fc2ef8a36f3a500e147d7a41b.diff#/new-api.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  shared-mime-info
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
Conflicts:      python-xdg
BuildArch:      noarch
%python_subpackages

%description
PyXDG is a python library to access freedesktop.org standards. Currently supported are:
 * Base Directory Specification Version 0.6
 * Menu Specification Version 1.0
 * Desktop Entry Specification Version 1.0
 * Icon Theme Specification Version 0.8
 * Recent File Spec 0.2
 * Shared-MIME-Database Specification 0.13

%prep
%setup -q -n pyxdg-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://gitlab.freedesktop.org/xdg/pyxdg/issues/15
# test_get_type{,2} both fail but come from s-m-i package for data
# https://gitlab.freedesktop.org/xdg/pyxdg/merge_requests/4
# RulesTest.test_rule_from_node failure is https://gitlab.freedesktop.org/xdg/pyxdg/-/issues/20
%{python_expand sed -i "s/Exec=python.*$/Exec=$python/" test/resources.py
PYTHONPATH=%{buildroot}%{$python_sitelib} pytest-%{$python_bin_suffix} test/test-*.py -v -k 'not (test_get_type or test_rule_from_node)'
}

%files %{python_files}
%license COPYING
%doc README AUTHORS ChangeLog
%{python_sitelib}/xdg
%{python_sitelib}/pyxdg-%{version}-py*.egg-info

%changelog
