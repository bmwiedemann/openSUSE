#
# spec file for package mingw32-cross-gcc-bootstrap
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


%if 0%{?suse_version} < 1550
%define cpplibdir /lib
%else
%define cpplibdir %{_prefix}/lib
%endif

Name:           mingw32-cross-gcc-bootstrap
Version:        13.2.0
Release:        0
Summary:        MinGW Windows cross-compiler (GCC) for C
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            http://www.mingw.org/
Source:         ftp://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
Source100:      mingw32-gcc-rpmlintrc
Patch0:         gcc-13.2.0-build-with-fpie.patch
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 4.2.0
BuildRequires:  mingw32-cross-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-headers-dummy-pthread
BuildRequires:  mpc-devel >= 0.8.0
BuildRequires:  mpfr-devel >= 2.4.0
BuildRequires:  texinfo
BuildRequires:  xz
BuildRequires:  zlib-devel
#!BuildIgnore:  gcc-PIE
#!BuildIgnore:  post-build-checks
# NB: Explicit mingw32-filesystem dependency is REQUIRED here.
Requires:       mingw32-cross-binutils
Requires:       mingw32-cross-cpp-bootstrap >= %{version}
Requires:       mingw32-filesystem
Requires:       mingw32-headers
Requires:       mingw32-headers-dummy-pthread

%description
MinGW Windows cross-compiler (GCC) for C

%package -n mingw32-cross-cpp-bootstrap
Summary:        MinGW Windows cross-C Preprocessor
Group:          Development/Languages/C and C++

%description -n mingw32-cross-cpp-bootstrap
MinGW Windows cross-C Preprocessor

%prep
%autosetup -p1 -n gcc-%{version}

%build
mkdir -p build
cd build

languages="c"

CC="gcc %{optflags} -fPIC -fPIE -pie" \
CXX="g++ %{optflags} -fPIC -fPIE -pie" \
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
  --target=%{_mingw32_target} \
  --with-gnu-as --with-gnu-ld --verbose \
  --without-newlib \
  --disable-multilib \
  --enable-default-pie=no \
  --enable-shared \
  --disable-plugin \
  --with-system-zlib \
  --disable-nls --without-included-gettext \
  --disable-win32-registry \
  --enable-version-specific-runtime-libs \
  --with-sysroot=%{_mingw32_sysroot} \
  --enable-languages="$languages" \
  --enable-fully-dynamic-string \
  --enable-vtable-verify \
  --with-pkgversion="SUSE Linux"

make %{?_smp_mflags} all-gcc || make all-gcc

%install
cd build
make DESTDIR=%{buildroot} install-gcc

# These files conflict with existing installed files.
rm -rf %{buildroot}%{_infodir}
rm -f %{buildroot}%{_libdir}/libiberty*
rm -f %{buildroot}%{_mandir}/man7/*
rm -f %{buildroot}%{_bindir}/vxaddr2line

mkdir -p %{buildroot}%{cpplibdir}
ln -sf %{_bindir}/%{_mingw32_target}-cpp \
  %{buildroot}%{cpplibdir}/%{_mingw32_target}-cpp

%files
%{_bindir}/%{_mingw32_target}-gcc*
%{_bindir}/%{_mingw32_target}-gcov*
%{_bindir}/%{_mingw32_target}-lto-dump
%dir %{_libdir}/gcc/%{_mingw32_target}
%dir %{_libdir}/gcc/%{_mingw32_target}/%{version}
%dir %{_libdir}/gcc/%{_mingw32_target}/%{version}/include
%dir %{_libdir}/gcc/%{_mingw32_target}/%{version}/include-fixed
%{_libdir}/gcc/%{_mingw32_target}/%{version}/include-fixed/README
%{_libdir}/gcc/%{_mingw32_target}/%{version}/include/*.h
%dir %{_libdir}/gcc/%{_mingw32_target}/%{version}/install-tools
%{_libdir}/gcc/%{_mingw32_target}/%{version}/install-tools/*
%dir %{_libexecdir}/gcc/%{_mingw32_target}/%{version}/install-tools
%{_libexecdir}/gcc/%{_mingw32_target}/%{version}/install-tools/*
%{_mandir}/man1/%{_mingw32_target}-gcc.1*
%{_mandir}/man1/%{_mingw32_target}-gcov.1*
%{_mandir}/man1/%{_mingw32_target}-gcov-dump.1*
%{_mandir}/man1/%{_mingw32_target}-gcov-tool.1*
%{_mandir}/man1/%{_mingw32_target}-lto-dump.1*
%{_libexecdir}/gcc/%{_mingw32_target}/%{version}/collect2
%{_libexecdir}/gcc/%{_mingw32_target}/%{version}/lto-wrapper
%{_libexecdir}/gcc/%{_mingw32_target}/%{version}/lto1
%{_libexecdir}/gcc/%{_mingw32_target}/%{version}/liblto_plugin.so*
%{_libexecdir}/gcc/%{_mingw32_target}/%{version}/liblto_plugin.la

%files -n mingw32-cross-cpp-bootstrap
%{cpplibdir}/%{_mingw32_target}-cpp
%{_bindir}/%{_mingw32_target}-cpp
%{_mandir}/man1/%{_mingw32_target}-cpp.1*
%dir %{_libdir}/gcc/%{_mingw32_target}
%dir %{_libdir}/gcc/%{_mingw32_target}/%{version}
%{_libexecdir}/gcc/%{_mingw32_target}/%{version}/cc1

%changelog
