#
# spec file for package qbittorrent
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2014 Mariusz Fik <fisiu@opensuse.org>.
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


Name:           qbittorrent
Version:        4.4.5
Release:        0
Summary:        A BitTorrent client in Qt
License:        GPL-2.0-or-later
URL:            https://qbittorrent.org
Source:         https://downloads.sf.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sf.net/%{name}/%{name}-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/qbittorrent/qBittorrent/release-%{version}/5B7CC9A2.asc#/%{name}.keyring
Patch0:         harden_qbittorrent-nox@.service.patch
# PATCH-FIX-OPENSUSE qbittorrent-fix_boost_1.66_detection.patch search for libboost_system.so # aloisio@gmx.com
Patch1:         qbittorrent-fix_boost_1.66_detection.patch
BuildRequires:  cmake >= 3.16
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  pkgconfig
%if 0%{?sle_version} == 150400
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%endif
BuildRequires:  cmake(Qt6Core) >= 6.2
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 2.0.4
BuildRequires:  pkgconfig(openssl) >= 1.1.1
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib) >= 1.2.11
# contains the qt6 plugins to read SVG icons
%requires_ge    libQt6Svg6
# For search engines.
Recommends:     python3

%description
qBittorrent is a bittorrent client programmed in C++ and Qt that
uses libtorrent-rasterbar.

It has a streaming-like function to let users download and play video
files, supports Unicode and has a bandwith scheduler.

%package nox
Summary:        A BitTorrent client in Qt, CLI version
%{?systemd_requires}

%description nox
qBittorrent is a bittorrent client programmed in C++ and Qt that
uses libtorrent-rasterbar. This subpackage contains a command-line
version.

%prep
%autosetup -p1

%build
%if 0%{?sle_version} == 150400
export CC=gcc-11
export CXX=g++-11
%endif
for ui in nox gui; do
    [ "$ui" = nox ] && ui_opt="-DGUI=OFF" || ui_opt=
    %cmake \
      $ui_opt      \
      -DQT6=ON \
      -DSYSTEMD=ON \
      -DSystemd_SERVICES_INSTALL_DIR=%{_unitdir}
    # Override as this needs absurd amounts of RAM to build.
    %cmake_build -j1
    cd ..
    mv build build.$ui
done

%install
for ui in nox gui; do
    mv build.$ui build
    %cmake_install
    mv build build.$ui
done

mkdir -p %{buildroot}%{_sbindir}/
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-nox

%fdupes %{buildroot}%{_datadir}/

%preun nox
%service_del_preun %{name}-nox@.service

%pre nox
%service_add_pre %{name}-nox@.service

%postun nox
%service_del_postun %{name}-nox@.service

%post nox
%service_add_post %{name}-nox@.service

%files
%license COPYING
%doc AUTHORS Changelog README.md TODO
%{_bindir}/%{name}
%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/status/%{name}-tray.png
%{_datadir}/icons/hicolor/scalable/status/%{name}-tray*.svg
%{_datadir}/metainfo/org.qbittorrent.qBittorrent.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

%files nox
%license COPYING
%doc AUTHORS Changelog README.md TODO
%{_bindir}/%{name}-nox
%{_sbindir}/rc%{name}-nox
%{_unitdir}/%{name}-nox@.service
%{_mandir}/man?/%{name}-nox.?%{?ext_man}

%changelog
