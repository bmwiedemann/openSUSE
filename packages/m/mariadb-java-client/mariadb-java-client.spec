#
# spec file for package mariadb-java-client
#
# Copyright (c) 2020 SUSE LLC
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
Version:        2.4.3
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

# convert files from dos to unix line encoding
for file in README.md documentation/*.creole; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

# remove missing optional dependency waffle-jna
%pom_remove_dep com.github.waffle:waffle-jna
# also remove the file using the removed plugin
rm -f src/main/java/org/mariadb/jdbc/internal/com/send/authentication/gssapi/WindowsNativeSspiAuthentication.java
# patch the sources so that the missing file is not making trouble
%patch0 -p1

%{mvn_file} org.mariadb.jdbc:%{name} %{name}
%{mvn_alias} org.mariadb.jdbc:%{name} mariadb:mariadb-connector-java

%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin pl.project13.maven:git-commit-id-plugin
%pom_remove_plugin -r :maven-gpg-plugin

# remove preconfigured OSGi manifest file and generate OSGi manifest file
# with maven-bundle-plugin instead of using maven-jar-plugin
rm src/main/resources/META-INF/MANIFEST.MF
%pom_xpath_set "pom:packaging" bundle
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive/pom:manifestFile" '${project.build.outputDirectory}/META-INF/MANIFEST.MF'
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive/pom:manifestEntries"

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']" '
<executions>
  <execution>
    <goals>
      <goal>test-jar</goal>
    </goals>
  </execution>
</executions>'

%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>${project.groupId}</Bundle-SymbolicName>
    <Bundle-Name>MariaDB JDBC Client</Bundle-Name>
    <Bundle-Version>${project.version}.0</Bundle-Version>
    <Export-Package>org.mariadb.jdbc.*</Export-Package>
    <Import-Package>
      !com.sun.jna.*,
      javax.net;resolution:=optional,
      javax.net.ssl;resolution:=optional,
      javax.sql;resolution:=optional,
      javax.transaction.xa;resolution:=optional
    </Import-Package>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%build
# tests are skipped, while they require running application server
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc documentation/* README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
