#
# spec file for package pcsc-eco5000
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


Name:           pcsc-eco5000
%define _name eco5000
BuildRequires:  libtool
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
Version:        1.2.0
Release:        0
Group:          Productivity/Security
License:        GPL-2.0-or-later
URL:            http://www.cardcontact.de/download/driverdownload.html
Summary:        PC/SC IFD Handler for the ECO 5000 Serial Smart Card Reader
Source:         %{_name}-%{version}.tar.bz2
Patch0:         pcsc-eco5000-fix-compile-gcc14.patch
Patch1:         pcsc-eco5000-clean-warnings.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       pcsc-lite
%define ifddir %(pkg-config --variable=usbdropdir libpcsclite)

%description
Driver for the ECO 5000 Serial Smart Card Reader.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

This interface allows access to the terminal using the Card Terminal
Basic Command Set (CT-BCS). This driver also includes the support for
memory cards, exposed as Interindustry Command Set for Synchronous
Cards.

The CT-API driver supports the IFD Handler interface from PC/SC.

Please take a look in the included README document for further
information.

This driver only works with the serial interface version of the ECO
5000. ORGA also sells a USB version, that is incompatible with the
serial version. This driver will not work with the USB version!

%package devel
Summary:        PC/SC IFD Handler for the ECO 5000 Serial Smart Card Reader
Group:          Productivity/Security
Requires:       %{name} = %{version}

%description devel
Driver for the ECO 5000 Serial Smart Card Reader.


Authors:
--------
    Frank Thater <frank@thater-online.de>
    Andreas Schwier <andreas.schwier@cardcontact.de>

%prep
%setup -q -n %{_name}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1

%build
autoreconf -f -i
%configure\
	--libdir=%{ifddir}\
	--disable-static
make %{?jobs:-j%jobs}

%install
%makeinstall
rm $RPM_BUILD_ROOT%{ifddir}/*.la
# Unwanted generic header:
rm $RPM_BUILD_ROOT%{_includedir}/ctapi.h
rmdir $RPM_BUILD_ROOT%{_includedir}

%check
%make_build check

%files
%defattr(-,root,root)
%doc AUTHORS  ChangeLog NEWS README README.html
%license COPYING
%{ifddir}/libcteco5000.so.0.0.0
%{ifddir}/libcteco5000.so.0

%files devel
%{ifddir}/libcteco5000.so

%changelog
