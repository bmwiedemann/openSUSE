#
# spec file for package tiled
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


Name:           tiled
Version:        1.11.0
Release:        0
Summary:        A tilemap editor
License:        GPL-2.0-or-later
URL:            https://www.mapeditor.org
Source:         https://github.com/mapeditor/tiled/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  karchive-devel
BuildRequires:  qbs
BuildRequires:  qt6-base-common-devel
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-core-devel >= 6.4.2
BuildRequires:  qt6-declarative-devel
BuildRequires:  qt6-declarative-private-devel
BuildRequires:  qt6-gui-devel
BuildRequires:  qt6-linguist-devel
BuildRequires:  qt6-opengl-devel
BuildRequires:  qt6-qml-devel
BuildRequires:  qt6-quickcontrols2-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  shared-mime-info
BuildRequires:  zlib-devel
Recommends:     tmxtools
Provides:       tiled-qt

%description
Tiled is a general purpose tile map editor. It is built to work with
varying game engines, whether your game is an RPG, platformer or
Breakout clone. Tiled is written in C++, using the Qt application
framework.

%package -n tmxtools
Summary:        Commandline Tools for Tiled MapEditor
License:        BSD-2-Clause

%description -n tmxtools
This package contains tmxviewer, a simple application to view Tiled maps
and tmxrasterizer which is also a command line tool.

%prep
%setup -q
# Remove copy of zlib
rm -rf src/zlib

%build
# see gh/mapeditor/tiled#3613 why no --detect
qbs setup-toolchains --type gcc %{_bindir}/g++-13 gcc
qbs setup-qt %{_bindir}/qmake6 defprof
qbs config defaultProfile defprof
qbs qbs.installPrefix:"%{_prefix}" projects.Tiled.useRPaths:false projects.Tiled.libDir:%{_lib}

%install
qbs install --install-root %{buildroot}

# Clean build artefacts
find -name ".uic" -or -name ".moc" -or -name ".rcc" | xargs rm -rf

# locale files
%find_lang %{name} --with-qt

# Remove duplicates
%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} > 1130
%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun
%endif

%files -f %{name}.lang
%license COPYING LICENSE.GPL LICENSE.BSD
%doc AUTHORS NEWS.md README.md
%{_bindir}/%{name}
%{_bindir}/terraingenerator
%{_datadir}/applications/org.mapeditor.Tiled.desktop
%{_datadir}/metainfo/org.mapeditor.Tiled.appdata.xml
%{_datadir}/icons/hicolor/*/mimetypes/application-x-%{name}.*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/org.mapeditor.Tiled.xml
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_libdir}/libtiled.so
%{_libdir}/libtilededitor.so
%dir %{_libdir}/tiled
%dir %{_libdir}/tiled/plugins
%{_libdir}/tiled/plugins/libcsv.so
%{_libdir}/tiled/plugins/libdefold.so
%{_libdir}/tiled/plugins/libdefoldcollection.so
%{_libdir}/tiled/plugins/libdroidcraft.so
%{_libdir}/tiled/plugins/libflare.so
%{_libdir}/tiled/plugins/libgmx.so
%{_libdir}/tiled/plugins/libjson.so
%{_libdir}/tiled/plugins/libjson1.so
%{_libdir}/tiled/plugins/liblua.so
%{_libdir}/tiled/plugins/libreplicaisland.so
%{_libdir}/tiled/plugins/librpmap.so
%{_libdir}/tiled/plugins/libtbin.so
%{_libdir}/tiled/plugins/libtengine.so
%{_libdir}/tiled/plugins/libtscn.so
%{_libdir}/tiled/plugins/libyy.so

%files -n tmxtools
%license LICENSE.BSD
%{_bindir}/tmxrasterizer
%{_bindir}/tmxviewer
%{_mandir}/man1/tmxviewer.1%{?ext_man}
%{_mandir}/man1/tmxrasterizer.1%{?ext_man}
%dir %{_datadir}/thumbnailers/
%{_datadir}/thumbnailers/tiled.thumbnailer
%dir %{_datadir}/metainfo/

%changelog
