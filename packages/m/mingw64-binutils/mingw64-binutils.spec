#
# spec file for package mingw64-binutils
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mingw64-binutils
Version:        2.32
Release:        0
Summary:        GNU Binutils
License:        GPL-2.0+ AND LGPL-2.1+ AND GPL-3.0+ AND LGPL-3.0+
Group:          Development/Libraries
Url:            http://www.gnu.org/software/binutils/
Source:         http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
Source99:       mingw64-binutils-rpmlintrc
Patch0:         0001-COFF-Check-for-symbols-defined-in-discarded-section.patch
#!BuildIgnore: post-build-checks
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  texinfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%_mingw64_package_header_debug
BuildArch:      noarch

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
%setup -q -n binutils-%{version}
%patch0 -p1

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

make %{?_smp_mflags} || make

%install
cd build
make DESTDIR=%{buildroot} install %{?_smp_mflags}

rm -f %{buildroot}%{_mingw64_infodir}/dir

%files
%defattr(-,root,root)
%{_mingw64_bindir}/*.exe
%{_mingw64_prefix}/%{_mingw64_target}/bin/*.exe
%{_mingw64_prefix}/%{_mingw64_target}/lib/ldscripts/
%{_mingw64_mandir}/man1/*
%{_mingw64_infodir}/*.info*

%files devel
%defattr(-,root,root)
%{_mingw64_includedir}/
%{_mingw64_libdir}/libbfd.a
%{_mingw64_libdir}/libopcodes.a
# required by libbfd
%{_mingw64_libdir}/libiberty.a

%changelog
