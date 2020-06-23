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
Version:        2.4.1
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
# PATCH-FIX-OPENSUSE audacity-flacversion.patch davejplater@gmail.com -- Patch to fix build against libflac 1.3.1+.
Patch1:         audacity-flacversion.patch
Patch2:         audacity-misc-errors.patch
# PATCH-FIX-UPSTREAM audacity-no_return_in_nonvoid.patch
Patch3:         audacity-no_return_in_nonvoid.patch
# PATCH-FIX-OPENSUSE audacity-implicit-fortify-decl.patch davejplater@gmail.com -- Leap:15.1's build misses "UNIX" definition in nyquist/xlisp/security.c
Patch4:         audacity-implicit-fortify-decl.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
#!BuildIgnore:  gstreamer-0_10-plugins-base
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmp3lame-devel
BuildRequires:  libwx_gtk3u_core-suse-nostl3_1_3
BuildRequires:  wxWidgets-3_2-nostl-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac) >= 1.3.1
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec) >= 51.53
BuildRequires:  pkgconfig(libavformat) >= 52.12
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(lilv-0) >= 0.16
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(suil-0) >= 0.8.2
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vamp-hostsdk)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
# This would require to patch our portaudio package with "PortMixer"... an extra API that never got integrated in PortAudio.
#BuildRequires:  portaudio-devel
Recommends:     %{name}-lang
# WARNING Nothing provides libavutil without a suffix
Requires:       ffmpeg
Recommends:     libmp3lame0
Requires:       %{name}-plugins = %{version}
Requires:       libFLAC++6 >= 1.3.1
Requires:       libFLAC8 >= 1.3.1

%description
Audacity is a program that manipulates digital audio wave forms.
In addition to multitrack recording capabilities with effects, it
imports and exports many sound file formats, including WAV, AIFF,
AU, IRCAM, MP, and Ogg Vorbis. Wave data larger than the available
physical memory size can be edited.

%lang_package

%package plugins
Summary:        Enhancments for Audacity
Group:          Productivity/Multimedia/Sound
Requires:       %{name} =  %{version}

%description plugins
This package contains extra plugins for audacity.


%prep
%setup -q -n %{name}-Audacity-%{version}
%autopatch -p1

cp -f %{SOURCE1} LICENSE_NYQUIST.txt
# Make sure we use the system versions.
rm -rf lib-src/{expat,libvamp,libsoxr,ffmpeg,lame}/

%build
export CFLAGS="%{optflags} -fno-strict-aliasing -ggdb"
export CXXFLAGS="$CFLAGS -std=gnu++11"
%if 1 == 1
aclocal -I m4
autoconf
%configure \
%ifnarch %ix86 x86_64
  --disable-sse                \
%endif
%if 0%{?suse_version} > 1501
  --disable-dynamic-loading \
  %endif
  --with-ffmpeg=system \
  --with-libmad=system \
  --with-libtwolame=system \
  --with-lame=system \
  --docdir=%{_docdir}/%{name}/
%else
%cmake
%endif

make %{?_smp_mflags}

%install
%make_install

# E-mail wrote to feedback@audacityteam.org.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/
mv -f %{buildroot}%{_datadir}/pixmaps/gnome-mime-application-x-audacity-project.xpm \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-audacity-project.xpm
rm -rf %{buildroot}%{_datadir}/pixmaps/
rm %{buildroot}%{_docdir}/%{name}/LICENSE.txt
cp -v lib-src/portmixer/LICENSE.txt portmixer.LICENSE.txt
%find_lang %{name}

%files plugins
%license LICENSE.txt
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libsuil*.so

%files
%defattr(-,root,root)
%doc README.txt
%license LICENSE.txt LICENSE_NYQUIST.txt portmixer.LICENSE.txt
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/*%{name}*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
