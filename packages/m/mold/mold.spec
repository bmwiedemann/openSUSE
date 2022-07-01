#
# spec file for package mold
#
# Copyright (c) 2022 SUSE LLC
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


Name:           mold
Version:        1.3.1
Release:        0
Summary:        A Modern Linker (mold)
License:        AGPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/rui314/mold
Source:         https://github.com/rui314/mold/archive/v%{version}/mold-%{version}.tar.gz
ExclusiveArch:  aarch64 %arm x86_64 aarch64 riscv64
BuildRequires:  cmake
%if %{suse_version} < 1550
BuildRequires:  gcc10-c++
%else
# These libraries are not present for openSUSE Leap
BuildRequires:  gcc-c++
BuildRequires:  clang
BuildRequires:  libdwarf-tools
BuildRequires:  llvm
BuildRequires:  llvm-gold
BuildRequires:  tbb-devel
%ifarch x86_64
BuildRequires:  gcc-32bit
%endif
%endif
BuildRequires:  gdb
BuildRequires:  glibc-devel-static
BuildRequires:  openssl-devel
BuildRequires:  valgrind
BuildRequires:  xxhash-devel
BuildRequires:  zlib-devel
PreReq:         update-alternatives

%if %{suse_version} < 1550
%define build_args STRIP=true SYSTEM_XXHASH=1 USE_MIMALLOC=0
%else
%define build_args STRIP=true SYSTEM_TBB=1 SYSTEM_XXHASH=1 USE_MIMALLOC=0
%endif

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than LLVM lld linker, the second-fastest
open-source linker.
mold is created for increasing developer productivity by reducing
build time especially in rapid debug-edit-rebuild cycles.

%prep
%autosetup -p1

%build
%if %{suse_version} < 1550
export CC=gcc-10
export CXX=g++-10
%endif
export CXXFLAGS="%{optflags} -Wno-sign-compare"

%make_build -e \
CXXFLAGS="${CXXFLAGS}" \
LDFLAGS="${CXXFLAGS}" \
PREFIX=%{_prefix} \
BINDIR=%{_bindir} \
MANDIR=%{_mandir} \
LIBDIR=%{_libdir} \
LIBEXECDIR=%{_libexecdir} \
%{build_args}

%install
%make_install -e \
PREFIX=%{_prefix} \
BINDIR=%{_bindir} \
MANDIR=%{_mandir} \
LIBDIR=%{_libdir} \
LIBEXECDIR=%{_libexecdir} \
%{build_args}

%check
%if %{suse_version} < 1550
export TEST_CC=gcc-10
export TEST_CXX=g++-10
%endif
make test -k -e \
PREFIX=%{_prefix} \
BINDIR=%{_bindir} \
MANDIR=%{_mandir} \
LIBDIR=%{_libdir} \
LIBEXECDIR=%{_libexecdir} \
%{build_args}

%post
"%_sbindir/update-alternatives" --install \
	"%_bindir/ld" ld "%_bindir/ld.mold" 1

%pre
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] ; then
	"%_sbindir/update-alternatives" --remove ld "%_bindir/ld.mold";
fi;

%postun
if [ ! -f %{_bindir}/lld ] ; then
    "%{_sbindir}/update-alternatives" --remove ld "%{_bindir}/ld.mold"
fi

%files
%ghost %_sysconfdir/alternatives/ld
%{_bindir}/mold
%{_bindir}/ld.mold
%{_bindir}/ld64.mold
%dir %{_libdir}/mold
%{_libexecdir}/mold/ld
%dir %{_libexecdir}/mold
%{_libdir}/mold/mold-wrapper.so
%{_mandir}/man1/mold.1.gz

%changelog
