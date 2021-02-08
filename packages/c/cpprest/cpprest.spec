#
# spec file for package cpprest
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


%define major 2
%define minor 10
Name:           cpprest
Version:        2.10.18
Release:        0
Summary:        C++ REST library
# main: MIT (license.txt)
# Websocket++: BSD-3-Clause (ThirdPartyNotices.txt)
# base64/base64.hpp: Zlib (ThirdPartyNotices.txt)
# sha1/sha1.hpp: BSD-3-Clause (ThirdPartyNotices.txt)
# common/md5.hpp: Zlib (ThirdPartyNotices.txt)
# utf8_validation.hpp: MIT (ThirdPartyNotices.txt)
License:        MIT AND BSD-3-Clause AND Zlib
URL:            https://github.com/Microsoft/cpprestsdk
Source:         https://github.com/Microsoft/cpprestsdk/archive/%{version}/cpprestsdk-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://github.com/Microsoft/cpprestsdk/issues/576
Patch1:         cpprest-2.10.9-disable-test-extract_floating_point.patch
# PATCH-FIX-UPSTREAM -- https://github.com/microsoft/cpprestsdk/pull/1557
Patch2:         base64.patch
# PATCH-FIX-UPSTREAM -- https://github.com/microsoft/cpprestsdk/pull/1558
Patch3:         filestream.patch
BuildRequires:  cmake >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_random-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssl) >= 1.0
BuildRequires:  pkgconfig(websocketpp) >= 0.8
BuildRequires:  pkgconfig(zlib)

%description
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

Also known as Casablanca.

%package -n libcpprest%{major}_%{minor}
Summary:        C++ Rest library

%description -n libcpprest%{major}_%{minor}
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

%package devel
Summary:        Development files for %{name}
Requires:       libcpprest%{major}_%{minor} = %{version}

%description devel
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

Development files.

%prep
%setup -q -n cpprestsdk-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DWERROR=OFF
%cmake_build

%install
%cmake_install

# create a pkgconfig file
install -d %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: cloud-based client-server communication
URL: %{url}
Version: %{version}
Libs: -L%{_libdir} -lcpprest
Cflags: -I%{_includedir}/cpprest -I%{_includedir}/pplx
EOF

%check
# Tweak library path so that libccprest + libunittestpp are found
export LD_LIBRARY_PATH="$PWD/build/Release/Binaries"
# websocketsclient_test -> authentication_tests - online tests
# httpclient_test -> follows_retrieval_redirect - online test
%ctest --exclude-regex '(httpclient_test|websocketsclient_test)'

%post -n libcpprest%{major}_%{minor} -p /sbin/ldconfig
%postun -n libcpprest%{major}_%{minor} -p /sbin/ldconfig

%files -n libcpprest%{major}_%{minor}
%license license.txt ThirdPartyNotices.txt
%doc CONTRIBUTORS.txt ThirdPartyNotices.txt
%{_libdir}/libcpprest.so.%{major}.%{minor}

%files devel
%license license.txt ThirdPartyNotices.txt
%doc CONTRIBUTORS.txt
%{_includedir}/%{name}
%{_includedir}/pplx
%{_libdir}/libcpprest.so
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
