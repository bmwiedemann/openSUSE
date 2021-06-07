#
# spec file for package deepin-screen-recorder
#
# Copyright (c) 2021 SUSE LLC
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


Name:           deepin-screen-recorder
Version:        5.9.3
Release:        0
Summary:        Deepin Screen Recorder
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-screen-recorder
Source0:        https://github.com/linuxdeepin/deepin-screen-recorder/archive/%{version}/%{name}-%{version}.tar.gz
Group:          Productivity/Multimedia/Video/Editors and Convertors
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
BuildRequires:  update-desktop-files
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
BuildRequires:  pkgconfig(libprocps)
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
Requires:       %{name} = %{version}
Requires:       deepin-dock

%description -n deepin-dock-plugin-screen-recorder
The deepin screen recorder plugin of deepin dock

%lang_package

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '/include <X11.extensions.XTest.h>/a #undef min' src/event_monitor.cpp
sed -i '/#include <iostream>/d;1i #include <iostream>' src/screen_shot_event.cpp
sed -i '/include <X11.extensions.shape.h>/a #undef None' src/utils.cpp
sed -i 's|/usr/lib|$$LIB_INSTALL_DIR|g' src/dde-dock-plugins/recordtime/recordtime.pro

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

%suse_update_desktop_file %{name}

%files
%doc README.md CHANGELOG.md
%license LICENSE
%dir %{_sysconfdir}/due-shell
%dir %{_sysconfdir}/due-shell/json
%config %{_sysconfdir}/due-shell/json/screenRecorder.json
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/dbus-1/services/com.deepin.ScreenRecorder.service
%{_datadir}/dbus-1/services/com.deepin.Screenshot.service
%{_datadir}/deepin-manual/manual-assets/application/%{name}

%files -n deepin-dock-plugin-screen-recorder
%{_libdir}/dde-dock/plugins/libdeepin-screen-recorder-plugin.so

%files lang
%{_datadir}/%{name}

%changelog
