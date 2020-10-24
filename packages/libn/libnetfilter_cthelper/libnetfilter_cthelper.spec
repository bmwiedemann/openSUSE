#
# spec file for package libnetfilter_cthelper
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


Name:           libnetfilter_cthelper
%define lname	%{name}0
Version:        1.0.0
Release:        0
Summary:        Userspace library for the Netfilter Conntrack Helper extension
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://netfilter.org/projects/libnetfilter_cthelper/

#Git-Clone:	git://git.netfilter.org/libnetfilter_cthelper
#DL-URL:	http://netfilter.org/projects/libnetfilter_cthelper/files/
Source:         http://netfilter.org/projects/libnetfilter_cthelper/files/%name-%version.tar.bz2
Source2:        http://netfilter.org/projects/libnetfilter_cthelper/files/%name-%version.tar.bz2.sig
Source3:        baselibs.conf
Source4:        %name.keyring
Patch1:         fix_h_expect_policy_free.patch
#BuildRequires:  autoconf
#BuildRequires:  automake >= 1.6
#BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig(libmnl) >= 1.0.0

%description
This library provides the programming interface (API) to the
Netfilter userspace helper infrastructure.

%package -n %lname
Summary:        Userspace library for the Netfilter Conntrack Helper extension
Group:          System/Libraries

%description -n %lname
This library provides the programming interface (API) to the
Netfilter userspace helper infrastructure.

%package devel
Summary:        Userspace library for the Netfilter Conntrack Helper extension
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
This library provides the programming interface (API) to the
Netfilter userspace helper infrastructure.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then
	autoreconf -fi
fi
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --disable-static --includedir="%_includedir/%name"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libnetfilter_cthelper.so.0*

%files devel
%_includedir/%name/
%_libdir/libnetfilter_cthelper.so
%_libdir/pkgconfig/libnetfilter_cthelper.pc

%changelog
