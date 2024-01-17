#
# spec file for package libmpcdec
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


Name:           libmpcdec
Version:        1.2.6
Release:        0
Summary:        Musepack Audio Decoder
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://www.musepack.net/
Source0:        http://files.musepack.net/source/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch0:         libmpcdec-1.2.6-nosamples.patch
Patch1:         libmpcdec-byteswap.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
Musepack is an audio compression format with a strong emphasis on high
quality. It is not lossless, but it is designed for transparency, so
that you cannot hear differences between the original WAV file and the
much smaller MPC file.

It is based on the MPEG-1 Layer-2 / MP2 algorithms, but since 1997 it
has rapidly developed and vastly improved and is now at an advanced
stage in which it contains heavily optimized and patentless code.

Musepack is not particularly optimized for low bit rates. The encoder
was designed to be transparent at the --standard setting, thus little
low bit rate tuning has gone into the codec, unlike that of AAC,
Vorbis, WMA, and others that focus more on this region.

%package -n libmpcdec5
Summary:        Musepack Audio Decoder
Group:          System/Libraries
Provides:       %{name}
Obsoletes:      %{name}

%description -n libmpcdec5
Musepack is an audio compression format with a strong emphasis on high
quality. It is not lossless, but it is designed for transparency, so
that you cannot hear differences between the original WAV file and the
much smaller MPC file.

It is based on the MPEG-1 Layer-2 / MP2 algorithms, but since 1997 it
has rapidly developed and vastly improved and is now at an advanced
stage in which it contains heavily optimized and patentless code.

Musepack is not particularly optimized for low bit rates. The encoder
was designed to be transparent at the --standard setting, thus little
low bit rate tuning has gone into the codec, unlike that of AAC,
Vorbis, WMA, and others that focus more on this region.

%package devel
Summary:        Musepack Audio Decoder
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libmpcdec5 = %{version}

%description devel
Musepack is an audio compression format with a strong emphasis on high
quality. It's not lossless, but it is designed for transparency, so
that you won't be able to hear differences between the original wave
file and the much smaller MPC file.

It is based on the MPEG-1 Layer-2 / MP2 algorithms, but since 1997 it
has rapidly developed and vastly improved and is now at an advanced
stage in which it contains heavily optimized and patentless code.

Musepack is not particularly optimized for low bitrates. The encoder
was designed to be transparent at the --standard setting, thus little
low bitrate tuning has gone into the codec, opposite to that of AAC,
Vorbis, WMA and others which focus more on this region.

%prep
%setup -q
%patch0
%patch1

%build
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libmpcdec5 -p /sbin/ldconfig
%postun -n libmpcdec5 -p /sbin/ldconfig

%files -n libmpcdec5
%{_libdir}/*.so.5*

%files devel
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/*.so
%dir %{_includedir}/mpcdec
%{_includedir}/mpcdec/*.h

%changelog
