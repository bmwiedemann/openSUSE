#
# spec file for package mingw32-zlib
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           mingw32-zlib
Version:        1.2.11
Release:        0
Summary:        Zlib compression library
License:        Zlib
Group:          Productivity/Archiving/Compression
Url:            http://www.zlib.net/
Source:         http://www.zlib.net/zlib-%{version}.tar.xz
Patch0:         zlib-1.2.5-nostrip.patch
Patch1:         zlib-1.2.5-tml.patch
Patch2:         0001-cmake-Fix-pkgconfig-support-on-Windows.patch
#!BuildIgnore: post-build-checks
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  mingw32-cross-binutils
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-cross-pkg-config
BuildRequires:  mingw32-filesystem
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%_mingw32_package_header_debug
BuildArch:      noarch

%description
zlib is designed to be a free, general-purpose, legally unencumbered -- that
is, not covered by any patents -- lossless data-compression library for use on
virtually any computer hardware and operating system.

# deprecated, for compatibility only
%package -n mingw32-zlib1
Summary:        Zlib compression library
Group:          System/Libraries
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n mingw32-zlib1
zlib is designed to be a free, general-purpose, legally unencumbered -- that
is, not covered by any patents -- lossless data-compression library for use on
virtually any computer hardware and operating system.

%package -n mingw32-libz
Summary:        Zlib compression library
Group:          System/Libraries
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n mingw32-libz
zlib is designed to be a free, general-purpose, legally unencumbered -- that
is, not covered by any patents -- lossless data-compression library for use on
virtually any computer hardware and operating system.

%package devel
Summary:        Zlib compression library (development files)
Group:          Development/Libraries/C and C++

%description devel
zlib is designed to be a free, general-purpose, legally unencumbered -- that
is, not covered by any patents -- lossless data-compression library for use on
virtually any computer hardware and operating system.

This package contains all necessary include files and libraries needed to
develop applications that require the provided includes and libraries.

%package -n mingw32-libminizip1
Summary:        Zip archive library
Group:          System/Libraries
Obsoletes:      mingw32-minizip
Provides:       mingw32-minizip

%description -n  mingw32-libminizip1
Minizip manipulates files from a .zip archive.

%package -n mingw32-minizip-devel
Summary:        Development files for the minizip library
Group:          Development/Libraries/C and C++

%description -n mingw32-minizip-devel
This package contains the libraries and header files needed for developing
applications which use minizip.

%_mingw32_debug_package

%prep
%setup -q -n zlib-%{version}

%patch0 -p1 -b .nostrip
%patch1 -p1 -b .tml
%patch2 -p1

%build
%_mingw32_cmake . -DINSTALL_PKGCONFIG_DIR=%{_mingw32_libdir}/pkgconfig
%{_mingw32_make} CFLAGS=-shared LDFLAGS=-no-undefined

cd contrib/minizip
autoreconf -fi
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw32_cache}
MINGW32_CFLAGS="%{_mingw32_cflags} -I/$RPM_BUILD_DIR/%{name}-%{version}-%{release}" \
MINGW32_LDFLAGS="%{_mingw32_ldflags} -L/$RPM_BUILD_DIR/%{name}-%{version}-%{release}" \
%{_mingw32_configure}

%{_mingw32_make} CFLAGS=-shared LDFLAGS=-no-undefined

%install
make DESTDIR=%{buildroot} install
make -C contrib/minizip DESTDIR=%{buildroot} install
cp %{buildroot}%{_mingw32_bindir}/libz.dll %{buildroot}%{_mingw32_bindir}/zlib1.dll

%files -n mingw32-zlib1
%defattr(-,root,root)
%{_mingw32_bindir}/zlib1.dll

%files -n mingw32-libz
%defattr(-,root,root)
%{_mingw32_bindir}/libz.dll

%files devel
%defattr(-,root,root)
%{_mingw32_includedir}/zconf.h
%{_mingw32_includedir}/zlib.h
%{_mingw32_libdir}/libz.dll.a
%{_mingw32_libdir}/libz.a
%{_mingw32_libdir}/pkgconfig/zlib.pc
%{_mingw32_libdir}/pkgconfig/zlib-static.pc
%{_mingw32_datadir}/man

%files -n mingw32-libminizip1
%defattr(-,root,root,-)
%{_mingw32_bindir}/libminizip-1.dll

%files -n mingw32-minizip-devel
%defattr(-,root,root,-)
%{_mingw32_includedir}/minizip/*.h
%{_mingw32_libdir}/libminizip.dll.a
%{_mingw32_libdir}/pkgconfig/minizip.pc

%changelog
