#
# spec file for package ilmbase
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define sonum 24
%global so_suffix -2_3-24
Name:           ilmbase
Version:        2.3.0
Release:        0
Summary:        Base library for ILM software (OpenEXR)
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.openexr.com
Source0:        https://github.com/openexr/openexr/releases/download/v%{version}/ilmbase-%{version}.tar.gz
Source1:        https://github.com/openexr/openexr/releases/download/v%{version}/ilmbase-%{version}.tar.gz.sig
Source2:        baselibs.conf
Source3:        https://savannah.nongnu.org/project/memberlist-gpgkeys.php?group=openexr&download=1#/ilmbase.keyring
#PATCH-FIX-OPENSUSE: testBox.patch allow fuzzy comparison of floats, doubles
Patch0:         testBox.patch
#PATCH-FIX-OPENSUSE: testBoxAlgo.patch allow fuzzy match of b12 == b2
Patch1:         testBoxAlgo.patch
BuildRequires:  autoconf
BuildRequires:  automake
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
Requires:       libHalf%{sonum}
Requires:       libIex%{so_suffix}
Requires:       libIexMath%{so_suffix}
Requires:       libIlmThread%{so_suffix}
Requires:       libImath%{so_suffix}
Requires:       libstdc++-devel
Obsoletes:      IlmBase-devel <= 1.0.1
Provides:       IlmBase-devel = %{version}
Obsoletes:      libilmbase-devel <= 1.0.2
Provides:       libilmbase-devel = %{version}

%description devel
Devel files for ilmbase
Base library for Industrial Light & Magic software (OpenEXR).

%files devel
%doc AUTHORS ChangeLog NEWS README*
%license LICENSE
%{_includedir}/OpenEXR
%{_libdir}/libHalf.so
%{_libdir}/libIex.so
%{_libdir}/libImath.so
%{_libdir}/libIlmThread.so
%{_libdir}/libIexMath.so
%{_libdir}/pkgconfig/IlmBase.pc

%package -n libHalf%{sonum}
Summary:        16-bit floating-point encapsulation class for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libHalf%{sonum}
%{summary}.

%post -n libHalf%{sonum} -p /sbin/ldconfig
%postun -n libHalf%{sonum} -p /sbin/ldconfig

%files -n libHalf%{sonum}
%{_libdir}/libHalf.so.*

%package -n libIexMath%{so_suffix}
Summary:        Exception-based vector/matrix library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIexMath%{so_suffix}
%{summary}.

%post -n libIexMath%{so_suffix} -p /sbin/ldconfig
%postun -n libIexMath%{so_suffix} -p /sbin/ldconfig

%files -n libIexMath%{so_suffix}
%{_libdir}/libIexMath*.so.*

%package -n libIex%{so_suffix}
Summary:        Exception handling library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIex%{so_suffix}
%{summary}.

%post -n libIex%{so_suffix} -p /sbin/ldconfig
%postun -n libIex%{so_suffix} -p /sbin/ldconfig

%files -n libIex%{so_suffix}
%{_libdir}/libIex-*.so.*

%package -n libIlmThread%{so_suffix}
Summary:        Thread abstraction library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libIlmThread%{so_suffix}
%{summary}.

%post -n libIlmThread%{so_suffix} -p /sbin/ldconfig
%postun -n libIlmThread%{so_suffix} -p /sbin/ldconfig

%files -n libIlmThread%{so_suffix}
%{_libdir}/libIlmThread*.so.*

%package -n libImath%{so_suffix}
Summary:        Vector/matrix library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libImath%{so_suffix}
%{summary}.

%post -n libImath%{so_suffix} -p /sbin/ldconfig
%postun -n libImath%{so_suffix} -p /sbin/ldconfig

%files -n libImath%{so_suffix}
%{_libdir}/libImath*.so.*

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./bootstrap
export PTHREAD_LIBS="-lpthread"
%if %{debug_build}
export CXXFLAGS="%{optflags} -O0"
%endif
%configure --disable-static
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
make %{?_smp_mflags} check

%changelog
