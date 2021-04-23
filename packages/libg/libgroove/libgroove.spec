#
# spec file for package libgroove
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


%define sover   4
%define sobase  groove
%define soplayer  %{sobase}player
%define soloudness %{sobase}loudness
%define sofingerprinter %{sobase}fingerprinter
%define ffmpeg_includedir %(pkg-config --variable=includedir libavutil)
Name:           libgroove
Version:        4.3.0
Release:        0
Summary:        A library to streaming audio processing
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://andrewrk.github.io/libgroove/
Source0:        https://github.com/andrewrk/libgroove/archive/%{version}.tar.gz#/lib%{sobase}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM libdir.patch avvissu@yandex.by -- Change to install libdir
Patch0:         libgroove-4.3.0_libdir.patch
# PATCH-FIX-UPSTREAM ffmpeg-3.0.patch superjoe30@gmail.com -- Fixed in upstream
Patch1:         libgroove-4.3.0_ffmpeg-3.0.patch
Patch2:         libgroove-4.3.0-no_overflow.patch
# PATCH-FIX-UPSTREAM libgroove-4.3.0-no_Werror0.patch -- borrowed from debian, fixes Factory build
Patch3:         libgroove-4.3.0-no_Werror.patch
# PATCH-FIX-UPSTREAM libgroove-4.3.0_ffmpeg-4.0.patch -- Fix build with ffmpeg v4, borrowed from debian
Patch4:         libgroove-4.3.0_ffmpeg-4.0.patch
BuildRequires:  cmake
BuildRequires:  libebur128-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(sdl2)

%description
This library provides decoding and encoding of audio on a playlist. It is
intended to be used as a backend for music player applications. That said,
it is also generic enough to be used as a backend for any streaming audio
processing utility.

%package -n     lib%{sobase}%{sover}
Summary:        A library to streaming audio processing
Group:          System/Libraries

%description -n lib%{sobase}%{sover}
This library provides decoding and encoding of audio on a playlist. It is
intended to be used as a backend for music player applications. That said,
it is also generic enough to be used as a backend for any streaming audio
processing utility.

This package contains the shared library.

%package -n     lib%{soplayer}%{sover}
Summary:        A library to hardware audio playback for lib%{sobase}
Group:          System/Libraries

%description -n lib%{soplayer}%{sover}
This libgroove plugin plays audio via a sound device. It includes a dummy
player which can simulate playback without actually having access to a sound
device.

This package contains the shared library.

%package -n     lib%{soloudness}%{sover}
Summary:        A library to loudness scanner for lib%{sobase}
Group:          System/Libraries

%description -n lib%{soloudness}%{sover}
This libgroove plugin uses the EBU R128 standard to detect loudness. The
values it produces are compatible with ReplayGain.

This package contains the shared library.

%package -n     lib%{sofingerprinter}%{sover}
Summary:        A library to acoustid fingerprinter for lib%{sobase}
Group:          System/Libraries

%description -n lib%{sofingerprinter}%{sover}
This libgroove plugin generates audio fingerprints which can be used with the
acoustid.org service to find out metadata tags for the media.

This package contains the shared library.

%package -n     lib%{sobase}-devel
Summary:        Development files for lib%{sobase}
Group:          Development/Libraries/C and C++
Requires:       lib%{sobase}%{sover} = %{version}

%description -n lib%{sobase}-devel
A library to streaming audio processing.

This package contains header files and libraries needed to develop
application that use lib%{sobase}.

%package -n     lib%{soplayer}-devel
Summary:        Development files for lib%{soplayer}
Group:          Development/Libraries/C and C++
Requires:       lib%{sobase}-devel
Requires:       lib%{soplayer}%{sover} = %{version}

%description -n lib%{soplayer}-devel
A library to hardware audio playback for %{sobase}.

This package contains header files and libraries needed to develop
application that use lib%{soplayer}.

%package -n     lib%{soloudness}-devel
Summary:        Development files for lib%{soloudness}
Group:          Development/Libraries/C and C++
Requires:       lib%{sobase}-devel
Requires:       lib%{soloudness}%{sover} = %{version}

%description -n lib%{soloudness}-devel
A library to loudness scanner for %{sobase}.

This package contains header files and libraries needed to develop
application that use lib%{soloudness}.

%package -n     lib%{sofingerprinter}-devel
Summary:        Development files for %{sofingerprinter}
Group:          Development/Libraries/C and C++
Requires:       lib%{sobase}-devel
Requires:       lib%{sofingerprinter}%{sover} = %{version}

%description -n lib%{sofingerprinter}-devel
A library to acoustid fingerprinter for %{sobase}.

This package contains header files and libraries needed to develop
application that use lib%{sofingerprinter}.

%prep
%setup -q -n lib%{sobase}-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export CFLAGS="%{optflags} -Wno-deprecated-declarations"
export CXXFLAGS="$CFLAGS"
%cmake \
    -DAVFORMAT_INCLUDE_DIRS="%{ffmpeg_includedir}" \
    -DAVCODEC_INCLUDE_DIRS="%{ffmpeg_includedir}" \
    -DAVFILTER_INCLUDE_DIRS="%{ffmpeg_includedir}" \
    -DAVUTIL_INCLUDE_DIRS="%{ffmpeg_includedir}" \
    -DBUILD_EXAMPLE_PROGRAMS=OFF

make %{?_smp_mflags}

%install
%cmake_install

find %{buildroot} -name \*.a -exec rm -f {} \;

%post -n lib%{sobase}%{sover} -p /sbin/ldconfig
%postun -n lib%{sobase}%{sover} -p /sbin/ldconfig
%post -n lib%{soplayer}%{sover} -p /sbin/ldconfig
%postun -n lib%{soplayer}%{sover} -p /sbin/ldconfig
%post -n lib%{soloudness}%{sover} -p /sbin/ldconfig
%postun -n lib%{soloudness}%{sover} -p /sbin/ldconfig
%post -n lib%{sofingerprinter}%{sover} -p /sbin/ldconfig
%postun -n lib%{sofingerprinter}%{sover} -p /sbin/ldconfig

%files -n lib%{sobase}%{sover}
%license LICENSE
%doc CHANGELOG*
%{_libdir}/lib%{sobase}.so.*

%files -n lib%{soplayer}%{sover}
%license LICENSE
%doc CHANGELOG*
%{_libdir}/lib%{soplayer}.so.*

%files -n lib%{soloudness}%{sover}
%license LICENSE
%doc CHANGELOG*
%{_libdir}/lib%{soloudness}.so.*

%files -n lib%{sofingerprinter}%{sover}
%license LICENSE
%doc CHANGELOG*
%{_libdir}/lib%{sofingerprinter}.so.*

%files -n lib%{sobase}-devel
%{_includedir}/%{sobase}/
%{_libdir}/lib%{sobase}.so

%files -n lib%{soplayer}-devel
%{_includedir}/%{soplayer}/
%{_libdir}/lib%{soplayer}.so

%files -n lib%{soloudness}-devel
%{_includedir}/%{soloudness}/
%{_libdir}/lib%{soloudness}.so

%files -n lib%{sofingerprinter}-devel
%{_includedir}/%{sofingerprinter}/
%{_libdir}/lib%{sofingerprinter}.so

%changelog
