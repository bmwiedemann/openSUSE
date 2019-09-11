#
# spec file for package libtcnative-1-0
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


Name:           libtcnative-1-0
Version:        1.2.23
Release:        0
Summary:        JNI wrappers for Apache Portable Runtime for Tomcat
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
Url:            https://tomcat.apache.org/tomcat-7.0-doc/apr.html
Source0:        https://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/tomcat-native-%{version}-src.tar.gz
Source1:        https://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/tomcat-native-%{version}-src.tar.gz.asc
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  libapr1-devel >= 1.4.3
BuildRequires:  openssl-devel >= 1.0.2
BuildRequires:  pkgconfig
# Upstream compatibility:
Provides:       tcnative = %{version}
#Fedora compatibility
Provides:       tomcat-native = %{version}

%description
Tomcat can use the Apache Portable Runtime to provide superior
scalability, performance, and better integration with native server
technologies. The Apache Portable Runtime is a highly portable library
that is at the heart of Apache HTTP Server 2.x. APR has many uses,
including access to advanced IO functionality (such as sendfile, epoll
and OpenSSL), OS level functionality (random number generation, system
status, etc), and native process handling (shared memory, NT pipes and
Unix sockets).

These features allows making Tomcat a general purpose webserver, will
enable much better integration with other native web technologies, and
overall make Java much more viable as a full fledged webserver platform
rather than simply a backend focused technology.

%package devel
Summary:        JNI wrappers for Apache Portable Runtime for Tomcat
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       glibc-devel
Requires:       libapr1-devel
Requires:       libopenssl-devel

%description devel
Tomcat can use the Apache Portable Runtime to provide superior
scalability, performance, and better integration with native server
technologies. The Apache Portable Runtime is a highly portable library
that is at the heart of Apache HTTP Server 2.x. APR has many uses,
including access to advanced IO functionality (such as sendfile, epoll
and OpenSSL), OS level functionality (random number generation, system
status, etc), and native process handling (shared memory, NT pipes and
Unix sockets).

These features allows making Tomcat a general purpose webserver, will
enable much better integration with other native web technologies, and
overall make Java much more viable as a full fledged webserver platform
rather than simply a backend focused technology.

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
%doc CHANGELOG.txt LICENSE NOTICE README.txt
%{_libdir}/libtcnative-1.so.*
#bnc#622430 - java expects so files installed
%{_libdir}/libtcnative-1.so

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%changelog
