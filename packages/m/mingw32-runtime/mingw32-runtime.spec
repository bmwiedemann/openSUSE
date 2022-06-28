#
# spec file for package mingw32-runtime
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


Name:           mingw32-runtime
Version:        10.0.0
Release:        0
Summary:        MinGW-w64 runtime libraries for Win32
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            http://mingw-w64.sf.net/
Source:         http://downloads.sf.net/mingw-w64/mingw-w64-v%version.tar.bz2
Source100:      %name-rpmlintrc
BuildRequires:  mingw32-cross-binutils
BuildRequires:  mingw32-cross-gcc-bootstrap >= 4.4.0
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-headers >= %version
BuildRequires:  xz
#!BuildIgnore:  post-build-checks
# When building the CRT, any newer (>=) headers should be ok, since the CRT
# won't make use of them. At runtime, ensure that headers are not too new (<=)
# because ominous link failures can result -- let OBS go into unresolvable
# state instead.
Requires:       mingw32-headers <= %version
# Once this is installed, mingw32-bootstrap (binary bootstrapper) is no
# longer needed.
Obsoletes:      mingw32-runtime-bootstrap
BuildArch:      noarch
%_mingw32_package_header

%description
MinGW Win64 cross-compiler runtime, base libraries.

%prep
%autosetup -n mingw-w64-v%version/mingw-w64-crt

%build
%_mingw32_configure --enable-lib32 --disable-lib64
%make_build

%install
%make_install
rm -Rfv "%buildroot/%_mingw32_includedir"/*.c

%files
%_mingw32_libdir/

%changelog
