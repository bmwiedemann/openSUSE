#
# spec file for package deepin-movie
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


%define sover 0_1

Name:           deepin-movie
Version:        5.7.6.165
Release:        0
Summary:        Deepin Video Players
License:        GPL-3.0-or-later AND OpenSSL
Group:          Productivity/Multimedia/Video/Players
URL:            https://github.com/linuxdeepin/deepin-movie-reborn
Source:         https://github.com/linuxdeepin/deepin-movie-reborn/archive/%{version}/%{name}-reborn-%{version}.tar.gz
# PATCH-FIX-UPSTEAM Fix-library-link.patch hillwood@opensuse.org
# fix library link error and add this includedir for ffmpeg
Patch0:         Fix-library-link.patch
# PATCH-FIX-UPSTEAM deepin-movie-add-qthelper.patch hillwood@opensuse.org
# qthelper.hpp was removed from mpv project, move this api in this project.
Patch1:         deepin-movie-add-qthelper.patch
# PATCH-FIX-UPSTEAM libavformat-version-check.patch hillwood@opensuse.org - fix build on new ffmpeg
Patch2:         libavformat-version-check.patch
%ifarch aarch64
# PATCH-FIX-UPSTEAM fix-build-on-ARM.patch hillwood@opensuse.org
Patch3:         fix-build-on-ARM.patch
%endif
BuildRequires:  dtkcore >= 5.0.0
BuildRequires:  fdupes
BuildRequires:  glslang-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xtst)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The default media player for Deepin. QML is used to build its
graphical interface, combined with QtAV as its multimedia backend.

%package -n libdmr%{sover}
Summary:        Deepin Video Players
Group:          System/Libraries

%description -n libdmr%{sover}
libdmr is a library for accessing the Direct Rendering Manager on Linux, BSD and
other operating systems that support the ioctl interface, and for chipsets with
DRM memory manager, support for tracking relocations and buffers. libdmr is a
low-level library, typically used by graphics drivers such as the Mesa DRI and X
drivers.

%package devel
Summary:        Development tools for deepin movie
Group:          Development/Languages/C and C++
Requires:       libdmr%{sover} = %{version}

%description devel
The deepin-movie-devel package contains the header files and developer docs for
deepin movie.

%lang_package

%prep
%autosetup -p1 -n %{name}-reborn-%{version}
sed -i '/#include <DPalette>/a #include <QPainterPath>' src/widgets/{tip,toolbutton}.h
sed -i 's/Exec=deepin-movie/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-movie/g' src/%{name}.desktop

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%cmake_install

%fdupes %{buildroot}

%post -n libdmr%{sover} -p /sbin/ldconfig

%postun -n libdmr%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md HACKING.md CHANGELOG.md
%license LICENSE LICENSE.OpenSSL
%{_bindir}/%{name}
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/translations
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/com.deepin.deepin-movie.gschema.xml

%files -n libdmr%{sover}
%defattr(-,root,root)
%{_libdir}/libdmr.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libdmr.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libdmr

%files lang
%defattr(-,root,root)
%{_datadir}/%{name}/translations

%changelog
