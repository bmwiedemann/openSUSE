#
# spec file for package rpi-imager
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           rpi-imager
Version:        2.0.6
Release:        0
Summary:        Raspberry Pi Imaging Utility
License:        Apache-2.0
Group:          Hardware/Other
URL:            https://github.com/raspberrypi/rpi-imager
Source:         https://github.com/raspberrypi/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         remove-vendoring.patch
# QML: fix property name mismatch in ImFileDialog
# https://github.com/raspberrypi/rpi-imager/pull/1505
Patch1:         1505.patch
# Fix GenerateTimezones.cmake FALLBACK_FILE path
# https://github.com/raspberrypi/rpi-imager/pull/1514
Patch2:         1514.patch
# Add missing import to WritingStep.qml
# https://github.com/raspberrypi/rpi-imager/pull/1515
Patch3:         1515.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libarchive-devel >= 3.8.0
BuildRequires:  libcurl-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  lzma-devel
BuildRequires:  qt6-concurrent-devel
BuildRequires:  qt6-core-devel
BuildRequires:  qt6-dbus-devel
BuildRequires:  qt6-linguist-devel
BuildRequires:  qt6-quick-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  qt6-widgets-devel
BuildRequires:  util-linux-systemd
Requires:       dosfstools
Requires:       udisks2
Requires:       util-linux-systemd
Recommends:     polkit-gnome
ExcludeArch:    s390x

%description
Raspberry Pi Imager is the quick and easy way to install Raspberry Pi OS and
other operating systems to a microSD card, ready to use with your Raspberry
Pi. Watch our 45-second video to learn how to install an operating system
using Raspberry Pi Imager.

Download and install Raspberry Pi Imager to a computer with an SD card reader.
Put the SD card you'll use with your Raspberry Pi into the reader and run
Raspberry Pi Imager.

NOTE: Relies on polkit when run as regular user. It doesn't have to be
      polkit-gnome, but it has a low install base overhead.

%prep
%autosetup -p1

%build
pushd src
%cmake \
    -DIMAGER_VERSION_STR=%{version} \
    -DENABLE_CHECK_VERSION=OFF \
    -DENABLE_TELEMETRY=OFF \
    -DENABLE_VENDORING=OFF
%cmake_build
popd

%install
pushd src
%cmake_install
popd

%files
%doc README.md
%license license.txt
%{_bindir}/rpi-imager
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/metainfo/*

%changelog
