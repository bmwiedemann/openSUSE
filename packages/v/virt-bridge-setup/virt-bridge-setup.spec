#
# spec file for package virt-bridge-setup
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

Name:           virt-bridge-setup
Version:        2.6
Release:        1%{?dist}
Summary:        Script to setup virtual bridges
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/aginies/virt-bridge-setup
Source0:        https://github.com/aginies/virt-bridge-setup/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       NetworkManager
Requires: 	python3-dbus-python
BuildRequires:       make

%description
virt-bridge-setup is a script to automate the setup of virtual bridges using NetworkManager and dbus.
It simplifies the process of creating and managing network bridges for virtualization environments.

%prep
%setup -q

%build

%install
%make_install

%files
%license LICENSE
%doc README.md
%attr(0755,root,root) %{_sbindir}/%{name}

%changelog
