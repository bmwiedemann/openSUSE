#
# spec file for package libvorbis
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


Name:           libvorbis
Version:        1.3.7
Release:        0
Summary:        The Vorbis General Audio Compression Codec
License:        BSD-3-Clause
Group:          System/Libraries
URL:            http://www.vorbis.com/
Source:         https://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.xz
Source1:        https://downloads.xiph.org/releases/vorbis/libvorbis-%{version}.tar.xz.asc
Source10:       baselibs.conf
Source99:       libvorbis.keyring
Patch1:         libvorbis-lib64.dif
Patch2:         libvorbis-m4.dif
Patch12:        vorbis-ocloexec.patch
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
%{?suse_build_hwcaps_libs}

%description
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package -n libvorbis0
Summary:        The Vorbis General Audio Compression Codec
Group:          System/Libraries

%description -n libvorbis0
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package -n libvorbisenc2
Summary:        The Vorbis General Audio Compression Codec
Group:          System/Libraries

%description -n libvorbisenc2
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package -n libvorbisfile3
Summary:        The Vorbis General Audio Compression Codec
Group:          System/Libraries

%description -n libvorbisfile3
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package devel
Summary:        Include Files and Libraries mandatory for Ogg Vorbis Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libogg-devel
Requires:       libvorbis0 = %{version}
Requires:       libvorbisenc2 = %{version}
Requires:       libvorbisfile3 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libvorbis.

%prep
%setup -q
%patch2
# %%patch5 -p1
if [ "%{_lib}" == "lib64" ]; then
%patch1
fi
%patch12

%build
# Fix optimization level
sed -i s,-O20,-O3,g configure.ac

autoreconf -fiv
%configure \
	--disable-examples \
	--disable-static
%make_build

%install
%make_install
# docs are built in a separate spec file
rm -rf %{buildroot}%{_datadir}/doc/*
# remove unneeded files
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n libvorbis0 -p /sbin/ldconfig
%postun -n libvorbis0 -p /sbin/ldconfig
%post -n libvorbisenc2 -p /sbin/ldconfig
%postun -n libvorbisenc2 -p /sbin/ldconfig
%post -n libvorbisfile3 -p /sbin/ldconfig
%postun -n libvorbisfile3 -p /sbin/ldconfig

%files -n libvorbis0
%{_libdir}/libvorbis.so.0*

%files -n libvorbisenc2
%{_libdir}/libvorbisenc.so.2*

%files -n libvorbisfile3
%{_libdir}/libvorbisfile.so.3*

%files devel
%doc AUTHORS
%license COPYING
%{_datadir}/aclocal/*.m4
%{_includedir}/vorbis
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
