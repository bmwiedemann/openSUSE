#
# spec file for package davix
#
# Copyright (c) 2020 SUSE LLC
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


%define shlib lib%{name}0
Name:           davix
Version:        0.7.6
Release:        0
Summary:        File management over HTTP-based protocols
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://dmc.web.cern.ch/projects/davix/home
Source:         https://github.com/cern-fts/davix/releases/download/R_0_7_6/davix-%{version}.tar.gz
# PATCH-FIX-UPSTREAM davix-non-void-function.patch badshah400@gmail.com -- Fix non-void function that returns nothing
Patch0:         davix-non-void-function.patch
# PATCH-FIX-UPSTREAM davix-link-against-libdl.patch badshah400@gmail.com -- Link against libdl; patch taken from debian package build
Patch1:         davix-link-against-libdl.patch
BuildRequires:  cmake >= 2.6
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)

%description
Davix does file management over HTTP-based protocols. It focuses on
remote I/O and data management of large collections of files. There
is support for the WebDav, Amazon S3, Microsoft Azure, and HTTP
protocols.

It provides a C++ library offering an HTTP API, a remote I/O API, and
a POSIX compatibility layer. It also provides several utilities for
file transfer, large collections of files management and large files
management.

%package -n %{shlib}
Summary:        Library offering davix APIs for HTTP, remote I/O, and POSIX compatibility layer
Group:          System/Libraries

%description -n %{shlib}
This package provides the shared libraries for davix with APIs for
HTTP, remote I/O, and a POSIX compatibility layer.

%package devel
Summary:        Headers and sources for developing software using davix
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}

%description devel
This package provides the headers and sources needed for developing
applications using davix.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# REMOVE NON-STD DOC FILES, TO BE CORRECTLY INSTALLED USING %%doc macro
rm -fr %{buildroot}%{_datadir}/doc/davix

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files
%doc README.md RELEASE-NOTES.md
%license LICENSE
%{_bindir}/davix-get
%{_bindir}/davix-http
%{_bindir}/davix-ls
%{_bindir}/davix-mkdir
%{_bindir}/davix-mv
%{_bindir}/davix-put
%{_bindir}/davix-rm
%{_bindir}/davix-tester
%{_bindir}/davix-unit-tests
%{_mandir}/man1/davix-*.1%{?ext_man}

%files -n %{shlib}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/libdavix.3%{?ext_man}

%changelog
