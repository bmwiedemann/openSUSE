#
# spec file for package libmpeg2
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


%define libname libmpeg2-0
%define libconvertname libmpeg2convert0

Name:           libmpeg2
Version:        0.5.1
Release:        0
Summary:        MPEG-2 Video Stream Decoder
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://libmpeg2.sourceforge.net/
Source:         http://libmpeg2.sourceforge.net/files/libmpeg2-%{version}.tar.gz
Source99:       baselibs.conf

Patch0:         libmpeg2-0.5.1-altivec.patch
Patch1:         libmpeg2-0.5.1-arm-private-symbols.patch
Patch2:         libmpeg2-0.5.1-global-symbol-test.patch

BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xv)

%description
libmpeg2 is a library for decoding MPEG-1 and MPEG-2 video streams.

%package -n %{libname}
Summary:        MPEG-2 Video Stream Decoder
Group:          System/Libraries

%description -n %{libname}
libmpeg2 is a library for decoding MPEG-1 and MPEG-2 video streams.

%package -n %{libconvertname}
Summary:        MPEG-2 Video Stream Decoder
Group:          System/Libraries

%description -n %{libconvertname}
libmpeg2 is a library for decoding MPEG-1 and MPEG-2 video streams.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libconvertname} = %{version}
Requires:       %{libname} = %{version}
Requires:       SDL-devel

%description devel
Include Files and Libraries mandatory for libmpeg2 Development

%package -n mpeg2dec
Summary:        MPEG-2 Decoder
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       %{libconvertname} = %{version}
Requires:       %{libname} = %{version}

%description -n mpeg2dec
An MPEG2Decoder based on the libmpeg2 libraries.

%prep
%autosetup -p1

%build
autoreconf -vi
%configure \
	--disable-static \
	--disable-dependency-tracking \
	--enable-sdl \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n  %{libname} -p /sbin/ldconfig

%post -n %{libconvertname} -p /sbin/ldconfig
%postun -n  %{libconvertname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/libmpeg2.so.*

%files -n %{libconvertname}
%{_libdir}/libmpeg2convert.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README TODO
%doc doc/*.txt doc/*.c
%dir %{_includedir}/mpeg2dec
%{_includedir}/mpeg2dec/mpeg2.h
%{_includedir}/mpeg2dec/mpeg2convert.h
%{_libdir}/libmpeg2.so
%{_libdir}/libmpeg2convert.so
%{_libdir}/pkgconfig/libmpeg2.pc
%{_libdir}/pkgconfig/libmpeg2convert.pc

%files -n mpeg2dec
%{_bindir}/corrupt_mpeg2
%{_bindir}/extract_mpeg2
%{_bindir}/mpeg2dec
%{_mandir}/man?/mpeg2dec.?%{ext_man}
%{_mandir}/man?/extract_mpeg2.?%{ext_man}

%changelog
