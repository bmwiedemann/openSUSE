#
# spec file for package tiff
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define asan_build 0
%define debug_build 0
Name:           tiff
Version:        4.0.10
Release:        0
Summary:        Tools for Converting from and to the Tagged Image File Format
License:        HPND
Group:          Productivity/Graphics/Convertors
URL:            http://www.simplesystems.org/libtiff/
Source:         http://download.osgeo.org/libtiff/tiff-%{version}.tar.gz
Source2:        README.SUSE
Source3:        baselibs.conf
Patch0:         tiff-4.0.3-seek.patch
# http://bugzilla.maptools.org/show_bug.cgi?id=2442
Patch1:         tiff-4.0.3-compress-warning.patch
# http://bugzilla.maptools.org/show_bug.cgi?id=2798
# https://gitlab.com/libtiff/libtiff/merge_requests/44
Patch2:         tiff-CVE-2018-12900.patch
Patch3:         tiff-CVE-2018-17000,19210.patch
# http://bugzilla.maptools.org/show_bug.cgi?id=2836
# https://gitlab.com/libtiff/libtiff/merge_requests/50
Patch4:         tiff-CVE-2019-6128.patch
# http://bugzilla.maptools.org/show_bug.cgi?id=2833
# https://gitlab.com/libtiff/libtiff/merge_requests/54
# https://gitlab.com/libtiff/libtiff/merge_requests/60
Patch5:         tiff-CVE-2019-7663.patch
BuildRequires:  gcc-c++
BuildRequires:  libjbig-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  lzma-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
This package contains the library and support programs for the TIFF
image format.

%package -n libtiff5
Summary:        The Tiff Library (with JPEG and compression support)
Group:          System/Libraries
Provides:       libtiff = %{version}

%description -n libtiff5
This package includes the tiff libraries. To link a program with
libtiff, you will have to add -ljpeg and -lz to include the necessary
libjpeg and libz in the linking process.

%package -n libtiff-devel
Summary:        Development Tools for Programs which will use the libtiff Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libstdc++-devel
Requires:       libtiff5 = %{version}

%description -n libtiff-devel
This package contains the header files and static libraries for
developing programs which will manipulate TIFF format image files using
the libtiff library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="%{optflags} -fPIE"
%if %{debug_build}
CFLAGS="$CFLAGS -O0"
%endif
%configure --disable-static
%if %{asan_build}
find -name Makefile | xargs sed -i 's/\(^CFLAGS.*\)/\1 -fsanitize=address/'
%endif
make %{?_smp_mflags} LDFLAGS="-pie"

%install
mkdir -p %{buildroot}/{%{_mandir}/{man1,man3},usr/{bin,lib,include}}
%make_install
for f in `find %{buildroot}/%{_mandir} -type f -print ` ; do
  if [ `wc -l <$f` -eq 1 ] && grep -q "^\.so " $f ; then
    linkto=`sed -e "s|^\.so ||" $f`
    [ -f "`dirname $f`/$linkto" ] && ln -sf "$linkto" $f
  fi
done

cp %{SOURCE2} .
rm -rf %{buildroot}%{_datadir}/doc/tiff*
find %{buildroot} -type f -name "*.la" -delete -print
find html -name "Makefile*" | xargs rm
# remove pal2rgb, bsc#1071031
for tool in pal2rgb; do
  rm %{buildroot}%{_bindir}/$tool
  rm %{buildroot}%{_mandir}/man1/$tool.1
  rm html/man/$tool.1.html
done

%check
%if %{asan_build}
# ASAN needs /proc to be mounted
exit 0
%endif
for i in tools test; do
	(cd $i && make %{?_smp_mflags} check)
done

%post -n libtiff5 -p /sbin/ldconfig
%postun -n libtiff5 -p /sbin/ldconfig

%files
%{_bindir}/*
%doc html
%doc README.md VERSION ChangeLog TODO RELEASE-DATE
%{_mandir}/man1/*

%files -n libtiff5
%license COPYRIGHT
%doc README.md README.SUSE
%{_libdir}/*.so.*

%files -n libtiff-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%changelog
