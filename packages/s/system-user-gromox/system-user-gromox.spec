#
# spec file for package system-user-gromox
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


Name:           system-user-gromox
Version:        2
Release:        0
Summary:        System user and group gromox
License:        MIT
Group:          System/Fhs
URL:            https://grommunio.com/
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
%sysusers_requires

%description
This package provides the gromox account.

%prep

%build
echo 'u gromox - "Gromox services"' >u.conf
%sysusers_generate_pre u.conf user

%install
install -Dpm0644 u.conf "%buildroot/%_sysusersdir/system-user-gromox.conf"

%pre -f user.pre

%files
%_sysusersdir/*.conf

%changelog
