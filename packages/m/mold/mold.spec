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
Version:        1.7.1
Release:        0
Summary:        A Modern Linker (mold)
License:        AGPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/rui314/mold
Source:         https://github.com/rui314/mold/archive/v%{version}/mold-%{version}.tar.gz
BuildRequires:  cmake
%if %{suse_version} < 1550
BuildRequires:  gcc11-c++
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
BuildRequires:  libzstd-devel
BuildRequires:  openssl-devel
%ifnarch ppc64
BuildRequires:  valgrind
%endif
BuildRequires:  zlib-devel
BuildRequires:  zstd
PreReq:         update-alternatives
ExcludeArch:    ppc

%if %{suse_version} < 1550
%define build_args -DMOLD_USE_MIMALLOC=OFF -DMOLD_USE_MIMALLOC=OFF
%else
%define build_args -DMOLD_USE_MIMALLOC=OFF -DMOLD_USE_MIMALLOC=OFF -DMOLD_USE_SYSTEM_TBB=ON
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
export CC=gcc-11
export CXX=g++-11
%endif
%cmake %{build_args}
%cmake_build

%install
%cmake_install

%check
%if %{suse_version} < 1550
export TEST_CC=gcc-11
export TEST_CXX=g++-11
%endif
%ctest

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
%{_mandir}/man1/ld.mold.1.gz
%dir /usr/share/doc/mold
%doc /usr/share/doc/mold/LICENSE

%changelog
