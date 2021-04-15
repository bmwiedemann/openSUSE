#
# spec file for package deadbeef
#
# Copyright (c) 2021 SUSE LLC
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


# LTO breaks compiler test at configure stage,
# which is bad since Clang is the only suported compiler now.
%define _lto_cflags %{nil}
%bcond_with restricted
Name:           deadbeef
Version:        1.8.7
Release:        0
Summary:        GTK+ audio player
License:        Zlib AND GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Players
URL:            https://deadbeef.sourceforge.io/
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}.appdata.xml
# PATCH-FIX-OPENSUSE 0003-Fix-operator-precedence-and-uninitialized-value-warn.patch
Patch0:         0003-Fix-operator-precedence-and-uninitialized-value-warn.patch
# PATCH-FIX-OPENSUSE deadbeef-drop-documents-installation.patch hillwood@opensuse.org -- Install documents by rpmbuild.
Patch2:         %{name}-drop-documents-installation.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  clang
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libdispatch-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yasm
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
%if %{with restricted}
BuildRequires:  libfaad-devel
Requires:       %{name}-plugins-extra = %{version}-%{release}
%else
Recommends:     %{name}-plugins-extra = %{version}
%endif

%description
DeaDBeeF is an audio player using GTK+. Through use of the ffmpeg
libraries, it supports many formats. It also supports cuesheets,
chiptune formats with subtunes, song-length databases. It can be
extended using plugins (DSP, GUI, output, input, etc.). The GUI looks
similar to Foobar2000.

%lang_package

%if %{with restricted}
%package plugins-extra
Summary:        Extra plugins for DeaDBeeF
License:        Zlib AND GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND Unicode AND NonFree
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}
Recommends:     faac
Obsoletes:      %{name}-restricted-plugins < %{version}
Provides:       %{name}-restricted-plugins = %{version}-%{version}

%description plugins-extra
Extra plugins for DeaDBeeF audio player.
%endif

%package devel
Summary:        Development files for %{name}
License:        Zlib
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package provides headers for DeaDBeeF plugins development.

%prep
%autosetup -n %{name}-%{version} -p1

cp %{SOURCE1} %{name}.appdata.xml

%build
export CC=clang
export CXX=clang++
export CFLAGS="%{optflags} -fno-strict-aliasing -fpie -fPIC"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="$LDFLAGS -pie"

NOCONFIGURE=1 ./autogen.sh
%configure \
        --disable-static \
%ifarch %{ix86}
        --disable-soundtouch \
%endif
        --disable-psf
%make_build

%install
%make_install
rm -rf %{buildroot}%{_libexecdir}/debug/%{_libdir}/%{name}/ddb_soundtouch.so*
install -Dpm 0644 %{name}.appdata.xml \
%{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%suse_update_desktop_file %{name}
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
%fdupes -s %{buildroot}%{_libdir}/%{name}/data68/Replay

%files
%doc README README.md help.txt about.txt translators.txt CONTRIBUTING.md
%doc AUTHORS ChangeLog translation/help.ru.txt ABOUT-NLS
%license COPYING COPYING.GPLv2 COPYING.LGPLv2.1
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/adplug.so*
%{_libdir}/%{name}/alsa.so*
%{_libdir}/%{name}/artwork.so*
%{_libdir}/%{name}/cdda.so*
%{_libdir}/%{name}/ffap.so*
%{_libdir}/%{name}/ffmpeg.so*
%{_libdir}/%{name}/flac.so*
%{_libdir}/%{name}/gme.so*
%{_libdir}/%{name}/hotkeys.so*
%{_libdir}/%{name}/lastfm.so*
%{_libdir}/%{name}/notify.so*
%{_libdir}/%{name}/nullout.so*
%{_libdir}/%{name}/oss.so*
%{_libdir}/%{name}/pulse.so*
%{_libdir}/%{name}/rg_scanner.so*
%{_libdir}/%{name}/sid.so*
%{_libdir}/%{name}/sndfile.so*
%{_libdir}/%{name}/supereq.so*
%{_libdir}/%{name}/vfs_curl.so*
%{_libdir}/%{name}/vorbis.so*
%{_libdir}/%{name}/vtx.so*
%{_libdir}/%{name}/wavpack.so*
%{_libdir}/%{name}/wma.so*
%{_libdir}/%{name}/dca.so*
%{_libdir}/%{name}/mms.so*
%{_libdir}/%{name}/musepack.so*
%{_libdir}/%{name}/opus.so*
%{_libdir}/%{name}/shellexec.so*
%{_libdir}/%{name}/tta.so*
%{_libdir}/%{name}/wildmidi.so*
%{_libdir}/%{name}/converter.so*
%{_libdir}/%{name}/dsp_libsrc.so*
%{_libdir}/%{name}/m3u.so*
%{_libdir}/%{name}/mp3.so*
%{_libdir}/%{name}/vfs_zip.so*
%{_libdir}/%{name}/ddb_dumb.so*
%{_libdir}/%{name}/ddb_mono2stereo.so*
%{_libdir}/%{name}/ddb_shn.so*
%ifnarch %{ix86}
%{_libdir}/%{name}/ddb_soundtouch.so*
%endif
%{_libdir}/%{name}/alac.so*
%{_libdir}/%{name}/in_sc68.so*
%{_libdir}/%{name}/data68/
%{_libdir}/%{name}/converter_gtk?.so*
%{_libdir}/%{name}/ddb_gui_GTK?.so*
%{_libdir}/%{name}/pltbrowser_gtk?.so*
%{_libdir}/%{name}/shellexecui_gtk?.so*
%{_libdir}/%{name}/convpresets/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml

%files lang -f %{name}.lang

%if %{with restricted}
%files plugins-extra
%{_libdir}/%{name}/aac.so*
%endif

%files devel
%{_includedir}/%{name}/

%changelog
