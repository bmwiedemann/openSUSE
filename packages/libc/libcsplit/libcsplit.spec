#
# spec file for package libcsplit
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


Name:           libcsplit
%define lname	libcsplit1
Version:        20220109
Release:        0
Summary:        Library for C split string functions
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libcsplit
Source:         https://github.com/libyal/libcsplit/releases/download/%version/libcsplit-beta-%version.tar.gz
Source2:        https://github.com/libyal/libcsplit/releases/download/%version/libcsplit-beta-%version.tar.gz.asc
Source9:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20201121

%description
A library for C split string functions.

This package is part of the libyal library collection and is used by other libraries in the collection

%package -n %lname
Summary:        Library for C split string functions
Group:          System/Libraries

%description -n %lname
Library for C split string functions.

Part of the libyal family of libraries.

Also see:

    libcdata; generic data functions
    libcdatetime; date and time functions
    libcerror; error functions
    libclocale; locale functions
    libcnotify; notification functions
    libcfile; file functions
    libcpath; path functions
    libcthreads; threads functions

%package devel
Summary:        Development files for libcsplit, a C split string library
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
A library for C split string functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcsplit.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static --enable-wide-character-type
%make_build

%install
%make_install
rm -f "%{buildroot}/%{_libdir}"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%{_libdir}/libcsplit.so.1*

%files devel
%license COPYING*
%{_includedir}/libcsplit*
%{_libdir}/libcsplit.so
%{_libdir}/pkgconfig/libcsplit.pc
%{_mandir}/man3/libcsplit.3*

%changelog
