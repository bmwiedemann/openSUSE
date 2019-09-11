#
# spec file for package python-pyxdg
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Group:          Development/Languages/Python
URL:            http://freedesktop.org/wiki/Software/pyxdg
Source:         https://files.pythonhosted.org/packages/source/p/pyxdg/pyxdg-%{version}.tar.gz
Patch0:         resource_leak.patch
BuildRequires:  %{python_module nose}
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  shared-mime-info
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
Provides:       python-xdg = %{version}
Obsoletes:      python-xdg < %{version}
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-xdg < %{version}
Provides:       %{oldpython}-xdg = %{version}
%endif
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
%patch0 -p1

%build
%python_build

%install
%python_install

%check
# test_get_type{,2} both fail but come from s-m-i package for data
%python_expand nosetests-%{$python_bin_suffix} -e test_get_type*

%files %{python_files}
%license COPYING
%doc README AUTHORS ChangeLog
%{python_sitelib}/xdg
%{python_sitelib}/pyxdg-%{version}-py*.egg-info

%changelog
