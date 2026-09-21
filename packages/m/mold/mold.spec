#
# spec file for package mold
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


Name:           mold
Version:        2.42.1
Release:        0
Summary:        A Modern Linker (mold)
License:        MIT
URL:            https://github.com/rui314/mold
Source:         https://github.com/rui314/mold/archive/v%{version}/mold-%{version}.tar.gz
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  glibc-devel-static
BuildRequires:  libdwarf-tools
BuildRequires:  llvm
BuildRequires:  llvm-gold
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  valgrind
BuildRequires:  zstd
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Suggests:       update-alternatives
OrderWithRequires(pre): update-alternatives
%ifarch x86_64
BuildRequires:  gcc-32bit
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
%cmake \
  -DMOLD_USE_MIMALLOC=OFF \
  -DMOLD_USE_SYSTEM_TBB=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%pre
if [ $1 -eq 2 ] && [ -f %{_sbindir}/update-alternatives ] && [ -f %{_sysconfdir}/alternatives/ld ] ; then
  "%{_sbindir}/update-alternatives" --remove ld "%{_bindir}/ld.mold"
fi

%files
%{_bindir}/mold
%{_bindir}/ld.mold
%dir %{_libdir}/mold
%{_libexecdir}/mold/ld
%dir %{_libexecdir}/mold
%{_libdir}/mold/mold-wrapper.so
%{_mandir}/man1/mold.1%{?ext_man}
%{_mandir}/man1/ld.mold.1%{?ext_man}
%dir %{_docdir}/mold
%license %{_docdir}/mold/LICENSE

%changelog
