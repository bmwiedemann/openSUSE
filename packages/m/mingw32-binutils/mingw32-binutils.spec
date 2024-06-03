#
# spec file for package mingw32-binutils
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


%global _default_patch_fuzz 2

Name:           mingw32-binutils
Version:        2.39
Release:        0
Summary:        GNU Binutils
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries
URL:            http://www.gnu.org/software/binutils/
Source:         http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.xz
Source99:       mingw32-binutils-rpmlintrc
Patch0:         0001-PR29362-some-binutils-memory-leaks.patch
Patch1:         0001-Fix-bug-not-showing-correct-path-with-objdump-WL-wit.patch
Patch2:         0001-dllwrap-windres-and-dlltools-use-mktemp-which-should.patch
Patch3:         reproducible.patch
Patch4:         binutils-2.39-option-high-entry-va.patch
#!BuildIgnore: post-build-checks
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  mingw32-cross-binutils
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-filesystem
BuildRequires:  texinfo
BuildArch:      noarch
%_mingw32_package_header_debug

%description
The GNU Binutils are a collection of binary tools.
These utilities (like 'as', 'ld', 'strip') understand Windows executables and DLLs.

%package devel
Summary:        %{summary}
Group:          Development/Libraries

%description devel
libbfd, libiberty and libopcodes.a

%_mingw32_debug_package

%prep
%autosetup -p1 -n binutils-%{version}

%build
mkdir -p build
cd build
%{_mingw32_configure} \
  --verbose --disable-nls \
  --without-included-gettext \
  --disable-win32-registry \
  --with-sysroot=%{_mingw32_prefix} \
  --disable-werror \
  --enable-install-libiberty

%make_build || make

%install
cd build
%make_install

rm -f %{buildroot}%{_mingw32_infodir}/dir

%files
%{_mingw32_bindir}/*.exe
%{_mingw32_prefix}/%{_mingw32_target}/bin/*.exe
%{_mingw32_prefix}/%{_mingw32_target}/lib/ldscripts/
%dir %{_mingw32_prefix}/lib/bfd-plugins/
%{_mingw32_prefix}/lib/bfd-plugins/libdep.dll
%{_mingw32_mandir}/man1/*
%{_mingw32_infodir}/*.info*

%files devel
%{_mingw32_includedir}/
%{_mingw32_libdir}/libbfd.a
%{_mingw32_libdir}/libctf.a
%{_mingw32_libdir}/libctf-nobfd.a
%{_mingw32_libdir}/libopcodes.a
# required by libbfd.a
%{_mingw32_libdir}/libiberty.a

%changelog
