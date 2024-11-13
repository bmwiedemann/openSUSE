#
# spec file for package webcamoid
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


Name:           webcamoid
Version:        9.2.3
Release:        0
Summary:        Webcam applet for Plasma
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://webcamoid.github.io/
Source:         https://github.com/hipersayanX/Webcamoid/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM webcamoid-disable_autoupdate.patch
Patch0:         webcamoid-disable_autoupdate.patch
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flex
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc13-c++
%endif
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  perl-Text-Markdown
BuildRequires:  pkgconfig
BuildRequires:  qt6-tools-linguist
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(vlc-plugin)
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
export CXX=g++
test -x "$(type -p g++-13)" && export CXX=g++-13
%cmake_qt6 \
 -DPLUGINSDIR=%{_qt6_pluginsdir} \
 -DOUTPUT_QT_PLUGINS_DIR=%{_qt6_pluginsdir} \
 -DNOCHECKUPDATES=TRUE
%qt6_build

# generate help file
Markdown.pl --html4 README.md > README.html

%install
%qt6_install

rm %{buildroot}%{_libdir}/libavkys.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog README.html THANKS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/io.github.%{name}.Webcamoid.metainfo.xml
%{_datadir}/icons/hicolor
%{_libdir}/libavkys.so.*
%{_mandir}/man1/%{name}.1%{ext_man}
%{_qt6_pluginsdir}/avkys

%changelog
