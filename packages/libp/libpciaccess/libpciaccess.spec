#
# spec file for package libpciaccess
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


Name:           libpciaccess
%define lname	libpciaccess0
Version:        0.18.1
Release:        0
Summary:        Generic PCI access library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://cgit.freedesktop.org/xorg/lib/libpciaccess/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libpciaccess
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libpciaccess/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
Patch0:         u_libpciaccess-vgaarb-add-function-to-get-default-vga-device-and-it.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(zlib)

%description
Provides functionality for X to access the PCI bus and devices in a
platform-independent way.

%package -n %lname
Summary:        Generic PCI access library
Group:          System/Libraries

%description -n %lname
Provides functionality for X to access the PCI bus and devices in a
platform-independent way.

%package devel
Summary:        Development files for the Generic PCI access library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       libpciaccess0-devel = 7.6_%version-%release
Obsoletes:      libpciaccess0-devel < 7.6_%version-%release

%description devel
Provides functionality for X to access the PCI bus and devices in a
platform-independent way.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -p1

%build
%meson -Dpci-ids=%_datadir
%meson_build

%install
%meson_install

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libpciaccess.so.0*

%files devel
%defattr(-,root,root)
%_includedir/pciaccess.h
%_libdir/libpciaccess.so
%_libdir/pkgconfig/pciaccess.pc

%changelog
