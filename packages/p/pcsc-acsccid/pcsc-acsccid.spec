#
# spec file for package pcsc-acsccid
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Advanced Card Systems Ltd.
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


%if 0%{?suse_version} >= 1140
%if %( pkg-config --modversion udev ) > 190
%define _udevrulesdir /usr/lib/udev/rules.d
%else
%define _udevrulesdir /lib/udev/rules.d
%endif
%endif

%if 0%{?sles_version} == 11
%define libusb_ver 1.0.8
%define pcsc_lite_ver 1.4.102
%else
%define libusb_ver 1.0.9
%define pcsc_lite_ver 1.8.3
%endif

Name:           pcsc-acsccid
%define _name acsccid
BuildRequires:  flex
BuildRequires:  libusb-1_0-devel >= %{libusb_ver}
BuildRequires:  pcsc-lite-devel >= %{pcsc_lite_ver}
BuildRequires:  pkg-config
%if 0%{?suse_version} >= 1140
BuildRequires:  pkgconfig(udev)
%endif
Version:        1.1.11
Release:        0
URL:            http://acsccid.sourceforge.net/
Summary:        PCSC Driver for ACS CCID Based Smart Card Readers
License:        LGPL-2.1-or-later
Group:          Productivity/Security
Source:         http://downloads.sourceforge.net/%{_name}/%{_name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
%if 0%{?sles_version} == 11
# PATCH-FIX-SLE acsccid-1.1.10-libhal.patch godfrey.chung@acs.com.hk -- Fix the compatibility with libhal.
Patch0:         %{_name}-1.1.10-libhal.patch
# PATCH-FIX-SLE acsccid-1.1.11-polling-thread.patch godfrey.chung@acs.com.hk -- Add polling thread support for slot status.
Patch1:         %{_name}-1.1.11-polling-thread.patch
# PATCH-FIX-SLE acsccid-1.1.11-polling-unplug.patch godfrey.chung@acs.com.hk -- Let pcsc-lite delay the polling if the reader is unplugged.
Patch2:         %{_name}-1.1.11-polling-unplug.patch
# PATCH-FIX-SLE acsccid-1.1.10-libusb-1.0.8.patch godfrey.chung@acs.com.hk -- Fix the compatibility with libusb 1.0.8.
Patch3:         %{_name}-1.1.10-libusb-1.0.8.patch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       pcsc-lite >= %{pcsc_lite_ver}
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

Enhances:       modalias(usb:v072FpB301d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB304d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB305d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8300d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8302d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8307d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8301d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp90CCd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp90D8d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB100d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB500d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB101d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB102d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB103d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB10Cd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB104d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB113d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB114d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB116d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB117d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB000d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB501d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB504d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB506d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB505d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp90D2d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8306d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2011d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8900d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8901d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8902d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp1205d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp1204d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp1206d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2200d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2214d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp1280d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2207d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp222Bd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2206d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp222Ed*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2237d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2219d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2203d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp221Ad*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2229d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp222Dd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2218d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp221Bd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2232d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2242d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2238d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp225Fd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp224Fd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp223Bd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp223Ed*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp223Dd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2244d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2259d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp225Bd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp225Cd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp226Bd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp226Ad*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp223Fd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2239d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2211d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2252d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2100d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2224d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp220Fd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2217d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2223d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2208d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp0901d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp220Ad*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2215d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2220d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2233d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2234d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2235d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2236d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2213d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp222Cd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp220Cd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2258d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2303d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2308d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2302d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2307d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2306d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp230Ad*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2309d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2301d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp2300d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp0102d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp0103d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp0100d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp224Ad*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8201d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8206d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8207d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8202d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp8205d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp90DBd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB200d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB106d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072FpB112d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp9000d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp90CFd*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp0101d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp9006d*dc*dsc*dp*ic*isc*ip*)
Enhances:       modalias(usb:v072Fp90CEd*dc*dsc*dp*ic*isc*ip*)

%description
This package contains a ACS USB CCID (Chip/Smart Card Interface
Devices) driver.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup -q -n %{_name}-%{version}
%if 0%{?sles_version} == 11
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%endif
cp -a src/openct/LICENSE LICENSE.openct
cp -a src/towitoko/README README.towitoko

%build
%if 0%{?sles_version} == 11
%configure \
    PCSC_CFLAGS="-I%{_builddir}/%{_name}-%{version}/MacOSX" \
    PCSC_LIBS="%(pkg-config --libs libpcsclite 2>/dev/null)" \
    --enable-composite-as-multislot
%else
%configure
%endif
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%if 0%{?suse_version} >= 1140
mkdir -p %{buildroot}/%{_udevrulesdir}
sed 's:GROUP="pcscd":GROUP="scard":' <src/92_pcscd_acsccid.rules >%{buildroot}/%{_udevrulesdir}/92_pcscd_acsccid.rules
%endif

%files
%defattr(-,root,root)
%if 0%{?suse_version} < 1500
%doc AUTHORS ChangeLog COPYING LICENSE.openct README README.towitoko
%else
%doc AUTHORS ChangeLog README README.towitoko
%license COPYING LICENSE.openct
%endif
%{ifddir}/*
%if 0%{?suse_version} >= 1140
%{_udevrulesdir}/*.rules
%endif

%changelog
