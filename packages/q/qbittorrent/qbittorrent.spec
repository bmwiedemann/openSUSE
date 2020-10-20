#
# spec file for package qbittorrent
#
# Copyright (c) 2020 SUSE LLC
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
Version:        4.3.0
Release:        0
Summary:        A BitTorrent client in Qt
License:        GPL-2.0-or-later
URL:            https://qbittorrent.org
Source:         https://downloads.sf.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sf.net/%{name}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM qbittorrent-libtorrent_pthread.patch
Patch1:         qbittorrent-libtorrent_pthread.patch
BuildRequires:  cmake >= 3.9
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_system-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libtorrent-rasterbar-1) >= 1.1.13
%else
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 1.1.13
%endif
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
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
%setup -q
%if 0%{?suse_version} <= 1500
%patch1 -p1
%endif

%build
for ui in nox gui; do
    [ "$ui" = nox ] && ui_opt="-DGUI=OFF" || ui_opt=
    %cmake \
      $ui_opt      \
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
%{_datadir}/icons/hicolor/*/apps/%{name}.png
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
