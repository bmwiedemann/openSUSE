#
# spec file for package libtcnative-2-0
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
Name:           libtcnative-2-0
Version:        2.0.14
Release:        0
Summary:        Tomcat resources for performance, compatibility, etc
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://tomcat.apache.org/native-doc/index.html
Source0:        https://archive.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/tomcat-native-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/tomcat-native-%{version}-src.tar.gz.asc
# https://www.apache.org/dist/tomcat/tomcat-connectors/KEYS
Source2:        %{name}.keyring
Patch0:         apr163.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 11
BuildRequires:  libapr1-devel >= 1.6.3
BuildRequires:  libopenssl-3-devel
BuildRequires:  pkgconfig
Provides:       tcnative = %{version}
Provides:       tomcat-native = %{version}
%if 0%{?suse_version} < 1600 && 0%{?sle_version} < 150400
ExclusiveArch:  do-not-build
%endif

%description
The Apache Tomcat Native Library is an optional component for use
with Apache Tomcat that allows Tomcat to use OpenSSL as a
replacement for JSSE to support TLS connections.

%package devel
Summary:        Tomcat resources for performance, compatibility, etc
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       glibc-devel
Requires:       libapr1-devel >= 1.6.3
Requires:       libopenssl-3-devel
Conflicts:      libtcnative-1-0-devel

%description devel
The Apache Tomcat Native Library is an optional component for use
with Apache Tomcat that allows Tomcat to use OpenSSL as a
replacement for JSSE to support TLS connections.

%prep
%setup -q -n tomcat-native-%{version}-src
%patch -P 0 -p1

%build
cd native
%configure \
    --with-apr=%{_bindir}/apr-1-config
%make_build

%install
make -C native install DESTDIR=%{buildroot}
install -d -m 755 %{buildroot}/%{_includedir}
install -m 644 native/include/* %{buildroot}/%{_includedir}
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc CHANGELOG.txt README.txt
%{_libdir}/libtcnative-2.so.*
%{_libdir}/libtcnative-2.so

%files devel
%{_includedir}/*

%license LICENSE NOTICE

%changelog
