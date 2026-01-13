#
# spec file for package ansible-sap-launchpad
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


%define ansible_collection_name community-sap_launchpad-%{version}

Name:           ansible-sap-launchpad
Summary:        Ansible collection community.sap_launchpad for SAP Automation
License:        Apache-2.0
Version:        1.3.1
Release:        0
URL:            https://github.com/sap-linuxlab/community.sap_launchpad/
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
This package provides a Ansible collection community.sap_launchpad.

It automates download of SAP Software for SAP installations.
Downloads software using list of files or maintenance plan ID.

%prep
%autosetup -p1 -n community.sap_launchpad-%{version}

%build
# Execute python script to update documentation and remove unsupported roles
python3 %{_sourcedir}/transformation.py --config %{_sourcedir}/%{name}.yaml  --build_dir .
# Ensure there are no executable files present, except for sh and py files.
find . -type f -perm /u+x,g+x,o+x -not -name "*.sh" -not -name "*.py" -exec chmod -x {} \;
# Build the Ansible collection
ansible-galaxy collection build --output-path %{_builddir}

%install
# ansible-galaxy always appends ansible_collections folder into collections path
mkdir -p %{buildroot}%{_datadir}/ansible/collections
ansible-galaxy collection install --force %{_builddir}/%{ansible_collection_name}.tar.gz \
  --collections-path %{buildroot}%{_datadir}/ansible/collections

%files
%{_datadir}/ansible/collections/

%changelog
