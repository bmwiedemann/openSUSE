#
# spec file for package mysql-connector-java
#
# Copyright (c) 2025 SUSE LLC
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


%define new_name mysql-connector-j
Name:           mysql-connector-java
Version:        9.2.0
Release:        0
Summary:        Official JDBC Driver for MySQL
License:        GPL-2.0-or-later
Group:          Development/Languages/Java
URL:            https://dev.mysql.com/downloads/connector/j/
Source0:        https://github.com/mysql/mysql-connector-j/archive/refs/tags/%{version}.tar.gz#:/%{name}-%{version}.tar.gz
Patch0:         javac-check.patch
# NOTE: Oracle OCI is not packaged yet
#   The patch doesn't remove the file AuthenticationOciClient.java
#   therefore it's removed during prep phase
Patch1:         %{name}-remove-oci-support.patch
Patch2:         reproducible-build.patch
Patch3:         %{name}-remove-opentelemetry-support.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  apache-commons-logging
BuildRequires:  geronimo-jta-1_1-api
BuildRequires:  git
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  javassist >= 3.28.0
BuildRequires:  junit
BuildRequires:  protobuf-devel >= 26
BuildRequires:  protobuf-java >= 26
BuildRequires:  slf4j
BuildRequires:  xz
Requires:       jta >= 1.0
Requires:       slf4j
Provides:       mm.mysql = %{version}
Obsoletes:      mm.mysql < %{version}
# we'll be providing the new package name until this one is deprecated
Provides:       %{new_name}
# manual is no longer distributed
Provides:       %{name}-manual = %{version}
Obsoletes:      %{name}-manual < %{version}
BuildArch:      noarch
%if 0%{?suse_version} < 1500
BuildRequires:  log4j
Requires:       log4j
%else
BuildRequires:  reload4j
Requires:       reload4j
%endif

%description
MySQL Connector/J is a native Java driver that converts JDBC (Java
Database Connectivity) calls into the network protocol used by the
MySQL database. It lets developers working with the Java programming
language easily build programs and applets that interact with MySQL and
connect all corporate data, even in a heterogeneous environment. MySQL
Connector/J is a Type IV JDBC driver and has a complete JDBC feature
set that supports the capabilities of MySQL.

%prep
%setup -q -n mysql-connector-j-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

# remove OCI support
rm -rf src/main/protocol-impl/java/com/mysql/cj/protocol/a/authentication/AuthenticationOciClient.java

# remove OpenTelemetry support
rm -rf src/main/core-impl/java/com/mysql/cj/otel/OpenTelemetryHandler.java
rm -rf src/main/core-impl/java/com/mysql/cj/otel/OpenTelemetrySpan.java
rm -rf src/main/core-impl/java/com/mysql/cj/otel/OpenTelemetryScope.java

# extra libs
mkdir -p lib
mkdir -p src/lib
ln -f -s `find-jar ant/ant-contrib` lib/ant-contrib.jar
ln -f -s `find-jar slf4j/api` lib/slf4j-api.jar
ln -s `find-jar javassist` lib/javassist.jar
ln -s `find-jar protobuf` lib/protobuf.jar

%build

export CLASSPATH=$(build-classpath \
    ant-contrib \
    commons-logging \
    slf4j \
    jdbc-stdext \
    jta \
    junit \
    reload4j \
    protobuf)
ant \
    -Dsnapshot.version= \
    -Dcom.mysql.jdbc.extra.libs=lib \
    -Dant.java.version=1.8 \
    -Dant.build.javac.source=1.8 \
    -Dant.build.javac.target=1.8 \
    -Dcom.mysql.cj.build.jdk.javac=javac \
    -Dcom.mysql.cj.build.jdk.java=java \
    build

%install
install -d -m 755 %{buildroot}%{_javadir}

install build/%{new_name}-%{version}-SNAPSHOT/%{new_name}-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{new_name}.jar
ln -sf %{_javadir}/%{new_name}.jar %{buildroot}%{_javadir}/%{name}.jar

rm -rf %{buildroot}%{new_name}-%{version}/docs/release-test-output

install -d -m 755 %{buildroot}%{_mavenpomdir}

# Install the Maven build information as new name
%{mvn_install_pom} build/%{new_name}-%{version}-SNAPSHOT/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{new_name}.pom
sed -i 's/-SNAPSHOT//' %{buildroot}%{_mavenpomdir}/JPP-%{new_name}.pom
%add_maven_depmap JPP-%{new_name}.pom %{new_name}.jar -a "com.mysql:%{name}","mysql:%{name}"

%files -f .mfiles
%{_javadir}/%{name}.jar
%license LICENSE
%doc CHANGES README

%changelog
