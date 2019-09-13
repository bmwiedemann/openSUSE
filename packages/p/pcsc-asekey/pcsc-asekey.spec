#
# spec file for package pcsc-asekey
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pcsc-asekey
%define _name asekey
Summary:        ASEKey USB Token Driver
License:        BSD-3-Clause
Group:          Productivity/Security
Version:        3.7
Release:        0
%define tar_version %(echo %{version} | tr . -)
Url:            http://www.asedrive.com/downloads
Source:         %{_name}-%{tar_version}-tar.bz2
# PATCH-FIX-OPENSUSE pcsc-asekey-no-duplicated-install.patch sbrabec@suse.com -- Do not install driver twice. Keep only the one used by current pcsc-lite.
Patch1:         pcsc-asekey-no-duplicated-install.patch
# PATCH-FIX-OPENSUSE pcscd-group-no-longer-exist.patch -- specified group 'pcscd' unknown, pcscd is started as root.
Patch2:         pcscd-group-no-longer-exist.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libusb-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
BuildRequires:  udev
Requires:       pcsc-lite
Supplements:    modalias(usb:v0DC3p1701d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0DC3p1702d*dc*dsc*dp*ic*isc*ip*)
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)
%if %( echo `rpm -q --queryformat %%{version} udev` ) > 190
%define _udevrulesdir %{_libexecdir}/udev/rules.d
%else
%define _udevrulesdir /lib/udev/rules.d
%endif

%description
This package contains a driver for the ASEKey USB Token.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup -q -n %{_name}-%{version}
%patch1 -p1
%patch2 -p1

%build
%configure\
	--with-udev-rules-dir=%{_udevrulesdir}
make %{?jobs:-j%jobs} CC="%__cc" LD="%__ld" CPP="%__cpp" CXX="%__cxx"

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE README
%{ifddir}/ifd-ASEKey.bundle
%{_udevrulesdir}/*.rules

%changelog
