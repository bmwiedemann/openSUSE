#
# spec file for package libnetfilter_log
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libnetfilter_log
%define lname	%{name}1
Version:        1.0.1
Release:        0
Summary:        Userspace library for accessing logged packets
License:        GPL-2.0
Group:          Productivity/Networking/Security
Url:            http://netfilter.org/projects/libnetfilter_log/

#Git-Clone:	git://git.netfilter.org/libnetfilter_log
Source:         ftp://ftp.netfilter.org/pub/libnetfilter_log/%name-%version.tar.bz2
Source2:        ftp://ftp.netfilter.org/pub/libnetfilter_log/%name-%version.tar.bz2.sig
Source3:        baselibs.conf
Source4:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildRequires:  autoconf, automake >= 1.6, libtool
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  pkgconfig(libnfnetlink) >= 0.0.41

%description
libnetfilter_log is a userspace library providing interface to
packets that have been logged by the kernel packet filter. It is is
part of a system that deprecates the old syslog/dmesg based packet
logging. This library has been previously known as libnfnetlink_log.

%package -n %lname
Summary:        Userspace library for accessing logged packets
Group:          System/Libraries

%description -n %lname
libnetfilter_log is a userspace library providing interface to
packets that have been logged by the kernel packet filter. It is is
part of a system that deprecates the old syslog/dmesg based packet
logging. This library has been previously known as libnfnetlink_log.

%package devel
Summary:        Userspace library for accessing logged packets
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libnfnetlink-devel

%description devel
libnetfilter_log is a userspace library providing interface to
packets that have been logged by the kernel packet filter. It is is
part of a system that deprecates the old syslog/dmesg based packet
logging. This library has been previously known as libnfnetlink_log.

%prep
%setup -q

%build
%configure --disable-static --includedir="%_includedir/%name"
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libnetfilter_log.so.1*
%_libdir/libnetfilter_log_libipulog.so.1*

%files devel
%defattr(-,root,root)
%_includedir/%name/
%_libdir/libnetfilter_log.so
%_libdir/libnetfilter_log_libipulog.so
%_libdir/pkgconfig/libnetfilter_log.pc

%changelog
