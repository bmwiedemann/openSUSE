#
# spec file for package libnfnetlink
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


Name:           libnfnetlink
%define libsoname	%{name}0
Version:        1.0.1
Release:        0
Summary:        Low-level library for Netfilter-related kernel/userspace communication
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://netfilter.org/projects/libnfnetlink/

#Git-Clone:	git://git.netfilter.org/libnfnetlink
#DL-URL:	ftp://ftp.netfilter.org/pub/libnfnetlink/
Source:         http://netfilter.org/projects/libnfnetlink/files/%name-%version.tar.bz2
Source2:        http://netfilter.org/projects/libnfnetlink/files/%name-%version.tar.bz2.sig
Source3:        baselibs.conf
Source4:        %name.keyring

%description
libnfnetlink is the low-level library for netfilter related
kernel/userspace communication.

%package -n %libsoname
Summary:        Low-level library for Netfilter-related kernel/userspace communication
Group:          System/Libraries

%description -n %libsoname
libnfnetlink is the low-level library for netfilter related
kernel/userspace communication. It provides a generic messaging
infrastructure for in-kernel netfilter subsystems (such as
nfnetlink_log, nfnetlink_queue, nfnetlink_conntrack) and their
respective users and/or management tools in userspace.

%package devel
Requires:       %libsoname = %version
Summary:        Low-level library for Netfilter-related kernel/userspace communication
Group:          Development/Libraries/C and C++

%description devel
libnfnetlink is the low-level library for netfilter related
kernel/userspace communication.

This library is not meant as a public API for application developers.
It is only used by other netfilter.org projects, such as
libnetfilter_log, libnetfilter_queue or libnetfilter_conntrack.

%prep
%autosetup -p1

%build
%configure --disable-static --includedir="%_includedir/%name"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %libsoname -p /sbin/ldconfig
%postun -n %libsoname -p /sbin/ldconfig

%files -n %libsoname
%license COPYING
%doc README
%_libdir/libnfnetlink.so.0*

%files devel
%_includedir/%name/
%_libdir/libnfnetlink.so
%_libdir/pkgconfig/libnfnetlink.pc

%changelog
