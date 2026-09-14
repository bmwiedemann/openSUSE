#
# spec file for package droidcam
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


Name:           droidcam
Version:        2.1.5
Release:        0
Summary:        Use an Android/iOS device as a webcam on Linux
License:        GPL-2.0-or-later
URL:            https://www.dev47apps.com/droidcam/linux/
Source0:        droidcam-%{version}.tar.zst
# ---- Build-time dependencies ------------------------------------------------
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig

# Video / audio decoding (FFmpeg)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)

# JPEG decoding – system libturbojpeg, NOT the bundled /opt/libjpeg-turbo path
BuildRequires:  pkgconfig(libjpeg)

# ALSA audio
BuildRequires:  pkgconfig(alsa)

# Speex audio codec
BuildRequires:  pkgconfig(speex)

# iOS USB connectivity via usbmuxd
# libusbmuxd >= 2.0.2 exports "libusbmuxd-2.0"; older versions "libusbmuxd".
BuildRequires:  libusbmuxd-devel

# GTK3 GUI
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(x11)

# ---- Runtime dependencies ---------------------------------------------------
Requires:       kmod(v4l2loopback.ko)
Requires:       hicolor-icon-theme >= 0.17
Recommends:     adb
Recommends:     usbmuxd

%description
DroidCam turns an Android or iOS device into a wireless (or USB) webcam.
The virtual video device created by v4l2loopback is used by video-conferencing
and streaming applications (Skype, Zoom, Teams, OBS Studio, etc.).

This package installs the GTK3 GUI client (droidcam).
See the droidcam-cli sub-package for the command-line-only client.

%package cli
Summary:        Command-line client for DroidCam
Requires:       kmod(v4l2loopback.ko)
Recommends:     adb
Recommends:     usbmuxd

%description cli
DroidCam turns an Android or iOS device into a wireless (or USB) webcam.

This package installs only the command-line client (droidcam-cli), which
does not depend on GTK3.  Use it on headless systems or in terminal workflows.

# ---- Prep -------------------------------------------------------------------

%prep
%autosetup -n droidcam-%{version}

# ---- Build ------------------------------------------------------------------
%build
# Prefer libusbmuxd-2.0 (>= 2.0.2) pkg-config name; fall back to older name.
export USBMUXDLIBS="$(pkg-config --silence-errors --libs libusbmuxd-2.0 \
                      || pkg-config --silence-errors --libs libusbmuxd)"

%make_build \
    JPEG="-lturbojpeg" \
    USBMUXD="${USBMUXDLIBS}" \
    APPINDICATOR="ayatana-appindicator3-0.1" \
    CFLAGS="%{optflags} -DUSE_AYATANA_APPINDICATOR" \
    droidcam-cli

%make_build \
    JPEG="-lturbojpeg" \
    USBMUXD="${USBMUXDLIBS}" \
    APPINDICATOR="ayatana-appindicator3-0.1" \
    CFLAGS="%{optflags} -DUSE_AYATANA_APPINDICATOR" \
    droidcam

# ---- Install ----------------------------------------------------------------
%install
install -D -m 0755 droidcam-cli %{buildroot}%{_bindir}/droidcam-cli
install -D -m 0755 droidcam %{buildroot}%{_bindir}/droidcam
install -D -m 0644 icon2.png \
    %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/droidcam.png

%suse_update_desktop_file -c droidcam "DroidCam" "Use Android/iOS as a webcam" droidcam droidcam AudioVideo Video GTK

# ---- File lists -------------------------------------------------------------
%files
%license LICENSE
%doc README.md
%{_bindir}/droidcam
%{_datadir}/icons/hicolor/*/apps/droidcam.png
%{_datadir}/applications/droidcam.desktop

%files cli
%license LICENSE
%doc README.md
%{_bindir}/droidcam-cli

%changelog
