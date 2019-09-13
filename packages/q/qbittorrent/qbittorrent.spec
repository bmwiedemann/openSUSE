#
# spec file for package qbittorrent
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        4.1.7
Release:        0
Summary:        A BitTorrent client in Qt
License:        GPL-2.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://qbittorrent.org
Source:         https://downloads.sf.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sf.net/%{name}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.9
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 1.1.4
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
# For geolocalisation.
Requires:       GeoIP
%requires_ge    libtorrent-rasterbar9
Recommends:     python
# For search engines.
Recommends:     python3
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
BuildRequires:  update-desktop-files
%endif

%description
qBittorrent is a bittorrent client programmed in C++ and Qt that
uses libtorrent-rasterbar.

It has a streaming-like function to let users download and play video
files, supports Unicode and has a bandwith scheduler.

%package nox
Summary:        A BitTorrent client in Qt, CLI version
Group:          Productivity/Networking/File-Sharing
%{?systemd_requires}

%description nox
qBittorrent is a bittorrent client programmed in C++ and Qt that
uses libtorrent-rasterbar. This subpackage contains a command-line
version.

%prep
%setup -q

%build
for ui in nox gui; do
    [ "$ui" = nox ] && ui_opt="-DCMAKE_DISABLE_FIND_PACKAGE_Qt5Widgets=ON" || ui_opt=
    %cmake \
      $ui_opt      \
      -DSYSTEMD=ON \
      -DSystemd_SERVICES_INSTALL_DIR=%{_unitdir}
    %make_jobs
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

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

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
