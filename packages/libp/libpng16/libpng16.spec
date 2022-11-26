#
# spec file for package libpng16
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


%define debug_build 0
%define asan_build  0
%define major   1
%define minor   6
%define micro   39
%define branch  %{major}%{minor}
%define libname libpng%{branch}-%{branch}
%define debug_package_requires %{libname} = %{version}-%{release}
Name:           libpng16
Version:        %{major}.%{minor}.%{micro}
Release:        0
Summary:        Library for the Portable Network Graphics Format (PNG)
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            http://www.libpng.org/pub/png/libpng.html
Source0:        https://prdownloads.sourceforge.net/libpng/libpng-%{version}.tar.xz
Source2:        libpng16.keyring
Source3:        rpm-macros.libpng-tools
Source4:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%package -n %{libname}
Summary:        Library for the Portable Network Graphics Format (PNG)
Group:          System/Libraries
Provides:       libpng = %{version}

%package devel
Summary:        Development tools for applications which will use libpng
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel
Requires:       pkgconfig
Requires:       zlib-devel
Recommends:     libpng%{branch}-compat-devel
#

%package compat-devel
Summary:        Development tools for applications which will use libpng
Group:          Development/Libraries/C and C++
Requires:       libpng%{branch}-devel = %{version}
Conflicts:      libpng-devel
Provides:       libpng-devel = %{version}
Obsoletes:      libpng-devel < 1.2.44

%package tools
Summary:        Tools for Manipulating PNG Images
Group:          Productivity/Graphics/Other
Conflicts:      libpng-tools
Provides:       libpng-tools = %{version}

%description
libpng is the official reference library for the Portable Network
Graphics format (PNG).

%description -n %{libname}
libpng is the official reference library for the Portable Network
Graphics format (PNG).

%description devel
The libpng%{branch}-devel package includes the header files, libraries,
configuration files and development tools necessary for compiling and
linking programs which will manipulate PNG files using libpng%{branch}.

libpng is the official reference library for the Portable Network
Graphics (PNG) format.

%description compat-devel
The libpng%{branch}-compat-devel package contains unversioned symlinks
to the header files, libraries, configuration files and development
tools necessary for compiling and linking programs that don't care
about libpng version.

%description tools
Package consists of low level tools for manipulating and fixing particular
PNG files.

%prep
%setup -q -n libpng-%{version}

%build
# PNG_SAFE_LIMITS_SUPPORTED: http://www.openwall.com/lists/oss-security/2015/01/10/1
export CFLAGS="%{optflags} -O3 -DPNG_SAFE_LIMITS_SUPPORTED -DPNG_SKIP_SETJMP_CHECK $(getconf LFS_CFLAGS)"
export LDFLAGS="-Wl,-z,relro,-z,now"
%if %{debug_build}
export CFLAGS="$CFLAGS -Og"
%endif
%configure \
              --disable-static --enable-hardware-optimizations=yes
%if %{asan_build}
sed -i -e 's/^\(CFLAGS.*\)$/\1 -fsanitize=address/' \
       -e 's/\(^LIBS =.*\)/\1 -lasan/' Makefile
%endif
%make_build

%check
%make_build -j1 check

%install
%make_install
rm %{buildroot}/%{_libdir}/libpng*.la
mkdir -p %{buildroot}%{_sysconfdir}/rpm
install -D -m644 %{SOURCE3} %{buildroot}%{_rpmmacrodir}/macros.libpng-tools
%if %{debug_build} ||%{asan_build}
install -m755 .libs/pngcp %{buildroot}/%{_bindir}
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libpng%{branch}.so.*

%files devel
%{_bindir}/libpng%{branch}-config
%{_includedir}/libpng%{branch}
%{_libdir}/libpng%{branch}.so
%{_libdir}/pkgconfig/libpng%{branch}.pc
%license LICENSE
%doc CHANGES README TODO ANNOUNCE libpng-*.txt

%files compat-devel
%{_bindir}/libpng-config
%{_includedir}/*.h
%{_libdir}/libpng.so
%{_libdir}/pkgconfig/libpng.pc
%{_mandir}/man3/libpng.3%{?ext_man}
%{_mandir}/man3/libpngpf.3%{?ext_man}
%{_mandir}/man5/png.5%{?ext_man}

%files tools
%{_bindir}/png-fix-itxt
%{_bindir}/pngfix
%if %{debug_build} || %{asan_build}
%{_bindir}/pngcp
%endif
%{_rpmmacrodir}/macros.libpng-tools

%changelog
