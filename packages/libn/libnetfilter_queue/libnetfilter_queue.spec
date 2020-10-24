#
# spec file for package libnetfilter_queue
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


Name:           libnetfilter_queue
%define lname	%{name}1
Version:        1.0.5
Release:        0
Summary:        Userspace library for packets that have been queued by the kernel packet filter
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://netfilter.org/projects/libnetfilter_queue/

#Git-Clone:	git://git.netfilter.org/libnetfilter_queue
#DL-URL:	https://netfilter.org/projects/libnetfilter_queue/files/
Source:         https://netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-%version.tar.bz2
Source2:        https://netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-%version.tar.bz2.sig
Source3:        baselibs.conf
Source4:        %name.keyring
BuildRequires:  pkgconfig(libmnl) >= 1.0.3
BuildRequires:  pkgconfig(libnfnetlink) >= 0.0.41

%description
libnetfilter_queue is a userspace library providing an API to packets
that have been queued by the kernel packet filter. It is is part of a
system that deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue.

%package -n %lname
Summary:        Userspace library for packets that have been queued by the kernel packet filter
Group:          System/Libraries

%description -n %lname
libnetfilter_queue is a userspace library providing an API to packets
that have been queued by the kernel packet filter. It is is part of a
system that deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue.

%package devel
Summary:        Userspace library for packets that have been queued by the kernel packet filter
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libnfnetlink-devel

%description devel
libnetfilter_queue is a userspace library providing an API to packets
that have been queued by the kernel packet filter. It is is part of a
system that deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue.

%prep
%autosetup -p1

%build
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --disable-static --includedir="%_includedir/%name"
%make_build KERNELDIR="ignore"

%install
%make_install KERNELDIR="ignore"
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libnetfilter_queue.so.1*

%files devel
%_includedir/%name/
%_libdir/libnetfilter_queue.so
%_libdir/pkgconfig/libnetfilter_queue.pc

%changelog
