#
# spec file for package msgpack-c
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


Name:           msgpack-c
Version:        4.0.0
Release:        0
Summary:        Object serialization library for cross-language communication
License:        BSL-1.0
Group:          Development/Libraries/C and C++
URL:            https://msgpack.org
Source:         https://github.com/msgpack/msgpack-c/releases/download/c-%{version}/msgpack-c-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
MessagePack is a binary-based object serialization library. It enables to
exchange structured objects between many languages like JSON.

%package -n libmsgpackc2
Summary:        Object serialization library for cross-language communication
Group:          System/Libraries

%description -n libmsgpackc2
MessagePack is a binary-based object serialization library. It enables to
exchange structured objects between many languages like JSON.

%package devel
Summary:        Development headers for libmsgpack C library
Group:          Development/Libraries/C and C++
Requires:       libmsgpackc2 = %{version}-%{release}
Provides:       libmsgpack-devel = %{version}-%{release}
Provides:       libmsgpackc-devel = %{version}-%{release}
Conflicts:      msgpack-devel < 4

%description devel
MessagePack is a binary-based object serialization library. It enables to
exchange structured objects between many languages like JSON.

This package provides headers and other devel files.

%prep
%autosetup -n msgpack-c-%version

%build
%cmake
%make_jobs

%install
%cmake_install
find %{buildroot} -type f -name "*.a"  -delete -print

# Fix duplicated files.
%fdupes %{buildroot}/%{_includedir}/%{name}

%post -n libmsgpackc2 -p /sbin/ldconfig
%postun -n libmsgpackc2 -p /sbin/ldconfig

%files -n libmsgpackc2
%license COPYING
%{_libdir}/libmsgpackc.so.*

%files devel
%doc NOTICE README.md
%{_libdir}/libmsgpackc.so
%{_libdir}/pkgconfig/msgpack.pc
%{_libdir}/cmake/msgpack
%{_includedir}/msgpack.h
%{_includedir}/msgpack/

%changelog
