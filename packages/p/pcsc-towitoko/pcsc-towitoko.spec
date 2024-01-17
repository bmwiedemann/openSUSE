#
# spec file for package pcsc-towitoko
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


%define _name towitoko
%define scdir %(pkg-config libpcsclite --variable=usbdropdir)
Name:           pcsc-towitoko
Version:        2.0.8
Release:        0
Summary:        PCSC driver for Towitoko Smart Card Readers
License:        LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://github.com/cprados/towitoko-linux
Source:         https://github.com/cprados/towitoko-linux/archive/refs/tags/v%{version}.tar.gz
Patch1:         %{_name}-%{version}-install.diff
Patch2:         %{_name}-destdir.patch
Patch3:         towitoko-%{version}-implicit-decls.patch
BuildRequires:  libtool
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
Requires:       pcsc-lite
Supplements:    modalias(usb:v067Bp2303d*dc*dsc*dp*ic*isc*ip*)

%description
This package contains a driver for Towitoko Chipdrive Micro, Extern,
Extern II, Intern, and Twin and Kartenzwerg smart card readers.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

Please note, that many modern Towitoko readers are supported by the
openct package.

%package -n libtowitoko2
Summary:        Library for PCSC driver for Towitoko Smart Card Readers
Group:          System/Libraries

%description -n libtowitoko2
This package contains a driver for Towitoko Chipdrive Micro, Extern,
Extern II, Intern, and Twin and Kartenzwerg smart card readers.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

Please note, that many modern Towitoko readers are supported by the
openct package.

%package devel
Summary:        PCSC driver for Towitoko Smart Card Readers
Group:          Development/Libraries/C and C++
Requires:       libtowitoko2 = %{version}

%description devel
This package contains a driver for Towitoko Chipdrive Micro, Extern,
Extern II, Intern, and Twin and Kartenzwerg smart card readers.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

Please note, that many modern Towitoko readers are supported by the
openct package.

%prep
%setup -q -n %{_name}-linux-%{version}
%autopatch -p1

%build
autoreconf -f -i
%configure\
	--includedir=%{_includedir}/PCSC/towitoko\
	--with-pcsc-lite-dir=%{scdir}\
	--enable-win32-com\
	--enable-usb-bundle
%make_build

%install
%make_install
mv %{buildroot}%{_bindir}/tester %{buildroot}%{_bindir}/towitoko-tester

%post -n libtowitoko2 -p /sbin/ldconfig
%postun -n libtowitoko2 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/*
/%{scdir}/*

%files -n libtowitoko2
%{_libdir}/libtowitoko.so.2
%{_libdir}/libtowitoko.so.2.*

%files devel
%{_includedir}/PCSC/*
%{_libdir}/*.so
%{_libdir}/*.*a
%{_mandir}/man3/*.*

%changelog
