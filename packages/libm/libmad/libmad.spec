#
# spec file for package libmad
#
# Copyright (c) 2022 SUSE LLC
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


%define sover   0
%define libname %{name}%{sover}
Name:           libmad
Version:        0.15.1b
Release:        0
Summary:        An MPEG audio decoder library
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            http://www.underbit.com/products/mad/
Source:         https://sourceforge.net/projects/mad/files/libmad/%{version}/libmad-%{version}.tar.gz
Source1000:     baselibs.conf
Patch0:         libmad-0.15.1b-automake.patch
Patch1:         libmad-0.15.1b-pkgconfig.patch
Patch2:         libmad-0.15.1b-gcc43.patch
Patch3:         Provide-Thumb-2-alternative-code-for-MAD_F_MLN.diff
Patch4:         libmad.thumb.diff
Patch5:         libmad-0.15.1b-ppc.patch
Patch6:         length-check.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
Provides:       mad = %{version}-%{release}
Obsoletes:      mad < %{version}-%{release}

%description
MAD is a MPEG audio decoder. It currently supports MPEG-1 and the
MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are implemented.

MAD supports 24-bit PCM output. MAD computes using 100%% fixed-point
(integer) computation, so you can run it without a floating point
unit.

%package -n %{libname}
Summary:        An MPEG audio decoder library
Group:          System/Libraries

%description -n %{libname}
MAD is a MPEG audio decoder. It currently supports MPEG-1 and the
MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are implemented.

MAD supports 24-bit PCM output. MAD computes using 100%% fixed-point
(integer) computation, so you can run it without a floating point
unit.

%package devel
Summary:        Development package for libmad, an MP3 decoding library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       mad-devel = %{version}-%{release}
Obsoletes:      mad-devel < %{version}-%{release}

%description devel
This package contains the header files needed to
develop applications with libmad.

%prep
%setup -q
%patch -P 0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1

# new autoconf does not support deprecated declare (10 years in deprecation)
sed -i 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac

%build
autoreconf -fiv
%configure \
%if 0%{?__isa_bits} == 64
  --enable-fpm=64bit \
%endif
%ifarch %{arm}
  --enable-fpm=arm \
%endif
  --enable-accuracy \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install -D -m0644 mad.pc "%{buildroot}%{_libdir}/pkgconfig/mad.pc"

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc CHANGES COPYRIGHT CREDITS README TODO VERSION
%{_libdir}/libmad.so.%{sover}*

%files devel
%{_includedir}/mad.h
%{_libdir}/libmad.so
%{_libdir}/pkgconfig/mad.pc

%changelog
