#
# spec file for package openexr
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


%define prjname      openexr
%define flavor   @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define flavor   openexr
%endif

# perhaps you want to build against corresponding ilmbase build
%define asan_build  0
%define debug_build 0
%define sonum 25
%global so_suffix -2_5
Name:           %{flavor}
Version:        2.5.4
Release:        0
%if "%{flavor}" == "openexr"
Summary:        Utilities for working with HDR images in OpenEXR format
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
%endif
%if "%{flavor}" == "ilmbase"
Summary:        Base library for ILM software (OpenEXR)
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
%endif
URL:            http://www.openexr.com/
Source0:        https://github.com/openexr/openexr/archive/v%{version}.tar.gz
Source2:        baselibs.conf
Patch1:         0001-Use-absolute-CMAKE_INSTALL_FULL_LIBDIR-for-libdir-in.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
%if "%{flavor}" == "openexr"
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  pkgconfig(IlmBase) == %{version}
BuildRequires:  pkgconfig(zlib)
%endif
%if "%{flavor}" == "ilmbase"
BuildRequires:  libtool
%endif
%if "%{flavor}" == "openexr"
Obsoletes:      OpenEXR <= 1.6.1
Provides:       OpenEXR = %{version}
%endif
%if "%{flavor}" == "ilmbase"
Obsoletes:      IlmBase <= 1.0.1
Provides:       IlmBase = %{version}
%endif
%if %{asan_build} || %{debug_build}
BuildRequires:  ilmbase-debugsource
BuildRequires:  libHalf%{so_suffix}-%{sonum}-debuginfo
BuildRequires:  libIex%{so_suffix}-%{sonum}-debuginfo
BuildRequires:  libIexMath%{so_suffix}-%{sonum}-debuginfo
BuildRequires:  libIlmThread%{so_suffix}-%{sonum}-debuginfo
BuildRequires:  libImath%{so_suffix}-%{sonum}-debuginfo
%endif

%if "%{flavor}" == "openexr"

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
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIlmImf%{so_suffix}-%{sonum}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libIlmImf

%package -n libIlmImfUtil%{so_suffix}-%{sonum}
Summary:        Library to simplify development of OpenEXR utilities
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIlmImfUtil%{so_suffix}-%{sonum}
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains shared library libIlmImfUtil

%package devel
Summary:        Development files for the 16-bit FP EXR picture handling library
License:        BSD-3-Clause AND GPL-2.0-or-later
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
License:        BSD-3-Clause
Group:          Documentation/Other
Obsoletes:      OpenEXR-doc <= 1.6.1
Provides:       OpenEXR-doc = %{version}

%description doc
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.

This package contains documentation.

%endif

%if %{flavor} == "ilmbase"

%description
Base library for Industrial Light & Magic software (OpenEXR).

* Half is a class that encapsulates our 16-bit floating-point
   format.

* IlmThread is a thread abstraction library for use with OpenEXR and
   other software packages.  It currently supports pthreads and
   Windows threads.

* Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices,
   quaternions and other useful 2D and 3D math functions.

* Iex is an exception-handling library.

%package devel
Summary:        Base library for ILM software (OpenEXR)
# Renamed to libilmbase6 to met the Shared Library Policy
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libHalf%{so_suffix}-%{sonum}
Requires:       libIex%{so_suffix}-%{sonum}
Requires:       libIexMath%{so_suffix}-%{sonum}
Requires:       libIlmThread%{so_suffix}-%{sonum}
Requires:       libImath%{so_suffix}-%{sonum}
Requires:       libstdc++-devel

%description devel
Devel files for ilmbase
Base library for Industrial Light & Magic software (OpenEXR).

%package -n libHalf%{so_suffix}-%{sonum}
Summary:        16-bit floating-point encapsulation class for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libHalf%{so_suffix}-%{sonum}
%{summary}.

%package -n libIexMath%{so_suffix}-%{sonum}
Summary:        Exception-based vector/matrix library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIexMath%{so_suffix}-%{sonum}
%{summary}.

%package -n libIex%{so_suffix}-%{sonum}
Summary:        Exception handling library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIex%{so_suffix}-%{sonum}
%{summary}.

%package -n libIlmThread%{so_suffix}-%{sonum}
Summary:        Thread abstraction library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIlmThread%{so_suffix}-%{sonum}
%{summary}.

%package -n libImath%{so_suffix}-%{sonum}
Summary:        Vector/matrix library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libImath%{so_suffix}-%{sonum}
%{summary}.

%endif

%prep
%setup -q -n %{prjname}-%{version}
%patch1 -p1

%build
%if "%{flavor}" == "openexr"
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
%endif

%if %{flavor} == "ilmbase"
pushd IlmBase
%cmake
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
popd
%endif

%install
%if "%{flavor}" == "openexr"
pushd OpenEXR
%cmake_install
popd
%endif

%if "%{flavor}" == "ilmbase"
pushd IlmBase
%cmake_install
popd
%endif

%check
%if "%{flavor}" == "openexr"
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
%endif

%if "%{flavor}" == "ilmbase"
# https://github.com/openexr/openexr/issues/570
%ifnarch i586
pushd IlmBase
export LD_LIBRARY_PATH="$PWD/build/Imath:$PWD/build/Iex:$PWD/build/Half:$LD_LIBRARY_PATH"
%ctest
popd
%endif
%endif

%if "%{flavor}" == "openexr"
%post -n libIlmImf%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libIlmImf%{so_suffix}-%{sonum} -p /sbin/ldconfig

%post -n libIlmImfUtil%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libIlmImfUtil%{so_suffix}-%{sonum} -p /sbin/ldconfig
%endif

%if "%{flavor}" == "ilmbase"
%post -n libHalf%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libHalf%{so_suffix}-%{sonum} -p /sbin/ldconfig

%post -n libIexMath%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libIexMath%{so_suffix}-%{sonum} -p /sbin/ldconfig

%post -n libIex%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libIex%{so_suffix}-%{sonum} -p /sbin/ldconfig

%post -n libIlmThread%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libIlmThread%{so_suffix}-%{sonum} -p /sbin/ldconfig

%post -n libImath%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libImath%{so_suffix}-%{sonum} -p /sbin/ldconfig
%endif

%if "%{flavor}" == "openexr"
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
%endif

%if "%{flavor}" == "ilmbase"
%files devel
%doc CHANGES.md CODE_OF_CONDUCT.md CODEOWNERS CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md
%license LICENSE.md
%{_includedir}/OpenEXR
%{_libdir}/libHalf.so
%{_libdir}/libHalf%{so_suffix}.so
%{_libdir}/libIex.so
%{_libdir}/libIex%{so_suffix}.so
%{_libdir}/libImath.so
%{_libdir}/libImath%{so_suffix}.so
%{_libdir}/libIlmThread.so
%{_libdir}/libIlmThread%{so_suffix}.so
%{_libdir}/libIexMath.so
%{_libdir}/libIexMath%{so_suffix}.so
%{_libdir}/pkgconfig/IlmBase.pc
%dir %{_libdir}/cmake/IlmBase/
%{_libdir}/cmake/IlmBase/*.cmake

%files -n libHalf%{so_suffix}-%{sonum}
%{_libdir}/libHalf%{so_suffix}.so.*

%files -n libIexMath%{so_suffix}-%{sonum}
%{_libdir}/libIexMath%{so_suffix}.so.*

%files -n libIex%{so_suffix}-%{sonum}
%{_libdir}/libIex%{so_suffix}.so.*

%files -n libIlmThread%{so_suffix}-%{sonum}
%{_libdir}/libIlmThread%{so_suffix}.so.*

%files -n libImath%{so_suffix}-%{sonum}
%{_libdir}/libImath%{so_suffix}.so.*
%endif

%changelog
