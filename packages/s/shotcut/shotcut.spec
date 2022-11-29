#
# spec file for package shotcut
#
# Copyright (c) 2022 SUSE LLC
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


# Find qt version used to build
%define qt5version %(pkg-config --modversion Qt5Core)

%bcond_with    x264

# Internal QML imports
%global __requires_exclude qmlimport\\((Shotcut\\.Controls|org\\.shotcut\\.qml).*

Name:           shotcut
Version:        22.11.25
Release:        0
# This package creates a build time version from the current date and uses it to check
# for updates. See patch1 and prep/build section. For reproducible builds.
%define _vstring %(echo %{version} |tr -d ".")
Summary:        Video and audio editor and creator
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www.shotcut.org/
Source:         https://github.com/mltframework/shotcut/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch1:         shotcut-libdir.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtdeclarative-private-headers-devel
BuildRequires:  mc
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(mlt++-7)
BuildRequires:  pkgconfig(mlt-framework-7)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vpx)
# frei0r-plugins prior to 1.4-7.1 are built against qt4 and cause a segfault on startup.
Requires:       frei0r-plugins >= 1.4-7.1
Requires:       ladspa
Requires:       libmlt7-modules
Requires:       melt7
Recommends:     lame
Requires:       ffmpeg >= 2.7
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libvpx.so) --qf '%%{NAME} >= %%{VERSION}')
%if %{with x264}
BuildRequires:  pkgconfig(x264)
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libx264.so) --qf '%%{NAME} >= %%{VERSION}')
%endif
# needed on runtime for the timeline to work see https://forums.opensuse.org/showthread.php/520592-shotcut-video-editor-timeline-blank/page3
Requires:       libQt5Sql5-sqlite
Requires:       libqt5-qtgraphicaleffects >= %{qt5version}
Requires:       libqt5-qtquickcontrols2 >= %{qt5version}

%description
Shotcut is an audio/video editor. It supports most audio, video and
image formats, as well as image sequences with a wide range of
filters and effects. It's compatible with JACK Audio and Melted
Server, and offers an experimental GPU Processing feature.
Shotcut can test MLT XML files, too.

%lang_package

%prep
%setup -q
echo "Qt5Core = %{qt5version}"
%autosetup -p0

# Search for executable files
find . \
\( -name \*.html -o -name \*.js \) -type f -executable -exec chmod a-x {} + || :

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_BUILD_TYPE=Release \
       -DSHOTCUT_VERSION=%{version} \
       -DDEFINES+=SHOTCUT_NOUPGRADE
%cmake_build

# CC=gcc-8 CPP=cpp-8 CXX=g++-8
%install
%cmake_install

install -D icons/%{name}-logo-64.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# Install language files
langlist="$PWD/%{name}.lang"
langdir="%{_datadir}/%{name}/translations"
basedir=$(basename "$langdir")
pushd $basedir
	for ts in *.ts; do
		[ -e "$ts" ] || continue
		lupdate-qt5 "$ts" && lrelease-qt5 "$ts"
	done
	for qm in *.qm; do
		[ -e "$qm" ] || continue
		if ! grep -wqs "%dir\ $langdir" "$langlist"; then
			echo "%dir $langdir" >>"$langlist"
		fi
		install -Dm0644 "$qm" "%{buildroot}/$langdir/$qm"
		lang="${qm%.qm}"
		echo "%lang($lang) $langdir/$qm" >>"$langlist"
	done
popd
%suse_update_desktop_file -i org.%{name}.Shotcut
chmod 0755 %{buildroot}/%{_datadir}/%{name}/qml/export-edl/rebuild.sh
chmod 0755 %{buildroot}/%{_datadir}/%{name}/qml/export-chapters/rebuild.sh
%fdupes -s %{buildroot}/%{_datadir}

%post
%mime_database_post
%desktop_database_post

%postun
%mime_database_postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_datadir}/icons/hicolor/64x64/apps/org.shotcut.Shotcut.png
%{_datadir}/icons/hicolor/128x128/apps/org.shotcut.Shotcut.png
%{_datadir}/metainfo/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/*
%{_datadir}/applications/org.%{name}.Shotcut.desktop
%exclude %{_datadir}/%{name}/translations
%{_libdir}/libCuteLogger.so

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
