#
# spec file for package python-pyxdg
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
%define oldpython python
%{?sle15_python_module_pythons}
Name:           python-pyxdg
Version:        0.28
Release:        0
Summary:        Implementations of freedesktop.org standards in python
License:        LGPL-2.1-only
URL:            https://freedesktop.org/wiki/Software/pyxdg
Source0:        https://files.pythonhosted.org/packages/source/p/pyxdg/pyxdg-%{version}.tar.gz
# Test data: examples
Source1:        https://gitlab.freedesktop.org/xdg/pyxdg/-/archive/rel-%{version}/pyxdg-rel-%{version}.tar.gz?path=test/example#/pyxdg-%{version}-test-example.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  shared-mime-info
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
Conflicts:      python-xdg
Obsoletes:      python-xdg
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
%setup -q -n pyxdg-%{version} -b 1
%autopatch -p1
cp -r ../pyxdg-rel-%{version}-test-example/test/example test/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test/test*.py -v

%files %{python_files}
%license COPYING
%doc README AUTHORS ChangeLog
%{python_sitelib}/xdg
%{python_sitelib}/pyxdg-%{version}-py*.egg-info

%changelog
