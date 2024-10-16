#
# spec file for package osgi-compendium
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


Name:           osgi-compendium
Version:        8.0.0
Release:        0
Summary:        Interfaces and Classes for use in compiling OSGi bundles
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.osgi.org
Source0:        https://osgi.org/download/r8/osgi.cmpn-%{version}.jar
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  cdi-api
BuildRequires:  fdupes
BuildRequires:  geronimo-jpa-3_0-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  javapackages-local >= 6
BuildRequires:  osgi-annotation
BuildRequires:  osgi-core
BuildRequires:  unzip
BuildArch:      noarch

%description
OSGi Compendium, Interfaces and Classes for use in compiling bundles.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -c
cp %{SOURCE1} build.xml

rm -r org
find -name '*.class' -delete

mkdir -p src/main/{java,resources}
mv OSGI-OPT/src/org src/main/java/
mv xmlns src/main/resources

mv META-INF/maven/org.osgi/osgi.cmpn/pom.xml .
mv META-INF/LICENSE .
mv META-INF/NOTICE .

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

%pom_remove_dep :
%pom_add_dep org.osgi:osgi.annotation::provided
%pom_add_dep org.osgi:osgi.core::provided
%pom_add_dep javax.servlet:javax.servlet-api::provided
%pom_add_dep javax.persistence:persistence-api::provided
%pom_add_dep javax.enterprise:cdi-api::provided
%pom_add_dep javax.inject:javax.inject::provided

rm -r src/main/java/org/osgi/service/jaxrs

mkdir -p lib
build-jar-repository -s lib geronimo-jpa-3.0-api glassfish-servlet-api osgi-annotation osgi-core javax.enterprise.inject atinject

%build
ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/osgi.cmpn-%{version}.jar %{buildroot}%{_javadir}/%{name}/osgi.cmpn.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/osgi.cmpn.pom
%add_maven_depmap %{name}/osgi.cmpn.pom %{name}/osgi.cmpn.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc
%license LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
