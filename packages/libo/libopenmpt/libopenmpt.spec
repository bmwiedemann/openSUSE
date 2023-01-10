#
# spec file for package libopenmpt
#
# Copyright (c) 2023 SUSE LLC
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


%define libopenmpt libopenmpt0
%define libopenmpt_modplug libopenmpt_modplug1
%define libopenmpt_modplug_version 0.8.9.0

Name:           libopenmpt
Version:        0.6.7
Release:        0
Summary:        C++ and C library to decode tracker music files
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Other
URL:            https://lib.openmpt.org/libopenmpt/
Source:         https://lib.openmpt.org/files/libopenmpt/src/%{name}-%{version}+release.autotools.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(zlib)
# GCC >= 8 is required for charconv header
%if 0%{suse_version} < 1550
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif

%description
libopenmpt is a C++ and C library to decode tracker music files
(modules) into a PCM audio stream. It is based on the player code of
the OpenMPT project, a descendant of the original ModPlug Tracker.

%package -n %{libopenmpt}
Summary:        Library to operate with module formats using the openmpt API
Group:          System/Libraries

%description -n %{libopenmpt}
libopenmpt is a C++ and C library to decode tracker music files
(modules) into a PCM audio stream. It is based on the player code of
the OpenMPT project, a descendant of the original ModPlug Tracker.

%package devel
Summary:        Development files for libopenmpt
Group:          Development/Libraries/C and C++
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
# disable werror
sed -i -e 's:-Werror ::g' configure.ac
# fix encoding
dos2unix LICENSE README.md

%build
%if 0%{suse_version} < 1550
export CXX=g++-11
%endif
autoreconf -fvi
# doxygen docu is better on their website, no need to ship it
# docdir points to devel as it is installing the devel examples
%configure \
    --docdir=%{_docdir}/%{name}-devel \
    --disable-static \
    --disable-silent-rules \
    --disable-doxygen-doc \
    --with-zlib \
    --with-mpg123 \
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

%post -n %{libopenmpt} -p /sbin/ldconfig
%postun -n %{libopenmpt} -p /sbin/ldconfig

%files -n openmpt123
%license LICENSE
%doc README.md
%{_bindir}/openmpt123
%{_mandir}/man1/openmpt123.1%{?ext_man}

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
%{_libdir}/pkgconfig/libopenmpt.pc

%files -n %{libopenmpt}
%{_libdir}/libopenmpt.so.*

%changelog
