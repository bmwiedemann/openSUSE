#
# spec file for package audacious-plugins
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define aud_ver_min 3.10.1
%define aud_ver_max 3.10.99
%bcond_with faad
Name:           audacious-plugins
Version:        3.10.1
Release:        0
Summary:        Plugins for Audacious
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-only AND MIT AND BSD-2-Clause
Group:          Productivity/Multimedia/Sound/Players
Url:            https://audacious-media-player.org/
Source:         https://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.5
BuildRequires:  libmp3lame-devel
BuildRequires:  lirc-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.2
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(alsa) >= 1.0.16
BuildRequires:  pkgconfig(audacious) >= %{aud_ver_min}
BuildRequires:  pkgconfig(dbus-1) >= 0.60
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.60
BuildRequires:  pkgconfig(flac) >= 1.2.1
BuildRequires:  pkgconfig(fluidsynth) >= 1.0.6
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.26
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.32
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.32
BuildRequires:  pkgconfig(gtk+-2.0)
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
BuildRequires:  pkgconfig(libmpg123) >= 1.12
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libpulse) >= 0.9.5
BuildRequires:  pkgconfig(libsidplayfp) >= 1.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(neon) >= 0.27
BuildRequires:  pkgconfig(ogg) >= 1.0
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2) >= 2.0
BuildRequires:  pkgconfig(sndfile) >= 0.19
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(vorbis) >= 1.0
BuildRequires:  pkgconfig(vorbisenc) >= 1.0
BuildRequires:  pkgconfig(vorbisfile) >= 1.0
BuildRequires:  pkgconfig(wavpack) >= 4.31
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
Requires:       libaudcore%{?_isa} <= %{aud_ver_max}
Requires:       libaudcore%{?_isa} >= %{aud_ver_min}
Recommends:     %{name}-extra
Recommends:     %{name}-lang
%if %{with faad}
BuildRequires:  libfaad-devel
%endif

%description
Plugins for the Audacious audio player.

%lang_package

%package extra
Summary:        Extra plugins for Audacious
License:        GPL-2.0-or-later AND MIT AND BSD-2-Clause
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description extra
Extra plugins for the Audacious audio player.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --enable-qt       \
  --enable-gtk      \
%ifarch %arm aarch64
  --disable-glspectrum \
  --disable-qtglspectrum \
%endif
%if %{with faad}
  --enable-aac     \
%else
  --disable-aac    \
%endif
  --enable-mpg123
make %{?_smp_mflags} V=1

%install
%make_install
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
