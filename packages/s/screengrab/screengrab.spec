#
# spec file for package screengrab
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


Name:           screengrab
Version:        2.1.0
Release:        0
Summary:        Qt tool for creating screenshots
License:        GPL-2.0-only
Group:          System/X11/Utilities
URL:            https://github.com/lxqt/screengrab
Source:         https://github.com/lxqt/screengrab/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/screengrab/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem) >= 5.36.0
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core) >= 5.12.0
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xdg) >= 3.6.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-xfixes)
Recommends:     %{name}-lang

%description
Screenshot taker with the ability to publish them via hosting services.

%lang_package

%prep
%setup -q

%build
%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DSG_DBUS_NOTIFY=ON \
    -DSG_EXT_EDIT=OFF \
    -DSG_EXT_UPLOADS=OFF \
    -DSG_GLOBALSHORTCUTS=OFF \
    -DUPDATE_TRANSLATIONS=OFF

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc

%find_lang %{name} --with-qt

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md docs/html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/screengrab/screengrab.conf

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/translations

%changelog
