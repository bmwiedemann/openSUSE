#
# spec file for package libnetfilter_cttimeout
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


Name:           libnetfilter_cttimeout
%define lname	%{name}1
Version:        1.0.0
Release:        0
Url:            http://netfilter.org/projects/libnetfilter_cttimeout/
Summary:        Userspace library for the Netfilter Conntrack Timeout extension
License:        GPL-2.0+
Group:          Productivity/Networking/Security

#Git-Clone:	git://git.netfilter.org/libnetfilter_cttimeout
Source:         ftp://ftp.netfilter.org/pub/libnetfilter_cttimeout/%name-%version.tar.bz2
Source2:        ftp://ftp.netfilter.org/pub/libnetfilter_cttimeout/%name-%version.tar.bz2.sig
Source3:        baselibs.conf
Source4:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:  autoconf, automake >= 1.6, libtool
BuildRequires:  glibc-devel >= 2.9
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  pkgconfig(libmnl) >= 1.0.0

%description
This library provides the programming interface (API) to the
Netfilter extended timeout settings infrastructure.

%package -n %lname
Summary:        Userspace library for the Netfilter Conntrack Timeout extension
Group:          System/Libraries

%description -n %lname
This library provides the programming interface (API) to the
Netfilter extended timeout settings infrastructure.

%package devel
Summary:        Userspace library for the Netfilter Conntrack Timeout extension
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
This library provides the programming interface (API) to the
Netfilter extended timeout settings infrastructure.

%prep
%setup -q

%build
if [ ! -e configure ]; then
	autoreconf -fi;
fi;
%configure --disable-static --includedir="%_includedir/%name"
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libnetfilter_cttimeout.so.1*

%files devel
%defattr(-,root,root)
%_includedir/%name/
%_libdir/libnetfilter_cttimeout.so
%_libdir/pkgconfig/libnetfilter_cttimeout.pc

%changelog
