#
# spec file for package speex
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


%define libname libspeex1
Name:           speex
Version:        1.2.1
Release:        0
Summary:        An Open Source, Patent Free Speech Codec
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://www.speex.org/
Source0:        https://downloads.xiph.org/releases/speex/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         speex-no-build-date.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(speexdsp)

%description
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package -n %{libname}
Summary:        An Open Source, Patent Free Speech Codec Library
Group:          System/Libraries
Obsoletes:      libspeex < %{version}
Provides:       libspeex = %{version}

%description -n %{libname}
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package devel
Summary:        Development package for SpeeX
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       speexdsp-devel
Provides:       libspeex-devel = %{version}-%{release}
Obsoletes:      libspeex-devel < %{version}-%{release}

%description devel
This package contains the files needed to compile programs that use the
SpeeX library.

%prep
%setup -q
%patch0

%build
%configure \
	--enable-binaries \
	--disable-static

%make_build

%install
%make_install
# remove duped documents
rm -rf %{buildroot}%{_datadir}/doc/speex*
# remove unneeded *.la files
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_libdir}/*.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/speex*
%{_mandir}/man?/*

%files -n %{libname}
%{_libdir}/libspeex.so.*

%files devel
%doc doc/manual.pdf
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
