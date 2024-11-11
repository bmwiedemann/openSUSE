#
# spec file for package screengrab
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


Name:           screengrab
Version:        2.9.0
Release:        0
Summary:        Qt tool for creating screenshots
License:        GPL-2.0-only
Group:          System/X11/Utilities
URL:            https://github.com/lxqt/screengrab
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(Qt5Xdg) >= 3.11.0
BuildRequires:  pkgconfig(Qt6Core) >= 6.6
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xdg) >= 4.0.0
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
%autosetup -p1

%build
%cmake_qt6 \
    -DSG_EXT_EDIT="1" \
    -DSG_DBUS_NOTIFY="1"
%qt6_build

%install
%qt6_install
rm -rf %{buildroot}%{_datadir}/doc

%find_lang %{name} --with-qt

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md docs/html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.conf
%{_datadir}/metainfo/%{name}.metainfo.xml

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/translations
%if 0%{?sle_version}
%{_datadir}/%{name}/translations/%{name}_???.qm
%endif

%changelog
