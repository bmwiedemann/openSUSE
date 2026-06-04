#
# spec file for package deadbeef
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


# LTO breaks compiler test at configure stage,
# which is bad since Clang is the only suported compiler now.
%define _lto_cflags %{nil}
%bcond_with restricted
Name:           deadbeef
Version:        1.10.2
Release:        0
Summary:        GTK+ audio player
License:        BSD-3-Clause AND GPL-2.0-or-later AND Zlib AND LGPL-2.1-or-later
URL:            https://deadbeef.sourceforge.io/
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.appdata.xml
# PATCH-FIX-OPENSUSE 0003-Fix-operator-precedence-and-uninitialized-value-warn.patch
Patch0:         0003-Fix-operator-precedence-and-uninitialized-value-warn.patch
ExclusiveArch:  aarch64 ppc64le x86_64 i586
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
BuildRequires:  pkgconfig(faad2)
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
BuildRequires:  pkgconfig(libpipewire-0.3)
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
Obsoletes:      %{name}-plugins-extra < %{version}-%{release}
Obsoletes:      %{name}-restricted-plugins < %{version}-%{release}
Provides:       %{name}-plugins-extra = %{version}-%{release}
Provides:       %{name}-restricted-plugins = %{version}-%{version}
Obsoletes:      deadbeef-plugin-mpris2 <= 1.16
Provides:       deadbeef-plugin-mpris2 = 1.16.1

%description
DeaDBeeF is an audio player using GTK+. Through use of the ffmpeg
libraries, it supports many formats. It also supports cuesheets,
chiptune formats with subtunes, song-length databases. It can be
extended using plugins (DSP, GUI, output, input, etc.). The GUI looks
similar to Foobar2000.

%lang_package

%package devel
Summary:        Development files for %{name}
License:        Zlib
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel
This package provides headers for DeaDBeeF plugins development.

%prep
%autosetup -n %{name}-%{version} -p1

cp %{SOURCE1} %{name}.appdata.xml

# Drop hardcoded -msse3
sed -i "s/-msse3//" ./external/ddb_dsp_libretro/Makefile.*

%build
export CC=clang
export CXX=clang++
export CFLAGS="%{optflags} -fno-strict-aliasing -Wno-error=unused-variable -Wno-unused-command-line-argument -Wno-unused-but-set-variable -fpie -fPIC"
export CXXFLAGS="$CFLAGS"
# libdispatch-devel puts Block.h in non standard directory
export CFLAGS="$CFLAGS -I%{_includedir}/block"
export LDFLAGS="$LDFLAGS -pie"

%configure \
%ifarch %{ix86}
        --disable-soundtouch \
%endif
        --disable-static \
        --disable-psf \
        --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
rm -rf %{buildroot}%{_libexecdir}/debug/%{_libdir}/%{name}/{ddb_soundtouch,mpris}.so*
rm -rf %{buildroot}%{_docdir}/%{name}
install -Dpm 0644 %{name}.appdata.xml \
%{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%suse_update_desktop_file %{name}
%suse_update_desktop_file %{name}_enqueue
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
%fdupes -s %{buildroot}%{_libdir}/%{name}/data68/Replay

%files
%doc README help.txt about.txt translators.txt ChangeLog
%license COPYING COPYING.GPLv2 COPYING.LGPLv2.1
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/aac.so*
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
%{_libdir}/%{name}/mpris.so*
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
%{_libdir}/%{name}/ddb_dsp_libretro.so*
%{_libdir}/%{name}/ddb_mono2stereo.so*
%{_libdir}/%{name}/ddb_out_pw.so*
%{_libdir}/%{name}/ddb_shn.so*
%{_libdir}/%{name}/medialib.so*
%ifnarch %{ix86}
%{_libdir}/%{name}/ddb_soundtouch.so*
%endif
%{_libdir}/%{name}/alac.so*
%{_libdir}/%{name}/in_sc68.so*
%{_libdir}/%{name}/data68/
%{_libdir}/%{name}/converter_gtk?.so*
%{_libdir}/%{name}/ddb_gui_GTK?.so*
%{_libdir}/%{name}/lyrics_gtk?.so*
%{_libdir}/%{name}/pltbrowser_gtk?.so*
%{_libdir}/%{name}/shellexecui_gtk?.so*
%{_libdir}/%{name}/convpresets/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_enqueue.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml

%files lang -f %{name}.lang

%files devel
%{_includedir}/%{name}/

%changelog
