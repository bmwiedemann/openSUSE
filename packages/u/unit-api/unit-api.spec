#
# spec file for package unit-api
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


Name:           unit-api
Version:        1.0
Release:        0
Summary:        JSR 363 - Units of Measurement API
# JSR-363 has been approved as an official JCP standard (https://jcp.org/en/jsr/results?id=5877)
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://unitsofmeasurement.github.io/
Source0:        https://github.com/unitsofmeasurement/unit-api/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
The Unit of Measurement library provides a set of
Java language programming interfaces for handling
units and quantities. The interfaces provide a layer
which separates client code, which would call the
API, from library code, which implements the API.

The specification contains Interfaces and abstract
classes with methods for unit operations:

* Checking of unit compatibility
* Expression of a quantity in various units
* Arithmetic operations on units

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

# Not available plugins
%pom_remove_plugin :coveralls-maven-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :formatter-maven-plugin
# Useless tasks
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

# Remove duplicate pom entry
%pom_remove_plugin :maven-jar-plugin
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin:'${maven.jar.version}' . "
<executions>
   <execution>
      <goals>
         <goal>test-jar</goal>
      </goals>
   </execution>
</executions>"
# Fix pom entries
%pom_remove_plugin :maven-bundle-plugin
%pom_add_plugin org.apache.felix:maven-bundle-plugin:'${felix.version}' . "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Specification-Title>\${project.name}</Specification-Title>
    <Specification-Version>\${project.version}</Specification-Version>
    <Specification-Vendor>\${project.organization.name}</Specification-Vendor>
    <Implementation-Vendor>Unit-API contributors</Implementation-Vendor>
    <Implementation-URL>\${project.organization.url}</Implementation-URL>
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
</executions>"

%{mvn_file}  : %{name}
%{mvn_file} :%{name}:tests: %{name}-tests
%{mvn_package} :%{name}:tests: %{name}

%build

%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
