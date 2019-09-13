#
# spec file for package deepin-calendar
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

%define _name dde-calendar

Name:           deepin-calendar
Version:        1.2.6
Release:        0
Summary:        A calendar application for Deepin Desktop
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        https://github.com/linuxdeepin/dde-calendar/archive/%{version}/%{_name}-%{version}.tar.gz
Group:          Productivity/Office/Organizers
BuildRequires:  fdupes
BuildRequires:  deepin-gettext-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  desktop-file-utils
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(dtkwidget)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The deepin-calendar is a calendar for Deepin Desktop Environment.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

%build
%qmake5 PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
%qmake5_install

%fdupes %{buildroot}
%suse_update_desktop_file -r %{_name} QT Office Calendar Core

%files
%defattr(-,root,root,-)
%doc README.md LICENSE CHANGELOG.md
%{_bindir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{_name}.svg
%{_datadir}/dbus-1/services/com.deepin.Calendar.service

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{_name}

%changelog
