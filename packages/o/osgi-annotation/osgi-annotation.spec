#
# spec file for package osgi-annotation
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


Name:           osgi-annotation
Version:        8.1.0
Release:        0
Summary:        Annotations for use in compiling OSGi bundles
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.osgi.org/
# Upstream project is behind an account registration system with no anonymous
# read access, so we download the source from maven central instead
Source0:        https://repo1.maven.org/maven2/org/osgi/osgi.annotation/%{version}/osgi.annotation-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/org/osgi/osgi.annotation/%{version}/osgi.annotation-%{version}.pom
Source2:        http://www.apache.org/licenses/LICENSE-2.0
Source3:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
BuildArch:      noarch

%description
Annotations for use in compiling OSGi bundles. This package is not normally
needed at run-time.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c

mkdir -p src/main/java && mv org src/main/java
cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} LICENSE
cp -p %{SOURCE3} build.xml

# Ensure OSGi metadata is generated
%pom_xpath_inject pom:project "
  <packaging>bundle</packaging>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <Bundle-Name>\${project.artifactId}</Bundle-Name>
            <Bundle-SymbolicName>\${project.artifactId}</Bundle-SymbolicName>
          </instructions>
        </configuration>
      </plugin>
    </plugins>
  </build>"

%build
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/osgi.annotation-%{version}.jar %{buildroot}%{_javadir}/%{name}/osgi.annotation.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/osgi.annotation.pom
%add_maven_depmap %{name}/osgi.annotation.pom %{name}/osgi.annotation.jar -a org.osgi:org.osgi.annotation
# javadoc
install -dm 0744 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
