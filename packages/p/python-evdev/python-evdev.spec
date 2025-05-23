#
# spec file for package python-evdev
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


%define modname evdev
%{?sle15_python_module_pythons}
Name:           python-evdev
Version:        1.9.2
Release:        0
Summary:        Python bindings to the Linux input handling subsystem
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/gvalkov/python-evdev
# Source needs to be pulled form Github as the source distribution on PyPI lacks the test directory
Source:         https://github.com/gvalkov/python-evdev/archive/refs/tags/v%{version}.tar.gz#/python-evdev-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
python-evdev provides bindings to the generic input event interface
in Linux. The evdev interface serves the purpose of passing events
generated in the kernel directly to userspace through character
devices that are typically located in /dev/input/.

This package also comes with bindings to uinput, the userspace input
subsystem. Uinput allows userspace programs to create and handle
input devices that can inject events directly into the input
subsystem.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}
%python_expand rm %{buildroot}/%{$python_sitearch}/%{modname}/*.c

%check
%pytest_arch tests -k 'not test_uinput'

%files %{python_files}
%{python_sitearch}/evdev*
%license LICENSE

%changelog
