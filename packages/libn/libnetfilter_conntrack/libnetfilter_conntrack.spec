#
# spec file for package libnetfilter_conntrack
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


Name:           libnetfilter_conntrack
%define lname	libnetfilter_conntrack3
Version:        1.0.8
Release:        0
Summary:        Userspace library for the in-kernel connection tracking state table
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://netfilter.org/projects/libnetfilter_conntrack/

#Git-Clone:	git://git.netfilter.org/libnetfilter_conntrack
Source:         ftp://ftp.netfilter.org/pub/libnetfilter_conntrack/%name-%version.tar.bz2
Source2:        ftp://ftp.netfilter.org/pub/libnetfilter_conntrack/%name-%version.tar.bz2.sig
Source3:        baselibs.conf
Source4:        %name.keyring
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  pkgconfig(libmnl) >= 1.0.3
BuildRequires:  pkgconfig(libnfnetlink) >= 1.0.0

%description
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table. The
library libnetfilter_conntrack has been previously known as
libnfnetlink_conntrack and libctnetlink. This library is currently
used by conntrack-tools among many other applications.

%package -n %lname
Summary:        Userspace library for the in-kernel connection tracking state table
Group:          System/Libraries

%description -n %lname
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table. The
library libnetfilter_conntrack has been previously known as
libnfnetlink_conntrack and libctnetlink. This library is currently
used by conntrack-tools among many other applications.

%package devel
Summary:        Userspace library for the in-kernel connection tracking state table
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table. The
library libnetfilter_conntrack has been previously known as
libnfnetlink_conntrack and libctnetlink. This library is currently
used by conntrack-tools among many other applications.

%prep
%autosetup -p1

%build
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --disable-static --includedir="%_includedir/%name"
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libnetfilter_conntrack.so.3*

%files devel
%_includedir/%name/
%_libdir/libnetfilter_conntrack.so
%_libdir/pkgconfig/libnetfilter_conntrack.pc

%changelog
