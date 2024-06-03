#
# spec file for package mingw32-cross-binutils
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

Name:           mingw32-cross-binutils
Version:        2.39
Release:        0
Summary:        GNU Binutils
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries
URL:            http://www.gnu.org/software/binutils/
Source:         http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.xz
Patch0:         0001-PR29362-some-binutils-memory-leaks.patch
Patch1:         0001-Fix-bug-not-showing-correct-path-with-objdump-WL-wit.patch
Patch2:         0001-dllwrap-windres-and-dlltools-use-mktemp-which-should.patch
Patch3:         reproducible.patch
Patch4:         binutils-2.39-option-high-entry-va.patch
#!BuildIgnore:  post-build-checks
#!BuildIgnore:  mingw32-cross-binutils-utils
#!BuildIgnore:  mingw32-cross-pkgconf-utils
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  mingw32-filesystem
BuildRequires:  texinfo
Requires:       mingw32-cross-binutils-utils
# NB: This must be left in.
Requires:       mingw32-filesystem

%description
The GNU Binutils are a collection of binary tools.
These utilities (like 'as', 'ld', 'strip') understand Windows executables and DLLs.

%package -n mingw32-cross-binutils-utils
Summary:        Utilities for packaging support

%description -n mingw32-cross-binutils-utils
Utilities (like strip and objdump) which are needed for generating package

%prep
%autosetup -p1 -n binutils-%{version}

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
  --includedir=%{_includedir} --libdir=/usr/%{_mingw32_target}/lib \
  --mandir=%{_mandir} --infodir=%{_infodir}

%make_build || make

%install
cd build
%make_install

# These files conflict with ordinary binutils.
rm -rf %{buildroot}%{_infodir}

for i in ar as dlltool ld ld.bfd nm objcopy objdump ranlib readelf strip; do
  rm -f %{buildroot}%{_bindir}/%{_mingw32_target}-$i;
  ln -s %{_prefix}/%{_mingw32_target}/bin/$i %{buildroot}%{_bindir}/%{_mingw32_target}-$i;
done

%files
%{_mandir}/man1/*
%exclude %{_mandir}/man1/%{_mingw32_target}-nm.1.gz
%exclude %{_mandir}/man1/%{_mingw32_target}-objcopy.1.gz
%exclude %{_mandir}/man1/%{_mingw32_target}-objdump.1.gz
%exclude %{_mandir}/man1/%{_mingw32_target}-strip.1.gz
%{_bindir}/%{_mingw32_target}-*
%exclude %{_bindir}/%{_mingw32_target}-nm
%exclude %{_bindir}/%{_mingw32_target}-objcopy
%exclude %{_bindir}/%{_mingw32_target}-objdump
%exclude %{_bindir}/%{_mingw32_target}-strip
%{_prefix}/%{_mingw32_target}/bin
%exclude %{_prefix}/%{_mingw32_target}/bin/nm
%exclude %{_prefix}/%{_mingw32_target}/bin/objcopy
%exclude %{_prefix}/%{_mingw32_target}/bin/objdump
%exclude %{_prefix}/%{_mingw32_target}/bin/strip
%{_prefix}/%{_mingw32_target}/lib

%files -n mingw32-cross-binutils-utils
%{_mandir}/man1/%{_mingw32_target}-nm.1.gz
%{_mandir}/man1/%{_mingw32_target}-objcopy.1.gz
%{_mandir}/man1/%{_mingw32_target}-objdump.1.gz
%{_mandir}/man1/%{_mingw32_target}-strip.1.gz
%{_bindir}/%{_mingw32_target}-nm
%{_bindir}/%{_mingw32_target}-objcopy
%{_bindir}/%{_mingw32_target}-objdump
%{_bindir}/%{_mingw32_target}-strip
%{_prefix}/%{_mingw32_target}/bin/nm
%{_prefix}/%{_mingw32_target}/bin/objcopy
%{_prefix}/%{_mingw32_target}/bin/objdump
%{_prefix}/%{_mingw32_target}/bin/strip

%changelog
