#
# spec file for package ansible-sap-launchpad
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


%define ansible_collection_name community-sap_launchpad-%{version}

Name:           ansible-sap-launchpad
Summary:        Ansible collection community.sap_launchpad for SAP Automation
License:        Apache-2.0
Version:        1.2.0
Release:        0
URL:            https://github.com/sap-linuxlab/community.sap_launchpad/
Source:         %{url}archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch


Requires:       ansible >= 9
Requires:       ansible-core >= 2.16
BuildRequires:  ansible >= 9
BuildRequires:  ansible-core >= 2.16

%description
This package provides a Ansible collection community.sap_launchpad.

It automates download of SAP Software for SAP installations.
Downloads software using list of files or maintenance plan ID.

%prep
# Extract tarball
cd %{_builddir}
tar -xzf %{_sourcedir}/%{name}-%{version}.tar.gz --strip-components=1

%build
# Build the Ansible collection
ansible-galaxy collection build --output-path %{_builddir}

%install
rm -rf %{buildroot}
# ansible-galaxy always appends ansible_collections folder into collections path
mkdir -p %{buildroot}%{_datadir}/ansible/collections
ansible-galaxy collection install --force %{_builddir}/%{ansible_collection_name}.tar.gz \
  --collections-path %{buildroot}%{_datadir}/ansible/collections

%files
%{_datadir}/ansible/collections/

%changelog
