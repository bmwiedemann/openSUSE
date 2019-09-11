#
# spec file for package openssl-cbs
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
%define libname libopenssl_cbs_lib
%define libnamefull %{libname}%{sover}

Name:           openssl-cbs
Version:        0.12.0
Release:        0
Summary:        Library which provides Crypto ByteString (CBS) functionality for OpenSSL
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/Maistra/openssl-cbs
Source0:        %{name}-%{version}.tar.xz
Source100:      WORKSPACE
Source101:      abseil_strings.BUILD
Source102:      abseil_time.BUILD
Source103:      bsslwrapper.BUILD
BuildRequires:  abseil-cpp-devel
BuildRequires:  bazel
BuildRequires:  bssl_wrapper-devel
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
ExclusiveArch:  aarch64 x86_64

%description
OpenSSL-CBS is a library which provides Crypto ByteString (CBS)
functionality for OpenSSL.

%package -n %{libnamefull}
Summary:        Library which provides Crypto ByteString (CBS) functionality for OpenSSL
Group:          System/Libraries

%description -n %{libnamefull}
OpenSSL-CBS is a library which provides Crypto ByteString (CBS)
functionality for OpenSSL.

%package devel
Summary:        Development files for OpenSSL-CBS
Group:          Development/Libraries/C and C++
Requires:       %{libnamefull} = %{version}

%description devel
OpenSSL-CBS is a library which provides Crypto ByteString (CBS)
functionality for OpenSSL.

This package contains development files for OpenSSL-CBS.

%prep
%setup -q
cp %{SOURCE100} .
cp %{SOURCE101} .
cp %{SOURCE102} .
cp %{SOURCE103} .
sed -i \
    -e 's|//external:abseil_strings|@abseil_strings//:abseil_strings|g' \
    -e 's|//external:abseil_time|@abseil_time//:abseil_time|g' \
    -e 's|//external:bssl_wrapper_lib|@bssl_wrapper_lib//:bssl_wrapper_lib|g' \
    BUILD

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
    --linkopt="-Wl,-soname,%{libname}.so.%{sover}" \
    --spawn_strategy=standalone \
    --strip=never \
    --verbose_failures \
    //...
bazel shutdown

%install
install -D -m755 bazel-bin/%{libname}.so %{buildroot}%{_libdir}/%{libname}.so.%{sover}
install -D -m644 opensslcbs/cbs.h %{buildroot}%{_includedir}/opensslcbs/cbs.h
ln -sf %{libname}.so.%{sover} %{buildroot}%{_libdir}/%{libname}.so

%post -n %{libnamefull} -p /sbin/ldconfig
%postun -n %{libnamefull} -p /sbin/ldconfig

%files -n %{libnamefull}
%doc README.md
%{_libdir}/%{libname}.so.%{sover}

%files devel
%{_includedir}/opensslcbs
%{_includedir}/opensslcbs/cbs.h
%{_libdir}/%{libname}.so

%changelog

