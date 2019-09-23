#
# spec file for package libvorbis
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libvorbis
Version:        1.3.6
Release:        0
Summary:        The Vorbis General Audio Compression Codec
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://www.vorbis.com/
Source:         http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
Patch1:         libvorbis-lib64.dif
Patch2:         libvorbis-m4.dif
Patch12:        vorbis-ocloexec.patch
Patch101:       vorbis-CVE-2017-14160.patch
Patch102:       vorbis-CVE-2018-10393.patch
Patch103:       vorbis-CVE-2018-10392.patch
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# bug437293 (SLES10 -> SLES11 upgrade path)
%ifarch ppc64
Obsoletes:      libvorbis-64bit
%endif

%description
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package -n libvorbis0
Summary:        The Vorbis General Audio Compression Codec
#
# libvorbis was last used in openSUSE 11.3
Group:          System/Libraries
Provides:       %{name} = 1.3.2
Obsoletes:      %{name} < 1.3.2
# bug437293 (SLES10 -> SLES11 upgrade path)
%ifarch ppc64
Obsoletes:      libvorbis-64bit
%endif

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
# bug437293 (SLES10 -> SLES11 upgrade path)
%ifarch ppc64
Obsoletes:      libvorbis-devel-64bit
%endif
#

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
%patch101 -p1
%patch102 -p1
%patch103 -p1

%build
# Fix optimization level
sed -i s,-O20,-O3,g configure.ac

autoreconf -fiv
%configure \
	--disable-examples \
	--disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# docs are built in a separate spec file
rm -rf %{buildroot}%{_datadir}/doc/*
# remove unneeded files
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n libvorbis0 -p /sbin/ldconfig

%postun -n libvorbis0 -p /sbin/ldconfig

%post -n libvorbisenc2 -p /sbin/ldconfig

%postun -n libvorbisenc2 -p /sbin/ldconfig

%post -n libvorbisfile3 -p /sbin/ldconfig

%postun -n libvorbisfile3 -p /sbin/ldconfig

%files -n libvorbis0
%defattr(0644,root,root,0755)
%{_libdir}/libvorbis.so.0*

%files -n libvorbisenc2
%defattr(0644,root,root,0755)
%{_libdir}/libvorbisenc.so.2*

%files -n libvorbisfile3
%defattr(0644,root,root,0755)
%{_libdir}/libvorbisfile.so.3*

%files devel
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{_datadir}/aclocal/*.m4
%{_includedir}/vorbis
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
