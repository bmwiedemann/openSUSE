#
# spec file for package mysql-connector-java
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


Name:           mysql-connector-java
Version:        8.0.25
Release:        0
Summary:        Official JDBC Driver for MySQL
License:        GPL-2.0-or-later
URL:            https://dev.mysql.com/downloads/connector/j/
Source0:        %{name}-%{version}-suse.tar.xz
Group:          Development/Languages/Java
# Script to repack upstream tarball
# ./generate-tarball.sh VERSION
Source99:       generate-tarball.sh
Patch0:         javac-check.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  apache-commons-logging
BuildRequires:  geronimo-jta-1_1-api
BuildRequires:  git
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools >= 5.3.1
BuildRequires:  javassist >= 3.23.1
BuildRequires:  junit
BuildRequires:  log4j12-mini
BuildRequires:  protobuf-java >= 3.9.2
BuildRequires:  slf4j
BuildRequires:  xz
Requires:       jta >= 1.0
Requires:       log4j12
Requires:       slf4j
Provides:       mm.mysql = %{version}
Obsoletes:      mm.mysql < %{version}
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
%setup -q
%patch0 -p1

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
    log4j12/log4j-12 \
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
    dist

%install
install -d -m 755 %{buildroot}%{_javadir}

install build/%{name}-%{version}-SNAPSHOT/%{name}-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar

rm -rf %{buildroot}%{name}-%{version}/docs/release-test-output

# Install the Maven build information
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 build/%{name}-%{version}-SNAPSHOT/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
sed -i 's/-SNAPSHOT//' %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%license LICENSE
%doc CHANGES README

#    -Dcom.mysql.cj.build.jdk.javac=/usr/lib64/jvm/java-1.8.0/bin/javac \
#    -Dcom.mysql.cj.build.jdk.java=/usr/lib64/jvm/java-1.8.0/bin/java \
    dist

install -d -m 755 %{buildroot}%{_javadir}

install build/%{name}-%{version}-SNAPSHOT/%{name}-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar

rm -rf %{buildroot}%{name}-%{version}/docs/release-test-output

# Install the Maven build information
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 build/%{name}-%{version}-SNAPSHOT/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
sed -i 's/-SNAPSHOT//' %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%license LICENSE
%doc CHANGES README

%changelog
