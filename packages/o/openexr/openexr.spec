#
# spec file for package openexr
#
# Copyright (c) 2020 SUSE LLC
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
%define sonum 25
%global so_suffix -2_5
Name:           openexr
Version:        2.5.3
Release:        0
Summary:        Utilities for working with HDR images in OpenEXR format
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            http://www.openexr.com/
Source0:        https://github.com/openexr/openexr/archive/v%{version}.tar.gz
Source2:        baselibs.conf
Patch1:         0001-Use-absolute-CMAKE_INSTALL_FULL_LIBDIR-for-libdir-in.patch
BuildRequires:  cmake
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(IlmBase) == %{version}
BuildRequires:  pkgconfig(zlib)
Obsoletes:      OpenEXR <= 1.6.1
Provides:       OpenEXR = %{version}
%if %{asan_build} || %{debug_build}
BuildRequires:  ilmbase-debugsource
BuildRequires:  libHalf%{so_suffix}-%{sonum}-debuginfo
BuildRequires:  libIex%{so_suffix}-%{sonum}-debuginfo
BuildRequires:  libIexMath%{so_suffix}-%{sonum}-debuginfo
BuildRequires:  libIlmThread%{so_suffix}-%{sonum}-debuginfo
BuildRequires:  libImath%{so_suffix}-%{sonum}-debuginfo
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

%package -n libIlmImf%{so_suffix}-%{sonum}
Summary:        Library to Handle EXR Pictures in 16-Bit Floating-Point Format
Group:          System/Libraries

%description -n libIlmImf%{so_suffix}-%{sonum}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libIlmImf

%package -n libIlmImfUtil%{so_suffix}-%{sonum}
Summary:        Library to simplify development of OpenEXR utilities
Group:          System/Libraries

%description -n libIlmImfUtil%{so_suffix}-%{sonum}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libIlmImfUtil

%package devel
Summary:        Development files for the 16-bit FP EXR picture handling library
Group:          Development/Libraries/C and C++
Requires:       ilmbase-devel >= 2.3.0
Requires:       libIlmImf%{so_suffix}-%{sonum} = %{version}
Requires:       libIlmImfUtil%{so_suffix}-%{sonum} = %{version}
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
Summary:        Documentation for the 16-bit FP EXR picture handling library
Group:          Documentation/Other
Obsoletes:      OpenEXR-doc <= 1.6.1
Provides:       OpenEXR-doc = %{version}

%description doc
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains documentation.

%prep
%setup -q
%patch1 -p1

%build
pushd OpenEXR
export PTHREAD_LIBS="-lpthread"
%if %{debug_build}
export CXXFLAGS="%{optflags} -O0"
%endif
%cmake \
  -DCMAKE_INSTALL_DOCDIR="%{_docdir}/%{name}"
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
%cmake_build
popd

%install
pushd OpenEXR
%cmake_install
popd

%check
%ifnarch i586 ppc ppc64 s390 s390x
pushd OpenEXR
export LD_LIBRARY_PATH="%{buildroot}/%{_libdir}"
# tests can take longer than the default timeout of 25 minutes
%if 0%{?suse_version} < 1550
# HACK - older versions of the ctest macro do not allow passing additional parameters
%global __ctest %{__ctest} --timeout 3600
%ctest
%else
%ctest --timeout 3600
%endif
popd
%endif

%post -n libIlmImf%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libIlmImf%{so_suffix}-%{sonum} -p /sbin/ldconfig

%post -n libIlmImfUtil%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libIlmImfUtil%{so_suffix}-%{sonum} -p /sbin/ldconfig

%files
%license LICENSE.md
%doc CHANGES.md CODE_OF_CONDUCT.md CODEOWNERS CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md
%{_bindir}/exrenvmap
%{_bindir}/exrheader
%{_bindir}/exrmakepreview
%{_bindir}/exrmaketiled
%{_bindir}/exrstdattr
%{_bindir}/exrmultiview
%{_bindir}/exrmultipart
%{_bindir}/exr2aces

%files devel
%{_includedir}/OpenEXR
%{_libdir}/libIlmImf.so
%{_libdir}/libIlmImf%{so_suffix}.so
%{_libdir}/libIlmImfUtil.so
%{_libdir}/libIlmImfUtil%{so_suffix}.so
%{_libdir}/pkgconfig/OpenEXR.pc
%dir %{_libdir}/cmake/OpenEXR
%{_libdir}/cmake/OpenEXR/*.cmake

%files doc
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/{CHANGES.md,CODE_OF_CONDUCT.md,CODEOWNERS,CONTRIBUTING.md,CONTRIBUTORS.md,README.md,SECURITY.md}

%files -n libIlmImf%{so_suffix}-%{sonum}
%license LICENSE.md
%{_libdir}/libIlmImf-*.so.*

%files -n libIlmImfUtil%{so_suffix}-%{sonum}
%license LICENSE.md
%{_libdir}/libIlmImfUtil-*.so.*

%changelog
