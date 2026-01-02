#
# spec file for package fooyin
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           fooyin
Version:        0.9.2
Release:        0
Summary:        A customisable music player built with Qt
License:        GPL-3.0-only
URL:            https://www.fooyin.org/
Source0:        https://github.com/fooyin/fooyin/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch0 fixes build with QT 6.10.1 in fooyin 0.9.2
# see https://github.com/fooyin/fooyin/issues/779
# fixed upstream in master-branch, can be removed in the next version
Patch0:         Fix-compatibility-with-Qt-6.10.1.patch
# Patch1 fixes build with QT 6.10.1 in fooyin 0.9.2
# see https://github.com/fooyin/fooyin/pull/725
# fixed upstream in master-branch, can be removed in the next version
Patch1:         Add-missing-header-include-for-QElapsedTimer-class.patch
BuildRequires:  c++_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
# Fixes conflict with ffmepg-8-mini-devel
BuildRequires:  ffmpeg-7-mini-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  ninja
BuildRequires:  qt6-base-devel
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(xkbcommon)

%description
fooyin is a Qt6 music player built around customisation. It offers a
growing list of widgets to manage and play a local music collection.
It is extendable through the use of plugins, and many widgets make
use of FooScript to offer an even deeper level of control.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake -DBUILD_LIBVGM=OFF
%cmake_build

%install
%cmake_install

# fix "E: files-duplicated-waste"
rm -rv %{buildroot}%{_datadir}/doc

%find_lang %{name} --with-qt

%fdupes -s %{buildroot}%{_datadir}/%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.%{name}.%{name}.*
%{_datadir}/metainfo/org.%{name}.%{name}.metainfo.xml
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}_{core,gui,utils}.so.0.0.0
%{_libdir}/%{name}/plugins

%changelog
