#
# spec file for package pcsc-cyberjack
#
# Copyright (c) 2021 SUSE LLC
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


%if %suse_version >= 1120
%if %( pkg-config --modversion udev ) > 190
%define _udevrulesdir /usr/lib/udev/rules.d
%else
%define _udevrulesdir /lib/udev/rules.d
%endif
%endif

Name:           pcsc-cyberjack
Version:        3.99.5final.SP14
Release:        0
URL:            https://www.reiner-sct.com/support/support-anfrage/?productGroup=77304735&product=77304820&q=driver&os=Linux#choice5
Summary:        PC/SC IFD Handler for the Reiner SCT Cyberjack USB-SmartCard Readers
License:        LGPL-2.1-or-later
Group:          Productivity/Security
Source:         https://support.reiner-sct.de/downloads/LINUX/V3.99.5_SP14/%{name}_%{version}.tar.gz
Source1:        %{name}-README.SUSE
Source2:        40-cyberjack.rules
Patch1:         ctapi-cyberjack-configure.patch
Patch2:         no-checksuite.patch
Patch3:         no-libdialog.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define ifddir %(pkg-config --variable=usbdropdir libpcsclite)
BuildRequires:  distribution-release
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
%if %suse_version >= 1120
BuildRequires:  libusb-1_0-devel
BuildRequires:  pkgconfig(udev)
%else
BuildRequires:  hal-devel
BuildRequires:  libusb-devel
%endif
Supplements:    modalias(usb:v0C4Bp0100d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0300d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0400d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0401d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0412d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0485d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0500d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0501d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0502d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0503d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0504d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0505d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0506d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0507d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0525d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0580d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp2000d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp0551d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0C4Bp2002d*dc*dsc*dp*ic*isc*ip*)
Requires:       pcsc-lite

%description
This package includes the PC/SC IFD handler for the Reiner SCT
Cyberjack pinpad/e-com/RFID USB chipcard readers.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.


%prep
%setup -q
cp -a %{S:1} README.SUSE
%patch1
%patch2 -p1
%patch3 -p1

# unused at the moment; avoid adding GPL as a license
rm -rf libcyberjack checksuite
mkdir -p libcyberjack
cat <<EOF > libcyberjack/Makefile.in
all:
install:
EOF

%build
ACLOCAL="aclocal -I m4" autoreconf -f -i
%configure\
	--disable-static\
	--enable-release\
	--with-usbdropdir=%{ifddir}
make %{?_smp_mflags}

%install
%makeinstall
mkdir -p %{buildroot}/%{_udevrulesdir}
install %{SOURCE2} %{buildroot}/%{_udevrulesdir}
# clean up
mv %{buildroot}/%{_sysconfdir}/cyberjack.conf{.default,}
# exclude
rm -rf %{buildroot}/%{_sysconfdir}/hal/fdi/policy/10osvendor/80-cyberjack.fdi
rm -rf %{buildroot}/%{_libdir}/cyberjack/pcscd_init.diff
chmod a-x %{buildroot}%{_udevrulesdir}/*

%files
%defattr(-,root,root)
%doc COPYRIGHT.LGPL doc/README.* README.SUSE doc/LIESMICH.*
%dir %{ifddir}
%{ifddir}/libifd-cyberjack.bundle
%config(noreplace) %{_sysconfdir}/cyberjack.conf
%{_udevrulesdir}/*

%changelog
