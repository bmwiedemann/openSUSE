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
Version:        1.0.2
Release:        0
Summary:        A Modern Linker (mold)
License:        AGPL-3.0-or-later
URL:            https://github.com/rui314/mold
Source:         https://github.com/rui314/mold/archive/v%{version}/mold-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  tbb-devel
BuildRequires:  tbb-devel
BuildRequires:  xxhash-devel
BuildRequires:  zlib-devel
PreReq:         update-alternatives

%define build_args SYSTEM_TBB=1 SYSTEM_XXHASH=1

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than LLVM lld linker, the second-fastest
open-source linker.
mold is created for increasing developer productivity by reducing
build time especially in rapid debug-edit-rebuild cycles.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
export CFLAGS="%{optflags} -Wno-sign-compare"
export CXXFLAGS="${CFLAGS}"
export MANDIR=%{_mandir}
export LIBDIR=%{_libdir}
export BINDIR=%{_bindir}
%make_build %{build_args}

%install
%make_install PREFIX=%{_prefix} BINDIR=%{_bindir} MANDIR=%{_mandir} LIBDIR=%{_libdir} %{build_args}

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
