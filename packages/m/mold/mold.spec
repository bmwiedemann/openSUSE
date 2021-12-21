#
# spec file for package mold
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mold
Version:        1.0.0
Release:        0
Summary:        A Modern Linker (mold)
License:        AGPL-3.0-or-later
Url:            https://github.com/rui314/mold
Source:         https://github.com/rui314/mold/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  xxhash-devel
BuildRequires:  zlib-devel
PreReq:         update-alternatives

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than LLVM lld linker, the second-fastest
open-source linker.
mold is created for increasing developer productivity by reducing
build time especially in rapid debug-edit-rebuild cycles.

%prep
%autosetup -p1 -n mold-%{version}

%build
export CC=gcc
export CXX=g++
export CFLAGS="%{optflags}"
export CXXFLAGS="${CFLAGS}"

export MANDIR=%{_mandir}
export LIBDIR=%{_libdir}
export BINDIR=%{_bindir}
%make_build

%install
export MANDIR=%{_mandir}
export LIBDIR=%{_libdir}
export BINDIR=%{_bindir}
%make_install

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
%{_libdir}/mold/mold-wrapper.so
%{_mandir}/man1/mold.1.gz

%changelog
