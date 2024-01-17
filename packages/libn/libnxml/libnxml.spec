#
# spec file for package libnxml
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


%define soname 0
Name:           libnxml
Version:        0.18.3
Release:        0
Summary:        XML Parsing Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.autistici.org/bakunin/codes.php
Source:         http://www.autistici.org/bakunin/libnxml/libnxml-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         libnxml-curl_compat.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} == 0 || 0%{?suse_version} >= 1030
BuildRequires:  libcurl-devel
%else
BuildRequires:  curl-devel
%endif

%description
nXML is a C library for parsing, writing and creating XML 1.0 and 1.1 files or
streams. It supports UTF-8, UTF-16BE and UTF-16LE, UCS-4 (1234, 4321, 2143,
2312).

%package -n libnxml%{soname}
Summary:        XML Parsing Library
Group:          System/Libraries

%description -n libnxml%{soname}
nXML is a C library for parsing, writing and creating XML 1.0 and 1.1 files or
streams. It supports UTF-8, UTF-16be and UTF-16le, UCS-4 (1234, 4321, 2143,
2312).

%package -n libnxml-devel
Summary:        XML Parsing Library
Group:          Development/Libraries/C and C++
Requires:       libnxml%{soname} = %{version}-%{release}
%if 0%{?suse_version} == 0 || 0%{?suse_version} >= 1030
Requires:       libcurl-devel
%else
Requires:       curl-devel
%endif

%description -n libnxml-devel
nXML is a C library for parsing, writing and creating XML 1.0 and 1.1 files or
streams. It supports UTF-8, UTF-16be and UTF-16le, UCS-4 (1234, 4321, 2143,
2312).

%prep
%setup -q
%patch1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CPPFLAGS="$CFLAGS"
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libnxml%{soname} -p /sbin/ldconfig
%postun -n libnxml%{soname} -p /sbin/ldconfig

%files -n libnxml%{soname}
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS ChangeLog
%{_libdir}/libnxml.so.%{soname}
%{_libdir}/libnxml.so.%{soname}.*

%files -n libnxml-devel
%defattr(-,root,root)
%{_includedir}/nxml.h
%{_libdir}/libnxml.so
%{_libdir}/pkgconfig/nxml.pc

%changelog
