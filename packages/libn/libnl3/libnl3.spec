#
# spec file for package libnl3
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


Name:           libnl3
%define lname	libnl3-200
%define with_tools 1
%define uver	3_5_0
Version:        3.5.0
Release:        0
Summary:        Convenience library for working with Netlink sockets
License:        LGPL-2.1-only AND GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            http://www.carisma.slowglass.com/~tgr/libnl/#(outdated)

#Git-Clone:	https://github.com/thom311/libnl/
Source:         https://github.com/thom311/libnl/releases/download/libnl%uver/libnl-%version.tar.gz
Source2:        https://github.com/thom311/libnl/releases/download/libnl%uver/libnl-%version.tar.gz.sig
Source3:        baselibs.conf
BuildRequires:  bison >= 2.4
BuildRequires:  fdupes
BuildRequires:  flex >= 2.5.19

%description
The libnl suite is a collection of libraries providing APIs to
Netlink protocol based Linux kernel interfaces.

%package -n %lname
Summary:        Convenience library for working with Netlink sockets
License:        LGPL-2.1-only
Group:          System/Libraries
Requires:       libnl-config >= %version

%description -n %lname
The libnl suite is a collection of libraries providing APIs to
netlink protocol based Linux kernel interfaces.

%package devel
Summary:        Libraries and headers for libnl
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Provides:       libnl-devel = %version-%release
# Starting with libnl3(-3.2), no more conflicts

%description devel
The libnl suite is a collection of libraries providing APIs to
Netlink protocol based Linux kernel interfaces.

%if %with_tools
#
# Only one of the libnl packages should create the config and tools.
#

%package -n libnl-config
Summary:        Name maps for libnl
License:        LGPL-2.1-only AND GPL-2.0-only
Group:          Productivity/Networking/Security
%if 0%{?suse_version} >= 1130
BuildArch:      noarch
%endif

%description -n libnl-config
This package contains configuration files for libnl and programs using
the same; in particular
- name maps for class-ids -- class-names (like /etc/services)
- aliases for locations within a packet (ip6.dst => byte offset)

%package -n libnl-tools
Summary:        Command line utilities to directly work with Netlink
License:        GPL-2.0-only
Group:          Productivity/Networking/Security

%description -n libnl-tools
Various test program with which the functionality of libnl is
demonstrated.

%endif

%prep
%autosetup -p1 -n libnl-%version

%build
%configure --disable-static
%make_build pkglibdir="%_libdir/%lname"

%install
b="%buildroot"
%make_install pkglibdir="%_libdir/%lname"
find "$b" -iname "*.la" -delete
%if !%with_tools
rm -Rf "$b/%_sysconfdir/libnl"
rm -Rf "$b/%_sbindir" "$b/%_mandir/man8"
%endif
%if 0%{?fdupes:1}
%fdupes %buildroot/%_prefix
%endif

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libnl*.so.200*
%_libdir/%lname

%files devel
%_includedir/%name
%_libdir/libnl*.so
%_libdir/pkgconfig/*

%if %with_tools

%files -n libnl-config
%dir %_sysconfdir/libnl
%config %_sysconfdir/libnl/*

%files -n libnl-tools
%_mandir/man*/*
%_bindir/*
%endif

%changelog
