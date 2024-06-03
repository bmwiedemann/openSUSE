#
# spec file for package ansible-variables
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


%{?sle15_python_module_pythons}
%if 0%{?suse_version} < 1550
# Leap15, SLES15
%if %pythons == "python310"
%define ansible_python python310
%define ansible_python_executable python3.10
%define ansible_python_sitelib %python310_sitelib
%endif
%if %pythons == "python311"
%define ansible_python python311
%define ansible_python_executable python3.11
%define ansible_python_sitelib %python311_sitelib
%endif
%else
# Tumbleweed
%define pythons python3
%define ansible_python python3
%define ansible_python_executable python3
%define ansible_python_sitelib %python3_sitelib
%endif

Name:           ansible-variables
Version:        0.7.0
Release:        0
Summary:        Tool to show origin of Ansible host context variables
License:        GPL-3.0-or-later
URL:            https://github.com/hille721/ansible-variables
# the PyPI tarball does not contain all files required for the tests
Source:         https://github.com/hille721/ansible-variables/archive/v%{version}/ansible-variables-%{version}.tar.gz#/ansible-variables-%{version}.tar.gz
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  %{ansible_python}-wheel
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  ansible-core >= 2.11.0
BuildRequires:  %{ansible_python}-pytest
BuildRequires:  %{ansible_python}-rich
# /SECTION
BuildRequires:  fdupes
Requires:       %{ansible_python}-rich
Requires:       ansible-core >= 2.11.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%description
The Ansible inventory is a framework for declaring variables in a
hierarchical manner. There a lot of different places where a variable
can be defined. ansible-variables displays where host context
variables originate from.

%prep
%autosetup -p1 -n ansible-variables-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ansible-variables
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH="%{buildroot}%{_bindir}:$PATH"
%pytest

%post
%python_install_alternative ansible-variables

%postun
%python_uninstall_alternative ansible-variables

%files
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/ansible-variables
%{ansible_python_sitelib}/ansible_variables
%{ansible_python_sitelib}/ansible_variables-%{version}.dist-info

%changelog
