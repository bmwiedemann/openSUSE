#
# spec file for package mingw64-headers
#
# Copyright (c) 2019 SUSE LLC
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


Name:           mingw64-headers
Version:        7.0.0
Release:        0
Summary:        MinGW-w64 headers for Win32 and Win64
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            http://mingw-w64.sf.net/
Source:         http://downloads.sf.net/mingw-w64/mingw-w64-v%{version}.tar.bz2
Source1000:     %name-rpmlintrc
BuildRequires:  mingw64-filesystem
BuildRequires:  xz
#!BuildIgnore:	post-build-checks
Requires:       mingw64-unistd-pthread-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
MinGW-w64 delivers runtime, headers and libs for developing both 64
bit (x64) and 32 bit (x86) windows applications using GCC and other
free software compilers.

This subpackage contains the header files.

%package dummy-pthread
Summary:        Stub pthread header files for MinGW
Group:          Development/Libraries/C and C++
Provides:       mingw64-unistd-pthread-devel

%description dummy-pthread
This subpackage contains stub pthread header files that are empty
and only exist to satisfy dependencies in MinGW's unistd.h until
an actual pthread implementation (like winpthreads) is installed.

%prep
%setup -q -n mingw-w64-v%{version}/mingw-w64-headers

%build
%_mingw64_configure \
	--enable-sdk=all \
	--enable-secure-api
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%_mingw64_includedir/
%exclude %_mingw64_includedir/pthread_*.h

%files dummy-pthread
%defattr(-,root,root)
%dir %_mingw64_includedir
%_mingw64_includedir/pthread_*.h

%changelog
