#
# spec file for package libtcnative-1-0
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libtcnative-1-0
Version:        1.2.38
Release:        0
Summary:        Tomcat resources for performance, compatibility, etc
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://tomcat.apache.org/native-1.2-doc/index.html
Source0:        https://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/tomcat-native-%{version}-src.tar.gz
Source1:        https://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/tomcat-native-%{version}-src.tar.gz.asc
# https://www.apache.org/dist/tomcat/tomcat-connectors/KEYS
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  libapr1-devel >= 1.4.3
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  pkgconfig
# Upstream compatibility:
Provides:       tcnative = %{version}
#Fedora compatibility
Provides:       tomcat-native = %{version}

%description
The Apache Tomcat Native Library is an optional component for use
with Apache Tomcat that allows Tomcat to use certain native
resources for performance, compatibility, etc.

Specifically, the Apache Tomcat Native Library gives Tomcat access
to the Apache Portable Runtime (APR) library's network connection
(socket) implementation and random-number generator. See the Apache
Tomcat documentation for more information on how to configure Tomcat
to use the APR connector.

Features of the APR connector:

* Non-blocking I/O for Keep-Alive requests (between requests)
* Uses OpenSSL for TLS/SSL capabilities (if supported by linked APR
  library)
* FIPS 140-2 support for TLS/SSL (if supported by linked OpenSSL
  library)
* Support for IPv4, IPv6 and Unix Domain Sockets

%package devel
Summary:        Tomcat resources for performance, compatibility, etc
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       glibc-devel
Requires:       libapr1-devel
Requires:       libopenssl-devel

%description devel
The Apache Tomcat Native Library is an optional component for use
with Apache Tomcat that allows Tomcat to use certain native
resources for performance, compatibility, etc.

Specifically, the Apache Tomcat Native Library gives Tomcat access
to the Apache Portable Runtime (APR) library's network connection
(socket) implementation and random-number generator. See the Apache
Tomcat documentation for more information on how to configure Tomcat
to use the APR connector.

Features of the APR connector:

* Non-blocking I/O for Keep-Alive requests (between requests)
* Uses OpenSSL for TLS/SSL capabilities (if supported by linked APR
  library)
* FIPS 140-2 support for TLS/SSL (if supported by linked OpenSSL
  library)
* Support for IPv4, IPv6 and Unix Domain Sockets

%prep
%setup -q -n tomcat-native-%{version}-src

%build
cd native
%configure \
    --with-apr=%{_bindir}/apr-1-config \
    --with-java-home=%{java_home} \
    --with-java-platform=2
make %{?_smp_mflags}

%install
make -C native install DESTDIR=%{buildroot}
install -d -m 755 %{buildroot}/%{_includedir}
install -m 644 native/include/* %{buildroot}/%{_includedir}
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc CHANGELOG.txt README.txt
%{_libdir}/libtcnative-1.so.*
#bnc#622430 - java expects so files installed
%{_libdir}/libtcnative-1.so

%files devel
%{_includedir}/*

%license LICENSE NOTICE

%changelog
