#
# spec file for package QtAV
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


%define sover 1
%define src_name QtAV
%define Qt_name %{src_name}
%define ffmpeg_includedir -I%(pkg-config --variable=includedir libavutil)
Name:           QtAV
Version:        1.13.0
Release:        0
Summary:        Qt multimedia framework
License:        LGPL-2.1-or-later AND GPL-3.0-only
Group:          Productivity/Multimedia/Other
URL:            http://qtav.org/
Source0:        QtAV-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-build-with-Qt-5.14.patch
Patch1:         fix-linking.patch
Patch2:         disable_cuda.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-Fix-build-with-Qt-5.15.patch
BuildRequires:  ImageMagick
BuildRequires:  dos2unix
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(xv)
Requires:       %{Qt_name}-players = %{version}

%description
QtAV is a multimedia playback library based on Qt and FFmpeg. It can help
facilitate writing a player application.

Features include:
   * Hardware decoding suppprt: DXVA2, VAAPI, VDA, CedarX, CUDA
   * OpenGL and ES2 support for Hi10P and other 16-bit YUV videos
   * Real time preview
   * Video capture in RGB and YUV format
   * OSD and custom filters
   * Subtitles
   * Transform video using GraphicsItemRenderer. (rotate, shear, etc)
   * Playing frame by frame (currently support forward playing)
   * Playback speed control
   * Variant streams: locale file, http, rtsp, etc.
   * Audio channel, tracks and external audio tracks
   * Dynamically change render engine when playing
   * Multiple video outputs for 1 player
   * Region of interest(ROI), i.e. video cropping
   * Video eq: brightness, contrast, saturation, hue
   * QML support as a plugin. Most playback APIs are compatible with
     QtMultiMedia module

%package -n     lib%{Qt_name}%{sover}
Summary:        Qt multimedia framework library
Group:          System/Libraries

%description -n lib%{Qt_name}%{sover}
QtAV is a multimedia playback library based on Qt and FFmpeg.

This package contains the QtAV library.

%package -n     lib%{Qt_name}Widgets%{sover}
Summary:        QtAV Widgets module
Group:          System/Libraries

%description -n lib%{Qt_name}Widgets%{sover}
QtAV is a multimedia playback library based on Qt and FFmpeg.

This package contains a set of widgets to play media.

%package -n     %{Qt_name}-qml
Summary:        QtAV QML module
Group:          Productivity/Multimedia/Other

%description -n %{Qt_name}-qml
QtAV is a multimedia playback library based on Qt and FFmpeg.

This package contains the QtAV QML module for Qt declarative.

%package -n     %{Qt_name}-players
Summary:        QtAV/QML players
Group:          Productivity/Multimedia/Video/Players
Requires:       %{Qt_name}-qml = %{version}
Requires:       libQt5Svg5
Requires:       libqt5-qtquickcontrols

%description -n	%{Qt_name}-players
QtAV is a multimedia playback library based on Qt and FFmpeg.

This package contains the QtAV based players.

%package -n     %{Qt_name}-devel
Summary:        QtAV development files
Group:          Development/Libraries/C and C++
Requires:       lib%{Qt_name}Widgets%{sover} = %{version}
Requires:       libQt5OpenGL-devel

%description -n %{Qt_name}-devel
QtAV is a multimedia playback library based on Qt and FFmpeg.

This package contains the header development files for building some QtAV
applications using QtAV headers.

%prep
%autosetup -p1 -n %{src_name}-%{version}

# Fix incorrect sRGB profile
for f in $(find . -type f -name \*.png); do
convert $f -strip $f
done

BUILD_TIME=$(LC_ALL=C date -ur %{_sourcedir}/%{Qt_name}.changes +'%H:%M')
BUILD_DATE=$(LC_ALL=C date -ur %{_sourcedir}/%{Qt_name}.changes +'%b %d %Y')
grep -rl '__TIME__' . | xargs --verbose --no-run-if-empty \
sed -i "s/__TIME__/\"$BUILD_TIME\"/"
grep -rl '__DATE__' . | xargs --verbose --no-run-if-empty \
sed -i "s/__DATE__/\"$BUILD_DATE\"/"

find . -type f -name \*.pro | while read FILE; do
echo "QMAKE_CXXFLAGS_RELEASE += %{ffmpeg_includedir}" >> "$FILE"; done

%build
mkdir build
pushd build
%qmake5 "CONFIG+=no_rpath recheck" ../%{Qt_name}.pro
%make_jobs PREFIX=%{_prefix}
popd

%install
pushd build
%qmake5_install
popd

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
ln -s %{_libqt5_bindir}/Player %{buildroot}%{_bindir}/Player
ln -s %{_libqt5_bindir}/QMLPlayer %{buildroot}%{_bindir}/QMLPlayer

find %{buildroot} -name \*.a -exec rm {} \;

printf 'lib%{Qt_name}%{sover}\n
lib%{Qt_name}Widgets%{sover}\n' > %{_sourcedir}/baselibs.conf

# Duplicate files
rm -rf  %{buildroot}%{_datadir}/doc

%post -n  lib%{Qt_name}%{sover} -p /sbin/ldconfig
%postun -n  lib%{Qt_name}%{sover} -p /sbin/ldconfig
%post -n lib%{Qt_name}Widgets%{sover} -p /sbin/ldconfig
%postun -n lib%{Qt_name}Widgets%{sover} -p /sbin/ldconfig
%post -n %{Qt_name}-players %desktop_database_post
%postun -n %{Qt_name}-players %desktop_database_postun

%files
%license gpl-3.0* lgpl-2.1*
%doc Changelog README*

%files -n lib%{Qt_name}%{sover}
%{_libqt5_libdir}/lib%{Qt_name}.so.*

%files -n lib%{Qt_name}Widgets%{sover}
%{_libqt5_libdir}/lib%{Qt_name}Widgets.so.*

%files -n %{Qt_name}-qml
%dir %{_kf5_qmldir}/%{Qt_name}
%{_kf5_qmldir}/%{Qt_name}/Video.qml
%{_kf5_qmldir}/%{Qt_name}/libQmlAV.so
%{_kf5_qmldir}/%{Qt_name}/plugins.qmltypes
%{_kf5_qmldir}/%{Qt_name}/qmldir

%files -n %{Qt_name}-players
%{_bindir}/Player
%{_bindir}/QMLPlayer
%{_datadir}/applications/Player.desktop
%{_datadir}/applications/QMLPlayer.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{Qt_name}.svg
%{_libqt5_bindir}/Player
%{_libqt5_bindir}/QMLPlayer

%files -n %{Qt_name}-devel
%{_kf5_mkspecsdir}/qt_lib_av.pri
%{_kf5_mkspecsdir}/qt_lib_av_private.pri
%{_kf5_mkspecsdir}/qt_lib_avwidgets.pri
%{_kf5_mkspecsdir}/qt_lib_avwidgets_private.pri
%{_libqt5_archdatadir}/mkspecs/features/av.prf
%{_libqt5_archdatadir}/mkspecs/features/avwidgets.prf
%{_libqt5_includedir}/QtAV
%{_libqt5_includedir}/QtAVWidgets
%{_libqt5_libdir}/lib%{Qt_name}.prl
%{_libqt5_libdir}/lib%{Qt_name}.so
%{_libqt5_libdir}/lib%{Qt_name}Widgets.prl
%{_libqt5_libdir}/lib%{Qt_name}Widgets.so

%changelog
