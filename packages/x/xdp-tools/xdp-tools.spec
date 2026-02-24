#
# spec file for package xdp-tools
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover_major 1
%define libname libxdp%{sover_major}

# check_abi will fail otherwise
# See https://github.com/xdp-project/xdp-tools/issues/137
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

# workaround binutils/strip issue with BPF object, see #boo#1217108
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
Name:           xdp-tools
Version:        1.6.2
Release:        0
Group:          Productivity/Networking/Other
Summary:        Utilities and example programs for use with XDP
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-2.0-only
URL:            https://github.com/xdp-project/xdp-tools
Source:         https://github.com/xdp-project/xdp-tools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fixes "error: argument unused during compilation: '-c' [-Werror,-Wunused-command-line-argument]" with
# Clang 20. The command lines have both -c and -S, but should only have -S as they're producing textual IR.
BuildRequires:  bpftool
BuildRequires:  clang >= 10.0.0
BuildRequires:  gcc
BuildRequires:  libbpf-devel
BuildRequires:  libelf-devel
BuildRequires:  libpcap-devel
BuildRequires:  llvm >= 10.0.0
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
# For README.org file, but pulls in too much dependency
#BuildRequires:  emacs-nox
# Always keep xdp-tools and libxdp packages in sync
Requires:       %{libname} = %{version}-%{release}

%description
Utilities and example programs for use with XDP

%package -n %{libname}
Group:          System/Libraries
Summary:        XDP helper library

%description -n %{libname}
The libxdp package contains the libxdp library for managing XDP programs,
used by the %{name} package

%package -n libxdp-devel
Group:          Development/Libraries/C and C++
Summary:        Development files for libxdp
Requires:       %{libname} = %{version}-%{release}
Requires:       kernel-devel

%description -n libxdp-devel
The libxdp-devel package contains headers used for building XDP programs using
libxdp.

%prep
%setup -q
%autopatch -p1

%build
# Not Autoconf-based, so need to set environmental variables
# defined in lib/defines.mk
%set_build_flags
export LIBDIR='%{_libdir}'
export CLANG=%{_bindir}/clang
export LLC=%{_bindir}/llc
export PRODUCTION=1
export DYNAMIC_LIBXDP=1
export FORCE_SYSTEM_LIBBPF=1
#export FORCE_EMACS=1
export PATH="$PATH:/usr/sbin" # So bpftool can be found
./configure
%make_build

%install
# ./configure does not support arguments, only environmental variables defined
# in lib/define.mk
export SBINDIR='%{_sbindir}'
export LIBDIR='%{_libdir}'
export MANDIR='%{_mandir}'
export DATADIR='%{_datadir}'
export HDRDIR='%{_includedir}/xdp'
%make_install
# Remove the static libraries
rm -f %{buildroot}%{_libdir}/libxdp.a
# Remove test file to avoid rpmlint's arch-dependent-file-in-usr-share error
rm -rf %{buildroot}%{_datadir}/xdp-tools/

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_sbindir}/xdp-filter
%{_sbindir}/xdp-loader
%{_sbindir}/xdpdump
%{_sbindir}/xdp-bench
%{_sbindir}/xdp-monitor
%{_sbindir}/xdp-trafficgen
%{_sbindir}/xdp-forward
%{_libdir}/bpf/xdpfilt_*.o
%{_libdir}/bpf/xdpdump_*.o
%{_mandir}/man8/*

%files -n %{libname}
%dir %{_libdir}/bpf
%{_libdir}/libxdp.so.%{sover_major}*
%{_libdir}/bpf/xdp-dispatcher.o
%{_libdir}/bpf/xsk_def_xdp_prog*.o
%{_mandir}/man3/*

%files -n libxdp-devel
%license LICENSES/*
%dir %{_includedir}/xdp
%{_includedir}/xdp/*.h
%{_libdir}/libxdp.so
%{_libdir}/pkgconfig/libxdp.pc

%changelog
