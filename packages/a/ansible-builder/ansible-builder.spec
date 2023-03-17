#
# spec file for package ansible-builder
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


%if 0%{?suse_version} < 1550
# Leap15, SLES15
%define pythons python310
%define ansible_python python310
%define ansible_python_executable python3.10
%define ansible_python_sitelib %python310_sitelib
%else
# Tumbleweed
%define pythons python3
%define ansible_python python3
%define ansible_python_executable python3
%define ansible_python_sitelib %python3_sitelib
%endif

Name:           ansible-builder
Version:        1.2.0
Release:        0
Summary:        An Ansible execution environment builder
License:        Apache-2.0
URL:            https://github.com/ansible/ansible-builder
Source:         https://files.pythonhosted.org/packages/source/a/ansible-builder/ansible-builder-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-rpm-macros
BuildRequires:  %{ansible_python}-base >= 3.8
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  %{ansible_python}-pbr
# SECTION test requirements
BuildRequires:  %{ansible_python}-bindep
BuildRequires:  %{ansible_python}-PyYAML
BuildRequires:  %{ansible_python}-requirements-parser
# /SECTION
BuildRequires:  fdupes
Requires:       python3-bindep
Requires:       python3-PyYAML
Requires:       python3-requirements-parser

%description
Ansible Builder is a tool that automates the process of
building execution environments using the schemas and
tooling defined in various Ansible Collections and by
the user.

See the readthedocs page for ansible-builder at:
https://ansible-builder.readthedocs.io/en/latest/

%prep
%setup -q -n ansible-builder-%{version}

%build
%python_build

%install
%python_install
%fdupes %{buildroot}%{ansible_python_sitelib}

%files
%doc README.md
%license LICENSE.md
%{_bindir}/ansible-builder
%{ansible_python_sitelib}/ansible_builder
%{ansible_python_sitelib}/ansible_builder-*-info

%changelog
