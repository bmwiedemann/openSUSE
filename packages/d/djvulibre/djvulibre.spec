#
# spec file for package djvulibre
#
# Copyright (c) 2021 SUSE LLC
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


%define asan_build     0

%define	libname	lib%{name}21
Name:           djvulibre
Version:        3.5.28
Release:        0
Summary:        An Implementation of DjVu
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://djvu.sourceforge.net
Source:         http://downloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# CVE-2021-32490 [bsc#1185895], Out of bounds write in function DJVU:filter_bv() via crafted djvu file
Patch0:         djvulibre-CVE-2021-32490.patch
# CVE-2021-32491 [bsc#1185900], Integer overflow in function render() in tools/ddjvu via crafted djvu file
Patch1:         djvulibre-CVE-2021-32491.patch
# CVE-2021-32492 [bsc#1185904], Out of bounds read in function DJVU:DataPool:has_data() via crafted djvu file
Patch2:         djvulibre-CVE-2021-32492.patch
# CVE-2021-32493 [bsc#1185905], Heap buffer overflow in function DJVU:GBitmap:decode() via crafted djvu file
Patch3:         djvulibre-CVE-2021-32493.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
# libtool needed to regenerate missing configure script (v 3.5.28)
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libtiff-4)

%description
DjVu is a Web-centric format and software platform for distributing
documents and images. DjVuLibre is an implementation of DjVu,
including viewers, browser plug-ins, decoders, encoders, and
utilities. DjVu can replace PDF, PS, TIFF, JPEG, and GIF for
distributing scanned documents, digital documents, or high-resolution
pictures. DjVu content is often smaller and consumes less client
resources than competing formats.

%package -n %{libname}
Summary:        DjVu rendering library
Group:          Productivity/Graphics/Other

%description -n  %{libname}
DjVuLibre is an implementation of DjVu, a Web-centric format and
software platform for distributing documents and images.

This package contains the shared libraries.

%package -n libdjvulibre-devel
Summary:        Headers for djvulibre libraries
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}

%description -n libdjvulibre-devel
DjVuLibre is an implementation of DjVu, a Web-centric format and
software platform for distributing documents and images.

This package contains the development files.

%package doc
Summary:        Documentation for djvulibre
Group:          Productivity/Graphics/Other
BuildArch:      noarch

%description doc
DjVuLibre is an implementation of DjVu, a Web-centric format and
software platform for distributing documents and images.

This package contains the documentation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# configure script missing; generate using autogen.sh
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-silent-rules
%if %{asan_build}
sed -i -e 's/\(^CFLAGS.*\)/\1 -fsanitize=address/' \
       -e 's/\(^CXXFLAGS.*\)/\1 -fsanitize=address/' \
       -e 's/\(^LIBS =.*\)/\1 -lasan/' \
       Makefile */Makefile
%endif
make %{?_smp_mflags}

%install
%make_install

# do not ship these
rm %{buildroot}%{_libdir}/libdjvulibre.la

%fdupes %{buildroot}/%{_prefix}

%if 0%{?suse_version} < 1550
%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun
%endif

%post  -n  %{libname} -p /sbin/ldconfig

%postun -n  %{libname} -p /sbin/ldconfig

%files
%license COPYING COPYRIGHT
%doc NEWS README
%doc %{_mandir}/man1/*
%{_datadir}/djvu
%{_bindir}/*
%{_datadir}/icons/hicolor/*

%files -n %{libname}
%{_libdir}/libdjvulibre.so.*

%files -n libdjvulibre-devel
%{_libdir}/libdjvulibre.so
%dir %{_includedir}/libdjvu
%{_includedir}/libdjvu/*.h
%{_libdir}/pkgconfig/ddjvuapi.pc

%files doc
%doc doc/*

%changelog
