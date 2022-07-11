#
# spec file for package mingw64-cross-binutils
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


Name:           mingw64-cross-binutils
Version:        2.38
Release:        0
Summary:        GNU Binutils
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries
URL:            http://www.gnu.org/software/binutils/
Source:         http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.xz
#!BuildIgnore: post-build-checks
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  mingw64-filesystem
BuildRequires:  texinfo
# NB: This must be left in.
Requires:       mingw64-filesystem

%description
The GNU Binutils are a collection of binary tools.
These utilities (like 'as', 'ld', 'strip') understand Windows executables and DLLs.

%prep
%autosetup -p1 -n binutils-%{version}

%build
mkdir -p build
cd build
CFLAGS="%{optflags}" \
../configure \
  --build=%{_build} --host=%{_host} \
  --target=%{_mingw64_target} \
  --verbose --disable-nls \
  --without-included-gettext \
  --disable-win32-registry \
  --disable-werror \
  --with-sysroot=%{_mingw64_sysroot} \
  --prefix=%{_prefix} --bindir=%{_bindir} \
  --includedir=%{_includedir} --libdir=/usr/%{_mingw64_target}/lib \
  --mandir=%{_mandir} --infodir=%{_infodir}

%make_build || make

%install
cd build
%make_install

# These files conflict with ordinary binutils.
rm -rf %{buildroot}%{_infodir}

for i in ar as dlltool ld ld.bfd nm objcopy objdump ranlib readelf strip; do
  rm -f %{buildroot}%{_bindir}/%{_mingw64_target}-$i;
  ln -s %{_prefix}/%{_mingw64_target}/bin/$i %{buildroot}%{_bindir}/%{_mingw64_target}-$i;
done

%files
%{_mandir}/man1/*
%{_bindir}/%{_mingw64_target}-*
%{_prefix}/%{_mingw64_target}/bin
%{_prefix}/%{_mingw64_target}/lib

%changelog
