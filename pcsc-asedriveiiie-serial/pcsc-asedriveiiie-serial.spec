#
# spec file for package pcsc-asedriveiiie-serial
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


Name:           pcsc-asedriveiiie-serial
%define _name asedriveiiie-serial
Summary:        ASEDrive IIIe Serial Smartcard Reader Driver
License:        BSD-3-Clause
Group:          Productivity/Security
Version:        3.7
Release:        0
Url:            http://www.asedrive.com/downloads
# Original upstream file name: asedriveiiie-serial-3-7-tar.bz cannot be processed by setup.
Source:         %{_name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
Requires:       pcsc-lite
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
This package contains a driver for the ASEDrive IIIe Serial smart card
reader.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup -q -n %{_name}-%{version}
chmod -x ChangeLog LICENSE README

%build
%configure
make %{?jobs:-j%jobs} CC="%__cc" LD="%__ld" CPP="%__cpp" CXX="%__cxx"

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE README
%{ifddir}/ifd-ASEDriveIIIe-Serial

%changelog
