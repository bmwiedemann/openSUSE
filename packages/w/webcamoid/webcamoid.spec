#
# spec file for package webcamoid
#
# Copyright (c) 2022 SUSE LLC
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


Name:           webcamoid
Version:        9.0.0
Release:        0
Summary:        Webcam applet for Plasma
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://webcamoid.github.io/
Source:         https://github.com/hipersayanX/Webcamoid/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM webcamoid-manpath.patch
Patch0:         webcamoid-manpath.patch
# PATCH-FIX-UPSTREAM https://github.com/webcamoid/webcamoid/pull/560
Patch1:         webcamoid-ffmpeg5.patch
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-filesystem
BuildRequires:  libqt5-linguist
BuildRequires:  perl-Text-Markdown
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent) >= 5.15
BuildRequires:  cmake(Qt5Core) >= 5.15
BuildRequires:  cmake(Qt5DBus) >= 5.15
BuildRequires:  cmake(Qt5OpenGL) >= 5.15
BuildRequires:  cmake(Qt5QuickControls2) >= 5.15
BuildRequires:  cmake(Qt5Svg) >= 5.15
BuildRequires:  pkgconfig(libavcodec) >= 58.7.100
BuildRequires:  pkgconfig(libavdevice) >= 57.0.0
BuildRequires:  pkgconfig(libavformat) >= 58.0.102
BuildRequires:  pkgconfig(libavutil) >= 56.6.100
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libswscale) >= 5.0.101
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(vlc-plugin)
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
Provides:       plasmoid-webcamoid = %{version}
Obsoletes:      plasmoid-webcamoid < %{version}

%description
Webcam applet for Plasma.

Features:
* Take pictures with the webcam.
* Record videos.
* Manages multiple webcams.
* Play/Stop capture, this saves resources while the applet is not in use.
* Written in C++.
* Qt based software.
* Custom controls for each webcam.
* Popup applet support (you can embed Webcamoid in the panel).
* +50 video effects available.
* Effects with live previews.
* Translated to many languages.
* Stand alone installation mode (use it as a normal program).
* Use custom network and local files as capture devices.
* Capture from desktop.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

# generate help file
Markdown.pl --html4 ../README.md > ../README.html

%install
%cmake_install

%{kf5_post_install}

%fdupes %{buildroot}%{_datadir}

rm %{buildroot}%{_libdir}/libavkys.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog README.html THANKS
%license COPYING
%{_bindir}/%{name}
%{_kf5_applicationsdir}/%{name}.desktop
%{_libdir}/libavkys.so.*
%dir %{_libdir}/avkys
%{_libdir}/avkys/*.so
%{_kf5_mandir}/man1/%{name}.1%{ext_man}
%{_kf5_iconsdir}/hicolor

%changelog
