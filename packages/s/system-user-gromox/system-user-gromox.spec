#
# spec file for package system-user-gromox
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


Name:           system-user-gromox
Version:        6
Release:        0
Summary:        System user and group gromox
License:        MIT
Group:          System/Fhs
URL:            https://grommunio.com/
Source:         system-user-gromox.conf
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
%if 0%{?suse_version}
BuildRequires:  sysuser-tools
%sysusers_requires
%endif
%if 0%{?rhel} || 0%{?fedora_version}
%{?sysusers_requires_compat}
%endif

%description
This package provides the gromox account.

%prep

%build
# The conf file is provided by system-user-gromox rather than
# gromox.spec so that e.g. grommunio-admin-api does not grow a
# BuildRequire on gromox (wait times).
#
>user.pre
%if 0%{?suse_version}
%sysusers_generate_pre %_sourcedir/system-user-gromox.conf user
%endif

%install
install -Dpm0644 %_sourcedir/system-user-gromox.conf "%buildroot/%_sysusersdir/system-user-gromox.conf"

%pre -f user.pre
%if 0%{?rhel} || 0%{?fedora_version}
%sysusers_create_compat %_sourcedir/system-user-gromox.conf
%endif

%files
%_sysusersdir/*.conf

%changelog
