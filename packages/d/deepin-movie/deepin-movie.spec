#
# spec file for package deepin-movie
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

%define sover 0_1

Name:           deepin-movie
Version:        6.0.11
Release:        0
Summary:        Deepin Video Players
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://github.com/linuxdeepin/deepin-movie-reborn
Source:         %{url}/archive/%{version}/%{name}-reborn-%{version}.tar.gz
# PATCH-FIX-UPSTEAM Fix-library-link.patch hillwood@opensuse.org
# fix library link error and add this includedir for ffmpeg
Patch0:         Fix-library-link.patch
%ifarch aarch64
# PATCH-FIX-UPSTEAM fix-build-on-ARM.patch hillwood@opensuse.org
Patch1:         fix-build-on-ARM.patch
%endif
# PATCH-FIX-UPSTEAM fix-ftbfs-ffmpeg7.patch
Patch2:         fix-ftbfs-ffmpeg7.patch
BuildRequires:  dtkcore >= 5.0.0
BuildRequires:  fdupes
BuildRequires:  libQt5Gui-private-headers-devel
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  glslang-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dbusextended-qt5)
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(mpris-qt5)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xtst)
%if 0%{?suse_version} <= 1500
BuildRequires:  qtdbusextended-devel < 3.1.2
BuildRequires:  qtmpris-devel < 3.1.2
%endif
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
sed -i 's/Exec=deepin-movie/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-movie/g' %{name}.desktop
%if %{?suse_version} > 1500
sed -i 's/MPV_EVENT_TRACKS_CHANGED/MP_EVENT_TRACKS_CHANGED/g' src/backends/mpv/mpv_proxy.cpp
%endif

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DVERSION=%{version}-%{distribution}
%make_build

%install
%cmake_install

%fdupes %{buildroot}

%post -n libdmr%{sover} -p /sbin/ldconfig

%postun -n libdmr%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md README.zh_CN.md HACKING.md CHANGELOG.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/deepin-manual/manual-assets/application/%{name}
%exclude %{_datadir}/%{name}/translations
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/com.deepin.deepin-movie.gschema.xml
%{_datadir}/dbus-1/services/com.deepin.movie.service

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
