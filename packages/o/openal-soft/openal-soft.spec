#
# spec file for package openal-soft
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


Name:           openal-soft
Version:        1.19.1
Release:        0
Summary:        Audio library with an OpenGL-resembling API
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://www.openal-soft.org/
Source0:        https://www.openal-soft.org/openal-releases/openal-soft-%{version}.tar.bz2
Source1:        libopenalcompat.c
Source3:        baselibs.conf
# PATCH-FIX-UPSTREAM openal-no-autospawn.diff
Patch0:         openal-no-autospawn.diff
BuildRequires:  cmake >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)

%description
OpenAL is an audio library designed in the spirit of the OpenGL API.

OpenAL provides capabilities for playing audio in a virtual 3D
environment. Distance attenuation, doppler shift, and directional
sound emitters are among the features handled by the API. More
advanced effects, including air absorption, occlusion, and
environmental reverb, are available through the EFX extension. It
also facilitates streaming audio, multi-channel buffers, and audio
capture.

%package -n libopenal0
Summary:        Audio library with an OpenGL-resembling API
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libopenal0
OpenAL is an audio library designed in the spirit of the OpenGL API.
libopenal.so.0 is just a wrapper around libopenal.so.1 for
compatibility with old software.

%package devel
Summary:        Development headers for OpenAL Soft
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       libopenal1 = %{version}
Provides:       openal-devel = %{version}-%{release}

%description devel
OpenAL is an audio library designed in the spirit of the OpenGL API.
This subpackage contains libraries and header files for developing
applications that want to make use of openal-soft.

%package makehrtf
Summary:        OpenAL Soft HRTF generation utility
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Conflicts:      openal-soft-devel < %{version}
Provides:       openal-soft-devel:%{_bindir}/makehrtf

%description makehrtf
OpenAL is an audio library designed in the spirit of the OpenGL API.
This package contains the makehrtf utility for creating head-related
transfer functions (HRTF).

%package data
Summary:        OpenAL Soft auxiliary data and config
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       openal-soft = %{version}
Obsoletes:      openal-soft <= %{version}
BuildArch:      noarch

%description data
OpenAL is an audio library designed in the spirit of the OpenGL API.
This package contains auxiliary data and config files.

%package tools
Summary:        OpenAL Soft tools
License:        LGPL-2.1-or-later AND MIT
Group:          Productivity/Multimedia/Sound/Utilities
Conflicts:      openal-soft < %{version}
Provides:       openal-soft:%{_bindir}/openal-info

%description tools
OpenAL is an audio library designed in the spirit of the OpenGL API.
This package contains additional tools for OpenAL.

%package -n libopenal1
Summary:        Audio library with an OpenGL-resembling API
License:        LGPL-2.1-or-later
Group:          System/Libraries
Recommends:     openal-soft-data
Conflicts:      openal-soft < %{version}

%description -n libopenal1
OpenAL is an audio library designed in the spirit of the OpenGL API.

OpenAL provides capabilities for playing audio in a virtual 3D
environment. Distance attenuation, doppler shift, and directional
sound emitters are among the features handled by the API. More
advanced effects, including air absorption, occlusion, and
environmental reverb, are available through the EFX extension. It
also facilitates streaming audio, multi-channel buffers, and audio
capture.

%prep
%setup -q
%patch0 -p1
# License conflict with the rest of the stack, and we don't use it (Android backend)
rm -v Alc/backends/opensl.c

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DALSOFT_CONFIG=ON \
  -Wno-dev
%make_jobs
gcc -Wall %{optflags} -fPIC -DPIC -Wl,-soname,libopenal.so.0 -shared -Wl,--no-as-needed -L. -lopenal -o libopenal.so.0 %{SOURCE1}

%install
%cmake_install
install -D -m 0644 build/libopenal.so.0 %{buildroot}%{_libdir}/libopenal.so.0
install -D -m 0644 /dev/null %{buildroot}/%{_sysconfdir}/openal/alsoft.conf

%post -n libopenal0 -p /sbin/ldconfig
%postun -n libopenal0 -p /sbin/ldconfig
%post -n libopenal1 -p /sbin/ldconfig
%postun -n libopenal1 -p /sbin/ldconfig

%files tools
%license COPYING
%{_bindir}/openal-info
%{_bindir}/alsoft-config
%{_bindir}/altonegen
%{_bindir}/alrecord

%files makehrtf
%{_bindir}/makehrtf

%files data
%license COPYING
%dir %{_sysconfdir}/openal
%ghost %config(noreplace) %attr(0644,root,root) %{_sysconfdir}/openal/alsoft.conf
%dir %{_datadir}/openal
%{_datadir}/openal/alsoftrc.sample
%dir %{_datadir}/openal/hrtf
%{_datadir}/openal/hrtf/default-44100.mhr
%{_datadir}/openal/hrtf/default-48000.mhr
%dir %{_datadir}/openal/presets
%{_datadir}/openal/presets/3D7.1.ambdec
%{_datadir}/openal/presets/hexagon.ambdec
%{_datadir}/openal/presets/itu5.1.ambdec
%{_datadir}/openal/presets/itu5.1-nocenter.ambdec
%{_datadir}/openal/presets/presets.txt
%{_datadir}/openal/presets/rectangle.ambdec
%{_datadir}/openal/presets/square.ambdec

%files -n libopenal1
%{_libdir}/libopenal.so.1*

%files -n libopenal0
%{_libdir}/libopenal.so.0

%files devel
%{_libdir}/libopenal.so
%{_libdir}/pkgconfig/openal.pc
%dir %{_libdir}/cmake/OpenAL
%{_libdir}/cmake/OpenAL/OpenALConfig-release.cmake
%{_libdir}/cmake/OpenAL/OpenALConfig.cmake
%dir %{_includedir}/AL
%{_includedir}/AL/al.h
%{_includedir}/AL/alc.h
%{_includedir}/AL/alext.h
%{_includedir}/AL/efx.h
%{_includedir}/AL/efx-creative.h
%{_includedir}/AL/efx-presets.h

%changelog
