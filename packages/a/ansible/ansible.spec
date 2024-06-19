#
# spec file for package ansible
#
# Copyright (c) 2022 SUSE LLC
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

Name:           ansible
Version:        9.7.0
Release:        0
Summary:        Radically simple IT automation
License:        GPL-3.0+
URL:            https://ansible.com/
Source:         https://files.pythonhosted.org/packages/source/a/ansible/ansible-%{version}.tar.gz
Source99:       ansible-rpmlintrc
BuildRequires:  python-rpm-macros
BuildRequires:  %{ansible_python}-base >= 3.10
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  fdupes

# required to fix the azure collection line endings
BuildRequires:  dos2unix

# SECTION test requirements
BuildRequires:  ansible-core >= 2.16.8
# /SECTION

Requires:       %{ansible_python}-base >= 3.10
Requires:       ansible-core >= 2.16.8

# Do not check any files in collections for requires
%global __requires_exclude_from ^%{ansible_python_sitelib}/.*$

BuildArch:      noarch

%description
Ansible is a radically simple model-driven configuration management, multi-node
deployment, and remote task execution system. Ansible works over SSH and does
not require any software or daemons to be installed on remote nodes. Extension
modules can be written in any language and are transferred to managed machines
automatically.

%prep
%setup -q -n ansible-%{version}

for file in .git_keep .travis.yml ; do
  find . -name "$file" -delete
done

# remove .keep and .gitignore files
find ./ansible_collections/ -iname .gitignore -delete
find ./ansible_collections/ -iname .keep -delete

# azure collection has wrong file endings
find ./ansible_collections/azure -type f -exec dos2unix {} \;

%build
%python_build

%install
%python_install
%fdupes %{buildroot}/%{ansible_python_sitelib}/ansible_collections/

%files
%doc CHANGELOG-v9.rst README.rst
%license COPYING
%{_bindir}/ansible-community
%{ansible_python_sitelib}/

%changelog
