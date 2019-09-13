#
# spec file for package deepin-screenshot
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

Name:           deepin-screenshot
Version:        4.1.11
Release:        0
Summary:        Deepin Screenshot
License:        GPL-3.0+
Group:          Productivity/Graphics/Convertors
Url:            https://github.com/linuxdeepin/deepin-screenshot
Source0:        https://github.com/linuxdeepin/deepin-screenshot/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-appdata.xml
BuildRequires:  fdupes
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  libqt5-linguist
BuildRequires:  appstream-glib
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  deepin-gettext-tools
BuildRequires:  cmake
Requires:       desktop-file-utils
Requires:       deepin-turbo
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
sed -i 's/lrelease/lrelease-qt5/g' generate_translations.sh
sed -i 's/Delay_Screenshot/X-Delay_Screenshot/g;s/Full_Screenshot/X-Full_Screenshot/g' %{name}.desktop

%build
%cmake
make %{?_smp_mflags}

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
