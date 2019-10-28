#
# spec file for package mpg123
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


Name:           mpg123
Version:        1.25.13
Release:        0
Summary:        Console MPEG audio player and decoder library
License:        LGPL-2.1-only
Group:          Productivity/Multimedia/Sound/Players
URL:            http://www.mpg123.de/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2.sig
Source2:        mpg123.keyring
Source3:        baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(openal)
%endif
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sdl)

%description
The mpg123 distribution contains an MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1, 2 and 3 (most commonly MPEG 1.0 Layer 3 aka MP3), as well as re-usable decoding
and output libraries.

%package devel
Summary:        Files to develop against libmpg123
Group:          Development/Languages/C and C++
Requires:       libmpg123-0 = %{version}
Requires:       libout123-0 = %{version}

%description devel
The mpg123 distribution contains an MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1, 2 and 3 (most commonly MPEG 1.0 Layer 3 aka MP3), as well as re-usable decoding
and output libraries.

%package -n libmpg123-0
Summary:        MPEG audio decoder library
Group:          System/Libraries
Obsoletes:      mpg123-esound >= 1.25.7

%description -n libmpg123-0
MPEG 1.0/2.0/2.5 audio decoder library for layers 1, 2 and 3 (most
commonly MPEG 1.0 Layer 3 aka MP3).

%package -n libout123-0
Summary:        MPEG audio decoder library
Group:          System/Libraries

%description -n libout123-0
The mpg123 distribution contains a real time MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1,2 and 3 (most commonly MPEG 1.0 layer 3 aka MP3), as well as re-usable decoding
and output libraries.

%if 0%{?suse_version} >= 1500
%package openal
Summary:        OpenAL Support for %{name}
Group:          Productivity/Multimedia/Sound/Players
Supplements:    openal-soft

%description openal
The mpg123 distribution contains a real time MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1,2 and 3 (most commonly MPEG 1.0 layer 3 aka MP3), as well as re-usable decoding
and output libraries.

This package contains the plugin for openal output support.
%endif

%package pulse
Summary:        Pulseaudio Support for %{name}
Group:          Productivity/Multimedia/Sound/Players
Supplements:    pulseaudio

%description pulse
The mpg123 distribution contains a real time MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1,2 and 3 (most commonly MPEG 1.0 layer 3 aka MP3), as well as re-usable decoding
and output libraries.

This package contains the plugin for Pulseaudio output support.

%package jack
Summary:        Jack Support for %{name}
Group:          Productivity/Multimedia/Sound/Players
Supplements:    jack

%description jack
The mpg123 distribution contains a real time MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1,2 and 3 (most commonly MPEG 1.0 layer 3 aka MP3), as well as re-usable decoding
and output libraries.

This package contains the plugin for JACK output support.

%package portaudio
Summary:        Portaudio Support for %{name}
Group:          Productivity/Multimedia/Sound/Players

%description portaudio
The mpg123 distribution contains a real time MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1,2 and 3 (most commonly MPEG 1.0 layer 3 aka MP3), as well as re-usable decoding
and output libraries.

This package contains the plugin for Portaudio output support.

%package sdl
Summary:        SDL Support for %{name}
Group:          Productivity/Multimedia/Sound/Players

%description sdl
The mpg123 distribution contains a real time MPEG 1.0/2.0/2.5 audio player/decoder for
layers 1,2 and 3 (most commonly MPEG 1.0 layer 3 aka MP3), as well as re-usable decoding
and output libraries.

This package contains the plugin for SDL output support.

%prep
%setup -q

%build
%configure \
    --enable-modules=yes
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libmpg123-0 -p /sbin/ldconfig
%postun -n libmpg123-0 -p /sbin/ldconfig
%post   -n libout123-0 -p /sbin/ldconfig
%postun -n libout123-0 -p /sbin/ldconfig

%files
%doc ChangeLog README
%{_bindir}/mpg123
%{_bindir}/mpg123-id3dump
%{_bindir}/mpg123-strip
%{_bindir}/out123
%{_mandir}/man1/mpg123.1%{?ext_man}
%{_mandir}/man1/out123.1%{?ext_man}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/output_alsa.so
%{_libdir}/%{name}/output_dummy.so
%{_libdir}/%{name}/output_oss.so

%files -n libmpg123-0
%license COPYING
%{_libdir}/libmpg123.so.*

%files -n libout123-0
%{_libdir}/libout123.so.*

%files devel
%{_libdir}/libmpg123.so
%{_libdir}/libout123.so
%{_libdir}/pkgconfig/libmpg123.pc
%{_libdir}/pkgconfig/libout123.pc
%{_includedir}/fmt123.h
%{_includedir}/mpg123.h
%{_includedir}/out123.h

%files pulse
%{_libdir}/%{name}/output_pulse.so

%if 0%{?suse_version} >= 1500
%files openal
%{_libdir}/%{name}/output_openal.so
%endif

%files jack
%{_libdir}/%{name}/output_jack.so

%files portaudio
%{_libdir}/%{name}/output_portaudio.so

%files sdl
%{_libdir}/%{name}/output_sdl.so

%changelog
