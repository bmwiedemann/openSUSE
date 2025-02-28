# spec file for package ansible-linux_system_roles
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/\

# Define individual versions for each role
%global firewall_version 1.8.2
%global timesync_version 1.9.2
%global journald_version 1.3.5
%global ssh_version 1.5.2
%global crypto_policies_version 1.4.2
%global systemd_version 1.3.1
%global ha_cluster_version 1.22.1
%global certificate_version 1.3.8
%global mssql_version 2.5.2
%global suseconnect_version 1.0.0
%global auto_maintenance_version 1.94.2

%define ansible_collection_name linux_system_roles
%define ansible_collection_path %{_datadir}/ansible/collections/ansible_collections/suse/%{ansible_collection_name}

Name:           ansible-linux-system-roles
Version:        1.0.0
Release:        0
Summary:        Collection of Ansible roles for Linux system management
License:        GPL-3.0-or-later
URL:            https://github.com/SUSE
Source0:        %{url}/ansible-firewall/archive/refs/tags/%{firewall_version}-suse.tar.gz#/firewall-%{firewall_version}.tar.gz
Source1:        %{url}/ansible-timesync/archive/refs/tags/%{timesync_version}-suse.tar.gz#/timesync-%{timesync_version}.tar.gz
Source2:        %{url}/ansible-journald/archive/refs/tags/%{journald_version}-suse.tar.gz#/journald-%{journald_version}.tar.gz
Source3:        %{url}/ansible-ssh/archive/refs/tags/%{ssh_version}-suse.tar.gz#/ssh-%{ssh_version}.tar.gz
Source4:        %{url}/ansible-crypto_policies/archive/refs/tags/%{crypto_policies_version}-suse.tar.gz#/crypto_policies-%{crypto_policies_version}.tar.gz
Source5:        %{url}/ansible-systemd/archive/refs/tags/%{systemd_version}-suse.tar.gz#/systemd-%{systemd_version}.tar.gz
Source6:        %{url}/ansible-ha_cluster/archive/refs/tags/%{ha_cluster_version}-suse.tar.gz#/ha_cluster-%{ha_cluster_version}.tar.gz
Source7:        %{url}/ansible-certificate/archive/refs/tags/%{certificate_version}-suse.tar.gz#/certificate-%{certificate_version}.tar.gz
Source8:        %{url}/ansible-mssql/archive/refs/tags/%{mssql_version}-suse.tar.gz#/mssql-%{mssql_version}.tar.gz
Source9:        %{url}/ansible-suseconnect/archive/refs/tags/%{suseconnect_version}-suse.tar.gz#/suseconnect-%{suseconnect_version}.tar.gz
Source10:       %{url}/ansible-auto_maintenance/archive/refs/tags/%{auto_maintenance_version}-suse.tar.gz#/auto_maintenance-%{auto_maintenance_version}.tar.gz 
Source999:      galaxy.yml

BuildArch:      noarch

# Python macros are required for python detection
BuildRequires:  python-rpm-macros
BuildRequires:  python311-ruamel.yaml

# Minimum python version
%{?sle15_python_module_pythons}
BuildRequires: %{python_module base >= 3.11}
Requires:      %{python_module base >= 3.11}

# Select correct supported Ansible
%if 0%{?suse_version} >= 1600
Requires:      ansible-core
Requires:      ansible
BuildRequires: ansible-core
BuildRequires: ansible
%else
# Only Ansible 9 is supported on SLES 15
Requires:      ansible-core-2.16
Requires:      ansible-9
BuildRequires: ansible-core-2.16
BuildRequires: ansible-9
%endif

# Do not check any files in collections for requires
%global __requires_exclude_from ^%{python311_sitelib}/.*$

%description
Linux System Roles is a collection of Ansible roles and modules that provide a
stable and consistent configuration interface to manage Linux systems. These
roles are designed to be used with Ansible to configure and maintain various
aspects of a Linux system.

%prep

# Define roles with their versions
roles=(
  "firewall:%{firewall_version}"
  "timesync:%{timesync_version}"
  "journald:%{journald_version}"
  "ssh:%{ssh_version}"
  "crypto_policies:%{crypto_policies_version}"
  "systemd:%{systemd_version}"
  "ha_cluster:%{ha_cluster_version}"
  "certificate:%{certificate_version}"
  "mssql:%{mssql_version}"
  "suseconnect:%{suseconnect_version}"
  "auto_maintenance:%{auto_maintenance_version}"
)

# Create a directory to store extracted roles
mkdir -p %{_builddir}/roles
mkdir -p %{_builddir}/collections

# Extract all role tarballs
for role_entry in "${roles[@]}"; do
  role_name=${role_entry%%:*}
  role_version=${role_entry##*:}

  # Extract all roles uniformly
  tar -xzf %{_sourcedir}/${role_name}-${role_version}.tar.gz -C %{_builddir}/roles \
      --transform="s/^ansible-${role_name}-${role_version}-suse/${role_name}/"
done

# Process README documents to clean up internal links and remove unnecessary sections
for role_entry in "${roles[@]}"; do
  role_name=${role_entry%%:*}
  readme_path=%{_builddir}/roles/${role_name}/README.md
  readme_html_path=%{_builddir}/roles/${role_name}/README.html

  if [ -f "$readme_path" ]; then
    echo "Processing $readme_path..."
    # Remove internal links from README.md
    sed -r -i -e 's/\[([^[]+)\]\(#[^)]+\)/\1/g' "$readme_path"
    # Remove GitHub action badges
    sed -e "1,14 {\\,actions/workflows/,d; /\!\[/d}" -i "$readme_path"
    sed -i -e '/^###\? Requirements/,/^###\? /{ /^###\? /!d }' -e '/^###\? Requirements/d' "$readme_path"
    sed -i -e '/^###\? Collection requirements/,/^###\? /{ /^###\? /!d }' -e '/^###\? Collection requirements/d' "$readme_path"
    sed -i -e '/^###\? Compatibility/,/^###\? /{ /^###\? /!d }' -e '/^###\? Compatibility/d' "$readme_path"
  fi

  if [ -f "$readme_html_path" ]; then
    echo "Processing $readme_html_path..."
    # Remove internal links from README.html
    sed -r -i -e 's/\[([^[]+)\]\(#[^)]+\)/\1/g' "$readme_html_path"
    sed -e '/id="requirements">Requirements<\/h/,/^<h/{ /^<h/!d }' -e '/id="requirements">Requirements<\/h/d' \
        -i "$readme_html_path"
    sed -e '/id="optional-requirements">/,/^<h/{ /^<h/!d }' -e '/id="optional-requirements">/d' \
        -i "$readme_html_path"
    sed -e '/id="compatibility">Compatibility<\/h/,/^<h/{ /^<h/!d }' -e '/id="compatibility">Compatibility<\/h/d' \
        -i "$readme_html_path"
  fi
done

# Process roles with lsr_role2collection.py
for role_entry in "${roles[@]}"; do
  role_name=${role_entry%%:*}

  # Exclude auto-maintenance role for processing
  if [[ "${role_name}" == "auto_maintenance" ]]; then
    echo "Skipping Python processing for auto-maintenance role..."
    continue
  fi

  # Process the role with lsr_role2collection.py
  python3.11 %{_builddir}/roles/auto_maintenance/lsr_role2collection.py \
      --namespace suse \
      --collection linux_system_roles \
      --role ${role_name} \
      --src-path %{_builddir}/roles/${role_name} \
      --dest-path %{_builddir}/collections
done

# Clean up the entire roles directory after processing
rm -rf %{_builddir}/roles

cp %{_sourcedir}/galaxy.yml %{_builddir}/collections/ansible_collections/suse/linux_system_roles/galaxy.yml

%build
# Build Collection
cd %{_builddir}/collections/ansible_collections/suse/linux_system_roles/
ansible-galaxy collection build --output-path %{_builddir}

%install
# Creating directory for installing roles
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/ansible/collections
mkdir -p %{buildroot}%{_datadir}/ansible/roles

# ansible-galaxy always appends ansible_collections folder into collections path
ansible-galaxy collection install --force %{_builddir}/suse-%{ansible_collection_name}-%{version}.tar.gz \
  --collections-path %{buildroot}%{_datadir}/ansible/collections

%post
# Loop through roles in collection and create symlinks under %{_datadir}/ansible/roles/
# Installed community collection will take precedence over role symlinks.

# Create symlinks for Fedora, SUSE, and Linux system roles
for role in %{ansible_collection_path}/roles/*; do
  role_name=$(basename "$role")

  # Symlink for Fedora collection (namespace-based symlink)
  if [ ! -e %{_datadir}/ansible/roles/fedora.linux_system_roles.${role_name} ]; then
    ln -sf %{ansible_collection_path}/roles/${role_name} \
      %{_datadir}/ansible/roles/fedora.%{ansible_collection_name}.${role_name}
  fi

  # Symlink for Linux system roles
  if [ ! -e %{_datadir}/ansible/roles/linux-system-roles.${role_name} ]; then
    ln -sf %{ansible_collection_path}/roles/${role_name} \
      %{_datadir}/ansible/roles/linux-system-roles.${role_name}
  fi
done

%postun
# Loop through roles in %{_datadir}/ansible/roles/ and remove those that link to the collection
if [ "$1" -eq 0 ]; then
  # Remove symlinks for Fedora collection (namespace-based symlinks)
  for role in %{_datadir}/ansible/roles/fedora.%{ansible_collection_name}.*; do
    if [ -L "$role" ]; then
      target=$(readlink "$role")
      if ( [ -e "$target" ] && [ "$target" = "%{ansible_collection_path}/roles/$(basename "$role")" ] ) || [ ! -e "$target" ]; then
        rm -f "$role"
      fi
    fi
  done

  # Remove symlinks for Linux-system-roles
  for role in %{_datadir}/ansible/roles/linux-system-roles.*; do
    if [ -L "$role" ]; then
      target=$(readlink "$role")
      if ( [ -e "$target" ] && [ "$target" = "%{ansible_collection_path}/roles/$(basename "$role")" ] ) || [ ! -e "$target" ]; then
        rm -f "$role"
      fi
    fi
  done
fi

%files
%{_datadir}/ansible/collections
%{_datadir}/ansible/roles

%changelog
