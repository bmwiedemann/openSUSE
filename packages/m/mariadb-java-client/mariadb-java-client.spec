#
# spec file for package mariadb-java-client
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


Name:           mariadb-java-client
Version:        3.5.0
Release:        0
Summary:        Connects applications developed in Java to MariaDB and MySQL databases
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/
Source0:        https://github.com/MariaDB/mariadb-connector-j/archive/%{version}.tar.gz
Patch0:         remove_waffle-jna.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:jna-platform)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
Requires:       mariadb

%description
MariaDB Connector/J is a Type 4 JDBC driver, also known as the Direct to
Database Pure Java Driver. It was developed specifically as a lightweight
JDBC connector for use with MySQL and MariaDB database servers.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n mariadb-connector-j-%{version}
%patch -P 0 -p1

%pom_remove_dep com.github.waffle:waffle-jna
%pom_remove_dep ch.qos.logback:logback-classic
%pom_remove_dep software.amazon.awssdk:bom
%pom_remove_dep software.amazon.awssdk:rds
%pom_remove_dep org.junit:junit-bom
%pom_remove_dep org.junit.jupiter:junit-jupiter-engine

# used in buildtime for generating OSGI metadata
%pom_remove_plugin biz.aQute.bnd:bnd-maven-plugin

%pom_add_dep net.java.dev.jna:jna
%pom_add_dep net.java.dev.jna:jna-platform

# make the slf4j dependency version-independent
%pom_remove_dep org.slf4j:slf4j-api
%pom_add_dep org.slf4j:slf4j-api

# use the latest OSGi implementation
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core
%pom_change_dep -r :org.osgi.compendium org.osgi:osgi.cmpn

rm -r src/main/java/org/mariadb/jdbc/plugin/credential/aws

# removing dependencies and 'provides', which mariadb-java-client cannot process from module-info.java
sed -i '/aws/d' src/main/java9/module-info.java
sed -i '/waffle/d' src/main/java9/module-info.java

# removing missing dependencies form META-INF, so that the mariadb-java-client module would be valid
sed -i '/aws/d' src/main/resources/META-INF/services/org.mariadb.jdbc.plugin.CredentialPlugin
sed -i '/aws/d' src/test/resources/META-INF/services/org.mariadb.jdbc.plugin.CredentialPlugin
rm -f src/main/java/org/mariadb/jdbc/plugin/authentication/addon/gssapi/WindowsNativeSspiAuthentication.java

%{mvn_file} org.mariadb.jdbc:%{name} %{name}
%{mvn_alias} org.mariadb.jdbc:%{name} mariadb:mariadb-connector-java

%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
# tests are skipped, while they require running application server
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
