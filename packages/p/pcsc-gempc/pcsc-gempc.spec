#
# spec file for package pcsc-gempc
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


Name:           pcsc-gempc
%define _name ifd-gempc
BuildRequires:  libusb-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
Version:        1.0.8
Release:        0
Url:            http://ludovic.rousseau.free.fr/softwares/ifd-GemPC/
Summary:        PCSC driver for the Gemplus GemPC 410/430 smartcard readers
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Security
Source:         http://ludovic.rousseau.free.fr/softwares/ifd-GemPC/%{_name}-%{version}.tar.gz
Source1:        http://ludovic.rousseau.free.fr/softwares/ifd-GemPC/%{_name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE pcsc-gempc-1.0.0-devname.diff okir@suse.de -- Use standard device nodes.
Patch:          %{_name}-1.0.0-devname.diff
# PATCH-FIX-OPENSUSE pcsc-gempc-makefile.diff mjancar@suse.cz -- Fix build environment.
Patch1:         %{_name}-1.0.0-makefile.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       pcsc-lite
Supplements:    modalias(usb:v08E6p0430d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08E6p0432d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08E6p0435d*dc*dsc*dp*ic*isc*ip*)
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
This package contains a driver for the GemPC 410 and GemPC 430 smart
card readers produced by Gemplus.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup -q -n %{_name}-%{version}
%patch
%patch1
mv README.410 README_410
mv README.430 README_430
for DIR in GemPC410 GemPC430 ; do
    for FILE in $DIR/COPYING* $DIR/TODO* ; do
	SUFFIX=.${FILE##*.}
	if test "$SUFFIX" = ".$FILE" ; then
	    SUFFIX=
	fi
	mv $FILE ${FILE%.*}${DIR#GemPC}$SUFFIX
    done
done

%build
make %{?jobs:-j%jobs} CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changelog README* Gem*/COPYING* Gem*/TODO*
%{ifddir}/ifd*
%{ifddir}/serial/*
# FIXME: Maybe should be a part of pcsc-lite:
%dir %{ifddir}/serial

%changelog
