#
# spec file for package python-qmk_gui
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%bcond_without libalternatives
%define tag_version 0.1.12
Name:           python-qmk_gui
Version:        0.1.13
Release:        0
Summary:        Python GUI for qmk_hid
License:        BSD-3-Clause
URL:            https://github.com/FrameworkComputer/qmk_hid
Source0:        qmk_hid-%{version}.tar.gz
Source1:        qmk_hid-rpmlintrc
# PATCH-FIX-UPSTREAM fix-version.patch
Patch0:         fix-version.patch
# PATCH-FIX-UPSTREAM fix-open-browser.patch https://github.com/FrameworkComputer/qmk_hid/pull/49
Patch1:         fix-open-browser.patch
BuildRequires:  %{python_module hatch-requirements-txt}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hatch}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-hidapi
Requires:       python-tk
Requires:       qmk_hid
ExclusiveArch:  x86_64
%python_subpackages

%description
A GUI tool to control QMK keyboard, specifically of the Framework Laptop 16

%prep
%autosetup -p1 -n qmk_hid-%{version}/python

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/qmk_gui
%python_expand %fdupes %{buildroot}%{$python_sitelib}/qmk_hid

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative qmk_gui

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/qmk_gui
%{python_sitelib}/qmk_hid
%{python_sitelib}/qmk_hid-%{tag_version}.dist-info

%changelog
