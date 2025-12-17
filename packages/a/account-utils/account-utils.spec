#
# spec file for package pwaccess
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

%define lname   libpwaccess0
Name:           account-utils
Version:        1.0+git20251216.774fa6e
Release:        0
Summary:        Service for authentication and account management
License:        GPL-2.0-or-later AND BSD-2-Clause AND LGPL-2.1-or-later
URL:            https://github.com/thkukuk/account-utils
Source:         %{name}-%{version}.tar.xz
Source1:        account-utils.permissions
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libeconf)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd) >= 257
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  pkgconfig(pam) >= 1.6.0
# For test suite
BuildRequires:  user(nobody)
Requires(post): permissions
Conflicts:      shadow-pw-mgmt
Conflicts:      busybox-adduser
Requires(pre):  pam-config
Requires(posttrans): pam-config


%description
The account-utils package contains the utilities and services to do user management and authentication without the need for setuid/setgid binaries. This allows the stack to work with `NoNewPrivs` enabled (means setuid/setgid binaries will no longer work). Communication happens via varlink.

%package -n %{lname}
Summary:        Library to access pwaccess and pwupd services

%description -n %{lname}
The libpwaccess library provides interfaces to communicate with pwaccessd
and pwupdd.

%package devel
Summary:        Development files for libpwaccess
Requires:       %{lname} = %{version}

%description devel
This package contains all necessary include files and libraries
needed to develop applications that needs to communicate with the
pwaccess and pwupd services.

%prep
%autosetup

%build
%meson -Ddistribution=suse
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/permissions/permissions.d/
cp %{SOURCE1} %{buildroot}%{_datadir}/permissions/permissions.d/account-utils

%check
%meson_test

%pre
%service_add_pre pwaccessd.socket pwupdd.socket newidmapd.socket

%preun
%service_del_preun pwaccessd.socket pwupdd.socket newidmapd.socket

%post
%service_add_post pwaccessd.socket pwupdd.socket newidmapd.socket
%set_permissions %{_bindir}/chage
%set_permissions %{_bindir}/chfn
%set_permissions %{_bindir}/chsh
%set_permissions %{_bindir}/expiry
%set_permissions %{_bindir}/newgidmap
%set_permissions %{_bindir}/newuidmap
%set_permissions %{_bindir}/passwd
if [ "$1" -eq 1 ]; then
    pam-config -a --unix_ng || :
fi

%postun
%service_del_postun pwaccessd.socket pwupdd.socket newidmapd.socket
if [ "$1" -eq 0 ]; then
    pam-config -d --unix_ng || :
fi

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%verifyscript
%verify_permissions %{_bindir}/chage
%verify_permissions %{_bindir}/chfn
%verify_permissions %{_bindir}/chsh
%verify_permissions %{_bindir}/expiry
%verify_permissions %{_bindir}/newgidmap
%verify_permissions %{_bindir}/newuidmap
%verify_permissions %{_bindir}/passwd

%files
%license LICENSE.BSD-2-Clause
%license LICENSE.GPL2
%license LICENSE.LGPL2.1
%{_bindir}/chage
%{_bindir}/chfn
%{_bindir}/chsh
%{_bindir}/dump-privs
%{_bindir}/expiry
%{_bindir}/newgidmap
%{_bindir}/newuidmap
%{_bindir}/passwd
%{_bindir}/scan-caps
%{_prefix}/lib/systemd/system/newidmapd.service
%{_prefix}/lib/systemd/system/newidmapd.socket
%{_prefix}/lib/systemd/system/pwaccessd.service
%{_prefix}/lib/systemd/system/pwaccessd.socket
%{_prefix}/lib/systemd/system/pwupdd@.service
%{_prefix}/lib/systemd/system/pwupdd.socket
%{_libexecdir}/newidmapd
%{_libexecdir}/pwaccessd
%{_libexecdir}/pwupdd
%{_pam_moduledir}/pam_debuginfo.so
%{_pam_moduledir}/pam_unix_ng.so
%{_pam_vendordir}/passwd
%{_pam_vendordir}/pwupd-chfn
%{_pam_vendordir}/pwupd-chsh
%{_pam_vendordir}/pwupd-passwd
%{_mandir}/man1/chage.1%{?ext_man}
%{_mandir}/man1/chfn.1%{?ext_man}
%{_mandir}/man1/chsh.1%{?ext_man}
%{_mandir}/man1/expiry.1%{?ext_man}
%{_mandir}/man1/passwd.1%{?ext_man}
%{_mandir}/man8/pam_debuginfo.8%{?ext_man}
%{_mandir}/man8/pam_unix_ng.8%{?ext_man}
%{_datadir}/permissions/permissions.d/account-utils

%files -n %{lname}
%license LICENSE.LGPL2.1
%{_libdir}/libpwaccess.so.*

%files devel
%{_libdir}/libpwaccess.so
%{_includedir}/pwaccess.h
%{_libdir}/pkgconfig/libpwaccess.pc

%changelog
