#
# spec file for package pcsc-ccid
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


Name:           pcsc-ccid
%define _name ccid
Version:        1.6.0
Release:        0
Summary:        PCSC Driver for CCID Based Smart Card Readers and GemPC Twin Serial Reader
License:        LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://ccid.apdu.fr/
Source:         https://ccid.apdu.fr/files/%{_name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        https://ccid.apdu.fr/files/%{_name}-%{version}.tar.xz.asc
Source3:        %{name}.keyring
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  libusb-1_0-devel
BuildRequires:  meson
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(udev)
# openSUSE package pcsc-lite 1.6.6 is the first one which creates the scard UID and GID:
Requires:       pcsc-lite >= 1.6.6
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)
%define LBRACE (
%define RBRACE )
%define QUOTE "
%define BACKSLASH \\
%define USBDRIVERS %(set -x ; xz -d <%{S:0} | tr a-z A-Z | sed -n 's/^ATTRS{IDVENDOR}==%{QUOTE}%{BACKSLASH}%{LBRACE}[^%{QUOTE}]*%{BACKSLASH}%{RBRACE}%{QUOTE}, ATTRS{IDPRODUCT}==%{QUOTE}%{BACKSLASH}%{LBRACE}[^%{QUOTE}]*%{BACKSLASH}%{RBRACE}%{QUOTE}.*$/modalias%{LBRACE}usb:v%{BACKSLASH}1p%{BACKSLASH}2d*dc*dsc*dp*ic*isc*ip*%{RBRACE}/p' | tr '%{BACKSLASH}n' ' ')
# We are not using Supplements here. User may want to choose between pcsc-lite and openct:
# Generic CCID devices:
Enhances:       modalias(usb:*ic0Bisc00d*dc*dsc*dp*ic*isc*ip*)
# Kobil mIDentity:
Enhances:       modalias(usb:v0D46p4081d*dc*dsc*dp*ic*isc*ip*)
# Other supported devices:
Enhances:       %USBDRIVERS
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a generic USB CCID (Chip/Smart Card Interface
Devices) driver.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%autosetup -n %{_name}-%{version}
cp -a src/openct/LICENSE LICENSE.openct
cp -a src/towitoko/README README.towitoko

%build
%meson	-Dserial=true \
        -Dzlp=true

%meson_build %{?_smp_mflags}

%install
%meson_install
## make DESTDIR=%{buildroot} install %{?_smp_mflags}
# Copied elsewhere:
mkdir -p %{buildroot}/%{_udevrulesdir}
sed 's:GROUP="pcscd":GROUP="scard":' <src/92_pcscd_ccid.rules >%{buildroot}/%{_udevrulesdir}/92_pcscd_ccid.rules

%files
%defattr(-,root,root)
# NEWS is empty
%doc AUTHORS README.md contrib/Kobil_mIDentity_switch/README_Kobil_mIDentity_switch.txt SCARDGETATTRIB.md
%license COPYING LICENSE.openct
%config (noreplace) %{_sysconfdir}/reader.conf.d/*
%{ifddir}/*
%{_udevrulesdir}/*.rules

%changelog
