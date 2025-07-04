#
# spec file for package audacity
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


%bcond_with vst3

Name:           audacity
Version:        3.7.4
Release:        0
Summary:        A Multi Track Digital Audio Editor
License:        CC-BY-3.0 AND GPL-2.0-or-later AND GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://audacityteam.org/
Source:         https://github.com/audacity/audacity/archive/Audacity-%{version}.tar.gz
Source1:        audacity-license-nyquist
Source2:        audacity-rpmlintrc
%if %{with vst3}
#Source3:        vst3sdk-3.7.12_build_20.tar.xz
%endif
# PATCH-FIX-OPENSUSE audacity-no_buildstamp.patch davejplater@gmail.com -- Remove the buildstamp.
Patch0:         audacity-no_buildstamp.patch
# PATCH-FIX-UPSTREAM audacity-no_return_in_nonvoid.patch - Fix false positive errors Two new gcc10 ones ignoring assert
Patch1:         audacity-no_return_in_nonvoid.patch
# PATCH-FIX-OPENSUSE vst-system-path.patch - search fo vsts in /usr/lib64 in x86_64 and ARM system
Patch2:         Use-full-function-prototypes-in-libnyquist.patch
Patch3:         lib64-plugins-default-path.patch
BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
#!BuildIgnore:  gstreamer-0_10-plugins-base
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmp3lame-devel
BuildRequires:  portmidi-devel
BuildRequires:  wxWidgets-3_2-nostl-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac) >= 1.3.1
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec) >= 51.53
BuildRequires:  pkgconfig(libavformat) >= 52.12
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(lilv-0) >= 0.24.6
BuildRequires:  pkgconfig(lv2) >= 1.16.0
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(serd-0) >= 0.30.2
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0) >= 0.16.4
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(sratom-0) >= 0.6.4
BuildRequires:  pkgconfig(suil-0)  >= 0.10.6
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vamp-hostsdk)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon-x11)
# WARNING lilv-0 >= 0.24.6;lv2 >= 1.16.0;serd-0 >= 0.30.2;sord-0 >= 0.16.4;sratom-0 >= 0.6.4;suil-0 >= 0.10.6
# check these versions after every update otherwise audacity builds libsuil itself.

# This would require to patch our portaudio package with "PortMixer"... an extra API that never got integrated in PortAudio.
#BuildRequires:  portaudio-devel
Recommends:     %{name}-lang
# Nothing provides libavutil without a suffix
Requires:       ffmpeg
Requires:       libmp3lame0
Provides:       %{name}-plugins = %{version}
Obsoletes:      %{name}-plugins <= 2.4.2
# pipewire-libjack-0_3 replaces jack and when audacity loads it
# causes a sigsev See https://bugzilla.suse.com/show_bug.cgi?id=1191585
#Conflicts:      pipewire-libjack-0_3
#Doesn't build for 32 bit anymore
#error All sample block data is little endian...big endian not yet supported
ExcludeArch:    i586 s390x

%description
Audacity is a program that manipulates digital audio wave forms.
In addition to multitrack recording capabilities with effects, it
imports and exports many sound file formats, including WAV, AIFF,
AU, IRCAM, MP, and Ogg Vorbis. Wave data larger than the available
physical memory size can be edited.

%lang_package

%prep
%setup -q -n %{name}-Audacity-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%ifarch x86_64 aarch64
%patch -P 3 -p1
%endif

cp -f %{SOURCE1} LICENSE_NYQUIST.txt
# Make sure we use the system versions.
rm -rf lib-src/{expat,libvamp,libsoxr,ffmpeg,lame}/

#Included in src/AboutDialog.cpp but not supplied
touch include/RevisionIdent.h

%if %{with vst3}
tar xf %{SOURCE3} --strip-components=1 --one-top-level=vst3sdk
%endif

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
if ! test -e %{_libdir}/pkgconfig/lame.pc
then
export PKG_CONFIG_PATH="`echo $PWD`:%{_libdir}/pkgconfig"
fi
export CFLAGS="%{optflags} -fno-strict-aliasing -ggdb $(wx-config --cflags)"

%cmake  \
       -DAUDACITY_REV_TIME=$(date -u -d "@${SOURCE_DATE_EPOCH}" "+%Y-%m-%dT%H:%M:%SZ") \
       -DAUDACITY_REV_LONG=%{version} \
       -DAUDACITY_BUILD_LEVEL=2 \
       -DCMAKE_MODULE_LINKER_FLAGS:STRING="$(wx-config --libs)" \
       -DCMAKE_SHARED_LINKER_FLAGS:STRING="$(wx-config --libs)" \
       -Daudacity_conan_enabled=Off \
       -Daudacity_has_networking:BOOL=Off \
       -Daudacity_lib_preference:STRING=system \
       -Duse_lame:STRING=system \
       -Daudacity_use_ffmpeg:STRING=loaded \
%if %{without vst3}
       -Daudacity_has_vst3=off \
%endif
       -DVST3_DEFAULT_INSTALL_PATH=%{_libdir}/vst3/

%cmake_build

%install
%cmake_install

# E-mail wrote to feedback@audacityteam.org.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/
mv -f %{buildroot}%{_datadir}/pixmaps/gnome-mime-application-x-audacity-project.xpm \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-audacity-project.xpm
rm -rf %{buildroot}%{_datadir}/pixmaps/
rm -rf %{buildroot}%{_datadir}/doc

%find_lang %{name}

%post
ldconfig %{_libdir}/%{name}
%end

%postun
ldconfig %{_libdir}/%{name}
%end

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE.txt LICENSE_NYQUIST.txt
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_libdir}/%{name}/modules/mod-script-pipe.so
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
