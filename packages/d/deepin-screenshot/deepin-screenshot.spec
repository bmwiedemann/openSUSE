#
# spec file for package deepin-screenshot
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


Name:           deepin-screenshot
Version:        4.2.2
Release:        0
Summary:        Deepin Screenshot
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Convertors
URL:            https://github.com/linuxdeepin/deepin-screenshot
Source0:        https://github.com/linuxdeepin/deepin-screenshot/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
# PATCH-FIX-UPSTEAM deepin-screenshot-Qt-5_15.patch hillwood@opensuse.org - Support Qt 5.15
Patch0:         %{name}-Qt-5_15.patch
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  deepin-gettext-tools
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xtst)
Requires:       deepin-turbo
Requires:       desktop-file-utils
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Provide a quite easy-to-use screenshot tool. Features:
  * Global hotkey to triggle screenshot tool
  * Take screenshot of a selected area
  * Easy to add text and line drawings onto the screenshot

%lang_package

%prep
%setup -q
%if 0%{?suse_version} > 1500
%patch0 -p1
%endif
sed -i 's/lrelease/lrelease-qt5/g' generate_translations.sh
sed -i 's/Delay_Screenshot/X-Delay_Screenshot/g;s/Full_Screenshot/X-Full_Screenshot/g' %{name}.desktop

%build
%cmake
%make_build

%install
%cmake_install
install -Dm644 %SOURCE1 %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%suse_update_desktop_file -r -u %{name} GTK GNOME Utility X-GNOME-Utilities X-SuSE-DesktopUtility
sed -i '/NoDisplay/s|true|false|' %{buildroot}%{_datadir}/applications/%{name}.desktop
%fdupes %{buildroot}%{_prefix}

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/dbus-1/services/com.deepin.Screenshot.service

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
