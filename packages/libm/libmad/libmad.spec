#
# spec file for package libmad
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        0.16.4
Release:        0
Summary:        An MPEG audio decoder library
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
#Git-Clone:     https://codeberg.org/tenacityteam/libmad.git
URL:            https://www.underbit.com/products/mad/
Source:         https://codeberg.org/tenacityteam/libmad/releases/download/%{version}/libmad-%{version}.tar.gz
Source1000:     baselibs.conf
Patch0:         libmad-x86.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
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
%autosetup -p1 -n libmad

%build
%cmake -DOPTIMIZE=ACCURACY
%make_build

%install
%cmake_install

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING COPYRIGHT
%doc CHANGES CREDITS README.md TODO
%{_libdir}/libmad.so.%{sover}*

%files devel
%{_includedir}/mad.h
%{_libdir}/libmad.so
%{_libdir}/pkgconfig/mad.pc
%{_libdir}/cmake/mad

%changelog
