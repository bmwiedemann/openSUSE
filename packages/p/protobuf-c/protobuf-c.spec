#
# spec file for package protobuf-c
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2011 Pascal Bleser
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Version:        1.5.1
Release:        0
Summary:        C bindings for Google's Protocol Buffers
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://github.com/protobuf-c/protobuf-c
Source:         https://github.com/protobuf-c/protobuf-c/releases/download/v%version/%name-%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel >= 22

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

%package devel
Summary:        protobuf generator and headers
Group:          Development/Libraries/C and C++
Requires:       libprotobuf-c%sover = %version
Recommends:     (protobuf-devel >= 2.6.0 with protobuf-devel < 22)
Provides:       protobuf-c = %version-%release
Obsoletes:      protobuf-c <= %version-%release
Provides:       libprotobuf-c-devel = %version-%release
Obsoletes:      libprotobuf-c-devel <= %version-%release

%description devel
This package provides a code generator and runtime libraries to use Protocol
Buffers from pure C (not C++).

%prep
%autosetup -p1

%build
%{!?make_build:%define make_build make -O %{?_smp_mflags} V=1 VERBOSE=1}
autoreconf -fvi
%configure \
    --enable-static=no

%make_build

%install
%make_install
rm %buildroot/%_libdir/*.la

%check
make check

%ldconfig_scriptlets -n libprotobuf-c%sover

%files -n libprotobuf-c%sover
%license LICENSE
%_libdir/libprotobuf-c.so.%sover
%_libdir/libprotobuf-c.so.%sover.*

%files devel
%license LICENSE
%dir %_includedir/protobuf-c
%dir %_includedir/google
%dir %_includedir/google/protobuf-c
%_includedir/protobuf-c/*
%_includedir/google/protobuf-c/protobuf-c.h
%_bindir/protoc-c
%_bindir/protoc-gen-c
%_libdir/libprotobuf-c.so
%_libdir/pkgconfig/libprotobuf-c.pc

%changelog
