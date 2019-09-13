#
# spec file for package qsyncthingtray
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _name   QSyncthingTray
Name:           qsyncthingtray
Version:        0.5.8
Release:        0
Summary:        Qt-based Traybar Application for Syncthing
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/sieren/QSyncthingTray
Source:         https://github.com/sieren/QSyncthingTray/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
# PATCH-FIX-OPENSUSE qsyncthingtray-fix-qt-cmake.patch -- Fix Qt 5.11 CMake compatibility.
Patch0:         qsyncthingtray-fix-qt-cmake.patch
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  syncthing
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.6
BuildRequires:  pkgconfig(Qt5Network) >= 5.6
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.6
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6
Requires:       syncthing
Recommends:     syncthing-inotify
%if 0%{?suse_version} >= 1500 || (0%{?sle_version} > 120200 && 0%{?is_opensuse})
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.6
%else
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.6
%endif

%description
A Traybar Application for Syncthing written in Qt.

Features:
 * Show number of connections at a glance.
 * Traffic statistics and graphs about throughput and connections.
 * Launch Syncthing and Syncthing-Inotify if specified.
 * Quickly pause Syncthing with one click.
 * Last Synchronised Files - Quickly see the recently synchronised
   files and open their directory.
 * Quick Access to all shared directories.
 * Present Syncthing UI in a separate view instead of using the
   browser.
 * Support authenticated HTTPS connections.
 * Use System Notifications about current connection status.
 * A toggle for monochrome icon.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
cp %{SOURCE1} %{name}.desktop
cp %{SOURCE2} %{name}.appdata.xml
sed -i 's|%{_prefix}/local|%{_prefix}|g' includes/platforms/linux/posixUtils.hpp

%build
%cmake \
%if 0%{?suse_version} >= 1500 || (0%{?sle_version} > 120200 && 0%{?is_opensuse})
  -DQST_BUILD_WEBKIT=OFF
%else
  -DQST_BUILD_WEBKIT=ON
%endif
make %{?_smp_mflags} V=1

%install
install -Dpm 0755 build/%{_name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 %{name}.desktop \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 %{name}.appdata.xml \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

for size in 16 32 48 64 128 256 512; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
    convert -strip -resize ${size}x${size} resources/images/Icon1024.png \
      %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

%suse_update_desktop_file %{name}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%if 0%{?suse_version} >= 1500
%license COPYING.GPLv3+.txt LICENSE.txt
%else
%doc COPYING.GPLv3+.txt LICENSE.txt
%endif
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
