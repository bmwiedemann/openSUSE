#
# spec file for package shotcut
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


# Find qt version used to build
%define qt6version %(qmake6 --version |grep "Using Qt version"|cut -d " " -f 4)
# Internal QML imports
%global __requires_exclude qmlimport\\((Shotcut\\.Controls|org\\.shotcut\\.qml).*
# This package creates a build time version from the current date and uses it to check
# for updates. See patch1 and prep/build section. For reproducible builds.
%define _vstring %(echo %{version} |tr -d ".")
# NOTE: Appears there are no .pc files in qt6
#%%(pkg-config --modversion Qt6Core)
%bcond_with    x264
Name:           shotcut
Version:        24.06.26
Release:        0
Summary:        Video and audio editor and creator
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://www.shotcut.org/
Source:         https://github.com/mltframework/shotcut/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libebur128-devel >= 1.2.6
BuildRequires:  pkgconfig
BuildRequires:  qt6-declarative-private-devel >= 6.4.3
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Concurrent) >= 6.4.3
BuildRequires:  cmake(Qt6Core) >= 6.4.3
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(mlt++-7) >= 7.22.0
BuildRequires:  pkgconfig(mlt-framework-7)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vpx)
Requires:       ffmpeg >= 2.7
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libvpx.so) --qf '%%{NAME} >= %%{VERSION}')
# frei0r-plugins prior to 1.4-7.1 are built against qt4 and cause a segfault on startup.
Requires:       frei0r-plugins >= 1.4-7.1
Requires:       ladspa
#Requires:       libmlt7-modules
Requires:       melt7
# needed on runtime for the timeline to work see https://forums.opensuse.org/showthread.php/520592-shotcut-video-editor-timeline-blank/page3
Requires:       qt6-sql-sqlite = %{qt6version}
Recommends:     lame
ExclusiveArch:  ppc64 ppc64le %{ix86} x86_64
%if 0%{?suse_version} == 1500
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif
%if %{with x264}
BuildRequires:  pkgconfig(x264)
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libx264.so) --qf '%%{NAME} >= %%{VERSION}')
%endif
# NOTE: Can't find a matching package suspect it's merged into another package
#Requires:       libqt6-qtgraphicaleffects >= %%{qt6version}
# This is already pulled in by rpm
#Requires:       libQt6QuickControls2-6 >= %%{qt6version}

%description
Shotcut is an audio/video editor. It supports most audio, video and
image formats, as well as image sequences with a wide range of
filters and effects. It's compatible with JACK Audio and Melted
Server, and offers an experimental GPU Processing feature.
Shotcut can test MLT XML files, too.

%lang_package

%prep
%setup -q
echo "Qt6Core = %{qt6version}"
%autosetup -p0
# Search for executable files
find . \
\( -name \*.html -o -name \*.js \) -type f -executable -exec chmod a-x {} + || :

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_BUILD_TYPE=Release \
       -DSHOTCUT_VERSION=%{version} \
%if 0%{?suse_version} == 1500
       -DCMAKE_CXX_COMPILER:FILEPATH=%{_bindir}/g++-12 \
%endif
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
		lupdate6 "$ts" && lrelease6 "$ts"
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

%changelog
