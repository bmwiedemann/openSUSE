#
# spec file for package system-user-vault-sync
#
# Copyright (c) 2020 SUSE LLC
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

Name:           system-user-vault-sync
Version:        1.0.0
Release:        0
Summary:        System user and group 'vault-sync'
License:        Apache-2.0
Source0:        system-user-vault-sync.conf
BuildRequires:  sysuser-tools
BuildArch:      noarch
%sysusers_requires

%description
This package provides a system user for the vault-sync service.

%prep
%setup -q -c -T

%build
%sysusers_generate_pre %{SOURCE0} user

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_sysusersdir}/system-user-vault-sync.conf

%pre -f user.pre

%files
%{_sysusersdir}/system-user-vault-sync.conf

%changelog
