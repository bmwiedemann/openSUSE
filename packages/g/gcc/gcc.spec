#
# spec file
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


%define flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "build"
%define gccsuffix -build
%define gcc_version 13
%define gcc_suffix 13
%else
%define gccsuffix %{nil}
%define gcc_version 13
%define gcc_suffix 13
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
%define libgccjit_sover 0
URL:            http://gcc.gnu.org/
Version:        %{gcc_version}
Release:        0
Summary:        The system GNU C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Provides:       c_compiler
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
Requires:       gcc%{gcc_version}-32bit
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-32bit
The system GNU C Compiler.

%package -n gcc%{gccsuffix}-64bit
Summary:        The system GNU C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
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
Requires:       gcc%{gcc_version}-devel
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-devel
The system GNU C Compiler Plugin development files.

%package -n gcc%{gccsuffix}-locale
Summary:        The system GNU Compiler locale files
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-locale

%description -n gcc%{gccsuffix}-locale
The system GNU Compiler locale files.

%package -n gcc%{gccsuffix}-info
Summary:        The system GNU Compiler documentation
License:        GFDL-1.2-only
Group:          Development/Languages/C and C++
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
Requires:       gcc%{gcc_version}-c++
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-c++
The system GNU C++ Compiler.

%package -n gcc%{gccsuffix}-c++-32bit
Summary:        The system GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-c++-32bit
Requires:       gcc%{gccsuffix}-32bit = %{version}
Requires:       gcc%{gccsuffix}-c++ = %{version}

%description -n gcc%{gccsuffix}-c++-32bit
The system GNU C++ Compiler 32 bit support.

%package -n gcc%{gccsuffix}-c++-64bit
Summary:        The system GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-c++-64bit
Requires:       gcc%{gccsuffix}-64bit = %{version}
Requires:       gcc%{gccsuffix}-c++ = %{version}

%description -n gcc%{gccsuffix}-c++-64bit
The system GNU C++ Compiler 64 bit support.

%package -n libstdc++%{gccsuffix}-devel
Summary:        The system GNU C++ development files
License:        GPL-3.0-only WITH GCC-exception-3.1
Group:          System/Libraries
Requires:       libstdc++6-devel-gcc%{gcc_version}

%description -n libstdc++%{gccsuffix}-devel
The system GNU C++ development files.

%package -n libstdc++%{gccsuffix}-devel-32bit
Summary:        The system GNU C++ 32bit development files
License:        GPL-3.0-only WITH GCC-exception-3.1
Group:          System/Libraries
Requires:       libstdc++%{gccsuffix}-devel
Requires:       libstdc++6-devel-gcc%{gcc_version}-32bit

%description -n libstdc++%{gccsuffix}-devel-32bit
The system GNU C++ 32bit development files.

%package -n libstdc++%{gccsuffix}-devel-64bit
Summary:        The system GNU C++ 64bit development files
License:        GPL-3.0-only WITH GCC-exception-3.1
Group:          System/Libraries
Requires:       libstdc++%{gccsuffix}-devel
Requires:       libstdc++6-devel-gcc%{gcc_version}-64bit

%description -n libstdc++%{gccsuffix}-devel-64bit
The system GNU C++ 64bit development files.

%package -n gcc%{gccsuffix}-fortran
Summary:        The system GNU Fortran Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
Requires:       gcc%{gcc_version}-fortran
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-fortran
The system GNU Fortran Compiler.

%package -n gcc%{gccsuffix}-fortran-32bit
Summary:        The system GNU Fortran Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
Requires:       gcc%{gcc_version}-fortran-32bit
Requires:       gcc%{gccsuffix}-fortran = %{version}

%description -n gcc%{gccsuffix}-fortran-32bit
The system GNU Fortran Compiler 32 bit support.

%package -n gcc%{gccsuffix}-fortran-64bit
Summary:        The system GNU Fortran Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
Requires:       gcc%{gcc_version}-fortran-64bit
Requires:       gcc%{gccsuffix}-fortran = %{version}

%description -n gcc%{gccsuffix}-fortran-64bit
The system GNU Fortran Compiler 64 bit support.

%package -n gcc%{gccsuffix}-objc
Summary:        The system GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
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
Requires:       gcc%{gcc_version}-objc-32bit
Requires:       gcc%{gccsuffix}-objc = %{version}

%description -n gcc%{gccsuffix}-objc-32bit
The system GNU Objective C Compiler 32 bit support.

%package -n gcc%{gccsuffix}-objc-64bit
Summary:        The system GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc%{gcc_version}-objc-64bit
Requires:       gcc%{gccsuffix}-objc = %{version}

%description -n gcc%{gccsuffix}-objc-64bit
The system GNU Objective C Compiler 64 bit support.

%package -n gcc%{gccsuffix}-obj-c++
Summary:        The system GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc%{gcc_version}-obj-c++
Requires:       gcc%{gccsuffix}-objc = %{version}

%description -n gcc%{gccsuffix}-obj-c++
The system GNU Objective C++ Compiler.

%package -n gcc%{gccsuffix}-PIE
Summary:        A default configuration to build all binaries in PIE mode
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
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
Requires:       gcc%{gcc_version}-ada
Requires:       gcc%{gccsuffix} = %{version}

%description -n gcc%{gccsuffix}-ada
The system GNU Ada Compiler.

%package -n gcc%{gccsuffix}-ada-32bit
Summary:        The system GNU Ada Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-ada-32bit
Requires:       gcc%{gccsuffix}-ada = %{version}

%description -n gcc%{gccsuffix}-ada-32bit
The system GNU Ada Compiler 32 bit support.

%package -n gcc%{gccsuffix}-ada-64bit
Summary:        The system GNU Ada Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-ada-64bit
Requires:       gcc%{gccsuffix}-ada = %{version}

%description -n gcc%{gccsuffix}-ada-64bit
The system GNU Ada Compiler 64 bit support.

%package -n gcc%{gccsuffix}-go
Summary:        The system GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-go
Requires:       gcc%{gccsuffix} = %{version}
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description -n gcc%{gccsuffix}-go
The system GNU Go Compiler.

%package -n gcc%{gccsuffix}-go-32bit
Summary:        The system GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-go-32bit
Requires:       gcc%{gccsuffix}-go = %{version}

%description -n gcc%{gccsuffix}-go-32bit
The system GNU Go Compiler 32bit support.

%package -n gcc%{gccsuffix}-go-64bit
Summary:        The system GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-go-64bit
Requires:       gcc%{gccsuffix}-go = %{version}

%description -n gcc%{gccsuffix}-go-64bit
The system GNU Go Compiler 64bit support.

%package -n gcc%{gccsuffix}-d
Summary:        The system GNU D Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-d
Requires:       gcc%{gccsuffix} = %{version}
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description -n gcc%{gccsuffix}-d
The system GNU D Compiler.

%package -n gcc%{gccsuffix}-d-32bit
Summary:        The system GNU D Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-d-32bit
Requires:       gcc%{gccsuffix}-d = %{version}

%description -n gcc%{gccsuffix}-d-32bit
The system GNU D Compiler 32bit support.

%package -n gcc%{gccsuffix}-d-64bit
Summary:        The system GNU D Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc%{gcc_version}-d-64bit
Requires:       gcc%{gccsuffix}-d = %{version}

%description -n gcc%{gccsuffix}-d-64bit
The system GNU D Compiler 64bit support.

%package -n libgccjit%{gccsuffix}-devel
Summary:        Support for embedding GCC inside programs and libraries
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       libgccjit%{libgccjit_sover}-devel-gcc%{gcc_version}

%description -n libgccjit%{gccsuffix}-devel
Package contains header files and documentation for GCC JIT front-end.

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
	gcc-ar gcc-nm gcc-ranlib \
    ; do
  ln -sf $program-%{gcc_suffix} $RPM_BUILD_ROOT%{_prefix}/bin/$program
done
# For go and gofmt use alternatives since they are shared with golang
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/go %{buildroot}%{_bindir}/go
ln -sf %{_sysconfdir}/alternatives/gofmt %{buildroot}%{_bindir}/gofmt
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

%post -n gcc%{gccsuffix}-go
# we don't want a BuildRequires on gccN-go but otherwise the install
# step of the build fails, so simply skip the script when gccN-go isn't there
if [ -f %{_bindir}/go-%{gcc_suffix} ] ; then
update-alternatives \
  --install %{_bindir}/go go %{_bindir}/go-%{gcc_suffix} 100 \
  --slave %{_bindir}/gofmt gofmt %{_bindir}/gofmt-%{gcc_suffix}
fi

%postun -n gcc%{gccsuffix}-go
if [ $1 -eq 0 ] ; then
  update-alternatives --remove go %{_bindir}/go-%{gcc_suffix}
fi

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
%if 0%{!?sle_version:1}
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
%{_bindir}/go
%{_bindir}/gofmt
%ghost %{_sysconfdir}/alternatives/go
%ghost %{_sysconfdir}/alternatives/gofmt
%doc %{_mandir}/man1/gccgo.1.gz

%if %{build_d}
%files -n gcc%{gccsuffix}-d
%defattr(-,root,root)
%{_bindir}/gdc
%doc %{_mandir}/man1/gdc.1.gz
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

%endif

%files -n libgccjit%{gccsuffix}-devel
%defattr(-,root,root)
# empty - only for the dependency

%changelog
