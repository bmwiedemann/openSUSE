#
# spec file for package pcsc-asedriveiiie-usb
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%if %( echo `rpm -q --queryformat %%{version} udev` ) > 190
%define _udevprefix /usr/lib
%else
%define _udevprefix /lib
%endif

Name:           pcsc-asedriveiiie-usb
%define _name asedriveiiie-usb
Summary:        ASEDrive IIIe USB Smart Card Reader Driver
License:        BSD-3-Clause
Group:          Productivity/Security
Version:        3.7
Release:        0
%define tar_version %(echo %{version} | tr . -)
Url:            http://www.asedrive.com/downloads
Source:         %{_name}-%{tar_version}-tar.bz2
# PATCH-FIX-OPENSUSE asedriveiiie-usb-destdir.patch sbrabec@suse.cz -- Fix destdir installation.
Patch1:         asedriveiiie-usb-destdir.patch
Patch2:         pcscd-group-no-longer-exist.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libusb-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
# for directory ownership
BuildRequires:  udev
Requires:       pcsc-lite
Supplements:    modalias(usb:v0DC3p0802d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0DC3p1104d*dc*dsc*dp*ic*isc*ip*)
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
This package contains a driver for the ASEDrive IIIe USB smart card
reader.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup -q -n %{_name}-%{version}
chmod -x ChangeLog LICENSE README
%patch1 -p1
%patch2 -p1

%build
%configure
make %{?jobs:-j%jobs} CC="%__cc" LD="%__ld" CPP="%__cpp" CXX="%__cxx"

%install
%makeinstall
# Move udev rules provided by packages to %%{_udevprefix}
mkdir -p $RPM_BUILD_ROOT%{_udevprefix}/
mv $RPM_BUILD_ROOT/etc/udev $RPM_BUILD_ROOT%{_udevprefix}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE README
%{ifddir}/ifd-ASEDriveIIIe-USB.bundle
%{_udevprefix}/udev/rules.d/*.rules

%changelog
