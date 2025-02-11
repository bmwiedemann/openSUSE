#
# spec file for package mingw64-runtime
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


Name:           mingw64-runtime
Version:        12.0.0
Release:        0
Summary:        MinGW-w64 runtime libraries for Win64
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            http://mingw-w64.sf.net/
Source:         http://downloads.sf.net/mingw-w64/mingw-w64-v%version.tar.bz2
Source100:      %name-rpmlintrc
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-cross-gcc-bootstrap >= 4.4.0
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-headers >= %version
BuildRequires:  xz
#!BuildIgnore:  post-build-checks
# When building the CRT, any newer (>=) headers should be ok, since the CRT
# won't make use of them. At runtime, ensure that headers are not too new (<=)
# because ominous link failures can result -- let OBS go into unresolvable
# state instead.
Requires:       mingw64-headers <= %version
# Once this is installed, mingw64-bootstrap (binary bootstrapper) is no
# longer needed.
Obsoletes:      mingw64-runtime-bootstrap
BuildArch:      noarch
%_mingw64_package_header_debug

%description
MinGW Win64 cross-compiler runtime, base libraries.

%prep
%autosetup -n mingw-w64-v%version/mingw-w64-crt

%build
%_mingw64_configure --disable-lib32 --enable-lib64 \
	--with-default-msvcrt=msvcrt
%make_build

%install
%make_install
rm -Rfv "%buildroot/%_mingw64_includedir"/*.c

%files
%_mingw64_libdir/

%changelog
