#
# spec file for package libbinio
#
# Copyright (c) 2023 SUSE LLC
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


%define sover 1
%define libname libbinio%{sover}
Name:           libbinio
Version:        1.5
Release:        0
Summary:        Binary I/O Stream Class Library
License:        LGPL-2.1-only
Group:          System/Libraries
#Git-Clone:     https://github.com/adplug/libbinio.git
URL:            https://adplug.github.io/libbinio/
Source:         https://github.com/adplug/libbinio/archive/refs/tags/libbinio-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  makeinfo

%description
The binary I/O stream class library presents a platform-independent way to
access binary data streams in C++. It transparently converts between
machine-internal binary data representation and can be used on arbitrary
binary data sources.

%package -n %{libname}
Summary:        Binary I/O Stream Class Library
Group:          System/Libraries

%description -n %{libname}
The binary I/O stream class library presents a platform-independent way to
access binary data streams in C++. It transparently converts between
machine-internal binary data representation and can be used on arbitrary
binary data sources.

%package -n libbinio-devel
Summary:        Development files for libbinio
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}

%description -n libbinio-devel
The binary I/O stream class library presents a platform-independent way to
access binary data streams in C++. It transparently converts between
machine-internal binary data representation and can be used on arbitrary
binary data sources.

This subpackage contains libraries and header files for developing
applications that want to make use of libbinio.

%prep
%setup -q -n "libbinio-libbinio-%{version}"

%build
autoreconf -fiv
%configure \
  --enable-maintainer-mode \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc ChangeLog NEWS README
%{_libdir}/libbinio.so.%{sover}*

%files -n libbinio-devel
%{_includedir}/libbinio
%{_libdir}/libbinio.so
%{_libdir}/pkgconfig/libbinio.pc
%{_infodir}/libbinio.info%{?ext_info}

%changelog
