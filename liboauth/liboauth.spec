#
# spec file for package liboauth
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


Name:           liboauth
Version:        1.0.3
Release:        1
License:        MIT
Summary:        OAuth library
Url:            http://liboauth.sourceforge.net/
Group:          Development/Libraries/C and C++
BuildRequires:  pkg-config
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://sourceforge.net/projects/liboauth/files/liboauth-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         liboauth-openssl_1.1_compatibility.patch

%description
liboauth is a collection of c functions implementing the http://oauth.net API.

liboauth provides functions to escape and encode stings according to
OAuth specifications and offers high-level functionality built on top to sign
requests or verify signatures using either NSS or OpenSSL for calculating
the hash/signatures.

%define libname liboauth0
%package -n %{libname}
Group:          System/Libraries
Summary:        Shared library from liboauth
%description -n %{libname}
liboauth is a collection of c functions implementing the http://oauth.net API.

liboauth provides functions to escape and encode stings according to
OAuth specifications and offers high-level functionality built on top to sign
requests or verify signatures using either NSS or OpenSSL for calculating
the hash/signatures.

This archive contains the shared library files from liboauth.

%package devel
Summary:        Development and Include Files for liboauth
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       %{libname} = %{version}
%description devel
liboauth is a collection of c functions implementing the http://oauth.net API.

liboauth provides functions to escape and encode stings according to
OAuth specifications and offers high-level functionality built on top to sign
requests or verify signatures using either NSS or OpenSSL for calculating
the hash/signatures.

This archive contains the header files for liboauth development.

%prep
%setup -q
%patch0 -p1

%build
sed -i -e '/^Libs.private/d' -e '/^Requires.private/d' oauth.pc.in
autoreconf --force --install
%configure --disable-static --with-pic
make %{?_smp_flags} all

%install
make install DESTDIR=%{buildroot}
# empty dependency libs
rm -f %{buildroot}%{_libdir}/liboauth.la

%post   -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING* README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/oauth.pc
%{_mandir}/man*/*

%changelog
