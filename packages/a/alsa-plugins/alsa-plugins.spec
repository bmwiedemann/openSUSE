#
# spec file for package alsa-plugins
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if 0%{?suse_version} >= 1550
%define build_aaf 1
%else
%define build_aaf 0
%endif

Name:           alsa-plugins
Version:        1.1.9
Release:        0
Summary:        Extra Plug-Ins for the ALSA Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Url:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/plugins/alsa-plugins-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkgconfig(alsa) >= 1.1.6
%if %{build_aaf}
BuildRequires:  pkgconfig(avtp)
%endif
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(jack) >= 0.98
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse) >= 0.9.11
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(speexdsp) >= 1.2
%ifarch s390x
Recommends:     %{name}-32bit = %{version}
%endif

%description
This package contains the extra plug-ins for the ALSA library.

%package jack
Summary:        JACK I/O Plug-In for the ALSA Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       jack
%ifarch s390x
Recommends:     %{name}-jack-32bit = %{version}
%endif

%description jack
This package contains the JACK (Jack Audio Connection Kit) I/O plug-in
for the ALSA library.

%package pulse
Summary:        Pulseaudio Plug-In for the ALSA Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       pulseaudio
%ifarch s390x
Recommends:     %{name}-pulse-32bit = %{version}
%endif

%description pulse
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package contains the polypaudio I/O plug-in for the ALSA library.

%package maemo
Summary:        Maemo Plug-Ins for the ALSA Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description maemo
This package contains the ALSA-library plug-ins using maemo SDK for
Nokia 770.

%package samplerate
Summary:        Samplerate Plug-In for the ALSA Library
License:        GPL-2.0-or-later
Group:          System/Libraries
%ifarch s390x
Recommends:     %{name}-samplerate-32bit = %{version}
%endif

%description samplerate
This package contains the sample rate converter plugin for the ALSA
library using libsamplerate.

%package speex
Summary:        Speex Prerocessor Plug-In for the ALSA Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
%ifarch s390x
Recommends:     %{name}-speex-32bit = %{version}
%endif

%description speex
This package contains the Speex preprocessor plugin for the ALSA
library using libspeexdsp.

%package a52
Summary:        A52 Output Plug-In for the ALSA Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description a52
This package contains the A52 (aka AC3) output plug-in for the ALSA library.

%package lavrate
Summary:        Rate Converter Plug-In for the ALSA Library using libavcodec
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       alsa-plugins-lavcrate = %{version}
Obsoletes:      alsa-plugins-lavcrate < %{version}

%description lavrate
This package contains the sample rate converter plugin for the ALSA
library using libavcodec.

%package aaf
Summary:        AVTP Audio Format PCM Plug-In for the ALSA Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description aaf
This package contains the AVTP AUdio Format (AAF) I/O plug-in
for the ALSA library.

%prep
%setup -q

%build
export AUTOMAKE_JOBS="%{?_smp_mflags}"
# autoreconf -fi
%configure --enable-maemo-plugin --enable-maemo-resource-manager \
    --with-speex=builtin
make %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}
mkdir -p %{buildroot}%{_sysconfdir}/alsa/conf.d
touch %{buildroot}%{_sysconfdir}/alsa/conf.d/99-pulseaudio-default.conf
# modules don't need *.la files
find %{buildroot} -type f -name "*.la" -delete -print

%post pulse
if command -v setup-pulseaudio > /dev/null; then
    setup-pulseaudio --auto
fi
exit 0

%postun pulse
if command -v setup-pulseaudio > /dev/null; then
    setup-pulseaudio --auto
fi
exit 0

%files
%defattr(-, root, root)
%license COPYING
%doc doc/README-pcm-oss
%doc doc/README-arcam-av
%doc doc/upmix.txt
%doc doc/vdownmix.txt
%doc doc/speexrate.txt
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_ctl_oss.so
%{_libdir}/alsa-lib/libasound_module_pcm_oss.so
%{_libdir}/alsa-lib/libasound_module_pcm_upmix.so
%{_libdir}/alsa-lib/libasound_module_pcm_vdownmix.so
%{_libdir}/alsa-lib/libasound_module_pcm_usb_stream.so
%{_libdir}/alsa-lib/libasound_module_rate_speexrate*.so
%{_libdir}/alsa-lib/libasound_module_ctl_arcam_av.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/10-speexrate.conf
%{_datadir}/alsa/alsa.conf.d/50-arcam-av-ctl.conf
%{_datadir}/alsa/alsa.conf.d/50-oss.conf
%{_datadir}/alsa/alsa.conf.d/60-upmix.conf
%{_datadir}/alsa/alsa.conf.d/60-vdownmix.conf
%{_datadir}/alsa/alsa.conf.d/98-usb-stream.conf
%{_sysconfdir}/alsa/conf.d/10-speexrate.conf
%{_sysconfdir}/alsa/conf.d/50-arcam-av-ctl.conf
%{_sysconfdir}/alsa/conf.d/50-oss.conf
%{_sysconfdir}/alsa/conf.d/60-upmix.conf
%{_sysconfdir}/alsa/conf.d/60-vdownmix.conf
%{_sysconfdir}/alsa/conf.d/98-usb-stream.conf

%files jack
%defattr(-, root, root)
%license COPYING
%doc doc/README-jack
%{_libdir}/alsa-lib/libasound_module_pcm_jack.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/50-jack.conf
%{_sysconfdir}/alsa/conf.d/50-jack.conf

%files pulse
%defattr(-, root, root)
%license COPYING
%doc doc/README-pulse
%{_libdir}/alsa-lib/libasound_module_ctl_pulse.so
%{_libdir}/alsa-lib/libasound_module_pcm_pulse.so
%{_libdir}/alsa-lib/libasound_module_conf_pulse.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/50-pulseaudio.conf
%{_sysconfdir}/alsa/conf.d/50-pulseaudio.conf
%{_sysconfdir}/alsa/conf.d/99-pulseaudio-default.conf.example
%ghost %{_sysconfdir}/alsa/conf.d/99-pulseaudio-default.conf

%files maemo
%defattr(-, root, root)
%license COPYING
%doc doc/README-maemo
%{_libdir}/alsa-lib/libasound_module_ctl_dsp_ctl.so
%{_libdir}/alsa-lib/libasound_module_pcm_alsa_dsp.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/98-maemo.conf
%{_sysconfdir}/alsa/conf.d/98-maemo.conf

%files samplerate
%defattr(-, root, root)
%license COPYING.GPL
%doc doc/samplerate.txt
%{_libdir}/alsa-lib/libasound_module_rate_samplerate*.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/10-samplerate.conf
%{_sysconfdir}/alsa/conf.d/10-samplerate.conf

%files speex
%defattr(-, root, root)
%license COPYING
%doc doc/speexdsp.txt
%{_libdir}/alsa-lib/libasound_module_pcm_speex.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/60-speex.conf
%{_sysconfdir}/alsa/conf.d/60-speex.conf

%files a52
%defattr(-, root, root)
%license COPYING
%doc doc/a52.txt
%{_libdir}/alsa-lib/libasound_module_pcm_a52.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/60-a52-encoder.conf
%{_sysconfdir}/alsa/conf.d/60-a52-encoder.conf

%files lavrate
%defattr(-, root, root)
%license COPYING
%doc doc/lavrate.txt
%{_libdir}/alsa-lib/libasound_module_rate_lavrate.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_fast.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_faster.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_high.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_higher.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/10-rate-lav.conf
%{_sysconfdir}/alsa/conf.d/10-rate-lav.conf

%if %{build_aaf}
%files aaf
%defattr(-, root, root)
%license COPYING
# %doc doc/aaf.txt
%{_libdir}/alsa-lib/libasound_module_pcm_aaf.so
%endif

%changelog
