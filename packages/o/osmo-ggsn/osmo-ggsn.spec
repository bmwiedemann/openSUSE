#
# spec file for package osmo-ggsn
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


%define _lto_cflags %nil
Name:           osmo-ggsn
%define lname   libgtp6
Version:        1.11.0
Release:        0
Summary:        GPRS Support Node
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Productivity/Telephony/Servers
URL:            https://osmocom.org/projects/openggsn/wiki/OsmoGGSN
Source:         https://github.com/osmocom/osmo-ggsn/archive/%version.tar.gz
Patch1:         build-fixes.diff
Patch2:         ppc64.diff
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  pkgconfig(libgtpnl) >= 1.2.0
BuildRequires:  pkgconfig(libosmocore) >= 1.9.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.9.0
BuildRequires:  pkgconfig(libosmovty) >= 1.9.0
Obsoletes:      openggsn

%description
Osmo-GGSN is a C-language implementation of a GGSN (Gateway GPRS
Support Node), a core network element of ETSI/3GPP cellular networks
such as GPRS, EDGE, UMTS or HSPA.

%package -n %lname
Summary:        Library implementing GTP between SGSN and GGSN
License:        GPL-2.0-only
Group:          System/Libraries

%description -n %lname
libgtp implements the GPRS Tunneling Protocol between SGSN and GGSN.

%package -n libgtp-devel
Summary:        Development files for the GTP library
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n libgtp-devel
libgtp implements the GPRS Tunneling Protocol between SGSN and GGSN.

This subpackage contains libraries and header files for developing
applications that want to make use of libgtp.

%package -n gtp-echo-responder
Summary:        Small program answering GTP ECHO Request with GTP ECHO Response
License:        MIT
Group:          Productivity/Telephony/Utilities

%description -n gtp-echo-responder
Small program answering GTP ECHO Request with GTP ECHO Response for both GTPCv1
and GTPCv2.

%prep
%autosetup -p1
sed -i 's|%_bindir/osmo-ggsn|%_sbindir/osmo-ggsn|g' contrib/systemd/osmo-ggsn.service

%build
echo "%version" >.tarball-version
autoreconf -fi
# bugzilla.opensuse.org/795968 for rationale
%configure \
	--enable-gtp-linux \
	--includedir="%_includedir/%name" \
	--disable-static --docdir="%_docdir/%name" \
	--with-systemdsystemunitdir="%_unitdir"
%make_build

%install
b="%buildroot"
%make_install
find "$b" -type f -name "*.la" -delete -print
install -d "$b/%_sysconfdir/osmocom"
install -m 0644 doc/examples/osmo-ggsn.cfg "$b/%_sysconfdir/osmocom/osmo-ggsn.cfg"
install -m 0644 doc/examples/sgsnemu.conf "$b/%_sysconfdir/osmocom/sgsnemu.conf"

%pre
%service_add_pre %name.service

%post
%service_add_post %name.service

%preun
%service_del_preun %name.service

%postun
%service_del_postun %name.service

%ldconfig_scriptlets -n %lname

%files
%license COPYING
%doc AUTHORS README.md
%_sbindir/osmo-ggsn
%_sbindir/sgsnemu
%_mandir/man8/osmo-ggsn.8*
%_mandir/man8/sgsnemu.8*
%_unitdir/%name.service
%dir %_docdir/%name/examples
%_docdir/%name/examples/osmo-ggsn-kernel-gtp.cfg
%_docdir/%name/examples/osmo-ggsn.cfg
%_docdir/%name/examples/sgsnemu.conf
%dir %_sysconfdir/osmocom
%config(noreplace) %_sysconfdir/osmocom/osmo-ggsn.cfg
%config(noreplace) %_sysconfdir/osmocom/sgsnemu.conf

%files -n %lname
%_libdir/libgtp.so.6*

%files -n libgtp-devel
%_includedir/%name/
%_libdir/libgtp.so
%_libdir/pkgconfig/libgtp.pc

%files -n gtp-echo-responder
%_bindir/gtp-echo-responder

%changelog
