#
# spec file for package qbittorrent
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?sle_version} == 150500 || 0%{?sle_version} == 150600
%define _pyalt  11
%endif
%if 0%{?sle_version} == 150400
%define _pyalt  10
%endif

Name:           qbittorrent
Version:        5.1.2
Release:        0
Summary:        A BitTorrent client in Qt
License:        GPL-2.0-or-later
URL:            https://qbittorrent.org
Source:         https://downloads.sf.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sf.net/%{name}/%{name}-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/qbittorrent/qBittorrent/release-%{version}/5B7CC9A2.asc#/%{name}.keyring
Patch0:         harden_qbittorrent-nox@.service.patch
# PATCH-FIX-OPENSUSE qbittorrent-fix_boost_1.75_build.patch search for libboost_system.so and patch stacktrace function # aloisio@gmx.com
Patch2:         qbittorrent-fix_boost_1.75_build.patch
# PATCH-FIX-OPENSUSE qbittorrent-altpython.patch force newer python for the plugins -- aloisio@gmx.com
Patch3:         qbittorrent-altpython.patch
# PATCH-FIX-OPENSUSE qbittorrent-Qt610.patch
Patch4:         qbittorrent-Qt610.patch
BuildRequires:  cmake >= 3.16
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version} > 1500
BuildRequires:  libboost_system-devel
%else
BuildRequires:  libboost_system1_75_0-devel
%endif
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core) >= 6.5.0
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 2.0.9
BuildRequires:  pkgconfig(openssl) >= 3.0.2
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib) >= 1.2.11
# contains the qt6 plugins to read SVG icons
%requires_ge    libQt6Svg6
# For search engines.
Recommends:     python3%{_pyalt}

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
sed -e 's/__PYTHON_ALT__/python3%{?_pyalt:.%{_pyalt}}/' -i src/base/utils/foreignapps.cpp

%build
for ui in nox gui; do
    [ "$ui" = nox ] && ui_opt="-DGUI=OFF" || ui_opt=

    # Use a separate build dir for each variant
    %define __qt6_builddir build_$ui

    %cmake_qt6 \
      -DQT6=ON \
      -DSYSTEMD=ON \
      -DSystemd_SERVICES_INSTALL_DIR=%{_unitdir} \
      $ui_opt

    %qt6_build
done

%install
for ui in nox gui; do
    %define __qt6_builddir build_$ui
    %qt6_install
done

mkdir -p %{buildroot}%{_sbindir}/
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-nox

%find_lang %{name} --with-man
%find_lang %{name}-nox --with-man

%fdupes %{buildroot}%{_datadir}/

%preun nox
%service_del_preun %{name}-nox@.service

%pre nox
%service_add_pre %{name}-nox@.service

%postun nox
%service_del_postun %{name}-nox@.service

%post nox
%service_add_post %{name}-nox@.service

%files -f %{name}.lang
%license COPYING
%doc AUTHORS Changelog README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/status/%{name}-tray.png
%{_datadir}/icons/hicolor/scalable/status/%{name}-tray*.svg
%{_datadir}/metainfo/org.qbittorrent.qBittorrent.metainfo.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

%files nox -f %{name}-nox.lang
%license COPYING
%doc AUTHORS Changelog README.md
%{_bindir}/%{name}-nox
%{_sbindir}/rc%{name}-nox
%{_unitdir}/%{name}-nox@.service
%{_mandir}/man?/%{name}-nox.?%{?ext_man}

%changelog
