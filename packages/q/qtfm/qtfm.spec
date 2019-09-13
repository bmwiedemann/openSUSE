#
# spec file for package qtfm
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           qtfm
Version:        6.1.9
Release:        0
Summary:        Qt File Manager
License:        GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/File utilities
URL:            https://qtfm.eu
Source0:        https://github.com/rodlie/qtfm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       ImageMagick
Recommends:     adwaita-icon-theme
Recommends:     udisks2

%description
Lightweight file manager using Qt.

Features:
 * Desktop (theme/applications/mime) integration
 * Customizable interface
 * Powerful custom command system
 * Customizable key bindings
 * Drag & drop functionality
 * Tabs
 * Udisks support
 * System tray daemon

%prep
%setup -q

%build
%qmake5 PREFIX=%{_prefix}
%make_jobs

%install
%qmake5_install
%fdupes %{buildroot}/%{_datadir}

# Installing the app icon to hicolor
# Fix: directories not owned by a package
pushd %{buildroot}
find ./ -type d -d | while read _list; do
    echo $_list | grep '[0-9]x[0-9]' || continue
    _path=$(echo $_list | sed 's/[^/]//')
    ls $_path &> /dev/null || rm -rv %{buildroot}$_path
done
popd

rm -rv %{buildroot}%{_datadir}/doc

%if 0%{?suse_version} < 1500 
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_bindir}/qtfm
%{_bindir}/qtfm-tray
%{_datadir}/applications/qtfm.desktop
%{_datadir}/icons/hicolor/*/apps/qtfm.??g
%{_sysconfdir}/xdg/autostart/qtfm-tray.desktop
%{_mandir}/man?/qtfm-tray.?%{ext_info}
%{_mandir}/man?/qtfm.?%{ext_info}

%changelog
