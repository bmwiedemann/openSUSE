#
# spec file for package wtmpdb
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


%define lname   libwtmpdb0
Name:           wtmpdb
Version:        0.71.0+git20250206.608632a
Release:        0
Summary:        Database for recording the last logged in users and system reboots
License:        BSD-2-Clause
URL:            https://github.com/thkukuk/wtmpdb
Source:         %{name}-%{version}.tar.xz
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(libsystemd) >= 257
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(sqlite3)
Requires(post): pam-config
Requires(postun): pam-config
# Split provide for last
Provides:       util-linux:/usr/bin/last

%description
pam_wtmpdb and wtmpdb are Y2038-safe versions of wtmp and the last
utility. pam_wtmpdb collects all data in a sqlite3 database and the
wtmpdb utility creates boot and shutdown entries or formats and
prints the contents of the wtmp database.

%package -n %{lname}
Summary:        PAM module to store login and logout of users

%description -n %{lname}
The libwtmpdb provides various interfaces to read, write or modify
the wtmpdb database.

%package devel
Summary:        Development files for libwtmpdb
Requires:       %{lname} = %{version}

%description devel
This package contains all necessary include files and libraries
needed to develop applications that needs to read, write or modify
the wtmpdb database.

%prep
%autosetup

%build
%meson -Dman=enabled -Dcompat-symlink=true -Dwtmpdbd=enabled
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_mandir}/man1
echo ".so man8/wtmpdb.8" > %{buildroot}%{_mandir}/man1/last.1

%check
%meson_test

%pre
%service_add_pre wtmpdb-update-boot.service wtmpdb-rotate.timer wtmpdbd.socket

%preun
%service_del_preun wtmpdb-update-boot.service wtmpdb-rotate.timer wtmpdbd.socket

%post
%tmpfiles_create wtmpdb.conf
%service_add_post wtmpdb-update-boot.service wtmpdb-rotate.timer wtmpdbd.socket
pam-config -a --wtmpdb --wtmpdb-skip_if=sshd

%postun
if [ "$1" -eq 0 ]; then
    pam-config -d --wtmpdb
fi
%service_del_postun_without_restart wtmpdb-update-boot.service
%service_del_postun wtmpdb-rotate.timer wtmpdbd.socket

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/last
%{_bindir}/wtmpdb
%{_libexecdir}/wtmpdbd
%{_unitdir}/wtmpdb-update-boot.service
%{_unitdir}/wtmpdb-rotate.service
%{_unitdir}/wtmpdb-rotate.timer
%{_prefix}/lib/systemd/system/wtmpdbd.service
%{_prefix}/lib/systemd/system/wtmpdbd.socket
%{_tmpfilesdir}/wtmpdb.conf
%{_pam_moduledir}/pam_wtmpdb.so
%ghost %{_localstatedir}/lib/wtmpdb
%{_mandir}/man1/last.1%{?ext_man}
%{_mandir}/man8/wtmpdb.8%{?ext_man}
%{_mandir}/man8/wtmpdbd.8%{?ext_man}
%{_mandir}/man8/wtmpdbd.service.8%{?ext_man}
%{_mandir}/man8/wtmpdbd.socket.8%{?ext_man}
%{_mandir}/man8/pam_wtmpdb.8%{?ext_man}

%files -n %{lname}
%license LICENSE
%{_libdir}/libwtmpdb.so.*

%files devel
%{_libdir}/libwtmpdb.so
%{_includedir}/wtmpdb.h
%{_libdir}/pkgconfig/libwtmpdb.pc

%changelog
