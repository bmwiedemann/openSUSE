#
# spec file for package sqlite-jdbc
#
# Copyright (c) 2024 SUSE LLC
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
%global version 3.47.1.0
%global amalgamation_version 3470100
%global debug_package %{nil}
Name:           sqlite-jdbc
Version:        %{version}
Release:        0
Summary:        SQLite JDBC Driver
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/xerial/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://sqlite.org/2024/sqlite-amalgamation-%{amalgamation_version}.zip
Patch0:         sqlite-jdbc-no-implicit-function-declaration.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  xmvn
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
SQLite JDBC is a library for accessing and creating SQLite database files in
Java.

Our SQLiteJDBC library requires no configuration since native libraries for
major OSs, including Windows, Mac OS X, Linux etc., are assembled into a single
JAR (Java Archive) file. The usage is quite simple; download our sqlite-jdbc
library, then append the library (JAR file) to your class path.

%package javadoc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1

find src/main/resources \
	\( -name \*.so -or -name \*.dylib -or -name \*.dll \) \
	-delete

%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin
%pom_remove_dep org.graalvm.sdk:nativeimage

sed -i -e '/org\.graalvm\.nativeimage/ d' src/main/java9/module-info.java
rm src/main/java9/org/sqlite/nativeimage/SqliteJdbcFeature.java

dos2unix SQLiteJDBC.wiki
mkdir -p target/classpath
cp %{SOURCE1} target/sqlite-$(sed -e 's/^version=//' VERSION)-amal.zip

ln -s %{_javadir}/slf4j/slf4j-api.jar target/classpath/

%{mvn_file} : %{name}

%build
%make_build native
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE* NOTICE
%doc CHANGELOG README.adoc {USAGE,SECURITY}.md SQLiteJDBC.wiki

%files javadoc -f .mfiles-javadoc
%license LICENSE* NOTICE

%changelog
