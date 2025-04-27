#
# spec file for package python-qmk_gui
#
# Copyright (c) 2025 SUSE LLC
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
%define tag_version 0.1.12
Name:           python-qmk_gui
Version:        0.1.12+git44
Release:        0
Summary:        Python GUI for qmk_hid
License:        BSD-3-Clause
URL:            https://github.com/FrameworkComputer/qmk_hid
Source0:        qmk_hid-%{version}.tar.gz
Source1:        qmk_hid-rpmlintrc
# PATCH-FIX-UPSTREAM fix-version.patch
Patch0:         fix-version.patch
BuildRequires:  %{python_module hatch-requirements-txt}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hatch}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%python_expand %fdupes %{buildroot}/%{python_sitelib}/qmk_hid
# for some reason python_expand doesn't work here, so do manual fdupes
%fdupes %{buildroot}/%{python311_sitelib}/qmk_hid/__pycache__
%fdupes %{buildroot}/%{python312_sitelib}/qmk_hid/__pycache__
%fdupes %{buildroot}/%{python313_sitelib}/qmk_hid/__pycache__

%post
%python_install_alternative qmk_gui

%postun
%python_uninstall_alternative qmk_gui

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/qmk_gui
%{python_sitelib}/qmk_hid
%{python_sitelib}/qmk_hid-%{tag_version}.dist-info

%changelog
