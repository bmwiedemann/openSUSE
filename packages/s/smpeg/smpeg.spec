#
# spec file for package smpeg
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


Name:           smpeg
Version:        0.4.5
Release:        0
Summary:        SDL MPEG Player Library
License:        LGPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://icculus.org/smpeg
Source:         %{name}-%{version}.tar.bz2
#PATCH-FIX-UPSTREAM export mpegaudio class
Patch5:         200_export_mpegaudio_class.diff
#PATCH-FIX-UPSTREAM gnu stack
Patch7:         320_gnu_stack.diff
#PATCH-FIX-UPSTREAM fix ftbfs with gcc 6
Patch9:         340_gcc6.diff
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl)

%description
SMPEG is a MPEG-1 video player library with sound support. Video
playback is based on the Berkeley MPEG player, mpeg_play v2.2. Audio
is played through a modified mpegsound library, part of Splay v0.8.2.
SMPEG supports MPEG-1 Layer 3 audio, MPEG-1 video, and MPEG system
streams.

%package -n libsmpeg-0_4-0
Summary:        SDL MPEG Player Library
Group:          System/Libraries

%description -n libsmpeg-0_4-0
SMPEG is a MPEG-1 video player library with sound support. Video
playback is based on the Berkeley MPEG player, mpeg_play v2.2. Audio
is played through a modified mpegsound library, part of Splay v0.8.2.
SMPEG supports MPEG-1 Layer 3 audio, MPEG-1 video, and MPEG system
streams.

%package devel
Summary:        Development files for libsmpeg
Group:          Development/Libraries/C and C++
Requires:       libsmpeg-0_4-0 = %{version}

%description devel
SMPEG is a MPEG-1 video player library with sound support. Video
playback is based on the Berkeley MPEG player, mpeg_play v2.2. Audio
is played through a modified mpegsound library, part of Splay v0.8.2.
SMPEG supports MPEG-1 Layer 3 audio, MPEG-1 video, and MPEG system
streams.

%prep
%autosetup -p1
NO_CONFIGURE=1 ./autogen.sh

%build
%configure --disable-static
%make_build

%install
%make_install
rm -rf %{buildroot}%{_bindir}/glmovie
rm -rf %{buildroot}%{_bindir}/plaympeg
rm -rf %{buildroot}%{_mandir}/man1/plaympeg.1
rm -rf %{buildroot}%{_mandir}/man1/gtv.1
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libsmpeg-0_4-0 -p /sbin/ldconfig
%postun -n libsmpeg-0_4-0 -p /sbin/ldconfig

%files -n libsmpeg-0_4-0
%license COPYING
%doc README
%{_libdir}/libsmpeg-0.4.so.0
%{_libdir}/libsmpeg-0.4.so.0.1.4

%files devel
%{_libdir}/libsmpeg.so
%{_bindir}/smpeg-config
%{_datadir}/aclocal/smpeg.m4
%{_includedir}/smpeg

%changelog
