#
# spec file for package qterminal
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


Name:           qterminal
Version:        1.4.0
Release:        0
Summary:        A Qt-based terminal emulator
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          System/X11/Terminals
URL:            https://github.com/lxqt/qterminal
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  lxqt-build-tools-devel >= 0.13.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(qtermwidget5) >= %{version}
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui) >= 5.15.0
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(libcanberra)
Recommends:     %{name}-lang

%description
The lightweight Qt terminal emulator.

%lang_package

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
%ctest

%files
%license LICENSE
%doc AUTHORS README.md CONTRIBUTING*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-drop.desktop
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/64x64/apps
%{_datadir}/icons/hicolor/64x64/apps/qterminal.png
%{_datadir}/metainfo/qterminal.metainfo.xml
%{_datadir}/qterminal/qterminal_bookmarks_example.xml

%files lang -f %{name}.lang
%license LICENSE
%dir %{_datadir}/qterminal
%{_datadir}/qterminal/translations

%changelog
