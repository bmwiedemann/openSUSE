#
# spec file for package mysql-connector-java
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


Name:           mysql-connector-java
Version:        5.1.47
Release:        0
Summary:        Official JDBC Driver for MySQL
License:        GPL-2.0-or-later
URL:            https://dev.mysql.com/downloads/connector/j/
Source0:        %{name}-%{version}-suse.tar.xz
# Script to repack upstream tarball
# ./generate-tarball.sh VERSION
Source99:       generate-tarball.sh
Patch0:         javac-check.patch
Patch1:         hibernate-check.patch
Patch2:         mysql-connector-java-jdbc-4.1.patch
Patch3:         disable-testsuite.patch
Patch4:         compile-jdk7.patch
Patch5:         mysql-connector-java-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  apache-commons-logging
BuildRequires:  geronimo-jta-1_1-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  log4j12-mini
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# dup
rm -f README
# wrong end of line encoding
sed -i -e 's/.$//' README.txt

# extra libs
mkdir -p lib
mkdir -p src/lib
ln -f -s %{_datadir}/java/ant/ant-contrib.jar lib/ant-contrib.jar
ln -f -s %{_datadir}/java/slf4j/api.jar lib/slf4j-api.jar

%build
# disable jboss integration
rm -rf src/com/mysql/jdbc/integration/jboss
rm src/testsuite/regression/ConnectionRegressionTest.java
rm src/testsuite/regression/DataSourceRegressionTest.java
rm src/testsuite/simple/ReadOnlyCallableStatementTest.java
rm src/testsuite/simple/jdbc4/StatementsTest.java
# disable hibernate4 integration
rm -rf src/com/mysql/fabric/hibernate
rm -rf src/demo

export CLASSPATH=$(build-classpath \
    ant-contrib \
    commons-logging \
    slf4j \
    jdbc-stdext\
    jta \
    junit \
    log4j12/log4j-12)
%{ant} \
    -Dcom.mysql.jdbc.jdk5.javac=%javac \
    -Dcom.mysql.jdbc.jdk8.javac=%javac \
    -Dsnapshot.version= \
    -Dcom.mysql.jdbc.extra.libs=lib \
    -Dant.java.version=1.6 \
    -Dant.build.javac.source=1.6 \
    -Dant.build.javac.target=1.6 \
    dist

%install
install -d -m 755 %{buildroot}%{_javadir}

install ./build/%{name}-%{version}/%{name}-%{version}-bin.jar \
        %{buildroot}%{_javadir}/%{name}.jar

rm -rf %{buildroot}%{name}-%{version}/docs/release-test-output

# Install the Maven build information
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 src/doc/sources/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
sed -i 's/>@.*</>%{version}</' %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%license COPYING
%doc CHANGES README.txt

%changelog
