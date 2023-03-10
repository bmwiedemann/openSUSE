#
# spec file for package rpi-imager
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.7.4
Release:        0
Summary:        Raspberry Pi Imaging Utility
License:        Apache-2.0
Group:          Hardware/Other
URL:            https://github.com/raspberrypi/rpi-imager
Source:         https://github.com/raspberrypi/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libqt5-qtquickcontrols2
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  util-linux-systemd
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickTest)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)

%description

Raspberry Pi Imager is the quick and easy way to install Raspberry Pi OS and other operating systems to a microSD card, ready to use with your Raspberry Pi. Watch our 45-second video to learn how to install an operating system using Raspberry Pi Imager.

Download and install Raspberry Pi Imager to a computer with an SD card reader. Put the SD card you'll use with your Raspberry Pi into the reader and run Raspberry Pi Imager.

%prep
%autosetup

%build
pushd src
%cmake -DENABLE_CHECK_VERSION=0 -DENABLE_TELEMETRY=0
%cmake_build

%install
pushd src
%cmake_install

mkdir -p %{buildroot}%{_datadir}/icons
cp icons/rpi-imager.png %{buildroot}%{_datadir}/icons/.

pwd
pushd linux
desktop-file-install --dir %{buildroot}%{_datadir}/applications/ rpi-imager.desktop
%suse_update_desktop_file rpi-imager -r Settings HardwareSettings
%suse_update_desktop_file rpi-imager -G Imager

%files
%doc README.md
%license license.txt
%{_bindir}/rpi-imager
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/metainfo/*

%changelog
