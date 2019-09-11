#
# spec file for package speexdsp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define package_version 1.2rc3
%define sover   1
%define libname lib%{name}%{sover}
Name:           speexdsp
Version:        1.2~rc3
Release:        0
Summary:        An Open Source, Patent Free Speech Codec
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Url:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/%{name}-%{package_version}.tar.gz
Source2:        baselibs.conf
# taken from upstream boo#929450
Patch0:         speexdsp-fixbuilds-774c87d.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ogg)
Conflicts:      speex <= 1.1.999_1.2rc1

%description
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package -n %{libname}
Summary:        An Open Source, Patent Free Speech Codec Library
Group:          System/Libraries

%description -n %{libname}
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package devel
Summary:        Development package for SpeeX
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Conflicts:      pkgconfig(speex) <= 1.1.999_1.2rc1

%description devel
This package contains the files needed to compile programs that use the
SpeeX library.

%prep
%setup -q -n %{name}-%{package_version}
%patch0 -p1

%build
autoreconf -fiv
# Disable NEON since it doesn't check for availability of the NEON
# extension at runtime
%configure \
  --disable-static \
  --disable-neon
make %{?_smp_mflags} V=1

%install
%make_install
# remove unneeded *.a and *.la files
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libspeexdsp.so.%{sover}*

%files devel
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/manual.pdf
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
