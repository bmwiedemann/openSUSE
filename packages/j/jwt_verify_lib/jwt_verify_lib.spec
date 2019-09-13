#
# spec file for package jwt_verify_lib
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


%define sover 0
%define libname lib%{name}%{sover}
%define maistra_name jwt-verify-lib-openssl
%define maistra_version 20190723

Name:           jwt_verify_lib
Version:        20190708
Release:        0
Summary:        JSON Web Tokens verification library for C++
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/google/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        %{maistra_name}-%{maistra_version}.tar.xz
Source100:      WORKSPACE
Source101:      BUILD
Source200:      abseil_strings.BUILD
Source201:      abseil_time.BUILD
Source202:      bsslwrapper.BUILD
Source203:      googletest.BUILD
Source204:      opensslcbs.BUILD
Source205:      zlib.BUILD
BuildRequires:  abseil-cpp-devel
BuildRequires:  bazel-skylib-source
BuildRequires:  bazel0.19
BuildRequires:  bssl_wrapper-devel
BuildRequires:  gcc-c++
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  openssl-cbs-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-source
BuildRequires:  rapidjson-devel
ExcludeArch:    %ix86

%description
jwt_verify_lib is a library which verifies JSON Web Tokens. It does not provide
any other features like signing or advanced checks.

%package -n %{libname}
Summary:        JSON web token verification library for C++
Group:          System/Libraries

%description -n %{libname}
jwt_verify_lib is a library which verifies JSON Web Tokens. It does not provide
any other features like signing or advanced checks.

This package contains shared library for jwt_verify_lib.

%package devel
Summary:        Development files for jwt_verify_lib
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
jwt_verify_lib is a library which verifies JSON Web Tokens. It does not provide
any other features like signing or advanced checks.

This package contains development files for jwt_verify_lib.

%prep
%setup -q -D -b 1 -n %{maistra_name}-%{maistra_version}

%setup -q
pushd ../%{maistra_name}-%{maistra_version}
./openssl.sh ../%{name}-%{version} SSL
popd
cp %{SOURCE100} .
cp %{SOURCE101} .
cp %{SOURCE200} .
cp %{SOURCE201} .
cp %{SOURCE202} .
cp %{SOURCE203} .
cp %{SOURCE204} .
cp %{SOURCE205} .

%build
# TODO(mrostecki): Create a macro in bazel package.
bazel build \
    -c dbg \
    --color=no \
    %(for opt in %{optflags}; do echo -e "--copt=${opt} \c"; done) \
    --curses=no \
    --distdir=%{_sourcedir} \
    --genrule_strategy=standalone \
    --host_javabase=@local_jdk//:jdk \
    --linkopt="-Wl,-soname,libjwt_verify_lib.so.%{sover}" \
    --spawn_strategy=standalone \
    --strip=never \
    --verbose_failures \
    //...
bazel shutdown

%install
install -D -m755 bazel-bin/libjwt_verify_lib.so %{buildroot}%{_libdir}/libjwt_verify_lib.so.%{sover}
ln -sf libjwt_verify_lib.so.%{sover} %{buildroot}%{_libdir}/libjwt_verify_lib.so
find jwt_verify_lib -type f -execdir install -D -m0644 "{}" "%{buildroot}%{_includedir}/jwt_verify_lib/{}" \;

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libjwt_verify_lib.so.%{sover}

%files devel
%{_includedir}/jwt_verify_lib
%{_includedir}/jwt_verify_lib/check_audience.h
%{_includedir}/jwt_verify_lib/jwks.h
%{_includedir}/jwt_verify_lib/jwt.h
%{_includedir}/jwt_verify_lib/status.h
%{_includedir}/jwt_verify_lib/verify.h
%{_libdir}/libjwt_verify_lib.so

%changelog
