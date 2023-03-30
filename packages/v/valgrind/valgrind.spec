#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?!make_build:1}
%define make_build make -O %{?_smp_mflags} V=1 VERBOSE=1
%endif

# during building the major version of glibc is built into the suppression file
%define glibc_main_version %(getconf GNU_LIBC_VERSION | cut -d' ' -f2 | cut -d. -f1)
%define glibc_major_version %(getconf GNU_LIBC_VERSION | cut -d' ' -f2 | cut -d. -f2)
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "client-headers"
%define psuffix  -client-headers-source
%endif
%bcond_without docs
Name:           valgrind%{?psuffix}
Version:        3.20.0
Release:        0
Summary:        Memory Management Debugger
License:        GFDL-1.2-only AND GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://valgrind.org/
Source0:        https://sourceware.org/pub/valgrind/valgrind-%{version}.tar.bz2
# https://bugs.kde.org/show_bug.cgi?id=390553
# https://github.com/olafhering/valgrind/compare/olh-base-master...olh-fixes-master
Patch0:         valgrind.xen.patch
Patch2:         armv6-support.diff
Patch9:         parallel-lto.patch
Patch10:        dhat-use-datadir.patch
BuildRequires:  automake
BuildRequires:  pkgconfig
ExclusiveArch:  aarch64 %{ix86} x86_64 ppc ppc64 ppc64le s390x armv7l armv7hl armv6l armv6hl
%if "%{flavor}" == ""
Requires:       glibc >= %{glibc_main_version}.%{glibc_major_version}
Requires:       glibc < %{glibc_main_version}.%{lua:print(rpm.expand("%{glibc_major_version}")+1)}
Provides:       callgrind = %{version}
Obsoletes:      callgrind < %{version}
%if %{with docs}
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
%endif
%if 0%{?suse_version} < 1500
BuildRequires:  gcc8-c++
%global cpp_version -8
%else
BuildRequires:  gcc-c++
%endif
%ifarch x86_64 ppc64
BuildRequires:  glibc-devel-32bit
%if 0%{?suse_version} < 1500
BuildRequires:  gcc8-c++-32bit
%else
BuildRequires:  gcc-c++-32bit
%endif
%endif
%else
%endif

%description
Valgrind checks all memory operations in an application, like read,
write, malloc, new, free, and delete. Valgrind can find uses of
uninitialized memory, access to already freed memory, overflows,
illegal stack operations, memory leaks, and any illegal
new/malloc/free/delete commands. Another program in the package is
"cachegrind," a profiler based on the valgrind engine.

To use valgrind you should compile your application with "-g -O0"
compiler options. Afterwards you can use it with:

valgrind --tool=memcheck --sloppy-malloc=yes --leak-check=yes
--db-attach=yes my_application, for example.

More valgrind options can be listed via "valgrind --help". There is
also complete documentation in the %{_docdir}/valgrind/
directory. A debugged application runs slower and needs much more
memory, but is usually still usable. Valgrind is still in development,
but it has been successfully used to optimize several KDE applications.

%package devel
Summary:        Header files for for Valgrind
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}
Requires:       %{name}-client-headers = %{version}

%description devel
This package contains the Valgrind header files.

%package -n valgrind-client-headers
Summary:        Header files for for Valgrind
# The client headers are permissively licensed under a BSD-style
# license. SPDX License Request filed.
# License:      BSD-3-Clause
License:        GFDL-1.2-only AND GPL-2.0-or-later
Group:          Development/Tools/Debuggers
Provides:       valgrind-devel:%{_includedir}/valgrind/valgrind.h
BuildArch:      noarch

%description -n valgrind-client-headers
This package contains the BSD-style licensed Valgrind header
files for inclusion into regular programs. The program can
detect if it is running under Valgrind and interact with the
Valgrind core and plugins.

%ifarch x86_64 ppc64 s390x
%package 32bit
Summary:        Memory Management Debugger
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}
Provides:       valgrind:%{_libdir}/valgrind/32bit-core.xml

%description 32bit
Valgrind checks all memory operations in an application, like read,
write, malloc, new, free, and delete. Valgrind can find uses of
uninitialized memory, access to already freed memory, overflows,
illegal stack operations, memory leaks, and any illegal
new/malloc/free/delete commands. Another program in the package is
"cachegrind," a profiler based on the valgrind engine.

To use valgrind you should compile your application with "-g -O0"
compiler options. Afterwards you can use it with:

valgrind --tool=memcheck --sloppy-malloc=yes --leak-check=yes
--db-attach=yes my_application, for example.

More valgrind options can be listed via "valgrind --help". There is
also complete documentation in the %{_docdir}/valgrind/
directory. A debugged application runs slower and needs much more
memory, but is usually still usable. Valgrind is still in development,
but it has been successfully used to optimize several KDE applications.

%endif

%prep
%setup -q -n valgrind-%{version}
%autopatch -p1

%build
%define _lto_cflags %{nil}
# The preloaded libs for intercepting rely on lazy binding (bsc#1208407)
export SUSE_ZNOW=0
export FLAGS="%{optflags}"
# not a good idea to build valgrind with fortify, as it does not link glibc
FLAGS="${FLAGS/-D_FORTIFY_SOURCE=2/}"
FLAGS="${FLAGS/-D_FORTIFY_SOURCE=3/}"
FLAGS="${FLAGS/-fstack-protector-strong/}"
FLAGS="${FLAGS/-fstack-protector/}"
# -m64 / -m32 is set explicitly everywhere, do not override it
FLAGS="${FLAGS/-m64/}"
export CFLAGS="$FLAGS"
export CXXFLAGS="$FLAGS"
export FFLAGS="$FLAGS"
export CXX="g++%{?cpp_version}"
export CC="gcc%{?cpp_version}"
autoreconf -fi

export GDB=%{_bindir}/gdb
%configure \
    --enable-lto=yes \
%ifarch aarch64
    --enable-only64bit \
%endif
    %{nil}

%if "%{flavor}" == ""
%make_build
%if %{with docs}
pushd docs
    #make all-docs
    # building the docs needs network access at the moment :-(
    %make_build FAQ.txt man-pages html-docs
popd
%endif
%endif

%install
%if "%{flavor}" == ""
%make_install
rm %{buildroot}/%{_libdir}/valgrind/lib*.a # drop unreproducible unused files to fix boo#1118163

mkdir -p %{buildroot}/%{_defaultdocdir}
if test -d %{buildroot}%{_datadir}/doc/valgrind; then
     # Remove Postscript manual (20 MByte), there are PDF and HTML versions
     rm %{buildroot}%{_datadir}/doc/valgrind/valgrind_manual.ps
     mv %{buildroot}%{_datadir}/doc/valgrind %{buildroot}/%{_defaultdocdir}
fi
mkdir -p %{buildroot}%{_docdir}/%{name}

rm %{buildroot}/%{_includedir}/valgrind/{valgrind,callgrind,dhat,drd,helgrind,memcheck}.h

%else
install -m 755 -d %{buildroot}/%{_includedir}/valgrind
install -m 644 -t %{buildroot}/%{_includedir}/valgrind \
    include/valgrind.h \
    callgrind/callgrind.h \
    dhat/dhat.h \
    drd/drd.h \
    helgrind/helgrind.h \
    memcheck/memcheck.h
%endif

%check
%if "%{flavor}" == ""
# OBS doesn't have a z13
%ifnarch s390x %{arm}
# has too many spurious failures
# make %{?_smp_mflags} regtest
#patent pending self test
VALGRIND_LIB=$PWD/.in_place VALGRIND_LIB_INNER=$PWD/.in_place ./coregrind/valgrind  %{_bindir}/perl -wc tests/vg_regtest
%endif
%endif

%if "%{flavor}" == ""
%files devel
%dir %{_includedir}/valgrind
%{_includedir}/valgrind/config.h
%{_includedir}/valgrind/vki
%{_includedir}/valgrind/libvex*.h
%{_includedir}/valgrind/pub_tool*.h
%{_libdir}/pkgconfig/valgrind.pc

%files -n valgrind
%license COPYING COPYING.DOCS
%{_bindir}/*
%doc README* NEWS AUTHORS
%doc %{_defaultdocdir}/%{name}/*
%{_mandir}/*/*
%dir %{_libexecdir}/valgrind
%ifarch aarch64
%{_libexecdir}/valgrind/*-arm64-linux
%endif
%ifarch x86_64
%{_libexecdir}/valgrind/*-amd64-linux
%endif
%ifarch %{ix86}
%{_libexecdir}/valgrind/*-x86-linux
%endif
%ifarch ppc
%{_libexecdir}/valgrind/*-ppc32-linux
%endif
%ifarch ppc64
%{_libexecdir}/valgrind/*-ppc64be-linux
%endif
%ifarch ppc64le
%{_libexecdir}/valgrind/*-ppc64le-linux
%endif
%ifarch s390x
%{_libexecdir}/valgrind/*-s390x-linux
%endif
%ifarch %{arm}
%{_libexecdir}/valgrind/*-arm-linux
%endif
%dir %{_datadir}/valgrind
%{_datadir}/valgrind/dh_view*
%{_libexecdir}/valgrind/*-linux.so
%{_libexecdir}/valgrind/*.supp
%{_libexecdir}/valgrind/64bit-core.xml
%{_libexecdir}/valgrind/64bit-linux.xml
%{_libexecdir}/valgrind/64bit-sse.xml
%{_libexecdir}/valgrind/64bit-core-valgrind-s*.xml
%{_libexecdir}/valgrind/64bit-linux-valgrind-s*.xml
%{_libexecdir}/valgrind/64bit-sse-valgrind-s*.xml
%{_libexecdir}/valgrind/amd64-coresse-valgrind.xml
%{_libexecdir}/valgrind/amd64-linux-valgrind.xml
%{_libexecdir}/valgrind/power64-core-valgrind-s*.xml
%{_libexecdir}/valgrind/power64-core.xml
%{_libexecdir}/valgrind/power64-core2-valgrind-s*.xml
%{_libexecdir}/valgrind/power64-linux-valgrind-s*.xml
%{_libexecdir}/valgrind/power64-linux.xml
%{_libexecdir}/valgrind/64bit-avx-valgrind-s*.xml
%{_libexecdir}/valgrind/64bit-avx.xml
%{_libexecdir}/valgrind/amd64-avx-coresse-valgrind.xml
%{_libexecdir}/valgrind/amd64-avx-coresse.xml
%{_libexecdir}/valgrind/amd64-avx-linux-valgrind.xml
%{_libexecdir}/valgrind/amd64-avx-linux.xml
%{_libexecdir}/valgrind/mips64-cp0-valgrind-s*.xml
%{_libexecdir}/valgrind/mips64-cp0.xml
%{_libexecdir}/valgrind/mips64-cpu-valgrind-s*.xml
%{_libexecdir}/valgrind/mips64-cpu.xml
%{_libexecdir}/valgrind/mips64-fpu-valgrind-s*.xml
%{_libexecdir}/valgrind/mips64-fpu.xml
%{_libexecdir}/valgrind/mips64-linux-valgrind.xml
%{_libexecdir}/valgrind/mips64-linux.xml
%{_libexecdir}/valgrind/power-core-valgrind-s*.xml
%{_libexecdir}/valgrind/s390x-core64-valgrind-s*.xml
%{_libexecdir}/valgrind/s390x-core64.xml
%{_libexecdir}/valgrind/s390x-generic-valgrind.xml
%{_libexecdir}/valgrind/s390x-generic.xml
%{_libexecdir}/valgrind/s390x-linux64-valgrind-s*.xml
%{_libexecdir}/valgrind/s390x-linux64.xml
%{_libexecdir}/valgrind/s390x-vx-linux-valgrind.xml
%{_libexecdir}/valgrind/s390x-vx-linux.xml
# See https://bugzilla.suse.com/show_bug.cgi?id=1147071#c0
%{_libexecdir}/valgrind/s390-acr-valgrind-s*.xml
%{_libexecdir}/valgrind/s390-acr.xml
%{_libexecdir}/valgrind/s390-fpr-valgrind-s*.xml
%{_libexecdir}/valgrind/s390-fpr.xml
%{_libexecdir}/valgrind/s390-vx-valgrind-s*.xml
%{_libexecdir}/valgrind/s390-vx.xml

%ifarch x86_64 ppc64 s390x
%files 32bit
%endif

%ifarch %{ix86} x86_64
%{_libexecdir}/valgrind/*-x86-linux
%endif

%ifarch ppc ppc64
%{_libexecdir}/valgrind/*-ppc32-linux
%endif
%{_libexecdir}/valgrind/mips-cp0-valgrind-s*.xml
%{_libexecdir}/valgrind/mips-cp0.xml
%{_libexecdir}/valgrind/mips-cpu-valgrind-s*.xml
%{_libexecdir}/valgrind/mips-cpu.xml
%{_libexecdir}/valgrind/mips-fpu-valgrind-s*.xml
%{_libexecdir}/valgrind/mips-fpu.xml
%{_libexecdir}/valgrind/mips-linux-valgrind.xml
%{_libexecdir}/valgrind/mips-linux.xml
%{_libexecdir}/valgrind/32bit-core.xml
%{_libexecdir}/valgrind/32bit-linux.xml
%{_libexecdir}/valgrind/32bit-sse.xml
%{_libexecdir}/valgrind/arm-core-valgrind-s*.xml
%{_libexecdir}/valgrind/arm-core.xml
%{_libexecdir}/valgrind/arm-vfpv3-valgrind-s*.xml
%{_libexecdir}/valgrind/arm-vfpv3.xml
%{_libexecdir}/valgrind/arm-with-vfpv3-valgrind.xml
%{_libexecdir}/valgrind/arm-with-vfpv3.xml
%{_libexecdir}/valgrind/32bit-core-valgrind-s*.xml
%{_libexecdir}/valgrind/32bit-linux-valgrind-s*.xml
%{_libexecdir}/valgrind/32bit-sse-valgrind-s*.xml
%{_libexecdir}/valgrind/i386-coresse-valgrind.xml
%{_libexecdir}/valgrind/i386-linux-valgrind.xml
%{_libexecdir}/valgrind/power-altivec-valgrind-s*.xml
%{_libexecdir}/valgrind/power-altivec.xml
%{_libexecdir}/valgrind/power-core.xml
%{_libexecdir}/valgrind/power-fpu-valgrind-s*.xml
%{_libexecdir}/valgrind/power-fpu.xml
%{_libexecdir}/valgrind/power-linux-valgrind-s*.xml
%{_libexecdir}/valgrind/power-linux.xml
%{_libexecdir}/valgrind/power-vsx-valgrind-s1.xml
%{_libexecdir}/valgrind/power-vsx-valgrind-s2.xml
%{_libexecdir}/valgrind/power-vsx.xml
%{_libexecdir}/valgrind/powerpc-altivec32l-valgrind.xml
%{_libexecdir}/valgrind/powerpc-altivec32l.xml
%{_libexecdir}/valgrind/powerpc-altivec64l-valgrind.xml
%{_libexecdir}/valgrind/powerpc-altivec64l.xml

%else

%files -n valgrind-client-headers
%dir %{_includedir}/valgrind
%{_includedir}/valgrind/callgrind.h
%{_includedir}/valgrind/dhat.h
%{_includedir}/valgrind/drd.h
%{_includedir}/valgrind/helgrind.h
%{_includedir}/valgrind/memcheck.h
%{_includedir}/valgrind/valgrind.h
%endif

%changelog
