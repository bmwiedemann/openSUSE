#
# spec file for package python-dbus-deviation
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


Name:           python-dbus-deviation
Version:        0.6.1
Release:        0
Summary:        Parse D-Bus introspection XML and process it in various ways
License:        LGPL-2.1-or-later
URL:            https://tecnocode.co.uk/dbus-deviation/
Source:         https://files.pythonhosted.org/packages/source/d/dbus-deviation/dbus-deviation-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#pwithnall/dbus-deviation#21
Patch0:         correct-test-assertion-methods.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lxml}
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
dbus-deviation is a project for parsing D-Bus introspection XML and processing
it in various ways. Its main tool is dbus-interface-diff, which calculates the
difference between two D-Bus APIs for the purpose of checking for API breaks.
This functionality is also available as a Python module, dbusdeviation.

%prep
%autosetup -p1 -n dbus-deviation-%{version}
sed -i -e "/setuptools_/d" setup.py
chmod -x dbusapi/tests/*.py dbusdeviation/tests/*.py dbusdeviation/utilities/*.py
sed -i '1 {/^#!/d}' dbusapi/tests/*.py dbusdeviation/tests/*.py dbusdeviation/utilities/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/dbus-interface-diff
%python_clone -a %{buildroot}%{_bindir}/dbus-interface-vcs-helper
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%post
%python_install_alternative dbus-interface-diff dbus-interface-vcs-helper

%postun
%python_uninstall_alternative dbus-interface-diff

%files %{python_files}
%doc AUTHORS NEWS README.md
%license COPYING
%python_alternative %{_bindir}/dbus-interface-diff
%python_alternative %{_bindir}/dbus-interface-vcs-helper
%{python_sitelib}/dbusapi
%{python_sitelib}/dbusdeviation
%{python_sitelib}/dbus_deviation-%{version}.dist-info

%changelog
