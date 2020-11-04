#
# spec file for package qterminal
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


Name:           qterminal
Version:        0.16.0
Release:        0
Summary:        A Qt-based terminal emulator
License:        GPL-2.0-only
Group:          System/X11/Terminals
URL:            https://github.com/lxqt/qterminal
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  qtermwidget-qt5-devel >= %{version}
BuildRequires:  utf8proc-devel
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core) >= 5.12.0
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(lxqt)
Recommends:     %{name}-lang

%description
The lightweight Qt terminal emulator.

%lang_package

%prep
%setup -q

%build
%cmake \
    -DUSE_QT5=ON \
    -DUSE_SYSTEM_QXT=OFF \
	-DPULL_TRANSLATIONS=No
%make_build

%install
%cmake_install

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc AUTHORS README.md CONTRIBUTING*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_drop.desktop
%{_datadir}/appdata/qterminal.appdata.xml
%{_datadir}/icons/hicolor/64x64/apps/qterminal.png

%files lang -f %{name}.lang
%dir %{_datadir}/qterminal
%{_datadir}/qterminal/translations

%changelog
