#
# spec file for package audacity
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


Name:           audacity
Version:        2.4.2
Release:        0
Summary:        A Multi Track Digital Audio Editor
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound
URL:            http://audacityteam.org/
Source:         https://github.com/audacity/audacity/archive/Audacity-%{version}.tar.gz
#Source:         https://www.fosshub.com/Audacity.html/%%{name}-minsrc-%%{version}.tar.xz
Source1:        audacity-license-nyquist
Source2:        audacity-rpmlintrc
# PATCH-FIX-OPENSUSE audacity-no_buildstamp.patch davejplater@gmail.com -- Remove the buildstamp.
Patch0:         audacity-no_buildstamp.patch
Patch2:         audacity-misc-errors.patch
# PATCH-FIX-UPSTREAM audacity-no_return_in_nonvoid.patch - Fix false positive errors Two new gcc10 ones ignoring assert
Patch3:         audacity-no_return_in_nonvoid.patch
BuildRequires:  cmake >= 3.15
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
#!BuildIgnore:  gstreamer-0_10-plugins-base
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmp3lame-devel
%if 0%{?suse_version} && 0%{?suse_version} > 1520
BuildRequires:  wxWidgets-3_2-nostl-devel
%else
BuildRequires:  wxWidgets-3_0-nostl-devel
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac) >= 1.3.1
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec) >= 51.53
BuildRequires:  pkgconfig(libavformat) >= 52.12
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(lilv-0) >= 0.24.6
BuildRequires:  pkgconfig(lv2) >= 1.16.0
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(serd-0) >= 0.30.2
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0) >= 0.16.4
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(sratom-0) >= 0.6.4
BuildRequires:  pkgconfig(suil-0)  >= 0.10.6
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vamp-hostsdk)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
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
#Doesn't build for 32 bit anymore
ExcludeArch:    i586

%description
Audacity is a program that manipulates digital audio wave forms.
In addition to multitrack recording capabilities with effects, it
imports and exports many sound file formats, including WAV, AIFF,
AU, IRCAM, MP, and Ogg Vorbis. Wave data larger than the available
physical memory size can be edited.

%lang_package

%prep
%setup -q -n %{name}-Audacity-%{version}
%autopatch -p1

cp -f %{SOURCE1} LICENSE_NYQUIST.txt
# Make sure we use the system versions.
rm -rf lib-src/{expat,libvamp,libsoxr,ffmpeg,lame}/
# Audacity's cmake can't find libmp3lame without a .pc file
# This is a temporary workaround.
if ! test -e %{_libdir}/pkgconfig/lame.pc
then
echo "creating lame.pc"
cat << EOF > lame.pc
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/lame

Name: mp3lame
Description: encoder that converts audio to the MP3 file format.
Version: 3.100
Libs: -L${libdir} -lmp3lame
Cflags: -I${includedir}
EOF
fi

#Included in src/AboutDialog.cpp but not supplied
touch include/RevisionIdent.h

%build
if ! test -e %{_libdir}/pkgconfig/lame.pc
then
export PKG_CONFIG_PATH="`echo $PWD`:%{_libdir}/pkgconfig"
fi
export CFLAGS="%{optflags} -fno-strict-aliasing -ggdb"
export CXXFLAGS="$CFLAGS -std=gnu++11"
%cmake \
       -Duse_lame:STRING=system \
       -Daudacity_use_ffmpeg:STRING=linked

make %{?_smp_mflags}

%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}/%{name}
find %{buildroot}%{_datadir} -name "*.so" -print -exec mv {} %{buildroot}%{_libdir}/%{name}/ \;

# E-mail wrote to feedback@audacityteam.org.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/
mv -f %{buildroot}%{_datadir}/pixmaps/gnome-mime-application-x-audacity-project.xpm \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-audacity-project.xpm
rm -rf %{buildroot}%{_datadir}/pixmaps/
rm -rf %{buildroot}%{_datadir}/doc
cp -v lib-src/portmixer/LICENSE.txt portmixer.LICENSE.txt

%find_lang %{name}

%files
%defattr(-,root,root)
%doc README.txt
%license LICENSE.txt LICENSE_NYQUIST.txt portmixer.LICENSE.txt
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/mod-script-pipe.so
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
