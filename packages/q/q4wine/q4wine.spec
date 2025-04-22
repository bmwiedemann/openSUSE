#
# spec file for package q4wine
#
# Copyright (c) 2025 SUSE LLC
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


Name:           q4wine
Version:        1.4.1
Release:        0
Summary:        Qt GUI for WINE
License:        GPL-3.0-only
Group:          System/Emulators/PC
URL:            https://q4wine.brezblock.org.ua/
Source0:        https://github.com/brezerk/q4wine/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fuseiso
BuildRequires:  hicolor-icon-theme
BuildRequires:  icoutils
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
Requires:       fuseiso
Requires:       icoutils
Requires:       sudo
Requires:       wine
Recommends:     %{name}-lang
# src/third-party/SingleApplication-3.5.2 is licensed under MIT
Provides:       bundled(SingleApplication) = 3.5.2

%description
Q4Wine is a Qt-based GUI for WINE. It can help manage Wine
prefixes and installed applications.

General features:
- Can export Qt color theme into Wine color settings.
- Can work with different Wine versions at the same time.
- Creation, deletion and management of prefixes (WINEPREFIX).
- Control for Wine process.
- Autostart icon support.
- CD image use.
- Icons can be extracted from PE files (.exe, .dll).
- Backup and restore for managed prefixes.
- Wine AppDB browser.
- Logging subsystem.
- Winetricks support.

%lang_package

%prep
%autosetup -p1

%build
%cmake \
  -DLIBS_ENTRY_PATH=%{_libdir} \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_SHARED_LINKER_FLAGS=""
%cmake_build

%install
%cmake_install
rm -vRf %{buildroot}%{_datadir}/icons/ubuntu-mono-dark/
%find_lang %{name} --with-qt

%files
%license COPYING
%doc AUTHORS.md Changelog.md README.md
%{_bindir}/q4wine
%{_bindir}/q4wine-cli
%{_bindir}/q4wine-helper
%{_datadir}/q4wine
%exclude %{_datadir}/%{name}/l10n
%{_datadir}/applications/q4wine.desktop
%{_datadir}/metainfo/ua.org.brezblock.q4wine.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/q4wine*.svg
%{_libdir}/lib%{name}*
%{_mandir}/man1/q4wine*%{?ext_man}

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/l10n

%changelog
