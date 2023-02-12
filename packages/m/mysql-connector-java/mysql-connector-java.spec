#
# spec file for package mysql-connector-java
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


%define new_name mysql-connector-j

Name:           mysql-connector-java
Version:        8.0.32
Release:        0
Summary:        Official JDBC Driver for MySQL
License:        GPL-2.0-or-later
URL:            https://dev.mysql.com/downloads/connector/j/
Source0:        https://github.com/mysql/mysql-connector-j/archive/refs/tags/%{version}.tar.gz#:/%{name}-%{version}.tar.gz
# NOTE:
#   the following file contains the generated protobuf files with
#   previous versions of protoc (protobuf) that are needed to build
#   in previous SUSE distros.
#   Source from:
#   https://github.com/mysql/mysql-connector-j/commit/6976d9d779b498c254fc5cab5e69cfc74fc3e4f0
Source1:        mysql-connector-java-generated-for-protobuf-3.9.2.tar.xz
Group:          Development/Languages/Java
Patch0:         javac-check.patch
# NOTE: Oracle OCI is not packaged yet
#   The patch doesn't remove the file AuthenticationOciClient.java
#   therefore it's removed during prep phase
Patch1:         %{name}-remove-oci-support.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  apache-commons-logging
BuildRequires:  geronimo-jta-1_1-api
BuildRequires:  git
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javassist >= 3.28.0
BuildRequires:  junit
BuildRequires:  protobuf-java >= 3.9.2
BuildRequires:  reload4j
BuildRequires:  slf4j
BuildRequires:  xz
Requires:       jta >= 1.0
Requires:       reload4j
Requires:       slf4j
Provides:       mm.mysql = %{version}
Obsoletes:      mm.mysql < %{version}
# we'll be providing the new package name until this one is deprecated
Provides:       %{new_name}
# manual is no longer distributed
Provides:       %{name}-manual = %{version}
Obsoletes:      %{name}-manual < %{version}
BuildArch:      noarch

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
%patch0 -p1
%patch1 -p1

%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150200
# ship protobuf generated files compatible with protobuf 3.9.2
# which is the version we have in SLE15 SP2, the files were taken
# from commit 6976d9d779b498c254fc5cab5e69cfc74fc3e4f0, which is
# the last version compatible with that version of protobuf and
# are equivalent in functionality
tar -xvf %SOURCE1 -C .
%endif

# remove OCI support
rm -rf src/main/protocol-impl/java/com/mysql/cj/protocol/a/authentication/AuthenticationOciClient.java

# extra libs
mkdir -p lib
mkdir -p src/lib
ln -f -s %{_datadir}/java/ant/ant-contrib.jar lib/ant-contrib.jar
ln -f -s %{_datadir}/java/slf4j/api.jar lib/slf4j-api.jar
ln -s %{_datadir}/java/javassist.jar lib/javassist.jar
ln -s %{_datadir}/java/protobuf.jar lib/protobuf.jar

%build

export CLASSPATH=$(build-classpath \
    ant-contrib \
    commons-logging \
    slf4j \
    jdbc-stdext\
    jta \
    junit \
    reload4j \
    protobuf)
%{ant} \
    -Dsnapshot.version= \
    -Dcom.mysql.jdbc.extra.libs=lib \
    -Dant.java.version=1.8 \
    -Dant.build.javac.source=1.8 \
    -Dant.build.javac.target=1.8 \
    -Dcom.mysql.cj.build.jdk=%{java_home} \
    -Dcom.mysql.cj.build.jdk.javac=%{javac} \
    -Dcom.mysql.cj.build.jdk.java=%{java} \
    build

%install
install -d -m 755 %{buildroot}%{_javadir}

install build/%{new_name}-%{version}-SNAPSHOT/%{new_name}-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{new_name}.jar

rm -rf %{buildroot}%{new_name}-%{version}/docs/release-test-output

install -d -m 755 %{buildroot}%{_mavenpomdir}

# Install the Maven build information as new name
install -pm 644 build/%{new_name}-%{version}-SNAPSHOT/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{new_name}.pom
sed -i 's/-SNAPSHOT//' %{buildroot}%{_mavenpomdir}/JPP-%{new_name}.pom
%add_maven_depmap JPP-%{new_name}.pom %{new_name}.jar

# Provide poms with "old name" mysql-connector-java (now it's mysql-connector-j)
install -pm 644 build/%{new_name}-%{version}-SNAPSHOT/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
sed -i 's/-SNAPSHOT//' %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{new_name}.jar

%files -f .mfiles
%license LICENSE
%doc CHANGES README

%changelog
