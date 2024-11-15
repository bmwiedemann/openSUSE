#
# spec file for package tiff
#
# Copyright (c) 2024 SUSE LLC
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


%global build_flavor @BUILD_FLAVOR@%{nil}

%if "%{?build_flavor}" == "man"
%bcond_without tiff_manpages
%else
%bcond_with    tiff_manpages
%endif

%define asan_build 0
%define debug_build 0
%define pkg_name tiff

%if "%{build_flavor}" == ""
Name:           tiff
%else
Name:           tiff-%{build_flavor}
%endif
Version:        4.7.0
Release:        0
Summary:        Tools for Converting from and to the Tagged Image File Format
License:        HPND
Group:          Productivity/Graphics/Convertors
URL:            https://libtiff.gitlab.io/libtiff/
Source:         https://download.osgeo.org/libtiff/tiff-%{version}.tar.xz
Source1:        https://download.osgeo.org/libtiff/tiff-%{version}.tar.xz.sig
Source2:        README.SUSE
Source3:        baselibs.conf
Source99:       tiff.keyring
Patch0:         tiff-4.0.3-seek.patch
%if %{with tiff_manpages}
BuildRequires:  %{primary_python}-Sphinx
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libjbig-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  lzma-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Recommends:     tiff-docs = %{versiong}

%description
This package contains the library and support programs for the TIFF
image format.

%package -n libtiff6
Summary:        The Tiff Library (with JPEG and compression support)
Group:          System/Libraries
Provides:       libtiff = %{version}

%description -n libtiff6
This package includes the tiff libraries. To link a program with
libtiff, you will have to add -ljpeg and -lz to include the necessary
libjpeg and libz in the linking process.

%package -n libtiff-devel
Summary:        Development Tools for Programs which will use the libtiff Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libstdc++-devel
Requires:       libtiff6 = %{version}
Recommends:     libtiff-devel-docs = %{version}

%description -n libtiff-devel
This package contains the header files and static libraries for
developing programs which will manipulate TIFF format image files using
the libtiff library.

%if %{with tiff_manpages}

%package -n tiff-docs
Summary:        Development Tools for Programs which will use the libtiff Library
Group:          Productivity/Graphics/Convertors
Requires:       tiff = %{version}
BuildArch:      noarch

%description -n tiff-docs
This package contains the header files and static libraries for
developing programs which will manipulate TIFF format image files using
the libtiff library.

This package holds the man pages for the command lint tools.

%package -n libtiff-devel-docs
Summary:        Development Documentation for Programs which will use the libtiff Library
Group:          Development/Libraries/C and C++
Requires:       libtiff-devel = %{version}
BuildArch:      noarch

%description -n libtiff-devel-docs
This package contains the header files and static libraries for
developing programs which will manipulate TIFF format image files using
the libtiff library.

This package holds the development man pages.
%endif

%prep
%autosetup -p1 -n %{pkg_name}-%{version}

%build
CFLAGS="%{optflags} -fPIC"
%if %{debug_build}
CFLAGS="$CFLAGS -O0"
%endif
# tools are not enabled for now due to test failure `FAIL: tiffcp-32bpp-None-jpeg.sh`
%cmake
%if %{asan_build}
find -name Makefile | xargs sed -i 's/\(^CFLAGS.*\)/\1 -fsanitize=address/'
%endif
%cmake_build

%install
%cmake_install

cp %{SOURCE2} .
rm -rf %{buildroot}%{_datadir}/doc/{,packages/}tiff*
find %{buildroot} -type f -name "*.la" -delete -print
%if %{with tiff_manpages}
rm -rv \
  %{buildroot}%{_bindir} \
  %{buildroot}%{_libdir} \
  %{buildroot}%{_includedir}

%files -n tiff-docs
%{_mandir}/man1/*

%files -n libtiff-devel-docs
%{_mandir}/man3/*

%else

%check
%if %{asan_build}
# ASAN needs /proc to be mounted
exit 0
%endif
%ctest

%ldconfig_scriptlets -n libtiff6

%files
%{_bindir}/*
%doc README.md VERSION ChangeLog TODO RELEASE-DATE

%files -n libtiff6
%license LICENSE.md
%doc README.md README.SUSE
%{_libdir}/*.so.*

%files -n libtiff-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/tiff/
%endif

%changelog
