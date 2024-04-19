#
# spec file for package mockito
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


Name:           mockito
Version:        5.11.0
Release:        0
Summary:        A Java mocking framework
License:        MIT
Group:          Development/Libraries/Java
URL:            http://%{name}.org
Source0:        %{name}-%{version}.tar.xz
# build with maven instead of gradle
Source2:        aggregator.pom
Source3:        https://repo1.maven.org/maven2/org/mockito/mockito-core/%{version}/mockito-core-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/mockito/mockito-junit-jupiter/%{version}/mockito-junit-jupiter-%{version}.pom
Patch0:         use-unbundled-asm.patch
Patch1:         keep-source-target-8.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-dep)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.opentest4j:opentest4j)
BuildArch:      noarch

%description
Mockito is a mocking framework. It lets you write tests. Tests
produce clean verification errors.

%package junit-jupiter
Summary:        Mockito JUnit 5 support
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description junit-jupiter
Mockito JUnit 5 support.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p1

cp %{SOURCE2} aggregator.pom
cp %{SOURCE3} pom.xml
cp %{SOURCE4} subprojects/junit-jupiter/pom.xml

# Compatibility alias
%{mvn_alias} org.%{name}:%{name}-core org.%{name}:%{name}-all

%pom_add_dep junit:junit
%pom_add_dep net.bytebuddy:byte-buddy-dep
%pom_remove_dep org.objenesis:objenesis
%pom_add_dep org.objenesis:objenesis
%pom_add_dep org.opentest4j:opentest4j

%pom_remove_dep org.junit.jupiter:junit-jupiter-api subprojects/junit-jupiter
%pom_add_dep org.junit.jupiter:junit-jupiter-api subprojects/junit-jupiter

mkdir -p src/main/resources/mockito-extensions
echo 'member-accessor-module' > src/main/resources/mockito-extensions/org.mockito.plugins.MemberAccessor
echo 'mock-maker-subclass' > src/main/resources/mockito-extensions/org.mockito.plugins.MockMaker

# see gradle/mockito-core/inline-mock.gradle
%pom_xpath_inject 'pom:project' '
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-antrun-plugin</artifactId>
      <version>any</version>
      <executions>
        <execution>
          <phase>process-classes</phase>
          <configuration>
            <target>
              <copy file="${project.build.outputDirectory}/org/mockito/internal/creation/bytebuddy/inject/MockMethodDispatcher.class"
                    tofile="${project.build.outputDirectory}/org/mockito/internal/creation/bytebuddy/inject/MockMethodDispatcher.raw"/>
            </target>
          </configuration>
          <goals>
            <goal>run</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-jar-plugin</artifactId>
      <version>any</version>
      <configuration>
        <excludes>
          <exclude>org/mockito/internal/creation/bytebuddy/inject/*.class</exclude>
        </excludes>
      </configuration>
    </plugin>
  </plugins>
</build>
'

%{mvn_package} :aggregator __noinstall

%build
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dmaven.compiler.source=8 -Dmaven.compiler.target=8 -Dsource=8 \
    -Dproject.build.sourceEncoding=UTF-8 -f aggregator.pom

%{mvn_package} org.mockito:mockito-junit-jupiter junit-jupiter

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md doc/design-docs/custom-argument-matching.md

%files junit-jupiter -f .mfiles-junit-jupiter

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
