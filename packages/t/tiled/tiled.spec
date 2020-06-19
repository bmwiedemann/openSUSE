#
# spec file for package tiled
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.4.0
Release:        0
Summary:        A tilemap editor
License:        GPL-2.0-or-later
URL:            https://www.mapeditor.org
Source:         https://github.com/bjorn/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5OpenGL-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  shared-mime-info
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt5Qml)
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

%package -n libtiled1
Summary:        Library for Tiled MapEditor
License:        BSD-2-Clause

%description -n libtiled1
This package contains libtiled a library for the Tiled map editor.

%prep
%setup -q
# Remove copy of zlib
rm -rf src/zlib

%build
qmake-qt5 -r PREFIX=%{_prefix} LIBDIR=%{_libdir} RPATH=no USE_FHS_PLUGIN_PATH=yes

make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

# Clean build artefacts
find -name ".uic" -or -name ".moc" -or -name ".rcc" | xargs rm -rf

# locale files
%find_lang %{name} --with-qt

# Removed development file (this version does not install headers anyway)
rm %{buildroot}%{_libdir}/lib%{name}.so

# Remove duplicates
%fdupes %{buildroot}%{_datadir}

%post -n libtiled1 -p /sbin/ldconfig
%postun -n libtiled1 -p /sbin/ldconfig

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
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n libtiled1
%license LICENSE.BSD
%{_libdir}/lib%{name}.so.*

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
