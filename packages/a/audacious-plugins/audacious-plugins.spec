#
# spec file for package audacious-plugins
#
# Copyright (c) 2023 SUSE LLC
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


%define __provides_exclude_from ^%{_libdir}/audacious/*/.*.so$
%define aud_ver_min 4.3
%define aud_ver_max 4.3.99
%bcond_with faad
Name:           audacious-plugins
Version:        4.3
Release:        0
Summary:        Plugins for Audacious
License:        BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-only AND MIT
URL:            https://audacious-media-player.org/
Source:         https://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE fix-linking-mpg123.patch boo#1187525
Patch0:         fix-linking-mpg123.patch
# PATCH-FIX-UPSTREAM audacious-plugins-fix-qt6-qthotkey.patch sor.alexei@meowr.ru -- Fix Qt6 support in qthotkey.
Patch1:         audacious-plugins-fix-qt6-qthotkey.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libmp3lame-devel
BuildRequires:  lirc-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  sndio-devel
BuildRequires:  pkgconfig(alsa) >= 1.0.16
BuildRequires:  pkgconfig(audacious) >= %{aud_ver_min}
BuildRequires:  pkgconfig(flac) >= 1.2.1
BuildRequires:  pkgconfig(fluidsynth) >= 1.0.6
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack) >= 1.9.7
BuildRequires:  pkgconfig(libavcodec) >= 53.40.0
BuildRequires:  pkgconfig(libavformat) >= 53.25.0
BuildRequires:  pkgconfig(libavutil) >= 51.27.0
BuildRequires:  pkgconfig(libbs2b) >= 3.0.0
BuildRequires:  pkgconfig(libcddb) >= 1.2.1
BuildRequires:  pkgconfig(libcdio) >= 0.70
BuildRequires:  pkgconfig(libcdio_cdda) >= 0.70
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(libcurl) >= 7.9.7
BuildRequires:  pkgconfig(libmms) >= 0.3
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmpg123) >= 1.12
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpulse) >= 0.9.5
BuildRequires:  pkgconfig(libsidplayfp) >= 2.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(neon) >= 0.27
BuildRequires:  pkgconfig(ogg) >= 1.0
BuildRequires:  pkgconfig(opus) >= 1.0.1
BuildRequires:  pkgconfig(opusfile) >= 0.4
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2) >= 2.0
BuildRequires:  pkgconfig(sndfile) >= 0.19
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile) >= 1.0
BuildRequires:  pkgconfig(wavpack) >= 4.31
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
Requires:       libaudcore%{?_isa} <= %{aud_ver_max}
Requires:       libaudcore%{?_isa} >= %{aud_ver_min}
Recommends:     %{name}-extra
%if 0%{?suse_version} > 1500
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libpipewire-0.3)
%else
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
%endif
%if %{with faad}
BuildRequires:  libfaad-devel
%endif

%description
Plugins for the Audacious audio player.

%lang_package

%package extra
Summary:        Extra plugins for Audacious
License:        BSD-2-Clause AND GPL-2.0-or-later AND MIT
Requires:       %{name} = %{version}

%description extra
Extra plugins for the Audacious audio player.

%prep
%autosetup -p1

%build
%meson \
  -Dqt=true     \
%if 0%{?suse_version} > 1500
  -Dqt6=true  \
%else
  -Dqt6=false \
%endif
  -Dgtk=true    \
  -Dgtk3=true   \
%ifarch %{arm} aarch64
  -Dgl-spectrum=false \
%endif
%if %{with faad}
  -Daac=true   \
%else
  -Daac=false  \
%endif
  -Dmpg123=true
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/

%files
%license COPYING
%{_libdir}/audacious/
%if %{with faad}
%exclude %{_libdir}/audacious/Input/aac-raw.so
%endif
%exclude %{_libdir}/audacious/Output/filewriter.so
%{_datadir}/audacious/

%files lang -f %{name}.lang

%files extra
%if %{with faad}
%{_libdir}/audacious/Input/aac-raw.so
%endif
%{_libdir}/audacious/Output/filewriter.so

%changelog
