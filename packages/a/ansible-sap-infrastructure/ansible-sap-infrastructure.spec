#
# spec file for package ansible-sap-infrastructure
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


%define ansible_collection_name sap_infrastructure
%define ansible_collection_path %{_datadir}/ansible/collections/ansible_collections/suse/%{ansible_collection_name}

Name:           ansible-sap-infrastructure
Summary:        Ansible collection suse.sap_infrastructure for SAP Automation
License:        Apache-2.0
Version:        1.3.1
Release:        0
URL:            https://github.com/SUSE/community.sap_infrastructure/
Source0:        %{url}archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.yaml
Source2:        transformation.py
Source99:       %{name}.rpmlintrc

BuildArch:      noarch


Requires:       ansible >= 9
Requires:       ansible-core >= 2.16
BuildRequires:  ansible >= 9
BuildRequires:  ansible-core >= 2.16

# Python module ruamel.yaml for collection-update.py
BuildRequires:  python3-ruamel.yaml

%description
This package provides a Ansible collection suse.sap_infrastructure.

It automates the provisioning of SAP infrastructure across various platforms:
- AWS EC2 Virtual Server instances
- Google Cloud Compute Engine Virtual Machines
- IBM Cloud, Intel Virtual Servers
- IBM Cloud, Power Virtual Servers
- Microsoft Azure Virtual Machines
- IBM PowerVM Virtual Machines

Ensure that you install all required packages, python modules and collections.
https://github.com/SUSE/community.sap_infrastructure/tree/main/roles/sap_vm_provision#requirements

Package and collection dependencies are not installed along with this package!

%prep
%autosetup -p1 -n community.%{ansible_collection_name}-%{version}

%build
# Execute python script to update documentation and remove unsupported roles
python3 %{_sourcedir}/transformation.py --config %{_sourcedir}/%{name}.yaml  --build_dir .
# Build the Ansible collection
ansible-galaxy collection build --output-path %{_builddir}

%install
mkdir -p %{buildroot}%{_datadir}/ansible/collections
mkdir -p %{buildroot}%{_datadir}/ansible/roles/

# ansible-galaxy always appends ansible_collections folder into collections path
ansible-galaxy collection install --force %{_builddir}/suse-%{ansible_collection_name}-%{version}.tar.gz \
  --collections-path %{buildroot}%{_datadir}/ansible/collections

%post
# Loop through roles in collection and create symlinks under /usr/share/ansible/roles/
# Installed community collection will take precedence over role symlinks.
for role in %{ansible_collection_path}/roles/*; do
  role_name=$(basename "$role")
  if [ ! -e %{_datadir}/ansible/roles/community.%{ansible_collection_name}.${role_name} ]; then
    ln -sf %{ansible_collection_path}/roles/${role_name} \
      %{_datadir}/ansible/roles/community.%{ansible_collection_name}.${role_name}
  fi
done

%postun
# Loop through roles in /usr/share/ansible/roles/ and remove those that link to collection
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
