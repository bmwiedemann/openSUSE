#
# spec file for package audacity
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


%if 0%{?suse_version} >= 1330 || 0%{?leap_version} >= 420300
%bcond_without mad
%else
%bcond_with mad
%endif

Name:           audacity
Version:        2.3.3
Release:        0
Summary:        A Multi Track Digital Audio Editor
License:        GPL-2.0-or-later
Group:          Multimedia;Sound Editors;Audio Editors;Audio Effects;
Url:            http://audacityteam.org/
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
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
#Audacity only builds with gcc >= 4.9
# WARNING: Anything built against wxWidgets with gcc >= 5 needs widgets built with relax-abi.diff and gcc >= 5
%if 0%{?suse_version} == 1315
BuildRequires:  cpp7
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif
#!BuildIgnore:  gstreamer-0_10-plugins-base
BuildRequires:  hicolor-icon-theme
BuildRequires:  wxWidgets-3_0-nostl-devel
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
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(suil-0) >= 0.8.2
BuildRequires:  pkgconfig(vamp-hostsdk)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
%if %{with mad}
BuildRequires:  libmp3lame-devel
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(twolame)
%endif
# This would require to patch our portaudio package with "PortMixer"... an extra API that never got integrated in PortAudio.
#BuildRequires:  portaudio-devel
Recommends:     %{name}-lang
# WARNING Nothing provides libavutil without a suffix
Requires:       ffmpeg
Recommends:     libmp3lame0
Requires:       libFLAC++6 >= 1.3.1
Requires:       libFLAC8 >= 1.3.1

%description
Audacity is a program that manipulates digital audio wave forms.
In addition to multitrack recording capabilities with effects, it
imports and exports many sound file formats, including WAV, AIFF,
AU, IRCAM, MP, and Ogg Vorbis. Wave data larger than the available
physical memory size can be edited.

%lang_package

%prep
%setup -q -n %{name}-Audacity-%{version}
%patch0
%patch1 -p0
%patch3 -p0
%patch2

cp -f %{SOURCE1} LICENSE_NYQUIST.txt
# Make sure we use the system versions.
rm -rf lib-src/{expat,libvamp,libsoxr,ffmpeg}/
%if %{with mad}
rm -rf lib-src/lame
%endif

%build
%if 0%{suse_version} == 1315
# WARNING: Do not alter, only for Leap.
export CC="%{_bindir}/gcc-7"
export CXX="%{_bindir}/g++-7"
export CPP="%{_bindir}/cpp-7"
%endif

export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS -std=gnu++11"
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
%if %{with mad}
  --with-libmad=system \
  --with-libtwolame=system \
  --with-lame=system \
%else
  --without-libmad \
  --without-libtwolame \
%endif
  --docdir=%{_docdir}/%{name}/

make %{?_smp_mflags}

%install
%make_install

# E-mail wrote to feedback@audacityteam.org.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/
mv -f %{buildroot}%{_datadir}/pixmaps/gnome-mime-application-x-audacity-project.xpm \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-audacity-project.xpm
rm -rf %{buildroot}%{_datadir}/pixmaps/
rm %{buildroot}%{_docdir}/%{name}/LICENSE.txt
%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%defattr(-,root,root)
%doc README.txt
%license LICENSE.txt LICENSE_NYQUIST.txt
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
