#
# spec file for package cmus
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007-2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%bcond_without sndio

Name:           cmus
Version:        2.8.0~20190219.ge27e813
Release:        0
Summary:        Text-mode music player
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Sound/Players
Url:            https://cmus.github.io/
Source:         %{name}-%{version}.tar.xz
# cmus only builds with gcc >= 4.9
%if 0%{?suse_version} > 1320
BuildRequires:  gcc
%else
%if 0%{?sle_version} == 120200
# Leap 42.2
BuildRequires:  gcc6
%else
# Leap 42.3+ / SLE12SP3Backports
BuildRequires:  gcc7
%endif
%endif
BuildRequires:  git-core
BuildRequires:  libmpcdec-devel
BuildRequires:  pkgconfig
%if %{with sndio}
BuildRequires:  sndio-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa) >= 1.0.11
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(libdiscid)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libpulse) >= 0.9.19
BuildRequires:  pkgconfig(libsystemd)
# BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
Recommends:     %{name}-plugin-cue = %{version}-%{release}
Recommends:     %{name}-plugin-ffmpeg = %{version}-%{release}
# cmus has problems with lavf and 24-bit audio
Recommends:     %{name}-plugin-flac = %{version}-%{release}
# these are not provided by tumbleweed ffmpeg yet
Recommends:     %{name}-plugin-mpc = %{version}-%{release}
Recommends:     %{name}-plugin-pulse = %{version}-%{release}
Recommends:     %{name}-plugin-wavpack = %{version}-%{release}

%description
C* Music Player is a small and fast text mode (ncurses-based) music player
for Unix-like operating systems.

%package plugin-libao
Summary:        Libao output plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-libao
This package provides libao output support for the C* Music Player.

%package plugin-jack
Summary:        JACK output plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-jack
This package provides JACK output support for the C* Music Player.

%package plugin-pulse
Summary:        Pulseaudio output plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-pulse
This package provides PulseAudio output support for the C* Music Player.

%if %{with sndio}
%package plugin-sndio
Summary:        Sndio output plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-sndio
This package provides sndio output support for the C* Music Player.
%endif

%package plugin-cdio
Summary:        CDIO plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-cdio
This package provides CDIO support for the C* Music Player.

%package plugin-cue
Summary:        CUE input plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-cue
This package provides CUE sheet support for the C* Music Player.

%package plugin-ffmpeg
Summary:        FFmpeg input plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-plugin-aac
Obsoletes:      %{name}-plugin-mad

%description plugin-ffmpeg
This package provides FFmpeg input support for the C* Music Player.

%package plugin-flac
Summary:        FLAC input plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-flac
This package provides FLAC input support for the C* Music Player.

%package plugin-vorbis
Summary:        Vorbis input plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-vorbis
This package provides Vorbis input support for the C* Music Player.

%package plugin-mikmod
Summary:        MikMod input plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-mikmod
This package provides MikMod (tracker) input support for the C* Music Player.

%package plugin-modplug
Summary:        Modplug input plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-modplug
This package provides modplug (tracker) input support for the C* Music Player.

%package plugin-mpc
Summary:        MPC (Musepack) input plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-mpc
This package provides MPC (Musepack) input support for the C* Music Player.

%package plugin-opus
Summary:        Opus input plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-opus
This package provides Opus input support for the C* Music Player.

%package plugin-wavpack
Summary:        WavPack input plugin for the C* Music Player
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description plugin-wavpack
This package provides WavPack input support for the C* Music Player.

%package plugins-all
Summary:        Installs all %{name} plugins
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-plugin-cdio = %{version}-%{release}
Requires:       %{name}-plugin-cue = %{version}-%{release}
Requires:       %{name}-plugin-ffmpeg = %{version}-%{release}
Requires:       %{name}-plugin-flac = %{version}-%{release}
Requires:       %{name}-plugin-jack = %{version}-%{release}
Requires:       %{name}-plugin-libao = %{version}-%{release}
Requires:       %{name}-plugin-mikmod = %{version}-%{release}
Requires:       %{name}-plugin-modplug = %{version}-%{release}
Requires:       %{name}-plugin-mpc = %{version}-%{release}
Requires:       %{name}-plugin-opus = %{version}-%{release}
Requires:       %{name}-plugin-pulse = %{version}-%{release}
%if %{with sndio}
Requires:       %{name}-plugin-sndio = %{version}-%{release}
%endif
Requires:       %{name}-plugin-vorbis = %{version}-%{release}
Requires:       %{name}-plugin-wavpack = %{version}-%{release}

%description plugins-all
This package pulls in all the plugins for the C* Music Player.

%prep
%setup -q

%build
# not autoconf
export CC=gcc
test -x "$(type -p gcc-5)" && export CC=gcc-5
test -x "$(type -p gcc-6)" && export CC=gcc-6
test -x "$(type -p gcc-7)" && export CC=gcc-7
./configure \
    prefix="%{_prefix}" \
    bindir="%{_bindir}" \
    datadir="%{_datadir}" \
    libdir="%{_libdir}" \
    mandir="%{_mandir}" \
    exampledir="%{_docdir}/%{name}.xxx/examples" \
%if %{with sndio}
    CONFIG_SNDIO=y \
%endif
    CONFIG_{ALSA,AO,CDDB,CDIO,CUE,DISCID,FFMPEG,FLAC,JACK,MIKMOD,MODPLUG,MPC,MPRIS,OPUS,OSS,PULSE,SAMPLERATE,VORBIS,WAVPACK,WAV}=y \
    CONFIG_{AAC,ARTS,COREAUDIO,MAD,BASS,MP4,ROAR,SUN,TREMOR,VTX,WAVEOUT}=n \
    USE_FALLBACK_IP=y \
    CFLAGS="%{optflags}"

make %{?_smp_mflags} V=1 CC=${CC}

%install
%make_install
rm -rfv "%{buildroot}%{_docdir}/%{name}.xxx"
chmod 0644 cmus-status-display

cat<<EOF >README.plugins-all
This subpackage is empty but requires all the available %{name} plugin packages
EOF

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README.md
%doc cmus-status-display
%doc data/rc
%{_bindir}/cmus
%{_bindir}/cmus-remote
%dir %{_libdir}/cmus
%dir %{_libdir}/cmus/ip
%{_libdir}/cmus/ip/wav.so
%dir %{_libdir}/cmus/op
%{_libdir}/cmus/op/alsa.so
%{_libdir}/cmus/op/oss.so
%dir %{_datadir}/cmus
%{_datadir}/cmus/*.theme
%config(noreplace) %{_datadir}/cmus/rc
%{_mandir}/man1/cmus*.1%{ext_man}
%{_mandir}/man7/cmus-tutorial.7%{ext_man}

%files plugin-libao
%defattr(-,root,root)
%{_libdir}/cmus/op/ao.so

%files plugin-jack
%defattr(-,root,root)
%{_libdir}/cmus/op/jack.so

%files plugin-pulse
%defattr(-,root,root)
%{_libdir}/cmus/op/pulse.so

%if %{with sndio}
%files plugin-sndio
%defattr(-,root,root)
%{_libdir}/cmus/op/sndio.so
%endif

%files plugin-cdio
%defattr(-,root,root)
%{_libdir}/cmus/ip/cdio.so

%files plugin-cue
%defattr(-,root,root)
%{_libdir}/cmus/ip/cue.so

%files plugin-flac
%defattr(-,root,root)
%{_libdir}/cmus/ip/flac.so

%files plugin-vorbis
%defattr(-,root,root)
%{_libdir}/cmus/ip/vorbis.so

%files plugin-ffmpeg
%defattr(-,root,root)
%{_libdir}/cmus/ip/ffmpeg.so

%files plugin-mikmod
%defattr(-,root,root)
%{_libdir}/cmus/ip/mikmod.so

%files plugin-modplug
%defattr(-,root,root)
%{_libdir}/cmus/ip/modplug.so

%files plugin-mpc
%defattr(-,root,root)
%{_libdir}/cmus/ip/mpc.so

%files plugin-opus
%defattr(-,root,root)
%{_libdir}/cmus/ip/opus.so

%files plugin-wavpack
%defattr(-,root,root)
%{_libdir}/cmus/ip/wavpack.so

%files plugins-all
%defattr(-,root,root)
%doc README.plugins-all

%changelog
