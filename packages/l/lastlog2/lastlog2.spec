#
# spec file for package lastlog2
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


%define lname   liblastlog2-0
Name:           lastlog2
Version:        0.6.2
Release:        0
Summary:        Reports most recent login of users
License:        BSD-2-Clause
URL:            https://github.com/thkukuk/lastlog2
Source:         %{name}-%{version}.tar.xz
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(sqlite3)
PreReq:         pam-config

%description
pam_lastlog2 and lastlog2 are Y2038 safe versions of the old lastlog utility. pam_lastlog2 collects all data in a sqlite3 database and lastlog2 formats and prints the contents. The username, port, and last login time will be printed.

%package -n %{lname}
Summary:        PAM module to report most recent login of users

%description -n %{lname}
The liblastlog2 provides various interfaces to read, write or modify the lastlog 2 database.

%package devel
Summary:        Development files for liblastlog2
Requires:       %{lname} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that needs to read, write or modify the lastlog2 database.

%prep
%setup -q

%build
%meson -Dman=true
%meson_build

%install
%meson_install

%check
%meson_test

%pre
%service_add_pre lastlog2-import.service

%preun
%service_del_preun lastlog2-import.service

%post
%tmpfiles_create lastlog2.conf
%service_add_post lastlog2-import.service
pam-config -a --lastlog2

%postun
if [ "$1" -eq 0 ]; then
    pam-config -d --lastlog2
fi
%service_del_postun lastlog2-import.service

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/lastlog2
%{_unitdir}/lastlog2-import.service
%{_tmpfilesdir}/lastlog2.conf
%{_pam_moduledir}/pam_lastlog2.so
%ghost %{_localstatedir}/lib/lastlog
%{_mandir}/man8/lastlog2.8%{?ext_man}
%{_mandir}/man8/pam_lastlog2.8%{?ext_man}

%files -n %{lname}
%license LICENSE
%{_libdir}/liblastlog2.so.*

%files devel
%{_libdir}/liblastlog2.so
%{_includedir}/lastlog2.h
%{_libdir}/pkgconfig/liblastlog2.pc

%changelog
