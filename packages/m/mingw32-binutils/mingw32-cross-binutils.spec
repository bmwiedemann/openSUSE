#
# spec file for package mingw32-cross-binutils
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mingw32-cross-binutils
Version:        2.32
Release:        0
Summary:        GNU Binutils
License:        GPL-2.0+ and LGPL-2.1+ and GPL-3.0+ and LGPL-3.0+
Group:          Development/Libraries
Url:            http://www.gnu.org/software/binutils/
Source:         http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
Patch0:         0001-COFF-Check-for-symbols-defined-in-discarded-section.patch
#!BuildIgnore: post-build-checks
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  mingw32-filesystem
BuildRequires:  texinfo
# NB: This must be left in.
Requires:       mingw32-filesystem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The GNU Binutils are a collection of binary tools.
These utilities (like 'as', 'ld', 'strip') understand Windows executables and DLLs.

%prep
%setup -q -n binutils-%{version}
%patch0 -p1

%build
mkdir -p build
cd build
CFLAGS="%{optflags}" \
../configure \
  --build=%{_build} --host=%{_host} \
  --target=%{_mingw32_target} \
  --verbose --disable-nls \
  --without-included-gettext \
  --disable-win32-registry \
  --disable-werror \
  --with-sysroot=%{_mingw32_sysroot} \
  --prefix=%{_prefix} --bindir=%{_bindir} \
  --includedir=%{_includedir} --libdir=%{_libdir} \
  --mandir=%{_mandir} --infodir=%{_infodir}

make %{?_smp_mflags} || make

%install
cd build
make DESTDIR=%{buildroot} install %{?_smp_mflags}

# These files conflict with ordinary binutils.
rm -rf %{buildroot}%{_infodir}

for i in ar as dlltool ld ld.bfd nm objcopy objdump ranlib readelf strip; do
  rm -f %{buildroot}%{_bindir}/%{_mingw32_target}-$i;
  ln -s %{_prefix}/%{_mingw32_target}/bin/$i %{buildroot}%{_bindir}/%{_mingw32_target}-$i;
done

%files
%defattr(-,root,root)
%{_mandir}/man1/*
%{_bindir}/%{_mingw32_target}-*
%{_prefix}/%{_mingw32_target}/bin
%{_prefix}/%{_mingw32_target}/lib/ldscripts

%changelog
