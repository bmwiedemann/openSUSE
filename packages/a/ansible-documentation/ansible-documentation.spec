#
# spec file for package ansible-documentation
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


Name:           ansible-documentation
Version:        2.16.8
Release:        0
Summary:        Ansible community documentation and example files
License:        GPL-3.0-only
URL:            https://github.com/ansible/ansible-documentation
Source:         ansible-documentation-%{version}.tar.gz
BuildRequires:  ansible-core = %{version}
BuildRequires:  fdupes
Requires:       ansible-core = %{version}
BuildArch:      noarch

%description
User documentation and example files related to the Ansible package and Ansible core.

%prep
%autosetup -p1 -n ansible-documentation-%{version}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/ansible/
cp examples/hosts %{buildroot}%{_sysconfdir}/ansible/
cp examples/ansible.cfg %{buildroot}%{_sysconfdir}/ansible/

%files
%doc README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/ansible/ansible.cfg
%config(noreplace) %{_sysconfdir}/ansible/hosts

%changelog
