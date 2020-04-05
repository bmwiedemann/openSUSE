#
# spec file for package protobuf-c
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2011 Pascal Bleser
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
Name:           protobuf-c
Version:        1.3.3
Release:        0
Summary:        C bindings for Google's Protocol Buffers
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://github.com/protobuf-c/protobuf-c
Source:         https://github.com/protobuf-c/protobuf-c/releases/download/v%version/%name-%version.tar.gz
Source99:       protobuf-c-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel >= 2.6.0
Requires:       libprotobuf-c-devel = %version

%description
This package provides a code generator and runtime libraries to use Protocol
Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

%package -n libprotobuf-c%sover
Summary:        C bindings for Google's Protocol Buffers
Group:          System/Libraries

%description -n libprotobuf-c%sover
This package provides a code generator and runtime libraries to use Protocol
Buffers from pure C (not C++).

%package -n libprotobuf-c-devel
Summary:        C bindings for Google's Protocol Buffers
Group:          Development/Libraries/C and C++
Requires:       libprotobuf-c%sover = %version

%description -n libprotobuf-c-devel
This package provides a code generator and runtime libraries to use Protocol
Buffers from pure C (not C++).

%prep
%autosetup -p1

%build
%define _lto_cflags %nil
autoreconf -fvi
%configure
make %{?_smp_mflags}

%install
%make_install
rm "%buildroot/%_libdir"/*.a "%buildroot/%_libdir"/*.la

%post   -n libprotobuf-c%sover -p /sbin/ldconfig
%postun -n libprotobuf-c%sover -p /sbin/ldconfig

%files
%doc ChangeLog TODO
%_bindir/protoc-c
%_bindir/protoc-gen-c

%files -n libprotobuf-c%sover
%license LICENSE
%_libdir/libprotobuf-c.so.%sover
%_libdir/libprotobuf-c.so.%sover.*

%files -n libprotobuf-c-devel
%_includedir/*/
%_libdir/libprotobuf-c.so
%_libdir/pkgconfig/libprotobuf-c.pc

%changelog
