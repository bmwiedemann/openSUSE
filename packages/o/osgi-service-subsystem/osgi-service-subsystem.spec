#
# spec file for package osgi-service-subsystem
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


Name:           osgi-service-subsystem
Version:        1.1.0
Release:        0
Summary:        OSGi Service Log
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.osgi.org
Source0:        https://repo1.maven.org/maven2/org/osgi/org.osgi.service.subsystem/%{version}/org.osgi.service.subsystem-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/org/osgi/org.osgi.service.subsystem/%{version}/org.osgi.service.subsystem-%{version}.pom
Source100:      %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 1.8
BuildRequires:  osgi-annotation
BuildRequires:  osgi-core
BuildRequires:  unzip
BuildArch:      noarch

%description
OSGi Companion Code for org.osgi.service.subsystem Version 1.1.0.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -c
mkdir -p src/main/java
mv org src/main/java/
cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE100} build.xml

%pom_add_dep org.osgi:osgi.annotation::provided
%pom_add_dep org.osgi:osgi.core::provided

# not needed for this build but useful to regenerate the osgi manifest
# when we change version
%pom_xpath_inject pom:project '
<packaging>bundle</packaging>
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Bundle-Name>${project.artifactId}</Bundle-Name>
          <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>'

%build
mkdir -p lib
build-jar-repository -s lib osgi-annotation osgi-core
ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/org.osgi.service.subsystem-%{version}.jar %{buildroot}%{_javadir}/%{name}/org.osgi.service.subsystem.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/org.osgi.service.subsystem.pom
%add_maven_depmap %{name}/org.osgi.service.subsystem.pom %{name}/org.osgi.service.subsystem.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
