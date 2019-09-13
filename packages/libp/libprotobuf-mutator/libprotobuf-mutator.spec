#
# spec file for package libprotobuf-mutator
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


Name:           libprotobuf-mutator
Version:        20181127
Release:        0
Summary:        A library to randomly mutate protobuffers
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/google/libprotobuf-mutator
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  protobuf-devel

%description
Libprotobuf-mutator is a library to randomly mutate protobuffers. 

%package -n libprotobuf-mutator0
Summary:        Shared library for libprotobuf-mutator
Group:          System/Libraries

%description -n libprotobuf-mutator0
Shared library for libprotobuf-mutator - a library to randomly mutate
protobuffers.

%package devel
Summary:        Development files for libprotobuf-mutator
Group:          Development/Libraries/C and C++

%description devel
Development files for libprotobuf-mutator - a library to randomly mutate
protobuffers.

%prep
%setup -q

%build
%cmake \
    -DLIB_DIR=lib64 \
    -DLIB_PROTO_MUTATOR_TESTING=OFF \
    -DPKG_CONFIG_PATH=%{_libdir}/pkgconfig
%make_jobs

%install
%cmake_install

%post -n libprotobuf-mutator0 -p /sbin/ldconfig
%postun -n libprotobuf-mutator0 -p /sbin/ldconfig

%files -n libprotobuf-mutator0
%license LICENSE
%doc README.md
%{_libdir}/libprotobuf-mutator-libfuzzer.so.0
%{_libdir}/libprotobuf-mutator.so.0

%files devel
%{_includedir}/libprotobuf-mutator
%{_libdir}/libprotobuf-mutator-libfuzzer.so
%{_libdir}/libprotobuf-mutator.so
%{_libdir}/pkgconfig/libprotobuf-mutator.pc

%changelog

