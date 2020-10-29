#
# spec file for package libgit2
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2011, Sascha Peilicke <saschpe@gmx.de>
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


%define sover 1_1
Name:           libgit2
Version:        1.1.0
Release:        0
Summary:        C git library
License:        GPL-2.0 WITH GCC-exception-2.0
Group:          Development/Libraries/C and C++
URL:            https://libgit2.github.com/
Source0:        https://github.com/libgit2/libgit2/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake >= 2.8
BuildRequires:  http-parser-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package -n %{name}-%{sover}
Summary:        C git library
Group:          System/Libraries

%description -n %{name}-%{sover}
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package devel
Summary:        C git library
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{sover} >= %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libgit2.

%prep
%autosetup -p1
find examples -type f -name ".gitignore" -print -delete

%build
%cmake \
	-DTHREADSAFE:BOOL=ON \
	-DUSE_SSH:BOOL=ON \
	-DUSE_SHA1DC:BOOL=ON \
	%{nil}
%cmake_build

%install
%cmake_install

%post -n %{name}-%{sover} -p /sbin/ldconfig
%postun -n %{name}-%{sover} -p /sbin/ldconfig

%files -n %{name}-%{sover}
%license COPYING
%doc AUTHORS README.md
%{_libdir}/%{name}.so.*

%files devel
%doc examples
%{_libdir}/%{name}.so
%{_includedir}/git2*
%{_libdir}/pkgconfig/libgit2.pc

%changelog
