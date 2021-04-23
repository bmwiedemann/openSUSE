#
# spec file for package deepin-calendar
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


%define _name dde-calendar

Name:           deepin-calendar
Version:        5.8.0.8
Release:        0
Summary:        A calendar application for Deepin Desktop
License:        GPL-3.0-or-later
Group:          Productivity/Office/Organizers
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        https://github.com/linuxdeepin/dde-calendar/archive/%{version}/%{_name}-%{version}.tar.gz
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(dtkwidget)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The deepin-calendar is a calendar for Deepin Desktop Environment.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
# %patch0 -p1
sed -i 's/lrelease)/lrelease-qt5)/g' CMakeLists.txt
sed -i 's/lupdate)/lupdate-qt5)/g' CMakeLists.txt
sed -i '/<QQueue>/a #include <QMouseEvent>' calendar-client/src/widget/dayWidget/daymonthview.cpp \
calendar-client/src/widget/weekWidget/weekheadview.cpp
sed -i '/<QStylePainter>/a #include <QMouseEvent>' calendar-client/src/widget/schedulesearchview.cpp
sed -i '/include <QJsonObject>/a #include <QMouseEvent>' calendar-client/src/view/draginfographicsview.cpp
sed -i '/include <QPainter>/a #include <QMouseEvent>' schedule-plugin/src/widget/itemwidget.h \
       schedule-plugin/src/widget/modifyscheduleitem.h

# Not included in https://github.com/linuxdeepin/dde-calendar/pull/30 yet
sed -i '/include <QPainter>/a #include <QPainterPath>' calendar-client/src/widget/schedulesearchview.cpp \
       calendar-client/src/widget/dayWidget/daymonthview.cpp \
       calendar-client/src/widget/weekWidget/weekheadview.cpp \
       calendar-client/src/customWidget/customframe.cpp \
       calendar-client/src/widget/yearWidget/yearview.cpp \
       schedule-plugin/src/widget/modifyscheduleitem.h \
       schedule-plugin/src/widget/itemwidget.h
sed -i '/include <QMessageBox>/a #include <QWheelEvent>' calendar-client/src/widget/yearWidget/yearwindow.cpp
sed -i 's/1.2.2/%{version}/g' calendar-client/CMakeLists.txt
sed -i 's/Exec=dde-calendar/Exec=env QT_QPA_PLATFORMTHEME=deepin dde-calendar/g' \
calendar-client/assets/dde-calendar.desktop

%build
%cmake
%make_build

%install
%cmake_install

install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m0644 calendar-client/assets/resources/icon/%{_name}.svg \
%{buildroot}%{_datadir}/icons/hicolor/scalable/apps

%fdupes %{buildroot}
%suse_update_desktop_file -r %{_name} QT Office Calendar Core

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{_name}
%{_prefix}/lib/deepin-aiassistant
%{_datadir}/applications/%{_name}.desktop
%{_sysconfdir}/xdg/autostart/%{_name}-service.desktop
%dir %{_prefix}/lib/deepin-daemon
%{_prefix}/lib/deepin-daemon/dde-calendar-service
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{_name}.svg

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{_name}

%changelog
