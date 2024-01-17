#
# spec file for package libfishsound
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define soname      1
Name:           libfishsound
Version:        1.0.0
Release:        0
Summary:        Wrapper library for audio decoding and encoding
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://www.xiph.org/fishsound/
Source:         https://downloads.xiph.org/releases/libfishsound/libfishsound-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
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
%setup -q

%build
%configure \
    --enable-experimental
make %{?_smp_mflags}

%install
%make_install

rm "%{buildroot}%{_libdir}"/*.{la,a}
rm -rf "%{buildroot}%{_datadir}/doc"

%post   -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libfishsound.so.%{soname}
%{_libdir}/libfishsound.so.%{soname}.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/fishsound
%{_libdir}/libfishsound.so
%{_libdir}/pkgconfig/fishsound.pc

%changelog
