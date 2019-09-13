#
# spec file for package libmrss
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname	libmrss0
Name:           libmrss
Version:        0.19.2
Release:        0
Summary:        RSS Parsing Library
License:        LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            http://www.autistici.org/bakunin/codes.php
Source:         http://www.autistici.org/bakunin/libmrss/libmrss-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         libmrss-curl_compat.patch
BuildRequires:  curl-devel
BuildRequires:  libnxml-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libmRSS is a C library for parsing, writing, and creating RSS (Rich Site
Summary, Really Simple Syndication, and RDF Site Summary) and ATOM files or
streams. The formats supported are: RSS 0.91, RSS 0.92, RSS 1.0, RSS 2.0, ATOM
0.3, and ATOM 1.0.

%package -n %{lname}
Summary:        RSS Parsing Library
Group:          System/Libraries

%description -n %{lname}
libmRSS is a C library for parsing, writing, and creating RSS (Rich Site
Summary, Really Simple Syndication, and RDF Site Summary) and ATOM files or
streams. The formats supported are: RSS 0.91, RSS 0.92, RSS 1.0, RSS 2.0, ATOM
0.3, and ATOM 1.0.

%package devel
Summary:        Headers and development package for libmrss
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       curl-devel
Requires:       libnxml-devel

%description devel
libmRSS is a C library for parsing, writing, and creating RSS (Rich Site
Summary, Really Simple Syndication, and RDF Site Summary) and ATOM files or
streams. The formats supported are: RSS 0.91, RSS 0.92, RSS 1.0, RSS 2.0, ATOM
0.3, and ATOM 1.0.

%prep
%setup -q
%patch1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%{_libdir}/libmrss.so.*
%doc COPYING

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/mrss.pc
%{_libdir}/libmrss.so
%{_includedir}/mrss.h

%changelog
