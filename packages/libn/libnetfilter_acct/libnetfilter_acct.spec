#
# spec file for package libnetfilter_acct
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libnetfilter_acct
%define lname	%{name}1
Version:        1.0.3
Release:        0
Summary:        Userspace library for the in-kernel Netfilter counters
License:        LGPL-2.1+
Group:          Productivity/Networking/Security
Url:            http://netfilter.org/projects/libnetfilter_acct/

#Git-Clone:	git://git.netfilter.org/libnetfilter_acct
Source:         ftp://ftp.netfilter.org/pub/libnetfilter_acct/%name-%version.tar.bz2
Source2:        ftp://ftp.netfilter.org/pub/libnetfilter_acct/%name-%version.tar.bz2.sig
Source3:        baselibs.conf
Source4:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  pkgconfig(libmnl) >= 1.0.0

%description
This library provides the programming interface (API) to the
Netfilter extended accounting infrastructure.

%package -n %lname
Summary:        Userspace library for the in-kernel Netfilter counters
Group:          System/Libraries

%description -n %lname
This library provides the programming interface (API) to the
Netfilter extended accounting infrastructure.

%package devel
Requires:       %lname = %version
Summary:        Userspace library for the in-kernel Netfilter counters
Group:          Development/Libraries/C and C++

%description devel
This library provides the programming interface (API) to the
Netfilter extended accounting infrastructure.

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
%_libdir/libnetfilter_acct.so.1*

%files devel
%defattr(-,root,root)
%_includedir/%name/
%_libdir/libnetfilter_acct.so
%_libdir/pkgconfig/libnetfilter_acct.pc

%changelog
