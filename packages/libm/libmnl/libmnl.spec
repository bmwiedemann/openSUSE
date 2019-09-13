#
# spec file for package libmnl
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


Name:           libmnl
%define lname	%{name}0
Version:        1.0.4
Release:        0
Url:            http://netfilter.org/projects/libmnl/
Summary:        Minimalistic Netlink communication library
License:        LGPL-2.1+
Group:          Productivity/Networking/Security

#Git-Clone:	git://git.netfilter.org/libmnl
Source:         ftp://ftp.netfilter.org/pub/libmnl/%name-%version.tar.bz2
Source2:        ftp://ftp.netfilter.org/pub/libmnl/%name-%version.tar.bz2.sig
Source3:        %name.keyring
Source9:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf, automake >= 1.6
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.21

%description
libmnl is a minimalistic user-space library oriented to Netlink
developers. There are a lot of common tasks in parsing, validating,
constructing of both the Netlink header and TLVs that are repetitive
and easy to get wrong. This library aims to provide simple helpers
that allows you to re-use code and to avoid re-inventing the wheel.

%package -n %lname
Summary:        Minimalistic Netlink communication library
Group:          System/Libraries

%description -n %lname
libmnl is a minimalistic user-space library oriented to Netlink
developers. There are a lot of common tasks in parsing, validating,
constructing of both the Netlink header and TLVs that are repetitive
and easy to get wrong. This library aims to provide simple helpers
that allows you to re-use code and to avoid re-inventing the wheel.

%package -n %name-devel
Requires:       %lname = %version
Summary:        Development files for libmnl
Group:          Development/Libraries/C and C++

%description -n %name-devel
libmnl is a minimalistic user-space library oriented to Netlink
developers. There are a lot of common tasks in parsing, validating,
constructing of both the Netlink header and TLVs that are repetitive
and easy to get wrong. This library aims to provide simple helpers
that allows you to re-use code and to avoid re-inventing the wheel.

%prep
%setup -q

%build
if [ ! -e configure ]; then
	autoreconf -fi;
fi;
%configure --includedir="%_includedir/%name"
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libmnl.so.0*

%files -n %name-devel
%defattr(-,root,root)
%_includedir/%name/
%_libdir/libmnl.so
%_libdir/pkgconfig/libmnl.pc

%changelog
