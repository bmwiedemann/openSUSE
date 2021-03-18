#
# spec file for package mingw64-winpthreads
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


Name:           mingw64-winpthreads
Version:        8.0.0
Release:        0
Summary:        A pthreads implementation for Windows
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/C and C++
URL:            http://mingw-w64.sf.net/
Source:         http://downloads.sf.net/mingw-w64/mingw-w64-v%{version}.tar.bz2
Source9:        %name-rpmlintrc
BuildRequires:  mingw64-cross-gcc-bootstrap
BuildRequires:  mingw64-cross-pkg-config
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-runtime
BuildRequires:  xz
%_mingw64_package_header_debug
BuildArch:      noarch
#!BuildIgnore:  post-build-checks

%description
mingw-w64's implementation of POSIX threads for Windows.

%package -n mingw64-libwinpthread1
Summary:        A pthreads implementation for Windows
Group:          System/Libraries
Obsoletes:      mingw64-winpthreads

%description -n mingw64-libwinpthread1
mingw-w64's implementation of POSIX threads for Windows.

%package devel
Summary:        Development files for mingw64-winpthreads
Group:          Development/Libraries/C and C++
Requires:       mingw64-libwinpthread1 = %version
Provides:       mingw64-unistd-pthread-devel
Obsoletes:      mingw64-headers-dummy-pthread
Conflicts:      mingw64-headers-dummy-pthread
Conflicts:      otherproviders(mingw64-unistd-pthread-devel)

%description devel
mingw-w64's implementation of POSIX threads for Windows.

%_mingw64_debug_package

%prep
%autosetup -p1 -n mingw-w64-v%version/mingw-w64-libraries/winpthreads

%build
# The build is trying to link with libpthread.a but it has no need
# of any symbol from there, so just create a fake library and use it.
mkdir fakelib
pushd fakelib
touch empty.c
%_mingw64_cc -c empty.c
%_mingw64_ar rsc libpthread.a empty.o
popd

# No ssp support in gcc-cross-bootstrap
# Hence we use dedicated LDFLAGS (without -fstack-protector)
%{_mingw64_configure} \
	--enable-static \
	--enable-shared \
    LDFLAGS="%{_mingw64_ldflags_bootstrap}"
%make_build

%install
%make_install

%files -n mingw64-libwinpthread1
%_mingw64_bindir/libwinpthread-1.dll

%files devel
%_mingw64_includedir/
%_mingw64_libdir/

%changelog
