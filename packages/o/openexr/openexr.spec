#
# spec file for package openexr
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


%define prjname      openexr
# perhaps you want to build against corresponding Imath build
%define debug_build 0
%define sonum 30
%global so_suffix -3_1
Name:           openexr
Version:        3.1.5
Release:        0
Summary:        Utilities for working with HDR images in OpenEXR format
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.openexr.com/
Source0:        https://github.com/openexr/openexr/archive/v%{version}.tar.gz
Source2:        baselibs.conf
BuildRequires:  cmake >= 3.12
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Imath)
BuildRequires:  pkgconfig(zlib)
Obsoletes:      OpenEXR <= 1.6.1
Provides:       OpenEXR = %{version}

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

%package -n libIex%{so_suffix}-%{sonum}
Summary:        Exception handling library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIex%{so_suffix}-%{sonum}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libIex

%package -n libIlmThread%{so_suffix}-%{sonum}
Summary:        Thread abstraction library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIlmThread%{so_suffix}-%{sonum}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libIlmThread

%package -n libOpenEXR%{so_suffix}-%{sonum}
Summary:        Library to Handle EXR Pictures in 16-Bit Floating-Point Format
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libOpenEXR%{so_suffix}-%{sonum}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libOpenEXR

%package -n libOpenEXRCore%{so_suffix}-%{sonum}
Summary:        Library to Handle EXR Pictures in 16-Bit Floating-Point Format
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libOpenEXRCore%{so_suffix}-%{sonum}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libOpenEXRCore

%package -n libOpenEXRUtil%{so_suffix}-%{sonum}
Summary:        Library to simplify development of OpenEXR utilities
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libOpenEXRUtil%{so_suffix}-%{sonum}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libOpenEXRUtil

%package devel
Summary:        Development files for the 16-bit FP EXR picture handling library
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       Imath-devel
Requires:       libOpenEXR%{so_suffix}-%{sonum} = %{version}
Requires:       libOpenEXRCore%{so_suffix}-%{sonum} = %{version}
Requires:       libOpenEXRUtil%{so_suffix}-%{sonum} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(zlib)
Obsoletes:      OpenEXR-devel <= 1.6.1
Provides:       OpenEXR-devel = %{version}
Obsoletes:      libopenexr-devel <= 1.7.0
Provides:       libopenexr-devel = %{version}
Obsoletes:      ilmbase-devel < 3.0
Provides:       ilmbase-devel = %{version}

%description devel
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains header files.

%package doc
Summary:        Documentation for the 16-bit FP EXR picture handling library
License:        BSD-3-Clause
Group:          Documentation/Other
Obsoletes:      OpenEXR-doc <= 1.6.1
Provides:       OpenEXR-doc = %{version}

%description doc
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains documentation.

%prep
%autosetup -p1

%build
export PTHREAD_LIBS="-lpthread"
%if %{debug_build}
export CXXFLAGS="%{optflags} -O0"
%endif
%cmake \
  -DCMAKE_INSTALL_DOCDIR="%{_docdir}/%{name}"
%cmake_build

%install
%cmake_install

%check
%ifnarch i586 ppc ppc64 s390 s390x
export LD_LIBRARY_PATH="%{buildroot}/%{_libdir}"
# tests can take longer than the default timeout of 25 minutes
%if 0%{?suse_version} < 1550
# HACK - older versions of the ctest macro do not allow passing additional parameters
%global __ctest %{__ctest} --timeout 3600
%ctest
%else
%ifarch ppc64le
# bsc#1205885
EXCLUDE_REGEX='testMultiTiledPartThreading'
%endif
%ctest --exclude-regex "$EXCLUDE_REGEX" --timeout 3600
%endif
%endif

%post -n libIex%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libIex%{so_suffix}-%{sonum} -p /sbin/ldconfig
%post -n libIlmThread%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libIlmThread%{so_suffix}-%{sonum} -p /sbin/ldconfig
%post -n libOpenEXR%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libOpenEXR%{so_suffix}-%{sonum} -p /sbin/ldconfig
%post -n libOpenEXRCore%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libOpenEXRCore%{so_suffix}-%{sonum} -p /sbin/ldconfig
%post -n libOpenEXRUtil%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libOpenEXRUtil%{so_suffix}-%{sonum} -p /sbin/ldconfig

%files
%license LICENSE.md
%doc CHANGES.md CODE_OF_CONDUCT.md CODEOWNERS CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md
%{_bindir}/exrenvmap
%{_bindir}/exrheader
%{_bindir}/exrinfo
%{_bindir}/exrmakepreview
%{_bindir}/exrmaketiled
%{_bindir}/exrstdattr
%{_bindir}/exrmultiview
%{_bindir}/exrmultipart
%{_bindir}/exr2aces

%files devel
%{_includedir}/OpenEXR
%{_libdir}/libIex.so
%{_libdir}/libIex%{so_suffix}.so
%{_libdir}/libIlmThread.so
%{_libdir}/libIlmThread%{so_suffix}.so
%{_libdir}/libOpenEXR.so
%{_libdir}/libOpenEXR%{so_suffix}.so
%{_libdir}/libOpenEXRCore.so
%{_libdir}/libOpenEXRCore%{so_suffix}.so
%{_libdir}/libOpenEXRUtil.so
%{_libdir}/libOpenEXRUtil%{so_suffix}.so
%{_libdir}/pkgconfig/OpenEXR.pc
%dir %{_libdir}/cmake/OpenEXR
%{_libdir}/cmake/OpenEXR/*.cmake

%files doc
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/{CHANGES.md,CODE_OF_CONDUCT.md,CODEOWNERS,CONTRIBUTING.md,CONTRIBUTORS.md,README.md,SECURITY.md}

%files -n libIex%{so_suffix}-%{sonum}
%license LICENSE.md
%{_libdir}/libIex-*.so.*

%files -n libIlmThread%{so_suffix}-%{sonum}
%license LICENSE.md
%{_libdir}/libIlmThread-*.so.*

%files -n libOpenEXR%{so_suffix}-%{sonum}
%license LICENSE.md
%{_libdir}/libOpenEXR-*.so.*

%files -n libOpenEXRCore%{so_suffix}-%{sonum}
%license LICENSE.md
%{_libdir}/libOpenEXRCore-*.so.*

%files -n libOpenEXRUtil%{so_suffix}-%{sonum}
%license LICENSE.md
%{_libdir}/libOpenEXRUtil-*.so.*

%changelog
