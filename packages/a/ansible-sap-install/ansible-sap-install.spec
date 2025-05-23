#
# spec file for package ansible-sap-install
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

%define ansible_collection_name sap_install
%define ansible_collection_path %{_datadir}/ansible/collections/ansible_collections/suse/%{ansible_collection_name}


Name:           ansible-sap-install
Summary:        Ansible collection suse.sap_install for SAP Automation
License:        Apache-2.0
Version:        1.5.3
Release:        0
URL:            https://github.com/SUSE/community.sap_install/
Source0:        %{url}archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        ansible-sap-install.yaml
Source2:        collection_update.py

BuildArch:      noarch


Requires: ansible-core >= 2.16
Requires: ansible >= 9
BuildRequires: ansible-core >= 2.16
BuildRequires: ansible >= 9

Requires: ansible-linux-system-roles

# Python module ruamel.yaml for collection-update.py
BuildRequires: python3-ruamel.yaml


%description
This package provides a Ansible collection suse.sap_install.

It automates the installation of various SAP software components,
 including SAP HANA, SAP NetWeaver, and SAP S/4HANA.

This collection can be used to simplify and accelerate the deployment,
management, and operation of SAP systems on Linux platforms.


%prep
# Extract tarball
cd %{_builddir}
tar -xzf %{_sourcedir}/%{name}-%{version}.tar.gz --strip-components=1

# Execute python script to update documentation and remove unsupported roles
python3 %{_sourcedir}/collection_update.py --config %{_sourcedir}/%{name}.yaml  --build_dir %{_builddir}


%build
# Build the Ansible collection
ansible-galaxy collection build --output-path %{_builddir}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/ansible/collections
mkdir -p %{buildroot}%{_datadir}/ansible/roles/

# ansible-galaxy always appends ansible_collections folder into collections path
ansible-galaxy collection install --force %{_builddir}/suse-%{ansible_collection_name}-%{version}.tar.gz \
  --collections-path %{buildroot}%{_datadir}/ansible/collections


%post
# Loop through roles in collection and create symlinks under %{_datadir}/ansible/roles/
# Installed community collection will take precedence over role symlinks.
for role in %{ansible_collection_path}/roles/*; do
  role_name=$(basename "$role")
  if [ ! -e %{_datadir}/ansible/roles/community.%{ansible_collection_name}.${role_name} ]; then
    ln -sf %{ansible_collection_path}/roles/${role_name} \
      %{_datadir}/ansible/roles/community.%{ansible_collection_name}.${role_name}
  fi
done


%postun
# Loop through roles in %{_datadir}/ansible/roles/ and remove those that link to collection
if [ "$1" -eq 0 ]; then
  for role in %{_datadir}/ansible/roles/community.%{ansible_collection_name}.*; do
    if [ -L "$role" ]; then
      target=$(readlink "$role")
      if ( [ -e "$target" ] && [ "$target" = "%{ansible_collection_path}/roles/$(basename "$role")" ] ) || [ ! -e "$target" ]; then
        rm -f "$role"
      fi
    fi
  done
fi


%files
%{_datadir}/ansible/collections/
%{_datadir}/ansible/roles/

%changelog
