#
# spec file for package libgadu
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname 3
Name:           libgadu
Version:        1.12.2
Release:        0
Summary:        Library for Handling of Gadu-Gadu Instant Messaging
License:        LGPL-2.1-or-later
Group:          System/Libraries
Url:            http://toxygen.net/libgadu/
Source:         http://github.com/wojtekka/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ca-certificates
BuildRequires:  doxygen
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(zlib)
# these packages are necessary for tests, but not necessary for a library:
# libexpat-devel, pkgconfig(libcurl), pkgconfig(libxml-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libgadu is a library for handling of protocol of a popular Polish
instant messenger Gadu-Gadu.

%package -n %{name}%{soname}
Summary:        Library for Handling of Gadu-Gadu Instant Messaging
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{name}%{soname}
libgadu is a library for handling of protocol of a popular Polish
instant messenger Gadu-Gadu.

%package devel
Summary:        Library for Handling of Gadu-Gadu Instant Messaging
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}
Requires:       glibc-devel

%description devel
libgadu is a library for handling of protocol of a popular Polish
instant messenger Gadu-Gadu.

%prep
%setup -q

%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
# remove installdox from html dir
rm -f docs/html/installdox
#
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{soname} -p /sbin/ldconfig

%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc docs/html
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
