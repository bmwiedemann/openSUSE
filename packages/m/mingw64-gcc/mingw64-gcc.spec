#
# spec file for package mingw64-gcc
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


%define include_ada 0
%_mingw64_package_header_debug
Name:           mingw64-gcc
Version:        13.2.0
Release:        0
Summary:        MinGW Windows compiler (GCC) for C
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            http://www.mingw.org/
Source0:        ftp://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
Source100:      mingw64-gcc-rpmlintrc
Patch0:         gcc-make-xmmintrin-header-cplusplus-compatible.patch
Patch1:         gcc-12.1.0-fix-install-gdb-support-files.patch
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-cross-gcc >= %{version}
BuildRequires:  mingw64-cross-gcc-c++ >= %{version}
BuildRequires:  mingw64-cross-gcc-fortran >= %{version}
BuildRequires:  mingw64-cross-gcc-objc >= %{version}
BuildRequires:  mingw64-cross-pkg-config
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gmp-devel >= 4.2.0
BuildRequires:  mingw64-headers >= 3.1.0
BuildRequires:  mingw64-mpc-devel >= 0.8.0
BuildRequires:  mingw64-mpfr-devel >= 2.4.0
BuildRequires:  mingw64-runtime >= 3.1.0
BuildRequires:  mingw64-zlib-devel
BuildRequires:  mpc-devel
BuildRequires:  mpfr-devel
BuildRequires:  texinfo
BuildRequires:  unzip
BuildRequires:  xz
BuildRequires:  zip
#!BuildIgnore:  gcc-PIE
#!BuildIgnore:  post-build-checks
Requires:       mingw64-binutils
Requires:       mingw64-cpp >= %{version}
Requires:       mingw64-headers
Requires:       mingw64-runtime
Requires:       mingw64-winpthreads-devel
%if %{include_ada}
BuildRequires:  gcc-ada
BuildRequires:  mingw64-cross-gcc-ada >= %{version}
%endif
BuildArch:      noarch
# bugzilla.opensuse.org/1184052
#!BuildIgnore:  mingw64(libstdc++-6.dll)
#!BuildIgnore:  mingw64(libgcc_s_sjlj-1.dll)

%description
MinGW Windows compiler (GCC) for C

%package -n mingw64-libgcc_s_seh1
Summary:        MinGW Windows compiler for C shared libraries
Group:          System/Libraries
Obsoletes:      mingw64-libgcc < %{version}-%{release}
Provides:       mingw64-libgcc = %{version}-%{release}

%description -n mingw64-libgcc_s_seh1
MinGW Windows compiler for C shared libraries

This libgcc build supports Structured Exception Handling (SEH), which
is the native exception handling mechanism for Windows.
[SEH support is currently only implemented for the x86_64 target,
which is why the 32bit mingw package set does not contain it.]

%package -n mingw64-libgcc_s_sjlj1
Summary:        MinGW Windows compiler for C shared libraries
Group:          System/Libraries
Obsoletes:      mingw64-libgcc < %{version}-%{release}
Provides:       mingw64-libgcc = %{version}-%{release}

%description -n mingw64-libgcc_s_sjlj1
MinGW Windows compiler for C shared libraries

This libgcc build uses SJLJ, a method for exception handling based on
setjmp/longjmp. SJLJ-based EH is much slower than DWARF-2 EH,
penalizing even normal execution when no exceptions are thrown, but
can work across code that has not been compiled with GCC or that does
not have call-stack unwinding information.

[The DWARF-2 EH implementation for Windows is not at all designed to
work under 64-bit Windows applications. In Win32 mode, the exception
unwind handler cannot propagate through non-DW2 aware code, which
means that any exception going through any non-DW2-aware "foreign
frame" code will fail, including Windows system DLLs and DLLs built
with Visual Studio. DWARF-2 unwinding code in GCC inspects the x86
unwinding assembly and is unable to proceed without other DWARF-2
unwind information.]

%package -n mingw64-libssp0
Summary:        MinGW Windows compiler for C shared libraries
Group:          System/Libraries
Obsoletes:      mingw64-libssp < %{version}-%{release}
Provides:       mingw64-libssp = %{version}-%{release}

%description -n mingw64-libssp0
MinGW Windows compiler for C shared libraries

%package -n mingw64-libgomp1
Summary:        MinGW Windows compiler for C shared libraries
Group:          System/Libraries
Obsoletes:      mingw64-libgomp < %{version}-%{release}
Provides:       mingw64-libgomp = %{version}-%{release}

%description -n mingw64-libgomp1
MinGW Windows compiler for C shared libraries

%package -n mingw64-cpp
Summary:        MinGW Windows C Preprocessor
Group:          Development/Languages/C and C++

%description -n mingw64-cpp
MinGW Windows C Preprocessor

%package c++
Summary:        MinGW Windows compiler for C++
Group:          Development/Languages/C and C++
Requires:       mingw64-libstdc++-gdb-printer = %{version}-%{release}

%description c++
MinGW Windows compiler for C++

%package -n mingw64-libstdc++6
Summary:        MinGW Windows compiler for C++ shared libraries
Group:          System/Libraries
Obsoletes:      mingw64-libstdc++ < %{version}-%{release}
Provides:       mingw64-libstdc++ = %{version}-%{release}

%description -n mingw64-libstdc++6
MinGW Windows compiler for C++ shared libraries

%package -n mingw64-libstdc++-gdb-printer
Summary:        MinGW Windows compiler for C++ gdb pretty printer for libstdc++
Group:          System/Libraries

%description -n mingw64-libstdc++-gdb-printer
MinGW Windows compiler for C++ gdb pretty printer for libstdc++

%package fortran
Summary:        MinGW Windows compiler for Fortran
Group:          Development/Languages/Fortran

%description fortran
MinGW Windows compiler for Fortran

%package -n mingw64-libgfortran5
Summary:        MinGW Windows compiler for Fortran shared libraries
Group:          System/Libraries
Obsoletes:      mingw64-libgfortran < %{version}-%{release}
Provides:       mingw64-libgfortran = %{version}-%{release}

%description -n mingw64-libgfortran5
MinGW Windows compiler for Fortran shared libraries

%package -n mingw64-libquadmath0
Summary:        MinGW Windows Fortran Compiler Quadmath Runtime Library
Group:          System/Libraries

%description -n mingw64-libquadmath0
The runtime library needed to run programs compiled with the Fortran
compiler of the GNU Compiler Collection (GCC) and quadruple precision
floating point operations.

%package -n mingw64-libatomic1
Summary:        The GNU Compiler Atomic Operations Runtime Library
Group:          System/Libraries

%description -n mingw64-libatomic1
The runtime library for atomic operations of the GNU Compiler Collection (GCC).

%package objc
Summary:        MinGW Windows compiler for Objective-C and Objective-C++
Group:          Development/Languages/Other

%description objc
MinGW Windows compiler for Objective-C and Objective-C++

%package -n mingw64-libobjc4
Summary:        MinGW Windows compiler for Objective-C and Objective-C++ shared libraries
Group:          System/Libraries
Obsoletes:      mingw64-libobjc < %{version}-%{release}
Provides:       mingw64-libobjc = %{version}-%{release}

%description -n mingw64-libobjc4
MinGW Windows compiler for Objective-C and Objective-C++ shared libraries

%_mingw64_debug_package

%prep
%autosetup -p1 -n gcc-%{version}

%build
mkdir -p build
cd build

languages="c,c++,fortran,objc,obj-c++"

%if %{include_ada}
languages+=",ada"
ada_options=-enable-libada
%else
ada_options=
%endif

CC_FOR_TARGET=%{_mingw64_cc} \
CXX_FOR_TARGET=%{_mingw64_cxx} \
GFORTRAN_FOR_TARGET=%{_mingw64_target}-gfortran \
GCJ_FOR_TARGET=%{_mingw64_gcj} \
CFLAGS_FOR_TARGET="-DGC_NOT_DLL %{_mingw64_cflags} -Wno-error=format -Wno-error=format-extra-args" \
CFLAGS_FOR_BUILD="-I-%{_mingw64_includedir}" \
CPPFLAGS_FOR_BUILD="-I-%{_mingw64_includedir}" \
CXXFLAGS_FOR_BUILD="-I-%{_mingw64_includedir}" \
CXXFLAGS_FOR_TARGET="-DGC_NOT_DLL %{_mingw64_cflags} -Wno-error=format -Wno-error=format-extra-args" \
CPPFLAGS_FOR_TARGET="-DGC_NOT_DLL %{_mingw64_cflags}" \
../configure \
  --prefix=%{_mingw64_prefix} \
  --disable-werror \
  --disable-werror-always \
  --disable-bootstrap \
  --host=%{_mingw64_host} \
  --with-gnu-as --with-gnu-ld --verbose \
  --without-newlib \
  --disable-multilib \
  --enable-plugin \
  --with-system-zlib \
  --disable-plugin \
  --disable-nls --without-included-gettext \
  --disable-win32-registry \
  --enable-threads=posix \
  --enable-version-specific-runtime-libs \
  --with-build-sysroot=%{_mingw64_sysroot} \
  --with-sysroot=%{_mingw64_prefix} \
  --enable-languages="$languages" $optargs \
  --without-x \
  ${ada_options} \
  --disable-gmp \
  --enable-hash-synchronization \
  --enable-fully-dynamic-string \
  --enable-libgomp \
  --enable-linker-build-id \
  --disable-vtable-verify \
  --with-pkgversion="SUSE Linux"

make %{?_smp_mflags} all || make all

%install
cd build

%make_install

rm -f %{buildroot}%{_mingw64_infodir}/dir

mv %{buildroot}%{_mingw64_libdir}/gcc/%{_mingw64_target}/lib/libgcc_s.a \
   %{buildroot}%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/

mv %{buildroot}%{_mingw64_libdir}/gcc/%{_mingw64_target}/*.dll \
   %{buildroot}%{_mingw64_bindir}

# Hack to work around a bug in GCC6
perl -pi -e 's#include_next\ \<stdlib\.h\>#include\ \<stdlib\.h\>#g' \
	%{buildroot}%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include/c++/cstdlib \
	%{buildroot}%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include/c++/bits/std_abs.h
perl -pi -e 's#include_next\ \<math\.h\>#include\ \<math\.h\>#g' \
	%{buildroot}%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include/c++/cmath

%files
%{_mingw64_bindir}/gcc*.exe
%{_mingw64_bindir}/gcov*.exe
%{_mingw64_bindir}/lto-dump*.exe
%exclude %{_mingw64_bindir}/%{_mingw64_target}-gcc*.exe
%dir %{_mingw64_libdir}/gcc/%{_mingw64_target}
%dir %{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/crtbegin.o
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/crtend.o
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/crtfastmath.o
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libcaf_single.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgcc.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgcc_eh.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgcc_s.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgcov.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libssp.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libssp.dll.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libssp_nonshared.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgomp.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgomp.dll.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgomp.spec
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libatomic.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libatomic.dll.a
%{_mingw64_infodir}/libgomp.info.gz
%dir %{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include
%dir %{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include-fixed
%dir %{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include/ssp
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include-fixed/README
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include/*.h
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include/ssp/*.h
%dir %{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/install-tools
%dir %{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/install-tools
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/install-tools/*
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/install-tools/*
%exclude %{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/install-tools/*.debug
%{_mingw64_mandir}/man1/gcc.1*
%{_mingw64_mandir}/man1/gcov.1*
%{_mingw64_mandir}/man1/gcov-dump.1*
%{_mingw64_mandir}/man1/gcov-tool.1*
%{_mingw64_mandir}/man1/lto-dump.1*
%{_mingw64_mandir}/man7/fsf-funding.7*
%{_mingw64_mandir}/man7/gfdl.7*
%{_mingw64_mandir}/man7/gpl.7*
%{_mingw64_infodir}/gcc*.info*
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/collect2.exe
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/g++-mapper-server.exe
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/liblto_plugin.dll
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/liblto_plugin.dll.a
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/lto1.exe
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/lto-wrapper.exe

%if "%{_mingw64_cpu}" == "x86_64"
%files -n mingw64-libgcc_s_seh1
%{_mingw64_bindir}/libgcc_s_seh-1.dll
%else

%files -n mingw64-libgcc_s_sjlj1
%{_mingw64_bindir}/libgcc_s_sjlj-1.dll
%endif

%files -n mingw64-libssp0
%{_mingw64_bindir}/libssp-0.dll

%files -n mingw64-libgomp1
%{_mingw64_bindir}/libgomp-1.dll

%files -n mingw64-libatomic1
%{_mingw64_bindir}/libatomic-1.dll

%files -n mingw64-cpp
%{_mingw64_bindir}/cpp.exe
%{_mingw64_mandir}/man1/cpp.1*
%dir %{_mingw64_libdir}/gcc/%{_mingw64_target}
%dir %{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/cc1.exe
%{_mingw64_infodir}/cpp*.info*

%files c++
%{_mingw64_bindir}/g++.exe
%{_mingw64_bindir}/c++.exe
%exclude %{_mingw64_bindir}/%{_mingw64_target}-g++.exe
%exclude %{_mingw64_bindir}/%{_mingw64_target}-c++.exe
%{_mingw64_mandir}/man1/g++.1*
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include/c++/
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libstdc++.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libstdc++.dll.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libstdc++exp.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libstdc++fs.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libsupc++.a
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/cc1plus.exe

%files -n mingw64-libstdc++6
%{_mingw64_bindir}/libstdc++-6.dll

%files -n mingw64-libstdc++-gdb-printer
%{_mingw64_bindir}/*-gdb.py
%{_mingw64_datadir}/gcc-%{version}/python

%files fortran
%{_mingw64_bindir}/gfortran.exe
%exclude %{_mingw64_bindir}/%{_mingw64_target}-gfortran.exe
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgfortran.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgfortran.dll.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libgfortran.spec
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libquadmath.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libquadmath.dll.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/ieee_arithmetic.mod
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/ieee_exceptions.mod
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/finclude/ieee_features.mod
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/f951.exe
%{_mingw64_mandir}/man1/gfortran.1*
%{_mingw64_infodir}/libquadmath.info.gz
%{_mingw64_infodir}/gfortran.info*

%files -n mingw64-libgfortran5
%{_mingw64_bindir}/libgfortran-5.dll

%files -n mingw64-libquadmath0
%{_mingw64_bindir}/libquadmath-0.dll

%files objc
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/include/objc
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libobjc.a
%{_mingw64_libdir}/gcc/%{_mingw64_target}/%{version}/libobjc.dll.a
%{_mingw64_libexecdir}/gcc/%{_mingw64_target}/%{version}/cc1obj*.exe

%files -n mingw64-libobjc4
%{_mingw64_bindir}/libobjc-4.dll

%changelog
