#
# spec file for package droidcam
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


Name:           droidcam
Version:        1.9.0
Release:        0
Summary:        Program to turn a mobile device into a webcam
License:        GPL-2.0-or-later
URL:            https://www.dev47apps.com/droidcam/linux/
Source0:        https://github.com/aramg/droidcam/archive/v%{version}.tar.gz#/droidcam-%{version}.tar.gz
Source1:        README-v4l2loopback.md
# PATCH-FIX-OPENSUSE
Patch2:         0003-Hack-backwards-compatibility-for-TurboJPEG-2.0.0.patch
# PATCH-FIX-OPENSUSE
Patch3:         0001-Use-icon-installed-to-theme-directory.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libswscale)
# libusbmuxd 2.0.2 provides libusbmuxd-2.0, while 1.x/2.0.1 provide libusbmuxd
# BuildRequires:  pkgconfig(libusbmuxd-2.0)
BuildRequires:  libusbmuxd-devel
BuildRequires:  pkgconfig(speex)
Requires:       hicolor-icon-theme >= 0.17
Requires:       kmod(v4l2loopback.ko)
# USB connection uses adb for Android, other
# options are usbmuxd (iOS) or Wifi
Recommends:     adb

%description
This program turns a mobile device into a webcam.

It can be used with chat programs like Skype, Zoom, Teams, or with
live streaming programs like OBS.

%package cli
Summary:        Command line client for droidcam
Requires:       kmod(v4l2loopback.ko)
Recommends:     adb

%description cli
This program turns a mobile device into a webcam.

It can be used with chat programs like Skype, Zoom, Teams, or with
live streaming programs like OBS.

%prep
%autosetup -p1

%build
export USBMUXDLIBS="`pkg-config --silence-errors --libs libusbmuxd-2.0 || pkg-config --silence-errors --libs libusbmuxd`"
# CC is used for CXXFLAGS
%make_build JPEG="-lturbojpeg" USBMUXD=${USBMUXDLIBS} CFLAGS="%{optflags}" droidcam-cli
%make_build JPEG="-lturbojpeg" USBMUXD=${USBMUXDLIBS} CFLAGS="%{optflags}" droidcam

%install
install -D -m 755 -t %{buildroot}%{_bindir} droidcam-cli
install -D -m 755 -t %{buildroot}%{_bindir} droidcam
install -D -m 755 icon2.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/droidcam.png
%suse_update_desktop_file -c droidcam droidcam "Virtual Webcam" droidcam droidcam Multimedia Video GTK Utility AudioVideo
cp %{S:1} ./

%files
%license LICENSE
%doc README-v4l2loopback.md
%{_bindir}/droidcam
%{_datadir}/icons/hicolor/*/apps/droidcam.png
%{_datadir}/applications/droidcam.desktop

%files cli
%license LICENSE
%doc README-v4l2loopback.md
%{_bindir}/droidcam-cli

%changelog
