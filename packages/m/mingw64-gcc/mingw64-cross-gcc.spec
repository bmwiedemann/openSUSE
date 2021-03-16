#
# spec file for package mingw64-cross-gcc
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


%define __os_install_post %{_prefix}/lib/rpm/brp-compress %{nil}
%define include_ada 0
Name:           mingw64-cross-gcc
Version:        9.2.0
Release:        0
Summary:        MinGW Windows cross-compiler (GCC) for C
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            http://www.mingw.org/
Source0:        ftp://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
Patch1:         gcc-make-xmmintrin-header-cplusplus-compatible.patch
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 4.2.0
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-headers >= 3.1.0
BuildConflicts: mingw64-headers-dummy-pthread
BuildRequires:  mingw64-runtime >= 3.1.0
BuildRequires:  mpc-devel >= 0.8.0
BuildRequires:  mpfr-devel >= 2.4.0
BuildRequires:  texinfo
BuildRequires:  unzip
BuildRequires:  xz
BuildRequires:  zip
BuildRequires:  zlib-devel
#!BuildIgnore:  gcc-PIE
#!BuildIgnore:  post-build-checks
# NB: Explicit mingw64-filesystem dependency is REQUIRED here.
Requires:       mingw64-cross-binutils
Requires:       mingw64-cross-cpp >= %{version}
Requires:       mingw64-filesystem
Requires:       mingw64-headers
Requires:       mingw64-runtime
# Once this full GCC is installed, it obsoletes the bootstrap GCC.
Conflicts:      mingw64-cross-gcc-bootstrap
%if %{include_ada}
BuildRequires:  gcc-ada
%endif

%description
MinGW Windows cross-compiler (GCC) for C

%package -n mingw64-cross-cpp
Summary:        MinGW Windows cross-C Preprocessor
Group:          Development/Languages/C and C++
Conflicts:      mingw64-cross-cpp-bootstrap

%description -n mingw64-cross-cpp
MinGW Windows cross-C Preprocessor

%package c++
Summary:        MinGW Windows cross-compiler for C++
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description c++
MinGW Windows cross-compiler for C++

%package fortran
Summary:        MinGW Windows cross-compiler for Fortran
Group:          Development/Languages/Fortran

%description fortran
MinGW Windows cross-compiler for Fortran

%package objc
Summary:        MinGW Windows cross-compiler for Objective-C and Objective-C++
Group:          Development/Languages/Other

%description objc
MinGW Windows cross-compiler for Objective-C and Objective-C++

%if %{include_ada}
%package ada
Summary:        MinGW Windows cross-compiler for Ada
Group:          Development/Languages/Other

%description ada
MinGW Windows cross-compiler for Ada

%endif

%prep
%setup -q -c
pushd gcc-%{version}
%patch1
popd

%build
cd gcc-%{version}

mkdir -p build
cd build

languages="c,c++,fortran,objc,obj-c++"

%if %{include_ada}
languages+=",ada"
ada_options=-enable-libada
%else
ada_options=
%endif

CC="gcc %{optflags}" \
CFLAGS_FOR_TARGET="-DGC_NOT_DLL %{_mingw64_cflags} -Wno-error=format -Wno-error=format-extra-args" \
CXXFLAGS_FOR_TARGET="-DGC_NOT_DLL %{_mingw64_cflags} -Wno-error=format -Wno-error=format-extra-args" \
CPPFLAGS_FOR_TARGET="-DGC_NOT_DLL %{_mingw64_cflags}" \
../configure \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libdir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --datadir=%{_datadir} \
  --build=%{_build} --host=%{_host} \
  --target=%{_mingw64_target} \
  --with-gnu-as --with-gnu-ld --verbose \
  --without-newlib \
  --disable-multilib \
  --enable-shared \
  --disable-plugin \
  --with-system-zlib \
  --disable-nls --without-included-gettext \
  --disable-win32-registry \
  --enable-threads=posix \
  --enable-version-specific-runtime-libs \
  --with-sysroot=%{_mingw64_sysroot} \
  --enable-languages="$languages" $optargs \
  ${ada_options} \
  --without-x \
  --enable-hash-synchronization \
  --enable-fully-dynamic-string \
  --enable-libgomp \
  --enable-linker-build-id \
  --disable-vtable-verify \
  --with-pkgversion="SUSE Linux"

make %{?_smp_mflags} all || make all

%install
cd gcc-%{version}
cd build
%make_install

# These files conflict with existing installed files.
rm -rf %{buildroot}%{_infodir}
rm -f %{buildroot}%{_libdir}/libiberty*
rm -f %{buildroot}%{_mandir}/man7/*
rm -f %{buildroot}%{_bindir}/vxaddr2line

mkdir -p %{buildroot}/lib
ln -sf ..%{_bindir}/%{_mingw64_target}-cpp \
  %{buildroot}/lib/%{_mingw64_target}-cpp

# The dlls that we will use are from the native build of gcc
find %{buildroot} -name \*.dll -exec rm {} +

mv %{buildroot}%{_libdir}/gcc/%{_mingw64_target}/lib/libgcc_s.a \
   %{buildroot}%{_libdir}/gcc/%{_mingw64_target}/%{version}/

rm -f %{buildroot}%{_bindir}/%{_mingw64_target}-aot-compile
rm -f %{buildroot}%{_bindir}/%{_mingw64_target}-rebuild-gcj-db
rm -f %{buildroot}%{_mandir}/man1/%{_mingw64_target}-aot-compile.1*
rm -f %{buildroot}%{_mandir}/man1/%{_mingw64_target}-gjdoc.1*
rm -f %{buildroot}%{_mandir}/man1/%{_mingw64_target}-rebuild-gcj-db.1*
rm -f %{buildroot}%{_mandir}/man3/%{_mingw64_target}-ffi.3*
rm -f %{buildroot}%{_mandir}/man3/%{_mingw64_target}-ffi_call.3*
rm -f %{buildroot}%{_mandir}/man3/%{_mingw64_target}-ffi_prep_cif*

rm -rf %{buildroot}%{_datadir}/python

find %{buildroot} -name \*.py -exec rm {} +

# Hack to work around a bug in GCC6
perl -pi -e 's#include_next\ \<stdlib\.h\>#include\ \<stdlib\.h\>#g' \
	%{buildroot}%{_libdir}/gcc/%{_mingw64_target}/%{version}/include/c++/cstdlib \
	%{buildroot}%{_libdir}/gcc/%{_mingw64_target}/%{version}/include/c++//bits/std_abs.h
perl -pi -e 's#include_next\ \<math\.h\>#include\ \<math\.h\>#g' \
	%{buildroot}%{_libdir}/gcc/%{_mingw64_target}/%{version}/include/c++/cmath

%files
%{_bindir}/%{_mingw64_target}-gcc*
%{_bindir}/%{_mingw64_target}-gcov*
%dir %{_libdir}/gcc/%{_mingw64_target}
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}
%{_libdir}/gcc/%{_mingw64_target}/%{version}/crtbegin.o
%{_libdir}/gcc/%{_mingw64_target}/%{version}/crtend.o
%{_libdir}/gcc/%{_mingw64_target}/%{version}/crtfastmath.o
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgcc.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgcc_eh.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgcc_s.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgcov.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libssp.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libssp.dll.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libssp.la
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libssp_nonshared.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libssp_nonshared.la
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libcaf_single.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libcaf_single.la
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgomp.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgomp.dll.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgomp.la
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgomp.spec
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libatomic.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libatomic.dll.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libatomic.la
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}/include
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}/include-fixed
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}/include/ssp
%{_libdir}/gcc/%{_mingw64_target}/%{version}/include-fixed/README
%{_libdir}/gcc/%{_mingw64_target}/%{version}/include-fixed/*.h
%{_libdir}/gcc/%{_mingw64_target}/%{version}/include/*.h
%{_libdir}/gcc/%{_mingw64_target}/%{version}/include/ssp/*.h
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}/install-tools
%{_libdir}/gcc/%{_mingw64_target}/%{version}/install-tools/*
%{_mandir}/man1/%{_mingw64_target}-gcc.1*
%{_mandir}/man1/%{_mingw64_target}-gcov.1*
%{_mandir}/man1/%{_mingw64_target}-gcov-dump.1*
%{_mandir}/man1/%{_mingw64_target}-gcov-tool.1*
%{_libdir}/gcc/%{_mingw64_target}/%{version}/collect2
%{_libdir}/gcc/%{_mingw64_target}/%{version}/lto-wrapper
%{_libdir}/gcc/%{_mingw64_target}/%{version}/lto1
%{_libdir}/gcc/%{_mingw64_target}/%{version}/liblto_plugin.so*
%{_libdir}/gcc/%{_mingw64_target}/%{version}/liblto_plugin.la

%files -n mingw64-cross-cpp
/lib/%{_mingw64_target}-cpp
%{_bindir}/%{_mingw64_target}-cpp
%{_mandir}/man1/%{_mingw64_target}-cpp.1*
%dir %{_libdir}/gcc/%{_mingw64_target}
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}
%{_libdir}/gcc/%{_mingw64_target}/%{version}/cc1

%files c++
%{_bindir}/%{_mingw64_target}-g++
%{_bindir}/%{_mingw64_target}-c++
%{_mandir}/man1/%{_mingw64_target}-g++.1*
%{_libdir}/gcc/%{_mingw64_target}/%{version}/include/c++/
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libstdc++.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libstdc++.dll.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libstdc++.la
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libsupc++.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libsupc++.la
%{_libdir}/gcc/%{_mingw64_target}/%{version}/cc1plus

%files fortran
%{_bindir}/%{_mingw64_target}-gfortran
%{_mandir}/man1/%{_mingw64_target}-gfortran.1*
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgfortran.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgfortran.dll.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgfortran.la
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libgfortran.spec
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libquadmath.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libquadmath.dll.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libquadmath.la
%{_libdir}/gcc/%{_mingw64_target}/%{version}/f951
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/ieee_arithmetic.mod
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/ieee_exceptions.mod
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/ieee_features.mod
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/openacc.f90
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/openacc.mod
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/openacc_kinds.mod
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/openacc_lib.h
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/omp_lib.f90
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/omp_lib.h
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/omp_lib.mod
%{_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/omp_lib_kinds.mod

%files objc
%{_libdir}/gcc/%{_mingw64_target}/%{version}/include/objc
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libobjc.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libobjc.dll.a
%{_libdir}/gcc/%{_mingw64_target}/%{version}/libobjc.la
%{_libdir}/gcc/%{_mingw64_target}/%{version}/cc1obj*

%if %{include_ada}
%files ada
%{_libdir}/gcc/%{_mingw64_target}/%{version}/adainclude
%{_libdir}/gcc/%{_mingw64_target}/%{version}/adalib
%{_libdir}/gcc/%{_mingw64_target}/%{version}/gnat1
%{_bindir}/%{_mingw64_target}-gnat*

%endif

%changelog
