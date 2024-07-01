#
# spec file for package qmmp
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


%global __provides_exclude_from ^%{_libdir}/qmmp-[0-9\.]*/
%define sover   2
%define mver    2.1
%bcond_with faad
%bcond_with restricted
Name:           qmmp
Version:        2.1.8
Release:        0
Summary:        Qt-based Multimedia Player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://qmmp.ylsoftware.com/
Source:         https://qmmp.ylsoftware.com/files/%{name}/%{mver}/%{name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE qmmp-default_pulse.patch reddwarf@opensuse.org -- Use PulseAudio instead of ALSA by default.
Patch0:         %{name}-default-pulse.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  musepack-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(enca)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libarchive)
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
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libprojectM)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(shout)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(wildmidi)
Requires:       %{name}(%{sover})(Input)
Requires:       %{name}(%{sover})(Output)
Requires:       %{name}(%{sover})(Ui)
ExclusiveArch:  %ix86 x86_64
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
Group:          System/Libraries
# Suggests instead of Recommends since MPlayer is too big of a dependency.
Suggests:       lib%{name}-plugin-mplayer
Provides:       %{name}(%{sover})(Input)
Provides:       %{name}(%{sover})(Output)
Provides:       %{name}(%{sover})(Ui)
# libqmmp0-plugins & qmmp-plugin-pack-simple-ui were last used in openSUSE 13.2 (in PMBS).
Provides:       %{name}-plugin-pack-simple-ui = %{version}
Obsoletes:      %{name}-plugin-pack-simple-ui < %{version}
Obsoletes:      lib%{name}0-plugins < %{version}

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
%autosetup -p1

%build
%cmake_qt6 \
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
%qt6_build

%install
%qt6_install

# Do not install weirdly-sized icons.
rm -r %{buildroot}/%{_datadir}/icons/hicolor/56x56

%post -n lib%{name}%{sover} -p /sbin/ldconfig

%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/solid/

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
