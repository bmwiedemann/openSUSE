#
# spec file for package alsa-scarlett-gui
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

Name:           alsa-scarlett-gui
Version:        0.5.1
Release:        0
Summary:        ALSA Scarlett Gen 2/3/4 Control Panel
License:        GPL-3.0-or-later or LGPL-3.0-or-later
URL:            https://github.com/geoffreybennett/alsa-scarlett-gui
Source:         https://github.com/geoffreybennett/alsa-scarlett-gui/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  alsa-devel
BuildRequires:  gtk4-devel
BuildRequires:  libopenssl-devel
# Focusrite Scarlett Gen 1
Supplements:    modalias(usb:v1235p8002*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8004*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p800c*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8012*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8014*dc*dsc*dp*ic*isc*ip*in*)
# Focusrite Scarlett Gen 2
Supplements:    modalias(usb:v1235p8201*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8203*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8204*dc*dsc*dp*ic*isc*ip*in*)
# Focusrite Clarett USB
Supplements:    modalias(usb:v1235p8206*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8207*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8208*dc*dsc*dp*ic*isc*ip*in*)
# Focusrite Clarett+
Supplements:    modalias(usb:v1235p820a*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p820b*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p820c*dc*dsc*dp*ic*isc*ip*in*)
# Focusrite Scarlett Gen 3
Supplements:    modalias(usb:v1235p8210*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8211*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8212*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8213*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8214*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8215*dc*dsc*dp*ic*isc*ip*in*)
# Focusrite Vocaster
Supplements:    modalias(usb:v1235p8216*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8217*dc*dsc*dp*ic*isc*ip*in*)
# Focusrite Scarlett Gen 4
Supplements:    modalias(usb:v1235p8218*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p8219*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1235p821a*dc*dsc*dp*ic*isc*ip*in*)

%description
A Gtk4 GUI for the ALSA controls presented by the Linux kernel Focusrite Scarlett2 USB Protocol Mixer Driver.

%prep
%autosetup

%build
%make_build -C src PREFIX=%{_prefix}

%install
%make_install -C src PREFIX=%{_prefix}

DOC_DIRECTORY=%{buildroot}/%{_docdir}/%{name}
mkdir -p $DOC_DIRECTORY
mkdir $DOC_DIRECTORY/docs
mkdir $DOC_DIRECTORY/demo
mkdir $DOC_DIRECTORY/img
cp *.md $DOC_DIRECTORY
cp demo/* $DOC_DIRECTORY/demo
cp docs/* $DOC_DIRECTORY/docs
cp img/*  $DOC_DIRECTORY/img

%files
%license LICENSES/GPL-3.0-or-later.txt LICENSES/LGPL-3.0-or-later.txt
%{_bindir}/%{name}
%{_docdir}/%{name}
%{_datadir}/applications/vu.b4.alsa-scarlett-gui.desktop
%{_datadir}/icons/hicolor/256x256/apps/vu.b4.alsa-scarlett-gui.png

%changelog

