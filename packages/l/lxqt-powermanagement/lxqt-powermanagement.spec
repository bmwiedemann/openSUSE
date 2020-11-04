#
# spec file for package lxqt-powermanagement
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


Name:           lxqt-powermanagement
Version:        0.16.0
Release:        0
Summary:        Power Management and Auto-suspend
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  lxqt-globalkeys-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WindowSystem) >= 5.36.0
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt) >= %{version}
#BuildRequires:  pkgconfig(xcb)
Requires:       upower
%requires_eq    libQt5Gui5
Recommends:     %{name}-lang

%description
LXQt daemon for power management and auto-suspend

%lang_package

%prep
%setup -q
# Changing LXQt into X-LXQt in desktop files to be freedesktop compliant and shut rpmlint warnings
#find -name '*desktop.in*' -exec sed -ri 's/(LXQt;)/X-\1/' {} +

%build
%cmake  -DPULL_TRANSLATIONS=No
%make_build

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/lxqt*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/devices/*.svg
%{_sysconfdir}/xdg/autostart/lxqt-powermanagement.desktop

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%{_datadir}/lxqt/translations/lxqt-powermanagement
%{_datadir}/lxqt/translations/lxqt-config-powermanagement

%changelog
