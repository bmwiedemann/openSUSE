#
# spec file for package mingw64-zlib
#
# Copyright (c) 2023 SUSE LLC
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


Name:           mingw64-zlib
Version:        1.2.13
Release:        0
Summary:        Zlib compression library
License:        Zlib
Group:          Productivity/Archiving/Compression
URL:            https://www.zlib.net/
Source:         https://www.zlib.net/zlib-%{version}.tar.gz
Source1000:     %{name}-rpmlintrc
Patch0:         zlib-1.2.5-nostrip.patch
Patch1:         zlib-1.2.5-tml.patch
Patch2:         0001-cmake-Fix-pkgconfig-support-on-Windows.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-cross-pkg-config
BuildRequires:  mingw64-filesystem
BuildRequires:  xz
%_mingw64_package_header_debug
BuildArch:      noarch

%description
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

%package -n mingw64-zlib1
Summary:        Zlib compression library
Group:          System/Libraries
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n mingw64-zlib1
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

%package -n mingw64-libz
Summary:        Zlib compression library
Group:          System/Libraries
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n mingw64-libz
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

Compatibility package.

%package devel
Summary:        Zlib compression library (development files)
Group:          Development/Libraries/C and C++
Requires:       mingw64-libz = %{version}

%description devel
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

This subpackage holds the development headers for the library.

%package -n mingw64-libminizip1
Summary:        Zip archive library
Group:          System/Libraries
Obsoletes:      mingw64-minizip < %{version}-%{release}
Provides:       mingw64-minizip = %{version}-%{release}

%description -n  mingw64-libminizip1
Minizip is a library for manipulation with files from .zip archives.

%package -n mingw64-minizip-devel
Summary:        Development files for the minizip library
Group:          Development/Libraries/C and C++
Requires:       mingw64-libminizip1 = %{version}

%description -n mingw64-minizip-devel
This package contains the libraries and header files needed for
developing applications which use minizip.

%_mingw64_debug_package

%prep
%autosetup -p1 -n zlib-%{version}

%build
%_mingw64_cmake . -DINSTALL_PKGCONFIG_DIR=%{_mingw64_libdir}/pkgconfig
%_mingw64_cmake_build CFLAGS=-shared LDFLAGS=-no-undefined

cd contrib/minizip
autoreconf -fi
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw64_cache}
%_mingw64_configure

cp ../../zconf.h.included zconf.h
ln -s build/libz.dll.a ../..
%_mingw64_make CFLAGS=-shared LDFLAGS=-no-undefined

%install
%_mingw64_cmake_install
%make_install -C contrib/minizip
# for compatibility with older packages
ln -sf libz.dll %{buildroot}%{_mingw64_bindir}/zlib1.dll

%files -n mingw64-zlib1
%{_mingw64_bindir}/zlib1.dll

%files -n mingw64-libz
%{_mingw64_bindir}/libz.dll

%files devel
%{_mingw64_includedir}/zconf.h
%{_mingw64_includedir}/zlib.h
%{_mingw64_libdir}/libz.dll.a
%{_mingw64_libdir}/libz.a
%{_mingw64_libdir}/pkgconfig/zlib.pc
%{_mingw64_libdir}/pkgconfig/zlib-static.pc
%{_mingw64_datadir}/man

%files -n mingw64-libminizip1
%{_mingw64_bindir}/libminizip-1.dll

%files -n mingw64-minizip-devel
%{_mingw64_includedir}/minizip/
%{_mingw64_libdir}/libminizip.dll.a
%{_mingw64_libdir}/pkgconfig/minizip.pc

%changelog
