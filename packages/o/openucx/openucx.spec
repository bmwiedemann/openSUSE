#
# spec file for package openucx
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


# Use for pulling RC versions
%define version_suf %{nil}
Name:           openucx
Version:        1.23.0
Release:        0
Summary:        Communication layer for Message Passing (MPI)
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://openucx.org/
#Git-Clone:	git://github.com/openucx/ucx
#Git-Web:	https://github.com/openucx/ucx
Source:         https://github.com/openucx/ucx/releases/download/v%version%{?version_suf}/ucx-%version.tar.gz
Source100:      README.md
Patch1:         openucx-s390x-support.patch
Patch2:         ucm-fix-UCX_MEM_MALLOC_RELOC.patch
BuildRequires:  autoconf >= 2.63
BuildRequires:  automake >= 1.10
BuildRequires:  binutils-devel
BuildRequires:  gcc-c++
BuildRequires:  libibverbs-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
ExclusiveArch:  aarch64 %power64 x86_64 s390x riscv64
%if 0%{?suse_version} < 1330
%ifnarch s390x
BuildRequires:  libnuma-devel
%endif
%else
BuildRequires:  libnuma-devel
%endif

%description
UCX stands for Unified Communication X. UCX provides a communication
layer for Message Passing (MPI), PGAS/OpenSHMEM libraries and
RPC/data-centric applications. UCX utilizes networks such as RDMA
(InfiniBand, RoCE, etc), Cray Gemini or Aries, for inter-node
communication, or TCP. UCX supports transfer of data in either main
memory (RAM) or GPU memory (through CUDA and ROCm libraries). UCX
provides intra-node communication by using shared memory mechanisms.

%package tools
Summary:        OpenUCX utilities
Group:          System/Console

%description tools
Miscallaneous utilities for Unified Communication X.

%package -n libucm0
Summary:        Memory (un)happing hooks for Unified Communication X
Group:          System/Libraries

%description -n libucm0
libucm is a standalone non-unloadable library which installs hooks
for virtual memory changes in the current process.

%package -n libucm-devel
Summary:        Development files for Unified Communication X Memory Hooks
Group:          Development/Libraries/C and C++
Requires:       libucm0 = %version

%description -n libucm-devel
libucm is a standalone non-unloadable library which installs hooks
for virtual memory changes in the current process.

%package -n libucp0
Summary:        Infiniband Unified Communication Protocols
Group:          System/Libraries

%description -n libucp0
High-level API uses UCT framework to construct protocols commonly
found in applications (MPI, OpenSHMEM, PGAS, etc.)

%package -n libucp-devel
Summary:        Development files for Unified Communication Protocols (UC-P)
Group:          Development/Libraries/C and C++
Requires:       libucp0 = %version

%description -n libucp-devel
High-level API uses UCT framework to construct protocols commonly
found in applications (MPI, OpenSHMEM, PGAS, etc.)

%package -n libucs0
Summary:        Infiniband Unicified Communication Services
Group:          System/Libraries

%description -n libucs0
This framework provides infrastructure for component based
programming, memory management, and system utilities.

%package -n libucs-devel
Summary:        Development files for Unified Communication Services (UC-S)
Group:          Development/Libraries/C and C++
Requires:       libucs0 = %version

%description -n libucs-devel
This framework provides infrastructure for component based
programming, memory management, and system utilities.

%package -n libuct0
Summary:        Infiniband Unified Communication Transport
Group:          System/Libraries

%description -n libuct0
Low-level API that expose network operations supported by underlying
hardware.

%package -n libuct-devel
Summary:        Development files for Unified Communication Transport (UC-T)
Group:          Development/Libraries/C and C++
Requires:       libuct0 = %version

%description -n libuct-devel
Low-level API that expose network operations supported by underlying
hardware.

%prep
%setup -q -n ucx-%version
%autopatch -p0

%build
autoreconf -fi
export UCX_CFLAGS="%optflags -Wno-error"
%ifarch x86_64
export UCX_CFLAGS="$UCX_CFLAGS -mno-avx"
%endif
%ifarch %ix86
export UCX_CFLAGS="$UCX_CFLAGS -mno-sse -mno-sse2"
%endif
%configure --disable-static --without-avx \
%if 0%{?suse_version} < 1330
%ifarch s390x
         --disable-numa \
%endif
%endif
         --docdir="%_docdir/%name" \
		 --disable-debug --disable-assertions \
		 --disable-params-check \
		 --with-rc --with-ud --with-dc \
                 --with-ib-hw-tm --with-dm --with-devx \
		 --with-mlx5 --with-rdmacm

# Override BASE_CFLAGS to disable Werror (boo#1121267)
%make_build BASE_CFLAGS="-g -Wall"

%ldconfig_scriptlets -n libucp0
%ldconfig_scriptlets -n libucs0
%ldconfig_scriptlets -n libuct0
%ldconfig_scriptlets -n libucm0

%install
%make_install
rm -fv "%buildroot/%_libdir"/*.la
rm -fv "%buildroot/%_libdir"/ucx/*.la
# Rename example dir for consistency with the package name
mv %buildroot/%_datadir/ucx  %buildroot/%_datadir/openucx
# io_demo should not be in %{bindir} and more likely in %{libexec}
mkdir -p %buildroot/%_libexecdir/%{name}/
mv %buildroot/%_bindir/io_demo  %buildroot/%_libexecdir/%{name}/
# Remove license as we package them using %license after
rm -f %{buildroot}/%{_docdir}/openucx/LICENSE %{buildroot}/%{_docdir}/openucx/THIRD_PARTY_NOTICES

%files tools
%_bindir/ucx_*
%_datadir/%{name}/
%_libexecdir/%{name}
%_libdir/pkgconfig/ucx.pc
%dir %_libdir/cmake/
%_libdir/cmake/ucx/
%dir %{_sysconfdir}/ucx/
%config %{_sysconfdir}/ucx/ucx.conf
%license LICENSE
%license THIRD_PARTY_NOTICES
%doc NEWS

%files -n libucm0
%_libdir/libucm.so.*

%files -n libucm-devel
%_includedir/ucm/
%_libdir/libucm.so

%files -n libucp0
%_libdir/libucp.so.*

%files -n libucp-devel
%_includedir/ucp/
%_libdir/libucp.so

%files -n libucs0
%_libdir/libucs.so.*
%_libdir/libucs_signal.so.*

%files -n libucs-devel
%_includedir/ucs/
%_libdir/libucs.so
%_libdir/libucs_signal.so
%_libdir/pkgconfig/ucx-ucs.pc

%files -n libuct0
%_libdir/libuct.so.*
%dir %_libdir/ucx/
%_libdir/ucx/libuct_*.so.*
%_libdir/ucx/libucx_perftest_mad.so.*

%files -n libuct-devel
%_includedir/uct/
%_libdir/libuct.so
%dir %_libdir/ucx/
%_libdir/ucx/libuct_*.so
%_libdir/ucx/libucx_perftest_mad.so
%_libdir/pkgconfig/ucx-uct.pc
%_libdir/pkgconfig/ucx-cma.pc
%_libdir/pkgconfig/ucx-ib.pc
%_libdir/pkgconfig/ucx-ib-efa.pc
%_libdir/pkgconfig/ucx-ib-mlx5.pc
%_libdir/pkgconfig/ucx-rdmacm.pc

%changelog
