#
# spec file for package deepin-screen-recorder
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


%define    procps_version    %(rpm -q --queryformat '%%{VERSION}' procps-devel)

Name:           deepin-screen-recorder
Version:        5.11.6
Release:        0
Summary:        Deepin Screen Recorder
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://github.com/linuxdeepin/deepin-screen-recorder
Source0:        https://github.com/linuxdeepin/deepin-screen-recorder/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-include-path.patch hillwood@opensuse.org - Add ffmpeg include path
Patch0:         fix-include-path.patch
# PATCH-FIX-UPSTREAM fix-reture-type.patch hillwood@opensuse.org
Patch1:         fix-reture-type.patch
# fdupes macro works
Source1:        %{name}-rpmlintrc
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  deepin-dock
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  procps-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(opencv4)
%else
BuildRequires:  pkgconfig(opencv)
%endif
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(libimagevisualresult)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l1)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xtst)
Recommends:     %{name}-lang
Requires:       byzanz
Requires:       ffmpeg
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
deepin-screen-recorder is free and open source software for screen recording.

%package -n deepin-dock-plugin-screen-recorder
Summary:        The screen recorder plugin of deepin dock
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       %{name} = %{version}
Requires:       deepin-dock

%description -n deepin-dock-plugin-screen-recorder
The deepin screen recorder plugin of deepin dock

%package -n deepin-dock-plugin-shot-start
Summary:        The shot start plugin of deepin dock
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       %{name} = %{version}
Requires:       deepin-dock

%description -n deepin-dock-plugin-shot-start
The shot start of deepin dock

%lang_package

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '/#include<opencv2/i #include <opencv2/imgproc/types_c.h>' src/utils/pixmergethread.h
%if 0%{?suse_version} > 1500
sed -i 's/dframeworkdbus/dframeworkdbus opencv4/' src/src.pro
%else
sed -i 's/dframeworkdbus/dframeworkdbus opencv/' src/src.pro
%endif
sed -i '/include <X11.extensions.XTest.h>/a #undef min' src/event_monitor.cpp
# sed -i '/#include <iostream>/d;1i #include <iostream>' src/screen_shot_event.cpp
# sed -i '/include <X11.extensions.shape.h>/a #undef None' src/utils.cpp
sed -i 's|/usr/lib|$$LIB_INSTALL_DIR|g' src/dde-dock-plugins/recordtime/recordtime.pro \
src/dde-dock-plugins/shotstart/shotstart.pro
sed -i "s^cat /etc/os-version | grep 'Community'^echo 'Community'^" src/src.pro

%if "%{procps_version}" >= "4.0.0"
sed -i '/find_library/s|procps|proc-2|' src/CMakeLists.txt
%endif

%build
%qmake5 LIB_INSTALL_DIR=%{_libdir} \
        lupdate=/usr/bin/lupdate-qt5 \
        lrelease=/usr/bin/lrelease-qt5
%make_build

%install
%qmake5_install

%fdupes %{buildroot}%{_datadir}

find %{buildroot}%{_datadir}/deepin-manual -name '*.svg' -type f -print -exec chmod -x {} \;
find %{buildroot}%{_datadir}/deepin-manual -name '*.md' -type f -print -exec chmod -x {} \;
chmod -x %{buildroot}%{_datadir}/dbus-1/services/com.deepin.PinScreenShots.service

%suse_update_desktop_file %{name}

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/deepin-pin-screenshots
%{_datadir}/applications/*.desktop
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/dbus-1/services/com.deepin.PinScreenShots.service
%{_datadir}/dbus-1/services/com.deepin.ScreenRecorder.service
%{_datadir}/dbus-1/services/com.deepin.Screenshot.service
%{_datadir}/deepin-manual/manual-assets/application/%{name}

%files -n deepin-dock-plugin-screen-recorder
%{_libdir}/dde-dock/plugins/libdeepin-screen-recorder-plugin.so

%files -n deepin-dock-plugin-shot-start
%{_libdir}/dde-dock/plugins/libshot-start-plugin.so
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.module.shot-start-plugin.gschema.xml

%files lang
%{_datadir}/%{name}
# %{_datadir}/deepin-pin-screenshots

%changelog
