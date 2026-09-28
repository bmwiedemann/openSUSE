#
# spec file for package libXi
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           libXi
%define lname   libXi6
Version:        1.8.3
Release:        0
Summary:        X Input Extension library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXi
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXi/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
Patch1:         0001-boo1281605_CVE-2026-93541_XQueryDeviceState-check-ValuatorClass-num_valuators-.patch
Patch2:         0002-boo1281606_CVE-2026-93542_size_classes-copy_classes-bound-XI2-class-lengths-to.patch
Patch3:         0003-boo1281608_CVE-2026-93543_size_classes-copy_classes-enforce-XI2-per-type-class.patch
Patch4:         0004-boo1281609_CVE-2026-93544_XIQueryDevice-keep-padded-name-and-class-bytes-withi.patch
Patch5:         0005-boo1281612_CVE-2026-93545_XListInputDevices-validate-device-name-lengths-again.patch
Patch6:         0006-boo1281615_CVE-2026-94281_XListInputDevices-validate-class-lengths-cumulativel.patch
Patch7:         0007-boo1281651_CVE-2026-94282_wireToEnterLeave-validate-buttons_len-against-the-re.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inputproto) >= 2.1.99.6
BuildRequires:  pkgconfig(x11) >= 1.4.99.1
BuildRequires:  pkgconfig(xext) >= 1.0.99.1
BuildRequires:  pkgconfig(xextproto) >= 7.0.3
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto) >= 7.0.13

%description
libXi is the client-side library for the X Input Extension.

%package -n %lname
Summary:        X Input Extension library
Group:          System/Libraries

%description -n %lname
libXi is the client-side library for the X Input Extension.

%package devel
Summary:        Development files for the X Input Extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       libXi6-devel = %version-%release
Obsoletes:      libXi6-devel < %version-%release

%description devel
libXi is the client-side library for the X Input Extension.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -p1

%build
%configure --docdir=%_docdir/%name --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXi.so.6*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXi.so
%_libdir/pkgconfig/xi.pc
%_docdir/%name
%_mandir/man3/*

%changelog
