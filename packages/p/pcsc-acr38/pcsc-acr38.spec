#
# spec file for package pcsc-acr38
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           pcsc-acr38
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
BuildRequires:  unzip
Version:        1.7.11
Release:        0
%define envelope_tar_version 101_P
%define tar_version 100711_P
Url:            http://www.acs.com.hk/drivers-manual.php?driver=ACR38
Summary:        PC/SC IFD Handler for the ACR38 Smart Card Reader
License:        GPL-2.0+
Group:          Productivity/Security
# This source is a zip that contains two tar files with drivers, one for
# non-CCID devices, one for CCID devices.
Source:         ACR38_Driver_Lnx_%{envelope_tar_version}.zip
Patch2:         ACR38_LINUX_100705_P-usb.diff
Patch3:         ACR38_LINUX_100710-automake-cleanup.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       pcsc-lite
Supplements:    modalias(usb:v072Fp9000d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v072Fp90CFd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v072Fp9006d*dc*dsc*dp*ic*isc*ip*)
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
This package contains a driver for the ACR 38 smart card reader
produced by ACS.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%package -n libacr38ucontrol0
Summary:        Library for PC/SC IFD Handler for the ACR38 Smart Card Reader
Group:          System/Libraries

%description -n libacr38ucontrol0
This package contains a driver for the ACR 38 smart card reader
produced by ACS.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%package devel
Summary:        PC/SC IFD Handler for the ACR38 Smart Card Reader
Group:          Development/Libraries/C and C++
Requires:       libacr38ucontrol0 = %{version}
Requires:       pcsc-lite-devel

%description devel
This package contains a driver for the ACR 38 smart card reader
produced by ACS.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup -q -c
cd non-ccid
tar -jxf ACR38_LINUX_%{tar_version}.tar.bz2
cd ACR38_LINUX_%{tar_version}
mv src/driver/Info.plist src/driver/Info.plist.in
%patch2
%patch3

%build
cd non-ccid/ACR38_LINUX_%{tar_version}
autoreconf -f -i
%configure\
	--disable-static
make %{?jobs:-j%jobs}

%install
cd non-ccid/ACR38_LINUX_%{tar_version}
%makeinstall
rm $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{ifddir}/*/*/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libacr38ucontrol0 -p /sbin/ldconfig

%postun -n libacr38ucontrol0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
# NEWS is empty
%doc non-ccid/ACR38_LINUX_%{tar_version}/AUTHORS non-ccid/ACR38_LINUX_%{tar_version}/COPYING non-ccid/ACR38_LINUX_%{tar_version}/ChangeLog non-ccid/ACR38_LINUX_%{tar_version}/README
%{ifddir}/*

%files -n libacr38ucontrol0
%defattr(-,root,root)
%{_libdir}/libacr38ucontrol.so.0
%{_libdir}/libacr38ucontrol.so.0.*

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
