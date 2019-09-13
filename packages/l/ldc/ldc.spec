#
# spec file for package ldc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_ver        86
%define lname_runtime libdruntime-%{name}
%define lname_phobos  libphobos2-%{name}
%define _bashcompletionsdir %{_datadir}/bash-completion/completions

# llvm7 does not support -flto=4 flag
%define _lto_cflags %{nil}

# Do bootstrap (even in Tumbleweed, and Leap 15+), otherwise LDC will build
# against old installed .so instead of new built one
%bcond_without ldc_bootstrap

%ifarch %{ix86} %arm
# 32-bit needs 1.12.0 intermediate build due to: https://github.com/ldc-developers/ldc/issues/2947
%bcond_without 1_12_0_intermediate
%else
%bcond_with 1_12_0_intermediate
%endif

%bcond_with ldc_tests

Name:           ldc
Version:        1.16.0
Release:        0
Summary:        The LLVM D Compiler
License:        BSD-3-Clause AND Artistic-1.0
Group:          Development/Languages/Other
Url:            https://wiki.dlang.org/LDC
Source0:        https://github.com/ldc-developers/ldc/releases/download/v%{version}/ldc-%{version}-src.tar.gz
Source1:        %{name}-rpmlintrc
Patch0:         ldc-1.9.0-fix_arm_build.patch
BuildRequires:  cmake
BuildRequires:  help2man
BuildRequires:  libconfig++-devel
BuildRequires:  libcurl-devel
BuildRequires:  libstdc++-devel
%if 0%{?suse_version} >= 1550
# Use clang7/llvm7 on Tumbleweed due to https://github.com/ldc-developers/ldc/issues/3109
BuildRequires:  clang7
BuildRequires:  llvm7-devel
%else
BuildRequires:  llvm-clang
BuildRequires:  llvm-devel >= 3.9
%endif
BuildRequires:  ncurses-devel
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bash-completion)
# Should be installed, at least runtime
Recommends:     ldc-phobos-devel = %{version}
Recommends:     ldc-runtime-devel = %{version}
Recommends:     %{name}-bash-completion
# Since version 1.13.0, ldc uses ld.gold by default
Requires:       binutils-gold
%if %{with ldc_bootstrap}
# v0.17.6 is the last version buildable with a C++ compiler, so use it for bootstrapping
Source10:       https://github.com/ldc-developers/ldc/releases/download/v0.17.6/ldc-0.17.6-src.tar.gz
%if %{with 1_12_0_intermediate}
# 1.12.0 is needed to build on 32-bit: https://github.com/ldc-developers/ldc/issues/2947
Source11:       https://github.com/ldc-developers/ldc/releases/download/v1.12.0/ldc-1.12.0-src.tar.gz
%endif
%endif
%if %{with ldc_tests}
BuildRequires:  gcc-c++
BuildRequires:  gdb
%endif
%if %{without ldc_bootstrap}
BuildRequires:  binutils-gold
BuildRequires:  ldc
BuildRequires:  ldc-phobos-devel
BuildRequires:  ldc-runtime-devel
%endif
%if %{with ldc_tests}
BuildRequires:  python
%endif
%if %{with ldc_tests}
BuildRequires:  timezone
BuildRequires:  unzip
%endif
# ppc64 is disabled due to boo#1113531
ExclusiveArch:  %{ix86} x86_64 %arm aarch64

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
Recommends:     ldc-phobos-devel = %{version}

%description runtime-devel
This package contains the druntime development files necessary for developing
with LDC.

%package -n %{lname_phobos}%{so_ver}
Summary:        The D standard library
Group:          System/Libraries

%description -n %{lname_phobos}%{so_ver}
This package includes ldc's phobos library - The D standard library.

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
Group:          System/Shells
Requires:       bash-completion

%description bash-completion
Optional dependency offering bash completion for ldc2


%prep
%setup -q -n ldc-%{version}-src
%patch0 -p1
%if %{with ldc_bootstrap}
tar xf %{SOURCE10}
pushd ldc-0.17.6-src
popd
%if %{with 1_12_0_intermediate}
tar xf %{SOURCE11}
pushd ldc-1.12.0-src
%patch0 -p1
popd
%endif
%endif

%build
%if %{with ldc_bootstrap}
pushd ldc-0.17.6-src
#Needs to be compiled with clang, but opensuse_rules.cmake forces gcc so disable rule
touch ./no-suse-rules
mkdir build && pushd build
# FIXME: you should use %%cmake macros
cmake \
    -DCMAKE_USER_MAKE_RULES_OVERRIDE=./no-suse-rules \
    -DCMAKE_C_COMPILER="%{_bindir}/clang" \
    -DCMAKE_CXX_COMPILER="%{_bindir}/clang++" \
    -DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/d \
    -DCMAKE_CXX_FLAGS="-std=c++11" \
    -DCMAKE_C_FLAGS="-fPIC" \
    ..
make %{?_smp_mflags}
popd
popd
%if %{with 1_12_0_intermediate}
pushd ldc-1.12.0-src
#Needs to be compiled with clang, but opensuse_rules.cmake forces gcc so disable rule
touch ./no-suse-rules
mkdir build && pushd build
# FIXME: you should use %%cmake macros
cmake \
    -DCMAKE_USER_MAKE_RULES_OVERRIDE=./no-suse-rules \
    -DCMAKE_C_COMPILER="%{_bindir}/clang" \
    -DCMAKE_CXX_COMPILER="%{_bindir}/clang++" \
    -DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/d \
    -DD_COMPILER:PATH=`pwd`/../../ldc-0.17.6-src/build/bin/ldmd2 \
    -DCMAKE_CXX_FLAGS="-std=c++11" \
    -DCMAKE_C_FLAGS="-fPIC" \
    ..
make %{?_smp_mflags}
popd
popd
%endif
%endif
#Needs to be compiled with clang, but opensuse_rules.cmake forces gcc so disable rule
touch no-suse-rules
%cmake \
    -DCMAKE_USER_MAKE_RULES_OVERRIDE=./no-suse-rules \
    -DCMAKE_C_COMPILER="%{_bindir}/clang" \
    -DCMAKE_CXX_COMPILER="%{_bindir}/clang++" \
    -DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/d \
%if %{with ldc_bootstrap}
%if %{with 1_12_0_intermediate}
    -DD_COMPILER:PATH=`pwd`/../ldc-1.12.0-src/build/bin/ldmd2 \
%else
    -DD_COMPILER:PATH=`pwd`/../ldc-0.17.6-src/build/bin/ldmd2 \
%endif
%endif
    -DCMAKE_CXX_FLAGS="-std=c++11"
make %{?_smp_mflags}

%if %{with ldc_tests}
%check
pushd build/
make %{?_smp_mflags} test
popd
%endif

%install
%cmake_install
# Install bash completion in the right folder
install -d %{buildroot}%{_bashcompletionsdir}
mv %{buildroot}/etc/bash_completion.d/ldc2 %{buildroot}%{_bashcompletionsdir}
rmdir %{buildroot}/etc/bash_completion.d/
# Build man pages
help2man %{buildroot}%{_bindir}/ldc2  > ldc2.1  && gzip ldc2.1
help2man %{buildroot}%{_bindir}/ldmd2 > ldmd2.1 && gzip ldmd2.1
install -d %{buildroot}%{_mandir}/man1
install -m 644 -t %{buildroot}%{_mandir}/man1/ ldmd2.1.gz ldc2.1.gz
rm -rf %{buildroot}%{_libexecdir}/debug

%post -n %{lname_runtime}%{so_ver} -p /sbin/ldconfig
%post -n %{lname_phobos}%{so_ver}  -p /sbin/ldconfig
%postun -n %{lname_runtime}%{so_ver} -p /sbin/ldconfig
%postun -n %{lname_phobos}%{so_ver}  -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/*.1%{?ext_man}
%config %{_sysconfdir}/ldc2.conf
%{_bindir}/ldc*
%{_bindir}/ldmd2

%files -n %{lname_runtime}%{so_ver}
%{_libdir}/%{lname_runtime}-shared.so.*
%{_libdir}/%{lname_runtime}-debug-shared.so.*

%files runtime-devel
%{_libdir}/%{lname_runtime}-shared.so
%{_libdir}/%{lname_runtime}-debug-shared.so
%dir %{_includedir}/d
%{_includedir}/d/core
%{_includedir}/d/ldc
%{_includedir}/d/object.d

%files -n %{lname_phobos}%{so_ver}
%{_libdir}/%{lname_phobos}-shared.so.*
%{_libdir}/%{lname_phobos}-debug-shared.so.*

%files phobos-devel
%{_libdir}/%{lname_phobos}-shared.so
%{_libdir}/%{lname_phobos}-debug-shared.so
%{_includedir}/d/etc
%{_includedir}/d/std

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_bashcompletionsdir}/ldc2

%changelog
