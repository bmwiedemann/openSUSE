#
# spec file for package mingw64-binutils
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


Name:           mingw64-binutils
Version:        2.42
Release:        0
Summary:        GNU Binutils
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries
URL:            http://www.gnu.org/software/binutils/
Source:         http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.xz
Source1:        http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.xz.sig
Source2:        mingw64-binutils.keyring
Source99:       mingw64-binutils-rpmlintrc
Patch0:         binutils-2.42-option-high-entry-va.patch
#!BuildIgnore: post-build-checks
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  texinfo
BuildArch:      noarch
%_mingw64_package_header_debug

%description
The GNU Binutils are a collection of binary tools.
These utilities (like 'as', 'ld', 'strip') understand Windows executables and DLLs.

%package devel
Summary:        %{summary}
Group:          Development/Libraries

%description devel
libbfd, libiberty and libopcodes.a

%_mingw64_debug_package

%prep
%autosetup -p1 -n binutils-%{version}

%build
mkdir -p build
cd build
%{_mingw64_configure} \
  --verbose --disable-nls \
  --without-included-gettext \
  --disable-win32-registry \
  --with-sysroot=%{_mingw64_prefix} \
  --disable-werror \
  --enable-install-libiberty

%make_build || make

%install
cd build
%make_install

rm -f %{buildroot}%{_mingw64_infodir}/dir

# mingw64-binutils.noarch: E: zero-length .../lib/ldscripts/stamp
for i in %{buildroot}%{_mingw64_prefix}/%{_mingw64_target}/lib/ldscripts/stamp; do
  if test -f $i; then
    rm $i
  fi
done

%files
%{_mingw64_bindir}/*.exe
%{_mingw64_prefix}/%{_mingw64_target}/bin/*.exe
%{_mingw64_prefix}/%{_mingw64_target}/lib/ldscripts/
%dir %{_mingw64_prefix}/lib/bfd-plugins/
%{_mingw64_prefix}/lib/bfd-plugins/libdep.dll
%{_mingw64_mandir}/man1/*
%{_mingw64_infodir}/*.info*

%files devel
%{_mingw64_includedir}/
%{_mingw64_libdir}/libbfd.a
%{_mingw64_libdir}/libctf.a
%{_mingw64_libdir}/libctf-nobfd.a
# required by libbfd.a
%{_mingw64_libdir}/libiberty.a
%{_mingw64_libdir}/libopcodes.a
%{_mingw64_libdir}/libsframe.a

%changelog
