#
# spec file for package bssl_wrapper
#
# Copyright (c) 2021 SUSE LLC
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
%define libname lib%{name}_lib%{sover}

Name:           bssl_wrapper
Version:        2.0.1
Release:        0
Summary:        Library which translates BoringSSL calls to OpenSSL calls
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/Maistra/%{name}
Source:         %{name}-%{version}.tar.xz
BuildRequires:  bazel
BuildRequires:  bazel-rules-cc-source
BuildRequires:  bazel-rules-java-source
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
ExclusiveArch:  aarch64 x86_64 ppc64le

%description
bssl_wrapper is a library which translates BoringSSL calls to OpenSSL calls.

%package -n %{libname}
Summary:        Library which translates BoringSSL calls to OpenSSL calls
Group:          System/Libraries

%description -n %{libname}
bssl_wrapper is a library which translates BoringSSL calls to OpenSSL calls.

%package devel
Summary:        Development files for bssl_wrapper
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
bssl_wrapper is a library which translates BoringSSL calls to OpenSSL calls.

This package contains development files for bssl_wrapper.

%prep
%setup -q

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
    --linkopt="-Wl,-soname,lib%{name}_lib.so.%{sover}" \
    --override_repository="rules_cc=/usr/src/bazel-rules-cc" \
    --override_repository="rules_java=/usr/src/bazel-rules-java" \
    --spawn_strategy=standalone \
    --strip=never \
    --verbose_failures \
    //...
bazel shutdown

%install
install -D -m755 bazel-bin/lib%{name}_lib.so %{buildroot}%{_libdir}/lib%{name}_lib.so.%{sover}
install -D -m644 %{name}/%{name}.h %{buildroot}%{_includedir}/%{name}/%{name}.h
ln -sf libbssl_wrapper_lib.so.%{sover} %{buildroot}%{_libdir}/libbssl_wrapper_lib.so

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig 

%files -n %{libname}
%doc README.md
%{_libdir}/lib%{name}_lib.so.%{sover}

%files devel
%{_includedir}/%{name}
%{_includedir}/%{name}/%{name}.h
%{_libdir}/lib%{name}_lib.so

%changelog
