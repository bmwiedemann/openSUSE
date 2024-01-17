#
# spec file for package system-user-grommunio
#
# Copyright (c) 2023 SUSE LLC
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


Name:           system-user-grommunio
Version:        3
Release:        0
Summary:        System users and groups for grommunio
License:        MIT
Group:          System/Fhs
URL:            https://grommunio.com/
Source:         dummy_for_debtransform.tgz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Obsoletes:      system-user-groweb < %version-%release
Provides:       system-user-groweb = %version-%release
%if 0%{?suse_version}
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Provides:       group(grommunio)
Provides:       group(groweb)
Provides:       user(grommunio)
Provides:       user(groweb)
Requires(pre):  /usr/sbin/useradd
Requires(pre):  /usr/sbin/groupadd
%endif

%description
This package provides the system accounts for grommunio.

%prep

%build
echo 'u grommunio - "user for grommunio administration"' >u.conf
echo 'u groweb - "user for grommunio-web"' >>u.conf
%if 0%{?suse_version}
%sysusers_generate_pre u.conf user system-user-grommunio.conf
%else
>user.pre
%endif

%install
install -Dpm0644 u.conf "%buildroot/%_sysusersdir/system-user-grommunio.conf"

%pre -f user.pre
%if !0%{?suse_version}
getent group grommunio >/dev/null || %_sbindir/groupadd -r grommunio
getent passwd grommunio >/dev/null || %_sbindir/useradd -g grommunio -s /sbin/nologin \
	-r -c "user for grommunio administration" -d / grommunio
getent group groweb >/dev/null || %_sbindir/groupadd -r groweb
getent passwd groweb >/dev/null || %_sbindir/useradd -g groweb -s /sbin/nologin \
	-r -c "user for grommunio-web" -d / groweb
%endif

%files
%_sysusersdir/*.conf

%changelog
