#
# spec file for package ansible-sap-playbooks
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


Name:           ansible-sap-playbooks
Summary:        Ansible Playbooks for SAP Automation
License:        Apache-2.0
Version:        1.3.0
Release:        0
URL:            https://github.com/SUSE/ansible.playbooks_for_sap/
Source0:        %{url}archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.yaml
Source2:        transformation.py
Source99:       %{name}.rpmlintrc

BuildArch:      noarch


Requires:       ansible >= 9
Requires:       ansible-core >= 2.16
BuildRequires:  ansible >= 9
BuildRequires:  ansible-core >= 2.16

Requires:       ansible-sap-install
Requires:       ansible-sap-operations
Requires:       ansible-sap-infrastructure

# Package ansible-sap-launchpad is present in PackageHub and it is not directly recommended.
# Recommends: ansible-sap-launchpad

# Python module ruamel.yaml for transformation.py
BuildRequires:  python3-ruamel.yaml

%description
This package provides a collection of Ansible Playbooks for SAP Automation,  designed to automate the setup and configuration of SAP environments.

The playbooks are installed in the following directory: /usr/share/ansible/playbooks/ansible.playbooks_for_sap/

IMPORTANT: Do not modify the playbooks in this directory directly. Any changes will be overwritten by future package updates (zypper up).
Instead, copy the playbooks to a different location before customizing or using them.

It is highly recommended to read the README file in the installation directory to understand the functionality and proper usage of the playbooks.

%prep
%autosetup -p1 -n ansible.playbooks_for_sap-%{version}

%build
# Execute python script to update documentation and remove unsupported roles
python3 %{_sourcedir}/transformation.py --config %{_sourcedir}/%{name}.yaml  --build_dir .

%install
mkdir -p %{buildroot}%{_datadir}/ansible/playbooks/
mkdir -p %{buildroot}%{_datadir}/ansible/playbooks/ansible.playbooks_for_sap
%{__cp} -a . %{buildroot}%{_datadir}/ansible/playbooks/ansible.playbooks_for_sap/

%files
%{_datadir}/ansible/playbooks

%changelog
