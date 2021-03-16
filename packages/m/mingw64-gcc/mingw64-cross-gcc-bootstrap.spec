#
# spec file for package mingw64-cross-gcc-bootstrap
#
# Copyright (c) 2021 SUSE LLC
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


%define __os_install_post %{_prefix}/lib/rpm/brp-compress %{nil}
Name:           mingw64-cross-gcc-bootstrap
Version:        9.2.0
Release:        0
Summary:        MinGW Windows cross-compiler (GCC) for C
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            http://www.mingw.org/
Source:         ftp://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 4.2.0
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-headers-dummy-pthread
BuildRequires:  mpc-devel >= 0.8.0
BuildRequires:  mpfr-devel >= 2.4.0
BuildRequires:  texinfo
BuildRequires:  xz
BuildRequires:  zlib-devel
#!BuildIgnore:  gcc-PIE
#!BuildIgnore:  post-build-checks
# NB: Explicit mingw64-filesystem dependency is REQUIRED here.
Requires:       mingw64-cross-binutils
Requires:       mingw64-cross-cpp-bootstrap >= %{version}
Requires:       mingw64-filesystem
Requires:       mingw64-headers
Requires:       mingw64-headers-dummy-pthread

%description
MinGW Windows cross-compiler (GCC) for C

%package -n mingw64-cross-cpp-bootstrap
Summary:        MinGW Windows cross-C Preprocessor
Group:          Development/Languages/C and C++

%description -n mingw64-cross-cpp-bootstrap
MinGW Windows cross-C Preprocessor

%prep
%setup -q -c

%build
cd gcc-%{version}

mkdir -p build
cd build

languages="c"

CC="gcc %{optflags}" \
../configure \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --datadir=%{_datadir} \
  --build=%{_build} --host=%{_host} \
  --target=%{_mingw64_target} \
  --with-gnu-as --with-gnu-ld --verbose \
  --without-newlib \
  --disable-multilib \
  --enable-shared \
  --disable-plugin \
  --with-system-zlib \
  --disable-nls --without-included-gettext \
  --disable-win32-registry \
  --enable-version-specific-runtime-libs \
  --with-sysroot=%{_mingw64_sysroot} \
  --enable-languages="$languages" \
  --enable-fully-dynamic-string \
  --enable-vtable-verify \
  --with-pkgversion="SUSE Linux"

make %{?_smp_mflags} all-gcc || make all-gcc

%install
cd gcc-%{version}
cd build
make DESTDIR=%{buildroot} install-gcc

# These files conflict with existing installed files.
rm -rf %{buildroot}%{_infodir}
rm -f %{buildroot}%{_libdir}/libiberty*
rm -f %{buildroot}%{_mandir}/man7/*
rm -f %{buildroot}%{_bindir}/vxaddr2line

mkdir -p %{buildroot}/lib
ln -sf ..%{_bindir}/%{_mingw64_target}-cpp \
  %{buildroot}/lib/%{_mingw64_target}-cpp

%files
%{_bindir}/%{_mingw64_target}-gcc*
%{_bindir}/%{_mingw64_target}-gcov*
%dir %{_libdir}/gcc/%{_mingw64_target}
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}/include
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}/include-fixed
%{_libdir}/gcc/%{_mingw64_target}/%{version}/include-fixed/README
%{_libdir}/gcc/%{_mingw64_target}/%{version}/include-fixed/*.h
%{_libdir}/gcc/%{_mingw64_target}/%{version}/include/*.h
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}/install-tools
%{_libdir}/gcc/%{_mingw64_target}/%{version}/install-tools/*
%dir %{_libexecdir}/gcc/%{_mingw64_target}/%{version}/install-tools
%{_libexecdir}/gcc/%{_mingw64_target}/%{version}/install-tools/*
%{_mandir}/man1/%{_mingw64_target}-gcc.1*
%{_mandir}/man1/%{_mingw64_target}-gcov.1*
%{_mandir}/man1/%{_mingw64_target}-gcov-dump.1*
%{_mandir}/man1/%{_mingw64_target}-gcov-tool.1*
%{_libexecdir}/gcc/%{_mingw64_target}/%{version}/collect2
%{_libexecdir}/gcc/%{_mingw64_target}/%{version}/lto-wrapper
%{_libexecdir}/gcc/%{_mingw64_target}/%{version}/lto1
%{_libexecdir}/gcc/%{_mingw64_target}/%{version}/liblto_plugin.so*
%{_libexecdir}/gcc/%{_mingw64_target}/%{version}/liblto_plugin.la

%files -n mingw64-cross-cpp-bootstrap
/lib/%{_mingw64_target}-cpp
%{_bindir}/%{_mingw64_target}-cpp
%{_mandir}/man1/%{_mingw64_target}-cpp.1*
%dir %{_libdir}/gcc/%{_mingw64_target}
%dir %{_libdir}/gcc/%{_mingw64_target}/%{version}
%{_libexecdir}/gcc/%{_mingw64_target}/%{version}/cc1

%changelog
