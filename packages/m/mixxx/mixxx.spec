# vim: set sw=4 ts=4 et:
#
# spec file for package mixxx
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2010-2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%if 0%{?sle_version} && 0%{?sle_version} < 160000
%global force_gcc_version 13
%endif

Name:           mixxx
Version:        2.5.3
Release:        0
Summary:        DJ mixing application
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://mixxx.org
Source0:        https://github.com/mixxxdj/mixxx/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc%{?force_gcc_version}
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  libqt5-linguist
BuildRequires:  ms-gsl-devel
BuildRequires:  pkg-config
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6LabsQmlModels)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6PrintSupport)
# BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlModels)
BuildRequires:  cmake(Qt6QmlWorkerScript)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickControls2Impl)
BuildRequires:  cmake(Qt6QuickLayouts)
BuildRequires:  cmake(Qt6QuickShapesPrivate)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(benchmark)
BuildRequires:  pkgconfig(djinterop) >= 0.26
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libkeyfinder)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmp3lame)
BuildRequires:  pkgconfig(libprofiler)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(portmidi)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(shout) >= 2.4.6
BuildRequires:  pkgconfig(shout-idjc) >= 2.4.6
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(x11)
ExclusiveArch:  %{ix86} x86_64
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(hidapi-libusb)
%endif
Requires:       qt6-sql-sqlite

%description
Mixxx is an audio mixing program.
Mixxx supports most common music file formats.
It can be controlled with MIDI and HID controllers and timecode vinyl
records in addition to computer keyboards and mice.

%prep
%autosetup -p1

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
v=$(rpm -q --whatprovides 'pkgconfig(djinterop)' --qf="%%{VERSION}")
perl -i -lpe 's{(LIBDJINTEROP_VERSION) 0.24.3}{$1 '$v'}g' CMakeLists.txt
# QML is still being worked on, inactive and currently broken in 2.5.0 with Qt > 6.7
%cmake -DSoundTouch_STATIC=NO -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name} -DQML=off
%cmake_build

%install

%cmake_install

L="$PWD/%{name}.lang"
echo -n > "$L"
cd "%{buildroot}/%{_datadir}/mixxx/translations"
for f in mixxx_*.qm; do
    [ -e "$f" ] || continue
    l="${f#mixxx_}"
    l="${l%.qm}"
    echo "%lang($l) %{_datadir}/mixxx/translations/$f" >> "$L"
done

%fdupes %{buildroot}/%{_prefix}

%files -f %{name}.lang
%{_bindir}/mixxx
%dir %{_datadir}/mixxx
%dir %{_datadir}/mixxx/translations
%dir %{_datadir}/mixxx/effects
%dir %{_datadir}/mixxx/effects/chains
%{_datadir}/mixxx/controllers
%{_datadir}/mixxx/effects/chains/*.xml
%{_datadir}/mixxx/keyboard
%{_datadir}/mixxx/skins
# broken in 2.5.0 with Qt > 6.7
# %%dir %%{_datadir}/mixxx/qml
# %%{_datadir}/mixxx/qml
%{_datadir}/applications/org.mixxx.Mixxx.desktop
%{_datadir}/icons/*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.mixxx.Mixxx.metainfo.xml
%{_docdir}/*
%{_udevrulesdir}/*-usb-uaccess.rules

%changelog
