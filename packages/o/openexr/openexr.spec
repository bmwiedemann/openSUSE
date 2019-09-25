#
# spec file for package openexr
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


# perhaps you want to build against corresponding ilmbase build
%define asan_build  0
%define debug_build 0
%define sonum 24
%global so_suffix -2_3-24
Name:           openexr
Version:        2.3.0
Release:        0
Summary:        Utilities for working with HDR images in OpenEXR format
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            http://www.openexr.com/
Source0:        https://github.com/openexr/openexr/releases/download/v%{version}/openexr-%{version}.tar.gz
Source1:        https://github.com/openexr/openexr/releases/download/v%{version}/openexr-%{version}.tar.gz.sig
Source2:        baselibs.conf
Source3:        openexr.keyring
# https://github.com/openexr/openexr/pull/401
Patch0:         openexr-CVE-2018-18444.patch
# https://github.com/openexr/openexr/pull/401
# CVE-2017-9111 [bsc#1040109], CVE-2017-9113 [bsc#1040113], CVE-2017-9115 [bsc#1040115]
Patch1:         openexr-CVE-2017-9111,9113,9115.patch
# CVE-2017-14988 [bsc#1061305]
Patch2:         openexr-CVE-2017-14988.patch
BuildRequires:  automake
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(IlmBase) >= 2.3.0
BuildRequires:  pkgconfig(zlib)
Obsoletes:      OpenEXR <= 1.6.1
Provides:       OpenEXR = %{version}
%if %{asan_build} || %{debug_build}
BuildRequires:  ilmbase-debugsource
BuildRequires:  libHalf%{sonum}-debuginfo
BuildRequires:  libIex%{so_suffix}-debuginfo
BuildRequires:  libIexMath%{so_suffix}-debuginfo
BuildRequires:  libIlmThread%{so_suffix}-debuginfo
BuildRequires:  libImath%{so_suffix}-debuginfo
%endif

%description
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications. This package
contains a set of utilities to work with this format.

* exrheader, a utility for dumping header information
* exrstdattr, a utility for modifying OpenEXR standard attributes
* exrmaketiled, for generating tiled and rip/mipmapped images
* exrenvmap, for creating OpenEXR environment maps
* exrmakepreview, for creating preview images for OpenEXR files
* exr2aces, converter to ACES format
* exrmultiview, combine two or more images into one multi-view

%package -n libIlmImf%{so_suffix}
Summary:        Library to Handle EXR Pictures in 16-Bit Floating-Point Format
Group:          System/Libraries

%description -n libIlmImf%{so_suffix}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libIlmImf

%post -n libIlmImf%{so_suffix} -p /sbin/ldconfig
%postun -n libIlmImf%{so_suffix} -p /sbin/ldconfig

%files -n libIlmImf%{so_suffix}
%license LICENSE
%{_libdir}/libIlmImf-*.so.*

%package -n libIlmImfUtil%{so_suffix}
Summary:        Library to simplify development of OpenEXR utilities
Group:          System/Libraries

%description -n libIlmImfUtil%{so_suffix}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libIlmImfUtil

%post -n libIlmImfUtil%{so_suffix} -p /sbin/ldconfig
%postun -n libIlmImfUtil%{so_suffix} -p /sbin/ldconfig

%files -n libIlmImfUtil%{so_suffix}
%license LICENSE
%{_libdir}/libIlmImfUtil-*.so.*

%package devel
Summary:        Development files for the 16-bit FP EXR picture handling library
Group:          Development/Libraries/C and C++
Requires:       libIlmImf%{so_suffix} = %{version}
Requires:       libIlmImfUtil%{so_suffix} = %{version}
Requires:       libilmbase-devel >= 2.3.0
Requires:       pkgconfig
Requires:       pkgconfig(zlib)
Obsoletes:      OpenEXR-devel <= 1.6.1
Provides:       OpenEXR-devel = %{version}
Obsoletes:      libopenexr-devel <= 1.7.0
Provides:       libopenexr-devel = %{version}

%description devel
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains header files.

%package doc
Summary:        Documentatino for the 16-bit FP EXR picture handling library
Group:          Documentation/PDF
Obsoletes:      OpenEXR-doc <= 1.6.1
Provides:       OpenEXR-doc = %{version}

%description doc
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains documentation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export PTHREAD_LIBS="-lpthread"
%if %{debug_build}
export CXXFLAGS="%{optflags} -O0"
%endif
%configure \
   --docdir=%{_docdir}/%{name} \
   --disable-static \
   --enable-large-stack \
   --enable-imfexamples \
   --enable-imfhugetest
%if %{asan_build}
vmemlimit=$(ulimit -v)
if [ $vmemlimit != unlimited ]; then
  echo "ulimit -v has to be unlimited (currently $vmemlimit) to run ASAN build"
  exit 1
fi
for i in $(find -name Makefile); do
  sed -i -e 's/\(^CXXFLAGS.*\)/\1 -fsanitize=address/' \
         -e 's/\(^LIBS =.*\)/\1 -lasan/' \
         $i
done
%endif
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%ifarch x86_64
make %{?_smp_mflags} check
%endif

%files
%license LICENSE
%doc AUTHORS ChangeLog NEWS README*
%{_bindir}/exrenvmap
%{_bindir}/exrheader
%{_bindir}/exrmakepreview
%{_bindir}/exrmaketiled
%{_bindir}/exrstdattr
%{_bindir}/exrmultiview
%{_bindir}/exrmultipart

%files devel
%{_includedir}/OpenEXR
%{_libdir}/libIlmImf.so
%{_libdir}/libIlmImfUtil.so
%{_libdir}/pkgconfig/OpenEXR.pc
%{_datadir}/aclocal/openexr.m4

%files doc
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/AUTHORS
%exclude %{_docdir}/%{name}/ChangeLog
%exclude %{_docdir}/%{name}/NEWS
%exclude %{_docdir}/%{name}/README*

%changelog
