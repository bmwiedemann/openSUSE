#
# spec file for package ldc
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


%define so_ver        110
%define lname_jit     libldc-jit
%define lname_runtime libdruntime-%{name}
%define lname_phobos  libphobos2-%{name}
%define _bashcompletionsdir %{_datadir}/bash-completion/completions

%define HOST_ARCH %(echo %{_host_cpu} | sed -e "s/i.86/i586/;s/ppc/powerpc/;s/sparc64.*/sparc64/;s/sparcv.*/sparc/;")
%ifarch ppc
%define LDCDIST powerpc64-suse-linux
%else
%ifarch %sparc
%define LDCDIST sparc64-suse-linux
%else
%ifarch %arm
%define LDCDIST %{HOST_ARCH}-suse-linux-gnueabi
%else
%define LDCDIST %{HOST_ARCH}-suse-linux
%endif
%endif
%endif

%define ldcincludedir %{_libdir}/ldc/%{LDCDIST}/include/d

# With bootstrap enabled (the default), gdc is used (through the gdmd wrapper)
# to build ldc (and shared runtime), then the built ldc is used to build ldc
# itself again. The final ldc with shared runtime is then installed.
# With bootstrap disabled, ldc from the ldc package is used directly to build
# the new ldc. Note that the resulting ldc is linked against the old ldc's
# runtime, which might not be compatible with the newly built one!
%bcond_without ldc_bootstrap

%bcond_with ldc_tests

# Dynamic compiling is not supported with LLVM >= 12
# https://github.com/ldc-developers/ldc/issues/3747
%global jit_support 0

# LLVM LTO is too much for 32bit ARM
%ifarch %{arm}
%define _lto_cflags %nil
%endif

Name:           ldc
Version:        1.40.0
Release:        0
Summary:        The LLVM D Compiler
License:        Artistic-1.0 AND BSD-3-Clause
Group:          Development/Languages/Other
URL:            https://wiki.dlang.org/LDC
Source0:        https://github.com/ldc-developers/ldc/releases/download/v%{version}/ldc-%{version}-src.tar.gz
Source1:        %{name}-rpmlintrc
Patch0:         ldc-1.9.0-fix_arm_build.patch
BuildRequires:  cmake
BuildRequires:  help2man
BuildRequires:  libconfig++-devel
BuildRequires:  libcurl-devel
BuildRequires:  libstdc++-devel
%if 0%{?suse_version} > 1550 || ( 0%{?is_opensuse} && 0%{?sle_version} > 150400 )
BuildRequires:  llvm-clang >= 15.0
BuildRequires:  llvm-devel >= 15.0
%else
BuildRequires:  llvm-clang >= 15.0
BuildRequires:  llvm-devel >= 15.0
%endif
BuildRequires:  ncurses-devel
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bash-completion)
# Should be installed, at least runtime
Recommends:     ldc-phobos-devel = %{version}
Recommends:     ldc-jit-devel = %{version}
Recommends:     ldc-runtime-devel = %{version}
%if %{with ldc_bootstrap}
# Use GDC 10, available on 15.3+
%if 0%{?suse_version} < 1550
%global gdc_version 10
%global gdc_suffix -%{gdc_version}
%endif
# Clang uses the newest gcc to find headers and libs
BuildRequires:  gcc%{?gdc_version}-c++
BuildRequires:  gdmd%{?gdc_suffix}
%else
BuildRequires:  ldc
BuildRequires:  ldc-phobos-devel
BuildRequires:  ldc-runtime-devel
%endif
%if %{with ldc_tests}
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  python
BuildRequires:  timezone
BuildRequires:  unzip
%endif
# ppc64 is disabled due to boo#1113531
ExclusiveArch:  %{ix86} x86_64 %arm aarch64 riscv64

%description
LDC is an LLVM based compiler for the D programming language. It uses the
frontend of the reference compiler (DMD), thereby supporting the same language
features, but profits from LLVM's superior optimizing and code generation
capabilities.

%package -n %{lname_runtime}%{so_ver}
Summary:        Minimal D runtime library
Group:          System/Libraries

%description -n %{lname_runtime}%{so_ver}
The minimal runtime library required to support the D programming language.

%package runtime-devel
Summary:        Development files for the D runtime library
Group:          Development/Libraries/Other
Requires:       %{lname_runtime}%{so_ver} = %{version}
# library version 99 wrongly packaged an unversioned file %{_libdir}/ldc_rt.dso.o
Conflicts:      %{lname_runtime}99
Recommends:     ldc-phobos-devel = %{version}

%description runtime-devel
This package contains the druntime development files necessary for developing
with LDC.

%package -n %{lname_phobos}%{so_ver}
Summary:        The D standard library
Group:          System/Libraries

%description -n %{lname_phobos}%{so_ver}
This package includes ldc's phobos library - The D standard library.

%package -n %{lname_jit}%{so_ver}
Summary:        The LDC jit library
Group:          System/Libraries

%description -n %{lname_jit}%{so_ver}
This package includes ldc's jit library.

%package jit-devel
Summary:        Development files for the D standard library
Group:          Development/Libraries/Other
Requires:       %{lname_jit}%{so_ver} = %{version}

%description jit-devel
This package contains the LDC jit development files.

%package phobos-devel
Summary:        Development files for the D standard library
Group:          Development/Libraries/Other
Requires:       %{lname_phobos}%{so_ver} = %{version}
Requires:       %{name}-runtime-devel = %{version}

%description phobos-devel
This package contains the Phobos development files necessary for developing
with LDC.

%package bash-completion
Summary:        LDC Bash completion
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Optional dependency offering bash completion for ldc2

%prep
%autosetup -p1 -n ldc-%{version}-src

%build
%if %{with ldc_bootstrap}
# Work around gdc bug with stdin (https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105544)
echo "pragma(msg, int(__VERSION__));" > feVer.d
sed -i "s# - -o-# \"$PWD/feVer.d\" -o-#" cmake/Modules/FindDCompiler.cmake

%define __builddir build-bootstrap

#Needs to be compiled with clang, but opensuse_rules.cmake forces gcc so disable rule
touch no-suse-rules
%cmake \
    -DCMAKE_USER_MAKE_RULES_OVERRIDE=./no-suse-rules \
%if 0%{?suse_version} > 1550 || ( 0%{?is_opensuse} && 0%{?sle_version} > 150400 )
    -DCMAKE_C_COMPILER="%{_bindir}/clang" \
    -DCMAKE_CXX_COMPILER="%{_bindir}/clang++" \
%else
    -DCMAKE_C_COMPILER="%{_bindir}/clang" \
    -DCMAKE_CXX_COMPILER="%{_bindir}/clang++" \
%endif
    -DINCLUDE_INSTALL_DIR:PATH=%{ldcincludedir} \
    -DD_COMPILER:PATH=%{_bindir}/gdmd%{?gdc_suffix} \
    -DCMAKE_CXX_FLAGS="-std=c++11"
%make_build
# The bootstrap compiler is used in-place instead of installed and will
# thus set an rpath on generated executables. The next/final stage will be
# installed and should use its own libs, so explicitly disable the rpath.
sed -i '/rpath/d' bin/ldc2.conf
export LD_LIBRARY_PATH="$PWD/%_lib"
cd ..

%define __builddir build
%endif

#Needs to be compiled with clang, but opensuse_rules.cmake forces gcc so disable rule
touch no-suse-rules
%cmake \
    -DCMAKE_USER_MAKE_RULES_OVERRIDE=./no-suse-rules \
%if 0%{?suse_version} > 1550 || ( 0%{?is_opensuse} && 0%{?sle_version} > 150400 )
    -DCMAKE_C_COMPILER="%{_bindir}/clang" \
    -DCMAKE_CXX_COMPILER="%{_bindir}/clang++" \
%else
    -DCMAKE_C_COMPILER="%{_bindir}/clang" \
    -DCMAKE_CXX_COMPILER="%{_bindir}/clang++" \
%endif
    -DINCLUDE_INSTALL_DIR:PATH=%{ldcincludedir} \
%if %{with ldc_bootstrap}
    -DD_COMPILER:PATH=$PWD/../build-bootstrap/bin/ldmd2 \
%endif
    -DCMAKE_CXX_FLAGS="-std=c++11"
%make_build

%if %{with ldc_tests}
%check
pushd build/
# Make sure it can find its own libs
export LD_LIBRARY_PATH="$PWD/%_lib"
%make_build test
popd
%endif

%install
%cmake_install
# Install bash completion in the right folder
if [ ! -d %{buildroot}%{_bashcompletionsdir} ]; then
  install -d %{buildroot}%{_bashcompletionsdir}
  mv %{buildroot}%{_sysconfdir}/bash_completion.d/ldc2 %{buildroot}%{_bashcompletionsdir}
  rmdir %{buildroot}%{_sysconfdir}/bash_completion.d/
fi
# Make sure it can find its own libs (help2man runs the binaries)
export LD_LIBRARY_PATH="$PWD/build/%_lib"
# Build man pages
help2man %{buildroot}%{_bindir}/ldc2  > ldc2.1  && gzip ldc2.1
help2man %{buildroot}%{_bindir}/ldmd2 > ldmd2.1 && gzip ldmd2.1
install -d %{buildroot}%{_mandir}/man1
install -m 644 -t %{buildroot}%{_mandir}/man1/ ldmd2.1.gz ldc2.1.gz
rm -rf %{buildroot}%{_prefix}/lib/debug

%post -n %{lname_runtime}%{so_ver} -p /sbin/ldconfig
%post -n %{lname_phobos}%{so_ver}  -p /sbin/ldconfig
%post -n %{lname_jit}%{so_ver}     -p /sbin/ldconfig
%postun -n %{lname_runtime}%{so_ver} -p /sbin/ldconfig
%postun -n %{lname_phobos}%{so_ver}  -p /sbin/ldconfig
%postun -n %{lname_jit}%{so_ver}     -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/*.1%{?ext_man}
%config %{_sysconfdir}/ldc2.conf
%{_bindir}/ldc*
%{_bindir}/ldmd2
%{_bindir}/timetrace2txt

%files -n %{lname_runtime}%{so_ver}
%{_libdir}/%{lname_runtime}-shared.so.%{so_ver}
%{_libdir}/%{lname_runtime}-shared.so.*
%{_libdir}/%{lname_runtime}-debug-shared.so.%{so_ver}
%{_libdir}/%{lname_runtime}-debug-shared.so.*

%files runtime-devel
%{_libdir}/%{lname_runtime}-shared.so
%{_libdir}/%{lname_runtime}-debug-shared.so
%{_libdir}/ldc_rt.dso.o
%dir %{_libdir}/ldc
%dir %{_libdir}/ldc/%{LDCDIST}
%dir %{_libdir}/ldc/%{LDCDIST}/include
%dir %{ldcincludedir}
%{ldcincludedir}/core
%{ldcincludedir}/ldc
%{ldcincludedir}/__importc_builtins.di
%{ldcincludedir}/importc.h
%{ldcincludedir}/object.d

%files -n %{lname_phobos}%{so_ver}
%{_libdir}/%{lname_phobos}-shared.so.%{so_ver}
%{_libdir}/%{lname_phobos}-shared.so.*
%{_libdir}/%{lname_phobos}-debug-shared.so.%{so_ver}
%{_libdir}/%{lname_phobos}-debug-shared.so.*

%if %jit_support
%files -n %{lname_jit}%{so_ver}
%{_libdir}/%{lname_jit}.so.%{so_ver}
%{_libdir}/%{lname_jit}.so.*

%files jit-devel
%{_libdir}/%{lname_jit}-rt.a
%{_libdir}/%{lname_jit}.so
%endif

%files phobos-devel
%{_libdir}/%{lname_phobos}-shared.so
%{_libdir}/%{lname_phobos}-debug-shared.so
%{ldcincludedir}%{_sysconfdir}
%{ldcincludedir}/std

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_bashcompletionsdir}/ldc2

%changelog
