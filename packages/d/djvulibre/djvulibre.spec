#
# spec file for package djvulibre
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


%define asan_build     0

%define	libname	lib%{name}21
Name:           djvulibre
Version:        3.5.27
Release:        0
Summary:        An Implementation of DjVu
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
Url:            http://djvu.sourceforge.net
Source:         http://downloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://sourceforge.net/p/djvu/djvulibre-git/ci/ff8e5b68f856a7fe17c9aa33d0f2220f4ba6b40c/
Patch0:         reproducible.patch
# CVE-2019-15143 [bsc#1146569]
Patch1:         djvulibre-CVE-2019-15143.patch
# CVE-2019-15144 [bsc#1146571]
Patch2:         djvulibre-CVE-2019-15144.patch
# CVE-2019-15145 [bsc#1146572]
Patch3:         djvulibre-CVE-2019-15145.patch
# CVE-2019-15142 [bsc#1146702]
Patch4:         djvulibre-CVE-2019-15142.patch
# do not segfault when libtiff encounters corrupted TIFF (upstream issue #295)
Patch5:         djvulibre-invalid-tiff.patch
# https://sourceforge.net/p/djvu/bugs/293/
Patch6:         djvulibre-always-assume-that-cpuid-works-on-x86_64.patch
# CVE-2019-18804 [bsc#1156188]
Patch7:         djvulibre-CVE-2019-18804.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libtiff-4)
Requires(post):    shared-mime-info
Requires(postun):  shared-mime-info
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
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

%post
%mime_database_post
%icon_theme_cache_post

%post  -n  %{libname} -p /sbin/ldconfig

%postun
%mime_database_postun
%icon_theme_cache_postun

%postun -n  %{libname} -p /sbin/ldconfig

%files
%license COPYING COPYRIGHT
%doc NEWS README
%doc %{_mandir}/man1/*
%{_datadir}/djvu
%{_bindir}/*
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/djvulibre-mime.xml

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
