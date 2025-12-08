#
# spec file for package gcc
#
# Copyright (c) 2025 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "build"
%define gccsuffix -build
%define gcc_version 13
%define gcc_suffix 13
%else
%define gccsuffix %{nil}
%define gcc_version 15
%define gcc_suffix 15
%endif

Name:           gcc%{gccsuffix}
%define separate_bi32 0
%define separate_bi64 0
%if 0%{!?disable_32bit:1}
%ifarch ppc sparcv9
%define separate_bi64 1
%endif
%ifarch x86_64 s390x ppc64 sparc64
%define separate_bi32 1
%endif
%endif
# Ada currently fails to build on a few platforms, enable it only
# on those that work
# Note that AdaCore only supports %%ix86, x86_64 and ia64
%ifarch %ix86 x86_64 ppc ppc64 ppc64le s390 s390x ia64 aarch64 riscv64
%define build_ada 1
%else
# alpha hppa arm
%define build_ada 0
%endif
%ifarch x86_64 %ix86 %arm aarch64 riscv64 s390x
%define build_d 1
%else
%define build_d 0
%endif
%define build_m2 1
%ifarch x86_64 aarch64 ppc64le riscv64
%if %{gcc_version} >= 15 && %{suse_version} >= 1699
%define build_cobol 1
%else
%define build_cobol 0
%endif
%else
%define build_cobol 0
%endif
%define quadmath_arch %ix86 x86_64 ia64 ppc64le
%define libgccjit_sover 0

URL:            http://gcc.gnu.org/
Version:        %{gcc_version}
Release:        0
Summary:        The system GNU C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Provides:       c_compiler
%if "%{gccsuffix}" != ""
Provides:       gcc = %{version}
Conflicts:      gcc
%endif
Requires:       cpp%{gccsuffix}
Requires:       gcc%{gcc_version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc%{gcc_version}
BuildRequires:  gcc%{gcc_version}-c++
BuildRequires:  gcc%{gcc_version}-fortran
BuildRequires:  gcc%{gcc_version}-go
%if %{build_ada}
BuildRequires:  gcc%{gcc_version}-ada
%endif
%if %{build_d}
BuildRequires:  gcc%{gcc_version}-d
%endif
%if %{build_m2}
BuildRequires:  gcc%{gcc_version}-m2
%endif
%if %{build_cobol}
BuildRequires:  gcc%{gcc_version}-cobol
%endif
Source:         cpp
%if "%{gccsuffix}" != "" && 0%{?is_opensuse}
ExclusiveArch:  do-not-build
%endif

%description -n gcc%{gccsuffix}
The system GNU C Compiler.

%package -n gcc%{gccsuffix}-32bit
Summary:        The system GNU C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-32bit = %{version}
Conflicts:      gcc-32bit
%endif
Requires:       gcc%{gcc_version}-32bit
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-32bit
The system GNU C Compiler.

%package -n gcc%{gccsuffix}-64bit
Summary:        The system GNU C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-64bit = %{version}
Conflicts:      gcc-64bit
%endif
Requires:       gcc%{gcc_version}-64bit
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-64bit
The system GNU C Compiler.

%package -n cpp%{gccsuffix}
Summary:        The system GNU Preprocessor
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       cpp%{gcc_version}
# Only one of the symlink packages can be installed at the same time
Provides:       cpp = %{version}-%{release}
Conflicts:      cpp

%description -n cpp%{gccsuffix}
The system GNU Preprocessor.

%package -n gcc%{gccsuffix}-devel
Summary:        The system GNU C Compiler Plugin development files
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-devel = %{version}
Conflicts:      gcc-devel
%endif
Requires:       gcc%{gcc_version}-devel
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-devel
The system GNU C Compiler Plugin development files.

%package -n gcc%{gccsuffix}-locale
Summary:        The system GNU Compiler locale files
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-locale = %{version}
Conflicts:      gcc-locale
%endif
Requires:       gcc%{gcc_version}-locale

%description -n gcc%{gccsuffix}-locale
The system GNU Compiler locale files.

%package -n gcc%{gccsuffix}-info
Summary:        The system GNU Compiler documentation
License:        GFDL-1.2-only
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-info = %{version}
Conflicts:      gcc-info
%endif
PreReq:         %{install_info_prereq}
PreReq:         gcc%{gcc_version}-info

%description -n gcc%{gccsuffix}-info
The system GNU Compiler documentation.














# install / update the entries
%post -n gcc%{gccsuffix}-info
%install_info --info-dir=%{_infodir} --name=cpp --description='The GNU C preprocessor.' %{_infodir}/cpp.info.gz
%install_info --info-dir=%{_infodir} --name=gcc --description='The GNU Compiler Collection.' %{_infodir}/gcc.info.gz
%install_info --info-dir=%{_infodir} --name=g++ --description='The GNU C++ compiler.' %{_infodir}/gcc.info.gz
%install_info --info-dir=%{_infodir} --name=gfortran --description='The GNU Fortran compiler.' %{_infodir}/gfortran.info.gz

# if we uninstall, clean the entries
%preun -n gcc%{gccsuffix}-info
if [ "$1" -eq "0" ] ; then
  %install_info --delete --info-dir=%{_infodir} --name=cpp %{_infodir}/cpp.info.gz
  %install_info --delete --info-dir=%{_infodir} --name=gcc %{_infodir}/gcc.info.gz
  %install_info --delete --info-dir=%{_infodir} --name=g++ %{_infodir}/gcc.info.gz
  %install_info --delete --info-dir=%{_infodir} --name=gfortran %{_infodir}/gfortran.info.gz
fi

%package -n gcc%{gccsuffix}-c++
Summary:        The system GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Provides:       c++_compiler
%if "%{gccsuffix}" != ""
Provides:       gcc-c++ = %{version}
Conflicts:      gcc-c++
%endif
Requires:       gcc%{gcc_version}-c++
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-c++
The system GNU C++ Compiler.

%package -n gcc%{gccsuffix}-c++-32bit
Summary:        The system GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-c++-32bit = %{version}
Conflicts:      gcc-c++-32bit
%endif
Requires:       gcc%{gcc_version}-c++-32bit
Requires:       gcc%{gccsuffix}-32bit = %{version}
Requires:       gcc%{gccsuffix}-c++ = %{version}

%description -n gcc%{gccsuffix}-c++-32bit
The system GNU C++ Compiler 32 bit support.

%package -n gcc%{gccsuffix}-c++-64bit
Summary:        The system GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-c++-64bit = %{version}
Conflicts:      gcc-c++-64bit
%endif
Requires:       gcc%{gcc_version}-c++-64bit
Requires:       gcc%{gccsuffix}-64bit = %{version}
Requires:       gcc%{gccsuffix}-c++ = %{version}

%description -n gcc%{gccsuffix}-c++-64bit
The system GNU C++ Compiler 64 bit support.

%package -n libstdc++%{gccsuffix}-devel
Summary:        The system GNU C++ development files
License:        GPL-3.0-only WITH GCC-exception-3.1
Group:          System/Libraries
%if "%{gccsuffix}" != ""
Provides:       libstdc++-devel = %{version}
Conflicts:      libstdc++-devel
%endif
Requires:       libstdc++6-devel-gcc%{gcc_version}

%description -n libstdc++%{gccsuffix}-devel
The system GNU C++ development files.

%package -n libstdc++%{gccsuffix}-devel-32bit
Summary:        The system GNU C++ 32bit development files
License:        GPL-3.0-only WITH GCC-exception-3.1
Group:          System/Libraries
%if "%{gccsuffix}" != ""
Provides:       libstdc++-devel-32bit = %{version}
Conflicts:      libstdc++-devel-32bit
%endif
Requires:       libstdc++%{gccsuffix}-devel
Requires:       libstdc++6-devel-gcc%{gcc_version}-32bit

%description -n libstdc++%{gccsuffix}-devel-32bit
The system GNU C++ 32bit development files.

%package -n libstdc++%{gccsuffix}-devel-64bit
Summary:        The system GNU C++ 64bit development files
License:        GPL-3.0-only WITH GCC-exception-3.1
Group:          System/Libraries
%if "%{gccsuffix}" != ""
Provides:       libstdc++-devel-64bit = %{version}
Conflicts:      libstdc++-devel-64bit
%endif
Requires:       libstdc++%{gccsuffix}-devel
Requires:       libstdc++6-devel-gcc%{gcc_version}-64bit

%description -n libstdc++%{gccsuffix}-devel-64bit
The system GNU C++ 64bit development files.

%package -n gcc%{gccsuffix}-fortran
Summary:        The system GNU Fortran Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
%if "%{gccsuffix}" != ""
Provides:       gcc-fortran = %{version}
Conflicts:      gcc-fortran
%endif
Requires:       gcc%{gcc_version}-fortran
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-fortran
The system GNU Fortran Compiler.

%package -n gcc%{gccsuffix}-fortran-32bit
Summary:        The system GNU Fortran Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
%if "%{gccsuffix}" != ""
Provides:       gcc-fortran-32bit = %{version}
Conflicts:      gcc-fortran-32bit
%endif
Requires:       gcc%{gcc_version}-fortran-32bit
Requires:       gcc%{gccsuffix}-fortran = %{version}

%description -n gcc%{gccsuffix}-fortran-32bit
The system GNU Fortran Compiler 32 bit support.

%package -n gcc%{gccsuffix}-fortran-64bit
Summary:        The system GNU Fortran Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
%if "%{gccsuffix}" != ""
Provides:       gcc-fortran-64bit = %{version}
Conflicts:      gcc-fortran-64bit
%endif
Requires:       gcc%{gcc_version}-fortran-64bit
Requires:       gcc%{gccsuffix}-fortran = %{version}

%description -n gcc%{gccsuffix}-fortran-64bit
The system GNU Fortran Compiler 64 bit support.

%package -n gcc%{gccsuffix}-objc
Summary:        The system GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
%if "%{gccsuffix}" != ""
Provides:       gcc-objc = %{version}
Conflicts:      gcc-objc
%endif
Requires:       gcc%{gcc_version}-objc
Requires:       gcc%{gccsuffix} = %{version}
%ifarch ppc64
Obsoletes:      gcc%{gccsuffix}-objc-64bit
%endif

%description -n gcc%{gccsuffix}-objc
The system GNU Objective C Compiler.

%package -n gcc%{gccsuffix}-objc-32bit
Summary:        The system GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
%if "%{gccsuffix}" != ""
Provides:       gcc-objc-32bit = %{version}
Conflicts:      gcc-objc-32bit
%endif
Requires:       gcc%{gcc_version}-objc-32bit
Requires:       gcc%{gccsuffix}-objc = %{version}

%description -n gcc%{gccsuffix}-objc-32bit
The system GNU Objective C Compiler 32 bit support.

%package -n gcc%{gccsuffix}-objc-64bit
Summary:        The system GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
%if "%{gccsuffix}" != ""
Provides:       gcc-objc-64bit = %{version}
Conflicts:      gcc-objc-64bit
%endif
Requires:       gcc%{gcc_version}-objc-64bit
Requires:       gcc%{gccsuffix}-objc = %{version}

%description -n gcc%{gccsuffix}-objc-64bit
The system GNU Objective C Compiler 64 bit support.

%package -n gcc%{gccsuffix}-obj-c++
Summary:        The system GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
%if "%{gccsuffix}" != ""
Provides:       gcc-objc-c++ = %{version}
Conflicts:      gcc-objc-c++
%endif
Requires:       gcc%{gcc_version}-obj-c++
Requires:       gcc%{gccsuffix}-objc = %{version}

%description -n gcc%{gccsuffix}-obj-c++
The system GNU Objective C++ Compiler.

%package -n gcc%{gccsuffix}-PIE
Summary:        A default configuration to build all binaries in PIE mode
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
%if "%{gccsuffix}" != ""
Provides:       gcc-PIE = %{version}
Conflicts:      gcc-PIE
%endif
Requires:       gcc%{gcc_version}-PIE

%description -n gcc%{gccsuffix}-PIE
This package contains a configuration file (spec) that changes the
compilers default setting to build all ELF binaries in the Position
Independend Executable (PIE) variant. This enables better address
space randomization (ASLR).

%package -n gcc%{gccsuffix}-ada
Summary:        The system GNU Ada Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-ada = %{version}
Conflicts:      gcc-ada
%endif
Requires:       gcc%{gcc_version}-ada
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-ada
The system GNU Ada Compiler.

%package -n gcc%{gccsuffix}-ada-32bit
Summary:        The system GNU Ada Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-ada-32bit = %{version}
Conflicts:      gcc-ada-32bit
%endif
Requires:       gcc%{gcc_version}-ada-32bit
Requires:       gcc%{gccsuffix}-ada = %{version}

%description -n gcc%{gccsuffix}-ada-32bit
The system GNU Ada Compiler 32 bit support.

%package -n gcc%{gccsuffix}-ada-64bit
Summary:        The system GNU Ada Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-ada-64bit = %{version}
Conflicts:      gcc-ada-64bit
%endif
Requires:       gcc%{gcc_version}-ada-64bit
Requires:       gcc%{gccsuffix}-ada = %{version}

%description -n gcc%{gccsuffix}-ada-64bit
The system GNU Ada Compiler 64 bit support.

%package -n gcc%{gccsuffix}-go
Summary:        The system GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-go = %{version}
Conflicts:      gcc-go
%endif
Requires:       gcc%{gcc_version}-go
Requires:       gcc%{gccsuffix} = %{version}
Requires(post): update-alternatives

%description -n gcc%{gccsuffix}-go
The system GNU Go Compiler.

%package -n gcc%{gccsuffix}-go-32bit
Summary:        The system GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-go-32bit = %{version}
Conflicts:      gcc-go-32bit
%endif
Requires:       gcc%{gcc_version}-go-32bit
Requires:       gcc%{gccsuffix}-go = %{version}

%description -n gcc%{gccsuffix}-go-32bit
The system GNU Go Compiler 32bit support.

%package -n gcc%{gccsuffix}-go-64bit
Summary:        The system GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-go-64bit = %{version}
Conflicts:      gcc-go-64bit
%endif
Requires:       gcc%{gcc_version}-go-64bit
Requires:       gcc%{gccsuffix}-go = %{version}

%description -n gcc%{gccsuffix}-go-64bit
The system GNU Go Compiler 64bit support.

%package -n gcc%{gccsuffix}-d
Summary:        The system GNU D Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-d = %{version}
Conflicts:      gcc-d
%endif
Requires:       gcc%{gcc_version}-d
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-d
The system GNU D Compiler.

%package -n gcc%{gccsuffix}-d-32bit
Summary:        The system GNU D Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-d-32bit = %{version}
Conflicts:      gcc-d-32bit
%endif
Requires:       gcc%{gcc_version}-d-32bit
Requires:       gcc%{gccsuffix}-d = %{version}

%description -n gcc%{gccsuffix}-d-32bit
The system GNU D Compiler 32bit support.

%package -n gcc%{gccsuffix}-d-64bit
Summary:        The system GNU D Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-d-64bit = %{version}
Conflicts:      gcc-d-64bit
%endif
Requires:       gcc%{gcc_version}-d-64bit
Requires:       gcc%{gccsuffix}-d = %{version}

%description -n gcc%{gccsuffix}-d-64bit
The system GNU D Compiler 64bit support.

%package -n libgccjit%{gccsuffix}-devel
Summary:        Support for embedding GCC inside programs and libraries
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       libgccjit-devel = %{version}
Conflicts:      libgccjit-devel
%endif
Requires:       libgccjit%{libgccjit_sover}-devel-gcc%{gcc_version}

%description -n libgccjit%{gccsuffix}-devel
Package contains header files and documentation for GCC JIT front-end.

%package -n libquadmath%{gccsuffix}-devel
Summary:        Development files for the quadprecision math library
License:        LGPL-2.1-only
Group:          Development/Languages/Fortran
%if "%{gccsuffix}" != ""
Provides:       libquadmath-devel = %{version}
Conflicts:      libquadmath-devel
%endif
Requires:       libquadmath0-devel-gcc%{gcc_version}

%description -n libquadmath%{gccsuffix}-devel
Development files for the quadprecision math library.

%package -n gcc%{gccsuffix}-m2
Summary:        The system GNU Modula-2 Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-m2 = %{version}
Conflicts:      gcc-m2
%endif
Requires:       gcc%{gcc_version}-m2
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-m2
The system GNU Modula-2 Compiler.

%package -n gcc%{gccsuffix}-m2-32bit
Summary:        The system GNU Modula-2 Compiler 32bit support
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-m2-32bit = %{version}
Conflicts:      gcc-m2-32bit
%endif
Requires:       gcc%{gcc_version}-m2-32bit
Requires:       gcc%{gccsuffix}-m2 = %{version}

%description -n gcc%{gccsuffix}-m2-32bit
The system GNU Modula-2 Compiler 32bit support

%package -n gcc%{gccsuffix}-m2-64bit
Summary:        The system GNU Modula-2 Compiler 64bit support
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-m2-64bit = %{version}
Conflicts:      gcc-m2-64bit
%endif
Requires:       gcc%{gcc_version}-m2-64bit
Requires:       gcc%{gccsuffix}-m2 = %{version}

%description -n gcc%{gccsuffix}-m2-64bit
The system GNU Modula-2 Compiler 64bit support

%package -n gcc%{gccsuffix}-cobol
Summary:        The system GNU Cobol Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
%if "%{gccsuffix}" != ""
Provides:       gcc-cobol = %{version}
Conflicts:      gcc-cobol
%endif
Requires:       gcc%{gcc_version}-cobol
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-cobol
The system GNU Cobol Compiler.

%prep

%install
mkdir -p $RPM_BUILD_ROOT/lib
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_infodir}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/doc/packages/gcc-objc/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/doc/packages/gcc-obj-c++/
# Link all the binaries
for program in \
        gcc gcov gcov-dump gcov-tool lto-dump \
        g++ \
        cpp \
        gfortran \
	gccgo \
%if %{build_ada}
	gnat gnatbind gnatchop gnatclean gnatkr \
	gnatlink gnatls gnatmake gnatname gnatprep \
%endif
%if %{build_d}
	gdc \
%endif
%if %{build_m2}
	gm2 \
%endif
%if %{build_cobol}
	gcobol gcobc \
%endif
	gcc-ar gcc-nm gcc-ranlib \
    ; do
  ln -sf $program-%{gcc_suffix} $RPM_BUILD_ROOT%{_prefix}/bin/$program
done
# Do not add a gofmt link from gofmt-%{gcc_suffix} since that conflicts with
# the golang libalternatives version of this.  Do not use gccgofmt either,
# that's nonstandard and not expected by anyone.
# Link section 1 manpages
for man1 in \
        gcc gcov gcov-dump gcov-tool lto-dump \
        g++ \
        cpp \
        gfortran \
	gccgo \
%if %{build_d}
	gdc \
%endif
%if %{build_m2}
	gm2 \
%endif
%if %{build_cobol}
	gcobol \
%endif
    ; do
  ln -sf $man1-%{gcc_suffix}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/$man1.1.gz
done
# Link info pages
for info in cpp gcc gfortran ; do
  ln -sf $info-%{gcc_suffix}.info.gz $RPM_BUILD_ROOT%{_infodir}/$info.info.gz
done
# Provide the traditional /lib/cpp (as /usr/lib/cpp on usrmerged systems)
# that only handles C
%if 0%{?suse_version} < 1550
cp $RPM_SOURCE_DIR/cpp $RPM_BUILD_ROOT/lib/
chmod 755 $RPM_BUILD_ROOT/lib/cpp
%else
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib
cp $RPM_SOURCE_DIR/cpp $RPM_BUILD_ROOT%{_prefix}/lib/
chmod 755 $RPM_BUILD_ROOT%{_prefix}/lib/cpp
%endif
# Provide extra symlinks
ln -sf g++-%{gcc_suffix} $RPM_BUILD_ROOT%{_prefix}/bin/c++
ln -sf gcc-%{gcc_suffix} $RPM_BUILD_ROOT%{_prefix}/bin/cc
ln -sf g++-%{gcc_suffix}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/c++.1.gz
ln -sf gcc-%{gcc_suffix}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/cc.1.gz
# Install the LTO linker plugin so it is auto-loaded by BFD
mkdir -p $RPM_BUILD_ROOT%{_libdir}/bfd-plugins
ln -s `gcc-%{gcc_suffix} -print-file-name=liblto_plugin.so` $RPM_BUILD_ROOT%{_libdir}/bfd-plugins/liblto_plugin.so

# We no longer register go/gofmt alternatives for gcc-go, but remove
# any existing one on upgrade
%post -n gcc%{gccsuffix}-go
update-alternatives --remove go %{_bindir}/go-%{gcc_suffix}

%files -n gcc%{gccsuffix}
%defattr(-,root,root)
%{_prefix}/bin/gcc
%{_prefix}/bin/cc
%{_prefix}/bin/gcov
%{_prefix}/bin/gcov-dump
%{_prefix}/bin/gcov-tool
%{_prefix}/bin/lto-dump
%{_prefix}/bin/gcc-ar
%{_prefix}/bin/gcc-nm
%{_prefix}/bin/gcc-ranlib
%dir %{_libdir}/bfd-plugins
%{_libdir}/bfd-plugins/liblto_plugin.so
%doc %{_mandir}/man1/gcc.1.gz
%doc %{_mandir}/man1/cc.1.gz
%doc %{_mandir}/man1/gcov.1.gz
%doc %{_mandir}/man1/gcov-dump.1.gz
%doc %{_mandir}/man1/gcov-tool.1.gz
%doc %{_mandir}/man1/lto-dump.1.gz

%files -n cpp%{gccsuffix}
%defattr(-,root,root)
%if 0%{?suse_version} < 1550
/lib/cpp
%else
%{_prefix}/lib/cpp
%endif
%{_prefix}/bin/cpp
%doc %{_mandir}/man1/cpp.1.gz

# Plugins are only enabled for Tumbleweed
%if 0%{?is_opensuse}
%files -n gcc%{gccsuffix}-devel
%defattr(-,root,root)
# empty - only for the dependency
%endif

%files -n gcc%{gccsuffix}-c++
%defattr(-,root,root)
%{_prefix}/bin/g++
%{_prefix}/bin/c++
%doc %{_mandir}/man1/g++.1.gz
%doc %{_mandir}/man1/c++.1.gz

%files -n gcc%{gccsuffix}-fortran
%defattr(-,root,root)
%{_prefix}/bin/gfortran
%doc %{_mandir}/man1/gfortran.1.gz

%files -n gcc%{gccsuffix}-objc
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-obj-c++
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-PIE
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-locale
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-info
%defattr(-,root,root)
%{_infodir}/cpp.info.gz
%{_infodir}/gcc.info.gz
%{_infodir}/gfortran.info.gz

%if %{build_ada}
%files -n gcc%{gccsuffix}-ada
%defattr(-,root,root)
%{_prefix}/bin/gnat
%{_prefix}/bin/gnatbind
%{_prefix}/bin/gnatchop
%{_prefix}/bin/gnatclean
%{_prefix}/bin/gnatkr
%{_prefix}/bin/gnatlink
%{_prefix}/bin/gnatls
%{_prefix}/bin/gnatmake
%{_prefix}/bin/gnatname
%{_prefix}/bin/gnatprep
%endif

%files -n libstdc++%{gccsuffix}-devel
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-go
%defattr(-,root,root)
%{_bindir}/gccgo
%doc %{_mandir}/man1/gccgo.1.gz

%if %{build_d}
%files -n gcc%{gccsuffix}-d
%defattr(-,root,root)
%{_bindir}/gdc
%doc %{_mandir}/man1/gdc.1.gz
%endif

%if %{build_m2}
%files -n gcc%{gccsuffix}-m2
%defattr(-,root,root)
%{_bindir}/gm2
%doc %{_mandir}/man1/gm2.1.gz
%endif

%if %{build_cobol}
%files -n gcc%{gccsuffix}-cobol
%defattr(-,root,root)
%{_bindir}/gcobol
%{_bindir}/gcobc
%doc %{_mandir}/man1/gcobol.1.gz
%endif

%if %{separate_bi32}

%files -n gcc%{gccsuffix}-32bit
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-c++-32bit
%defattr(-,root,root)
# empty - only for the dependency

%files -n libstdc++%{gccsuffix}-devel-32bit
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-fortran-32bit
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-objc-32bit
%defattr(-,root,root)
# empty - only for the dependency

%if %{build_ada}
%files -n gcc%{gccsuffix}-ada-32bit
%defattr(-,root,root)
# empty - only for the dependency
%endif

%files -n gcc%{gccsuffix}-go-32bit
%defattr(-,root,root)
# empty - only for the dependency

%if %{build_d}
%files -n gcc%{gccsuffix}-d-32bit
%defattr(-,root,root)
# empty - only for the dependency
%endif

%if %{build_m2}
%files -n gcc%{gccsuffix}-m2-32bit
%defattr(-,root,root)
# empty - only for the dependency
%endif

%endif

%if %{separate_bi64}

%files -n gcc%{gccsuffix}-64bit
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-c++-64bit
%defattr(-,root,root)
# empty - only for the dependency

%files -n libstdc++%{gccsuffix}-devel-64bit
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-fortran-64bit
%defattr(-,root,root)
# empty - only for the dependency

%files -n gcc%{gccsuffix}-objc-64bit
%defattr(-,root,root)
# empty - only for the dependency

%if %{build_ada}
%files -n gcc%{gccsuffix}-ada-64bit
%defattr(-,root,root)
# empty - only for the dependency
%endif

%files -n gcc%{gccsuffix}-go-64bit
%defattr(-,root,root)
# empty - only for the dependency

%if %{build_d}
%files -n gcc%{gccsuffix}-d-64bit
%defattr(-,root,root)
# empty - only for the dependency
%endif

%if %{build_m2}
%files -n gcc%{gccsuffix}-m2-64bit
%defattr(-,root,root)
# empty - only for the dependency
%endif

%endif

%files -n libgccjit%{gccsuffix}-devel
%defattr(-,root,root)
# empty - only for the dependency

%if %{gcc_version} >= 14
%ifarch %quadmath_arch
%files -n libquadmath%{gccsuffix}-devel
%defattr(-,root,root)
# empty - only for the dependency
%endif
%endif

%changelog
