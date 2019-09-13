#
# spec file for package libnsl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define debug_package_requires libnsl2 = %{version}-%{release}
Name:           libnsl
Version:        1.2.0
Release:        0
Summary:        Network Support Library (NIS/NIS+)
License:        LGPL-2.1-only
Group:          System/Libraries
Url:            http://github.com/thkukuk/libnsl
Source:         %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkg-config
%if 0%{?suse_version} >= 1310
BuildRequires:  libtirpc-devel >= 1.0
%endif

%description
The Network Support Library for NIS/NIS+ was formerly part of glibc and
is now a standalone library. The big difference is, that this library
has support for IPv6.
The NIS+ code is deprecated and only there "as is".

%package -n libnsl2
Summary:        Network Support Library (NIS/NIS+)
Group:          System/Libraries

%description -n libnsl2
The Network Support Library for NIS/NIS+ was formerly part of glibc and
is now a standalone library. The big difference is, that this library
has support for IPv6.
The NIS+ code is deprecated and only there "as is".

%package devel
Summary:        Development package for Network Support Library (NIS/NIS+)
Group:          Development/Libraries/C and C++
Requires:       libnsl2 = %{version}
Requires:       pkgconfig(libtirpc) >= 1.0.1

%description devel
The Network Support Library for NIS/NIS+ was formerly part of glibc and
is now a standalone library. The big difference is, that this library
has support for IPv6.
This package contains all files to develop and link against libnsl.
The NIS+ API is deprecated and only there "as is".

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
# Don't strip .symtab to allow debugging
export STRIP_KEEP_SYMTAB=libnsl*.so*
%make_install
# Remove .la file
rm %{buildroot}%{_libdir}/%{name}.la

%check
make %{?_smp_mflags} check

%post -n libnsl2 -p /sbin/ldconfig
%postun -n libnsl2 -p /sbin/ldconfig

%files -n libnsl2
%license COPYING
%{_libdir}/libnsl.so.2*

%files devel
%{_libdir}/libnsl.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
