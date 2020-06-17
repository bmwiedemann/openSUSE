#
# spec file for package libvc
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


%define c_lib   libvc0
Name:           libvc
Version:        006
Release:        0
Summary:        Library to read and write vcard files
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/libvc/libvc
Source0:        https://github.com/libvc/libvc/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool

%description
The libvc library is a C library for accessing and manipulating
vCard files.

%package -n %{c_lib}
Summary:        Library to read and write vcard files
Group:          System/Libraries

%description -n %{c_lib}
Library to read and write vcard files.

%package devel
Summary:        Development files for libvc
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description devel
Development files for libvc.

%prep
%setup -q

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.a"  -delete -print
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files -n %{c_lib}
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/libvc.so.*

%files devel
%{_libdir}/libvc.so
%{_includedir}/vc.h
%{_mandir}/man3/vc.3%{?ext_man}

%changelog
