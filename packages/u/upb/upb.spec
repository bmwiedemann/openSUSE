#
# spec file for package upb
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover 0
%define libname lib%{name}%{sover}
%define src_install_dir /usr/src/%{name}

Name:           upb
Version:        20190910
Release:        0
Summary:        A small protobuf implementation in C
License:        BSD-3-Clause
Url:            https://github.com/protocolbuffers/upb
Source0:        %{name}-%{version}.tar.xz
Source1:        upb-rpmlintrc
# PATCH-FIX-OPENSUSE 0001-cmake-Add-descriptor_upbproto-library-for-shared-lin.patch
Patch0:         0001-cmake-Add-descriptor_upbproto-library-for-shared-lin.patch
# PATCH-FIX-OPENSUSE 0002-cmake-Add-upb_-prefix-to-libraries-which-can-be-shar.patch
Patch1:         0002-cmake-Add-upb_-prefix-to-libraries-which-can-be-shar.patch
# PATCH-FIX-OPENSUSE 0003-cmake-Add-SOVERSION-to-shared-libraries.patch
Patch2:         0003-cmake-Add-SOVERSION-to-shared-libraries.patch
# PATCH-FIX-OPENSUSE 0004-cmake-Add-support-for-installation.patch
Patch3:         0004-cmake-Add-support-for-installation.patch
# PATCH-FIX-OPENSUSE 0005-Do-not-build-tests.patch
Patch4:         0005-Do-not-build-tests.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtest

%description
μpb (often written 'upb') is a small protobuf implementation written in C.

upb generates a C API for creating, parsing, and serializing messages as
declared in .proto files. upb is heavily arena-based: all messages always live
in an arena (note: the arena can live in stack or static memory if desired).

%package -n %{libname}
Summary:        Shared libraries for upb

%description -n %{libname}
μpb (often written 'upb') is a small protobuf implementation written in C.

upb generates a C API for creating, parsing, and serializing messages as
declared in .proto files. upb is heavily arena-based: all messages always live
in an arena (note: the arena can live in stack or static memory if desired).

This package provides shared libraries for upb.

%package devel
Summary:        Development files for upb
Requires:       %{libname} = %{version}

%description devel
μpb (often written 'upb') is a small protobuf implementation written in C.

upb generates a C API for creating, parsing, and serializing messages as
declared in .proto files. upb is heavily arena-based: all messages always live
in an arena (note: the arena can live in stack or static memory if desired).

This package provides development files for upb.

%package source
Summary:        Source code of upb
Requires:       %{libname} = %{version}

%description source
μpb (often written 'upb') is a small protobuf implementation written in C.

upb generates a C API for creating, parsing, and serializing messages as
declared in .proto files. upb is heavily arena-based: all messages always live
in an arena (note: the arena can live in stack or static memory if desired).

This package provides source code of upb.

%prep
%autosetup -p1
sed -i \
    -e "/@bazel_version/d" \
    -e "s|bazel_version|native.bazel_version|" \
    bazel/upb_proto_library.bzl

%build
%cmake 
%cmake_build

%install
%cmake_install
rm -rf build
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libdescriptor_upbproto.so.0
%{_libdir}/libupb.so.0
%{_libdir}/libupb_handlers.so.0
%{_libdir}/libupb_json.so.0
%{_libdir}/libupb_legacy_msg_reflection.so.0
%{_libdir}/libupb_pb.so.0
%{_libdir}/libupb_reflection.so.0

%files devel
%{_includedir}/upb
%{_libdir}/libdescriptor_upbproto.so
%{_libdir}/libupb.so
%{_libdir}/libupb_handlers.so
%{_libdir}/libupb_json.so
%{_libdir}/libupb_legacy_msg_reflection.so
%{_libdir}/libupb_pb.so
%{_libdir}/libupb_reflection.so

%files source
%{src_install_dir}

%changelog

