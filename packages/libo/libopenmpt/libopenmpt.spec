#
# spec file for package libopenmpt
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


%define libplug libmodplug1
%define libopenmpt libopenmpt0
%define libopenmpt_modplug libopenmpt_modplug1
%bcond_without mpg123
Name:           libopenmpt
Version:        0.4.9
Release:        0
Summary:        C++ and C library to decode tracker music files
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Other
URL:            https://lib.openmpt.org/libopenmpt/
Source:         https://lib.openmpt.org/files/libopenmpt/src/%{name}-%{version}+release.autotools.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM: modplug pc file needs to have full path
Patch0:         libmodpulg-pcfile.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(zlib)
%if %{with mpg123}
BuildRequires:  pkgconfig(libmpg123)
%endif

%description
libopenmpt is a C++ and C library to decode tracker music files
(modules) into a PCM audio stream. It is based on the player code of
the OpenMPT project, a descendant of the original ModPlug Tracker.

%package -n %{libplug}
Summary:        Library to operate with module formats
Group:          System/Libraries

%description -n %{libplug}
This is the Modplug library, based on the ModPlug sound engine coming
from libopenmpt.
- plays 22 different module formats
- plays zip, rar, gzip, and bzip2 compressed modules
- plays Timidity's GUS patch files (*.pat)
- plays all types of MIDI files (*.mid)
- plays textfiles written in the ABC music notation (*.abc)

%package -n libmodplug-devel
Summary:        Development files for libmodplug
Group:          Development/Libraries/C and C++
Requires:       %{libplug} = %{version}

%description -n libmodplug-devel
Files needed to program against libmodplug interface.
This version comes from libopenmpt.

%package -n %{libopenmpt}
Summary:        Library to operate with module formats using the openmpt API
Group:          System/Libraries

%description -n %{libopenmpt}
libopenmpt is a C++ and C library to decode tracker music files
(modules) into a PCM audio stream. It is based on the player code of
the OpenMPT project, a descendant of the original ModPlug Tracker.

%package -n %{libopenmpt_modplug}
Summary:        Modplug wrapper for a library to operate with module formats
Group:          System/Libraries

%description -n %{libopenmpt_modplug}
This package contains the modplug compatibility shared library. It is used by
programs that want to use libopenmpt's decoder, but are written using
libmodplug's API.

%package devel
Summary:        Development files for libopenmpt
Group:          Development/Libraries/C and C++
Requires:       %{libopenmpt_modplug} = %{version}
Requires:       %{libopenmpt} = %{version}

%description devel
This package contains the development files required to compile programs
using %{name}.

%package -n openmpt123
Summary:        Command line module player
Group:          Productivity/Multimedia/Sound/Players

%description -n openmpt123
This package contains the openmpt123 command-line module player.

%prep
%setup -q -n %{name}-%{version}+release.autotools
%patch0 -p1
# disable werror
sed -i -e 's:-Werror ::g' configure.ac
# fix encoding
dos2unix LICENSE README.md

%build
autoreconf -fvi
# doxygen docu is better on their website, no need to ship it
# docdir points to devel as it is installing the devel examples
%configure \
    --docdir=%{_docdir}/%{name}-devel \
    --disable-static \
    --disable-silent-rules \
    --enable-libopenmpt_modplug \
    --enable-libmodplug \
    --disable-doxygen-doc \
    --with-zlib \
%if %{with mpg123}
    --with-mpg123 \
%else
    --without-mpg123 \
%endif
    --with-ogg \
    --with-vorbis \
    --with-vorbisfile \
    --with-pulseaudio \
    --with-sndfile \
    --with-flac \
    --with-portaudio \
    --with-sdl2
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libplug} -p /sbin/ldconfig
%postun -n %{libplug} -p /sbin/ldconfig
%post -n %{libopenmpt} -p /sbin/ldconfig
%postun -n %{libopenmpt} -p /sbin/ldconfig
%post -n %{libopenmpt_modplug} -p /sbin/ldconfig
%postun -n %{libopenmpt_modplug} -p /sbin/ldconfig

%files -n openmpt123
%license LICENSE
%doc README.md
%{_bindir}/openmpt123
%{_mandir}/man1/openmpt123.1%{?ext_man}

%files -n libmodplug-devel
%dir %{_includedir}/libmodplug/
%{_includedir}/libmodplug/modplug.h
%{_includedir}/libmodplug/sndfile.h
%{_includedir}/libmodplug/stdafx.h
%{_libdir}/libmodplug.so
%{_libdir}/pkgconfig/libmodplug.pc

%files -n %{libplug}
%license LICENSE
%{_libdir}/libmodplug.so.*

%files devel
%dir %{_docdir}/%{name}-devel/
%{_docdir}/%{name}-devel/*
%dir %{_includedir}/libopenmpt/
%{_includedir}/libopenmpt/libopenmpt.h
%{_includedir}/libopenmpt/libopenmpt.hpp
%{_includedir}/libopenmpt/libopenmpt_config.h
%{_includedir}/libopenmpt/libopenmpt_ext.hpp
%{_includedir}/libopenmpt/libopenmpt_stream_callbacks_fd.h
%{_includedir}/libopenmpt/libopenmpt_stream_callbacks_file.h
%{_includedir}/libopenmpt/libopenmpt_version.h
%{_includedir}/libopenmpt/libopenmpt_ext.h
%{_includedir}/libopenmpt/libopenmpt_stream_callbacks_buffer.h
%{_libdir}/libopenmpt.so
%{_libdir}/libopenmpt_modplug.so
%{_libdir}/pkgconfig/libopenmpt.pc

%files -n %{libopenmpt}
%{_libdir}/libopenmpt.so.*

%files -n %{libopenmpt_modplug}
%{_libdir}/libopenmpt_modplug.so.*

%changelog
