#
# spec file for package python-dbus-deviation
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
Name:           python-dbus-deviation
Version:        0.6.0
Release:        0
Summary:        Parse D-Bus introspection XML and process it in various ways
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            http://people.collabora.com/~pwith/dbus-deviation/
Source:         https://files.pythonhosted.org/packages/source/d/dbus-deviation/dbus-deviation-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lxml}
# /SECTION
%python_subpackages

%description
dbus-deviation is a project for parsing D-Bus introspection XML and processing
it in various ways. Its main tool is dbus-interface-diff, which calculates the
difference between two D-Bus APIs for the purpose of checking for API breaks.
This functionality is also available as a Python module, dbusdeviation.

%prep
%setup -q -n dbus-deviation-%{version}
sed -i -e "/setuptools_/d" setup.py
chmod -x dbusapi/tests/*.py dbusdeviation/utilities/*.py
sed -i '1 {/^#!/d}' dbusapi/tests/*.py dbusdeviation/utilities/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS NEWS README
%license COPYING
%python3_only %{_bindir}/dbus-interface-diff
%python3_only %{_bindir}/dbus-interface-vcs-helper
%{python_sitelib}/*

%changelog
