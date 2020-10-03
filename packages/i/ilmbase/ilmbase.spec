#
# spec file for package ilmbase
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


%define asan_build  0
%define debug_build 0
%define sonum 25
%global so_suffix -2_5
Name:           ilmbase
Version:        2.5.3
Release:        0
Summary:        Base library for ILM software (OpenEXR)
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.openexr.com
Source0:        https://github.com/openexr/openexr/archive/v%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         0001-Use-absolute-CMAKE_INSTALL_FULL_LIBDIR-for-libdir-in.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
# Renamed to libilmbase6 to met the Shared Library Policy
Obsoletes:      IlmBase <= 1.0.1
Provides:       IlmBase = %{version}

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

%prep
%setup -q -n openexr-%{version}
%patch1 -p1

%build
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

%install
pushd IlmBase
%cmake_install
popd

%check
# https://github.com/openexr/openexr/issues/570
%ifnarch i586
pushd IlmBase
export LD_LIBRARY_PATH="$PWD/build/Imath:$PWD/build/Iex:$PWD/build/Half:$LD_LIBRARY_PATH"
%ctest
popd
%endif

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

%changelog
