#
# spec file for package droidcam
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.4
Release:        0
Summary:	Use a phone as a webcam device
License:        GPL-2.0-or-later
URL:            https://www.dev47apps.com/droidcam/linux/
Source:         https://github.com/aramg/droidcam/archive/v%{version}.tar.gz#/droidcam-%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Enhance-compatibility-with-upstream-v4l2loopback-dri.patch
# PATCH-FIX-OPENSUSE
Patch1:         0002-Accept-upstream-v4l2loopback-driver-as-device.patch
# PATCH-FIX-OPENSUSE
Patch2:         0003-Hack-backwards-compatibility-for-TurboJPEG-2.0.0.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libusbmuxd)
BuildRequires:  pkgconfig(speex)
Requires:       hicolor-icon-theme
Requires:       kmod(v4l2loopback.ko)
# USB connection uses adb for Android, other
# options are usbmuxd (iOS) or Wifi
Recommends:     adb

%description
Turns a mobile device into a webcam.

Use it with chat programs like Skype, Zoom, Teams, or with live
streaming programs like OBS.

%package cli
Summary:	Command line client for droidcam
Requires:       kmod(v4l2loopback.ko)
Recommends:     adb

%description cli
Turns a mobile device into a webcam.

Use it with chat programs like Skype, Zoom, Teams, or with live
streaming programs like OBS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
pushd linux
# CC is used for CXXFLAGS
%make_build JPEG="-lturbojpeg" CC="%{optflags} -std=c++11" droidcam-cli
%make_build JPEG="-lturbojpeg" CC="%{optflags} -std=c++11" droidcam
popd

%install
pushd linux
install -D -m 755 -t %{buildroot}%{_bindir} droidcam-cli
install -D -m 755 -t %{buildroot}%{_bindir} droidcam
install -D -m 755 icon2.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/droidcam.png
popd
%suse_update_desktop_file -c droidcam droidcam "Virtual Webcam" droidcam droidcam Multimedia Video GTK Utility AudioVideo

%files
%license linux/LICENCE
%doc linux/README.md
%{_bindir}/droidcam
%{_datadir}/icons/hicolor/*/apps/droidcam.png
%{_datadir}/applications/droidcam.desktop

%files cli
%license linux/LICENCE
%doc linux/README.md
%{_bindir}/droidcam-cli

%changelog
