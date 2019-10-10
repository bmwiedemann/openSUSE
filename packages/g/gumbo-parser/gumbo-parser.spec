#
# spec file for package gumbo-parser
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gumbo-parser
%define lname   libgumbo1
Version:        0.10.1
Release:        0
Summary:        Google's HTML5 parser library for C99
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            http://github.com/google/gumbo-parser

#Git-Clone:	git://github.com/google/gumbo-parser
Source:         https://github.com/google/gumbo-parser/archive/v%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf >= 2.65
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented
as a C99 library. It is fully conformant with the HTML5
specification, robust and resilient to bad input, supports source
locations and pointers back to the original text.

%package -n %lname
Summary:        Google's HTML5 parser library
Group:          System/Libraries

%description -n %lname
Gumbo is an implementation of the HTML5 parsing algorithm implemented
as a C99 library. It is fully conformant with the HTML5
specification, robust and resilient to bad input, supports source
locations and pointers back to the original text.

%package -n libgumbo-devel
Summary:        Development files for Google's C99 HTML5 parser
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n libgumbo-devel
Gumbo is an implementation of the HTML5 parsing algorithm implemented
as a C99 library. It is fully conformant with the HTML5
specification, robust and resilient to bad input, supports source
locations and pointers back to the original text.

This subpackage contains libraries and header files for developing
applications that want to make use of gumbo-parser.

%prep
%autosetup

%build
%define _configure ../configure
mkdir -p m4 obj
autoreconf -fi
pushd obj
%configure --includedir="%_includedir/%name" --disable-static
make %{?_smp_mflags}
popd

%install
pushd obj
%make_install docdir="%_defaultdocdir/%name"
popd
find "%buildroot/%_libdir" -type f -name "*.la" -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libgumbo.so.1*
%license COPYING

%files -n libgumbo-devel
%_includedir/%name/
%_libdir/libgumbo.so
%_libdir/pkgconfig/gumbo.pc

%changelog
