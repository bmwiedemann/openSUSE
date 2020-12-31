#
# spec file for package zita-resampler
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%define sover   1
%define libname libzita-resampler%{sover}
Name:           zita-resampler
Version:        1.8.0
Release:        0
Summary:        A C++ library for resampling audio signals
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://kokkinizita.linuxaudio.org/linuxaudio/zita-resampler/resampler.html
Source:         https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Patch0:         fix-makefile.patch
Patch1:         disable-sse.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sndfile)

%description
Zita resampler is a C++ library for resampling audio signals. It is
designed to be used within a real-time processing context, to be
fast, and to provide high-quality sample rate conversion.

%package -n %{libname}
Summary:        A C++ library for resampling audio signals
Group:          System/Libraries

%description -n %{libname}
Zita resampler is a C++ library for resampling audio signals. It is
designed to be used within a real-time processing context, to be
fast, and to provide high-quality sample rate conversion.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for %{name} including headers and libraries.

%package tools
Summary:        Resampler Application written with libzita-resampler
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Provides:       zresample
Provides:       zretune

%description tools
zresample copies an audio file, changing the sample rate and/or the
sample format. For 16-bit output it can also dither the audio signal.

zretune resamples an audio file by a the inverse of a ratio expressed
in cents, without changing the nominal sample rate. The result is to
change the musical pitch and lenght of the file.

The input for both tools can be any audio file readable by the
libsndfile library. The output file type is either WAV, WAVEX, CAF,
AIFF or FLAC.


%prep
%setup -q
%patch0 -p1
%ifnarch x86_64
%patch1 -p1
%endif

%build
export CXXFLAGS="%{optflags}"
cd source
%make_build
ln -sv "libzita-resampler.so.%{version}" "libzita-resampler.so"
cd ..
%make_build LDFLAGS+=" -L../source" CXXFLAGS+=" -I../source" -C apps

%install
make -C source SUFFIX=%(echo %_lib | sed s/lib//) DESTDIR=%{buildroot} PREFIX=%{_prefix} install
make -C apps DESTDIR=%{buildroot} PREFIX=%{_prefix} install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc AUTHORS README
%{_libdir}/libzita-resampler.so.%{sover}*

%files devel
%{_includedir}/zita-resampler
%{_libdir}/libzita-resampler.so

%files tools
%{_bindir}/zresample
%{_bindir}/zretune
%{_mandir}/man1/zresample.1%{?ext_man}
%{_mandir}/man1/zretune.1%{?ext_man}

%changelog
