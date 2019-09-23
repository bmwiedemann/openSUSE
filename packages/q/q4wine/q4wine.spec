#
# spec file for package q4wine
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.3.11
Release:        0
Summary:        Qt GUI for WINE
License:        GPL-3.0-only
Group:          System/Emulators/PC
URL:            http://q4wine.brezblock.org.ua/
Source0:        https://github.com/brezerk/q4wine/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.0
BuildRequires:  fdupes
BuildRequires:  fuseiso
BuildRequires:  hicolor-icon-theme
BuildRequires:  icoutils
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
Requires:       fuseiso
Requires:       icoutils
Requires:       sudo
Requires:       wine
Recommends:     %{name}-lang

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
%setup -q

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
    -DCMAKE_NO_BUILTIN_CHRPATH=ON \
    -DLIBS_ENTRY_PATH=%{_libdir}
make %{?_smp_mflags} VERBOSE=1

%install
pushd build
%make_install
popd
rm -fr %{buildroot}%{_datadir}/icons/ubuntu-mono-dark/
%find_lang %{name} --with-qt

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_bindir}/%{name}-helper
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/l10n/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/lib%{name}*
%{_mandir}/man?/*

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/l10n/

%changelog
