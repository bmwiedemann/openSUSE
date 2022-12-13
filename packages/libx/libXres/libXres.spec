#
# spec file for package libXres
#
# Copyright (c) 2022 SUSE LLC
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


%define lname	libXRes1
Name:           libXres
Version:        1.2.2
Release:        0
Summary:        X Resource extension client library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXRes
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXRes/
Source:         https://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(resourceproto) >= 1.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
libXRes provides an X Window System client interface to the Resource
extension to the X protocol. The Resource extension allows for X
clients to see and monitor the X resource usage of various clients
(pixmaps, et al).

%package -n %{lname}
Summary:        X Resource extension client library
Group:          System/Libraries

%description -n %{lname}
libXRes provides an X Window System client interface to the Resource
extension to the X protocol. The Resource extension allows for X
clients to see and monitor the X resource usage of various clients
(pixmaps, et al).

%package devel
Summary:        Development files for the X Resource extension library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libXRes provides an X Window System client interface to the Resource
extension to the X protocol. The Resource extension allows for X
clients to see and monitor the X resource usage of various clients
(pixmaps, et al).

This package contains the development headers for the library found
in %{lname}.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/libXRes.so.1*

%files devel
%{_includedir}/X11/*
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
%{_mandir}/man3/*

%changelog
