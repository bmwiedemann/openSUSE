#
# spec file for package qrencode
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_ver 4
Name:           qrencode
Version:        4.1.0
Release:        0
Summary:        C library for encoding data in a QR Code symbol
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Other
Url:            https://github.com/fukuchi/libqrencode
Source0:        https://fukuchi.org/works/qrencode/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  cmake >= 3.1.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpng)

%description
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robust.

%package -n libqrencode%{so_ver}
Summary:        C library for encoding data in a QR Code symbol
Group:          System/Libraries

%description -n libqrencode%{so_ver}
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robust.

%package devel
Summary:        C library for encoding data in a QR Code symbol - Development files
Group:          Development/Libraries/C and C++
Requires:       libqrencode%{so_ver} = %{version}

%description devel
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robust.

This package contains the development files for libqrencode.

%prep
%setup -q

%build
%cmake -DBUILD_SHARED_LIBS=TRUE
%make_jobs

%install
%cmake_install

%post -n libqrencode%{so_ver} -p /sbin/ldconfig
%postun -n libqrencode%{so_ver} -p /sbin/ldconfig

%files
%license COPYING
%doc README TODO NEWS ChangeLog
%{_mandir}/man1/qrencode.1%{ext_man}
%{_bindir}/qrencode

%files -n libqrencode%{so_ver}
%{_libdir}/libqrencode.so.%{so_ver}*

%files devel
%{_includedir}/qrencode.h
%{_libdir}/libqrencode.so
%{_libdir}/pkgconfig/libqrencode.pc

%changelog
