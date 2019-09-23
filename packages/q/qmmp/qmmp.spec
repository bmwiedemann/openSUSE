#
# spec file for package qmmp
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sover   1
%define mver    1.3
%bcond_with faad
%bcond_with restricted
Name:           qmmp
Version:        1.3.4
Release:        0
Summary:        Qt-based Multimedia Player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
ExclusiveArch:  %ix86 x86_64
URL:            http://qmmp.ylsoftware.com/
Source:         http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM qmmp-fix_cdda_version.patch pascal.bleser@opensuse.org -- Fix header detection for cdparanoia cdda.h.
Patch0:         %{name}-fix_cdda_version.patch
# PATCH-FEATURE-OPENSUSE qmmp-default_pulse.patch reddwarf@opensuse.org -- Use PulseAudio instead of ALSA by default.
Patch1:         %{name}-default-pulse.patch
# PATCH-FIX-OPENSUSE qmmp-fix-openmpt.patch -- Fix OpenMPT compatibility.
Patch2:         %{name}-fix-openmpt.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmpcdec-devel
BuildRequires:  libqt5-qttools-devel >= 5.4
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.4
BuildRequires:  pkgconfig(Qt5DBus) >= 5.4
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.4
BuildRequires:  pkgconfig(Qt5Network) >= 5.4
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.4
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.4
BuildRequires:  pkgconfig(Qt5Xml) >= 5.4
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(enca) >= 1.9
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmms)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libprojectM) >= 3.1.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(opus) >= 1.0.2
BuildRequires:  pkgconfig(opusfile) >= 0.2
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
Requires:       %{name}(%{sover})(Input)
Requires:       %{name}(%{sover})(Output)
Requires:       %{name}(%{sover})(Ui)
%if 0%{?suse_version} < 1500
BuildRequires:  update-desktop-files
%endif
%if %{with faad}
BuildRequires:  libfaad-devel
%endif

%description
This program is an audio-player, written with help of Qt library.

%package -n lib%{name}%{sover}
Summary:        Qmmp library
Group:          System/Libraries
Recommends:     lib%{name}-plugins

%description -n lib%{name}%{sover}
This program is an audio-player, written with help of Qt library.

This package provides the Qmmp library.

%package -n lib%{name}-plugins
Summary:        Plugins for libqmmp
# Suggests instead of Recommends since MPlayer is too big of a dependency.
Group:          System/Libraries
Suggests:       lib%{name}-plugin-mplayer
Provides:       %{name}(%{sover})(Input)
Provides:       %{name}(%{sover})(Output)
Provides:       %{name}(%{sover})(Ui)
# libqmmp0-plugins & qmmp-plugin-pack-simple-ui were last used in openSUSE 13.2 (in PMBS).
Provides:       %{name}-plugin-pack-simple-ui = %{version}
Obsoletes:      %{name}-plugin-pack-simple-ui < %{version}
Obsoletes:      lib%{name}0-plugins

%description -n lib%{name}-plugins
This program is an audio-player, written with help of Qt library.

This package provides plugins for libqmmp.

%if %{with restricted}
%package -n lib%{name}-plugin-mplayer
Summary:        MPlayer plugin for libqmmp
Group:          System/Libraries
Requires:       MPlayer

%description -n lib%{name}-plugin-mplayer
This program is an audio-player, written with help of Qt library.

This package provides MPlayer plugin for libqmmp.
%endif

%package -n lib%{name}-devel
Summary:        Development files for libqmmp
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description -n lib%{name}-devel
This program is an audio-player, written with help of Qt library.

Development files for libqmmp.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1

%build
%cmake \
  -DCMAKE_MODULE_LINKER_FLAGS="" \
  -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
  -DLIB_DIR=%{_lib}              \
  -DPLUGIN_DIR=%{_lib}/%{name}-%{mver} \
%if %{without restricted}
  -DUSE_MPLAYER=OFF              \
%endif
  -DUSE_HAL=OFF                  \
  -DUSE_OSS=OFF                  \
  -DUSE_OSS4=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install
# do not install werdly-sized cions
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/56x56

%post -n lib%{name}%{sover} -p /sbin/ldconfig

%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%post -n lib%{name}-plugins
%desktop_database_post

%postun -n lib%{name}-plugins
%desktop_database_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%if 0%{?suse_version} < 1500
%dir %{_datadir}/metainfo
%endif
%{_datadir}/metainfo/%{name}.appdata.xml

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}*.so.%{sover}*

%files -n lib%{name}-plugins
%{_libdir}/%{name}-%{mver}/
%if %{with restricted}
%exclude %{_libdir}/%{name}-%{mver}/Engines/libmplayer.so
%endif

%if %{with restricted}
%files -n lib%{name}-plugin-mplayer
%dir %{_libdir}/%{name}-%{mver}/
%dir %{_libdir}/%{name}-%{mver}/Engines/
%{_libdir}/%{name}-%{mver}/Engines/libmplayer.so
%endif

%files -n lib%{name}-devel
%{_includedir}/%{name}/
%{_includedir}/%{name}ui/
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}ui.pc

%changelog
