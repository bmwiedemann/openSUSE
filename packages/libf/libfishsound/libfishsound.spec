#
# spec file for package libfishsound
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define soname      1
Name:           libfishsound
Version:        1.0.1
Release:        0
Summary:        Wrapper library for audio decoding and encoding
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.xiph.org/fishsound/
Source:         https://downloads.xiph.org/releases/libfishsound/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(oggz)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(vorbis)

%description
libfishsound provides a programming interface for decoding and
encoding audio data using the three Xiph.org codecs FLAC, Speex and
Vorbis.

%package -n %{name}%{soname}
Summary:        Wrapper library for audio decoding and encoding
Group:          System/Libraries

%description -n %{name}%{soname}
libfishsound provides a programming interface for decoding and
encoding audio data using the three Xiph.org codecs FLAC, Speex and
Vorbis.

libfishsound can handle raw codec streams from a lower level layer
such as UDP datagrams. When these codecs are used in files, they are
commonly encapsulated in Ogg to produce Ogg FLAC, Speex and Ogg
Vorbis files.

libfishsound is a wrapper around the existing codec libraries and
provides a higher-level programming interface. It has no direct
dependencies on Ogg encapsulation, though it is most commonly used in
conjunction with liboggz to decode or encode audio tracks in Ogg
files, including Ogg Theora and Annodex.

%package devel
Summary:        Audio Decoding and Encoding Library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description devel
libfishsound provides a programming interface for decoding and
encoding audio data using the three Xiph.org codecs FLAC, Speex and
Vorbis.

This subpackage contains libraries and header files for developing
applications that want to make use of libfishsound.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--enable-experimental \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}/usr/share/doc/%{name} %{buildroot}%{_docdir}

%check
%make_build check

%ldconfig_scriptlets -n %{name}%{soname}

%files -n %{name}%{soname}
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/libfishsound.so.%{soname}
%{_libdir}/libfishsound.so.%{soname}.*

%files devel
%license COPYING
%{_includedir}/fishsound
%{_libdir}/libfishsound.so
%{_libdir}/pkgconfig/fishsound.pc
%{_docdir}/%{name}

%changelog
