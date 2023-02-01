#
# spec file for package osgi-service-log
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


Name:           osgi-service-log
Version:        1.5.0
Release:        0
Summary:        OSGi Service Log
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.osgi.org
Source0:        https://repo1.maven.org/maven2/org/osgi/org.osgi.service.log/%{version}/org.osgi.service.log-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/org/osgi/org.osgi.service.log/%{version}/org.osgi.service.log-%{version}.pom
Source2:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
OSGi Companion Code for org.osgi.service.log Version 1.5.0.

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
cp -p %{SOURCE2} LICENSE

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
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
