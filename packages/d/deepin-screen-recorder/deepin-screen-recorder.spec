#
# spec file for package deepin-screen-recorder
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           deepin-screen-recorder
Version:        5.8.1
Release:        0
Summary:        Deepin Screen Recorder
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/deepin-screen-recorder
Source0:        https://github.com/linuxdeepin/deepin-screen-recorder/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE deepin-screen-recorder-qt5.15.patch hillwood@opensuse.org - Support Qt 5.15+
Patch0:         %{name}-qt5.15.patch
Group:          Productivity/Multimedia/Video/Editors and Convertors
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  libqt5-linguist
BuildRequires:  gtest
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(libprocps)
Recommends:     %{name}-lang
Requires:       byzanz
Requires:       ffmpeg
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
deepin-screen-recorder is free and open source software for screen recording.

%lang_package

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '/include <X11.extensions.XTest.h>/a #undef min' src/event_monitor.cpp
sed -i '/#include <iostream>/d;1i #include <iostream>' src/screen_shot_event.cpp
sed -i '/include <X11.extensions.shape.h>/a #undef None' src/utils.cpp
sed -i 's|$$ETCDIR/modules-load.d|/usr/lib/modules-load.d|g' screen_shot_recorder.pro

%build
%qmake5 lupdate=/usr/bin/lupdate-qt5 \
        lrelease=/usr/bin/lrelease-qt5
%make_build

%install
%qmake5_install

rm %{buildroot}%{_sysconfdir}/modprobe.d/deepin-screen-recorder.conf \
%{buildroot}%{_prefix}/lib/modules-load.d/deepin-screen-recorder.conf

%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
# %config %{_sysconfdir}/modprobe.d/deepin-screen-recorder.conf
# %dir %{_sysconfdir}/modules-load.d
# %{_prefix}/lib/modules-load.d/deepin-screen-recorder.conf
%{_bindir}/%{name}
%dir %{_datadir}/dman
%{_datadir}/dman/%{name}/
%{_datadir}/applications/*.desktop
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/dbus-1/services/com.deepin.ScreenRecorder.service
%{_datadir}/dbus-1/services/com.deepin.Screenshot.service

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
