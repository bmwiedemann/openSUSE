#
# spec file for package libXxf86vm
#
# Copyright (c) 2024 SUSE LLC
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


%define lname	libXxf86vm1
Name:           libXxf86vm
Version:        1.1.6
Release:        0
Summary:        XFree86-VidMode X extension library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXxf86vm
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXxf86vm/
Source:         https://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  grep
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86vidmodeproto) >= 2.2.99.1
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)

%description
These functions provide aninterface to the server extension
XFree86-VidModeExtension which allows the video modes to be queried
and adjusted dynamically and mode switching to be controlled.

%package -n %{lname}
Summary:        XFree86-VidMode X extension library
Group:          System/Libraries

%description -n %{lname}
These functions provide aninterface to the server extension
XFree86-VidModeExtension which allows the video modes to be queried
and adjusted dynamically and mode switching to be controlled.

%package devel
Summary:        Development files for the XFree86-VidMode X extension library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
These functions provide aninterface to the server extension
XFree86-VidModeExtension which allows the video modes to be queried
and adjusted dynamically and mode switching to be controlled.

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
%fdupes %{buildroot}/%{_prefix}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/libXxf86vm.so.1*

%files devel
%{_includedir}/X11/*
%{_libdir}/libXxf86vm.so
%{_libdir}/pkgconfig/xxf86vm.pc
%{_mandir}/man3/*

%changelog
