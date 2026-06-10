#
# spec file for package junit5
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global platform_version 1.14.4
%global jupiter_version %{version}
%global vintage_version %{version}
%global base_name junit5
# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Version:        5.14.4
Release:        0
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://junit.org/junit5/
Source0:        https://github.com/junit-team/%{base_name}/archive/r%{version}/%{base_name}-%{version}.tar.gz
Source1:        %{base_name}-build.tar.xz
# Aggregator POM (used for packaging only)
Source100:      aggregator.pom
# Platform POMs
Source200:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-commons/%{platform_version}/junit-platform-commons-%{platform_version}.pom
Source201:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console/%{platform_version}/junit-platform-console-%{platform_version}.pom
Source202:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/%{platform_version}/junit-platform-console-standalone-%{platform_version}.pom
Source203:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-engine/%{platform_version}/junit-platform-engine-%{platform_version}.pom
Source204:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-launcher/%{platform_version}/junit-platform-launcher-%{platform_version}.pom
Source205:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-runner/%{platform_version}/junit-platform-runner-%{platform_version}.pom
Source206:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-api/%{platform_version}/junit-platform-suite-api-%{platform_version}.pom
Source207:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-commons/%{platform_version}/junit-platform-suite-commons-%{platform_version}.pom
Source208:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-engine/%{platform_version}/junit-platform-suite-engine-%{platform_version}.pom
Source209:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-testkit/%{platform_version}/junit-platform-testkit-%{platform_version}.pom
# Jupiter POMs
Source300:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter/%{jupiter_version}/junit-jupiter-%{jupiter_version}.pom
Source301:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-api/%{jupiter_version}/junit-jupiter-api-%{jupiter_version}.pom
Source302:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-engine/%{jupiter_version}/junit-jupiter-engine-%{jupiter_version}.pom
Source303:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-migrationsupport/%{jupiter_version}/junit-jupiter-migrationsupport-%{jupiter_version}.pom
Source304:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-params/%{jupiter_version}/junit-jupiter-params-%{jupiter_version}.pom
# Vintage POM
Source400:      https://repo1.maven.org/maven2/org/junit/vintage/junit-vintage-engine/%{vintage_version}/junit-vintage-engine-%{vintage_version}.pom
# BOM POM
Source500:      https://repo1.maven.org/maven2/org/junit/junit-bom/%{version}/junit-bom-%{version}.pom
Patch1:         0001-Drop-transitive-requirement-on-apiguardian.patch
Patch2:         0002-Add-missing-module-static-requires.patch
Patch3:         0003-Remove-legacy-XML-console-support.patch
Patch4:         0004-Add-JRE-class-generated-from-template.patch
BuildRequires:  apiguardian >= 1.1.2
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  opentest4j
Requires:       java-headless >= 1.8
Requires:       javapackages-tools
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{base_name}-minimal
Summary:        Java regression testing framework (minimal)
BuildRequires:  ant
BuildRequires:  javapackages-local >= 6
%else
Name:           %{base_name}
Summary:        Java regression testing framework
BuildRequires:  %{base_name}-minimal
BuildRequires:  maven-local
BuildRequires:  mvn(com.univocity:univocity-parsers)
BuildRequires:  mvn(info.picocli:picocli)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.opentest4j:opentest4j)
Requires:       %{base_name}-minimal >= %{version}
Obsoletes:      %{base_name}-guide < %{version}
%endif

%description
JUnit is a popular regression testing framework for Java platform.

%package bom
Summary:        JUnit 5 (Bill of Materials)
Group:          Development/Libraries/Java

%description bom
This Bill of Materials POM can be used to ease dependency management
when referencing multiple JUnit artifacts using Gradle or Maven.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Junit5 API documentation.

%prep
%setup -q -n junit-framework-r%{version} -a1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
find -name \*.jar -delete

cp -p %{SOURCE100} pom.xml
cp -p %{SOURCE200} junit-platform-commons/pom.xml
cp -p %{SOURCE201} junit-platform-console/pom.xml
cp -p %{SOURCE202} junit-platform-console-standalone/pom.xml
cp -p %{SOURCE203} junit-platform-engine/pom.xml
cp -p %{SOURCE204} junit-platform-launcher/pom.xml
cp -p %{SOURCE205} junit-platform-runner/pom.xml
cp -p %{SOURCE206} junit-platform-suite-api/pom.xml
cp -p %{SOURCE207} junit-platform-suite-commons/pom.xml
cp -p %{SOURCE208} junit-platform-suite-engine/pom.xml
cp -p %{SOURCE209} junit-platform-testkit/pom.xml
cp -p %{SOURCE300} junit-jupiter/pom.xml
cp -p %{SOURCE301} junit-jupiter-api/pom.xml
cp -p %{SOURCE302} junit-jupiter-engine/pom.xml
cp -p %{SOURCE303} junit-jupiter-migrationsupport/pom.xml
cp -p %{SOURCE304} junit-jupiter-params/pom.xml
cp -p %{SOURCE400} junit-vintage-engine/pom.xml
cp -p %{SOURCE500} junit-bom/pom.xml

for pom in $(find -mindepth 2 -name pom.xml | grep -v tests/ | sort -u); do
    # Set parent to aggregator
    %pom_add_parent org.fedoraproject.xmvn.junit5:aggregator:any $pom
    # Incorrect scope - API guardian is just annotation, needed only during compilation
    %pom_xpath_set -f "pom:dependency[pom:artifactId='apiguardian-api']/pom:scope" provided $pom
    %pom_xpath_set -f "pom:dependency[pom:scope='runtime']/pom:scope" compile $pom
done

%pom_remove_parent junit-bom

# Add deps which are shaded by upstream and therefore not present in POMs.
%pom_add_dep org.junit.platform:junit-platform-commons:%{platform_version} junit-platform-console
%pom_add_dep org.junit.platform:junit-platform-launcher:%{platform_version} junit-platform-console
%pom_add_dep info.picocli:picocli:4.7.5 junit-platform-console
%pom_add_dep com.univocity:univocity-parsers:2.5.4 junit-jupiter-params

# Disable the standalone console (just jar with shaded dependencies)
%pom_disable_module junit-platform-console-standalone
%pom_remove_dep org.junit.platform:junit-platform-reporting junit-platform-console

# Disable the modules built in -minimal package
%pom_disable_module junit-platform-commons
%pom_disable_module junit-jupiter-api

# Special BND instructions in several artifacts (converted from *.kts files)
%pom_xpath_inject pom:project "
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions combine.children=\"append\">
          <Provide-Capability>
            org.junit.platform.engine;
            org.junit.platform.engine=junit-jupiter;
            version:Version=\"\${version_cleanup;\${project.version}}\"
          </Provide-Capability>
          <Require-Capability>
            org.junit.platform.launcher;
            filter:='(&amp;(org.junit.platform.launcher=junit-platform-launcher)(version&gt;=\${version_cleanup;%{platform_version}})(!(version&gt;=\${versionmask;+;\${version_cleanup;%{platform_version}}})))';
            effective:=active
          </Require-Capability>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>" junit-jupiter-engine

%pom_xpath_inject pom:project "
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions combine.children=\"append\">
          <Import-Package>
            org.apiguardian.*;resolution:=\"optional\",
            org.junit;version=\"[4.12,5)\",
            org.junit.platform.commons.logging;status=INTERNAL,
            org.junit.rules;version=\"[4.12,5)\",
            *
          </Import-Package>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>" junit-jupiter-migrationsupport

%pom_xpath_inject pom:project "
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions combine.children=\"append\">
          <Require-Capability>
            org.junit.platform.engine;
            filter:='(&amp;(org.junit.platform.engine=junit-jupiter)(version&gt;=\${version_cleanup;\${project.version}})(!(version&gt;=\${versionmask;+;\${version_cleanup;\${project.version}}})))';
            effective:=active
          </Require-Capability>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>" junit-jupiter-params

%pom_xpath_inject pom:project "
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions combine.children=\"append\">
          <Import-Package>
            org.apiguardian.*;resolution:=\"optional\",
            kotlin.*;resolution:="optional",
            *
          </Import-Package>
          <_export-apiguardian></_export-apiguardian>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>" junit-platform-console-standalone

%pom_xpath_inject pom:project "
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions combine.children=\"append\">
          <Provide-Capability>
            org.junit.platform.launcher;
            org.junit.platform.launcher=junit-platform-launcher;
            version:Version=\"\${version_cleanup;\${project.version}}\"
          </Provide-Capability>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>" junit-platform-launcher

%pom_xpath_inject pom:project "
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions combine.children=\"append\">
          <Import-Package>
            org.apiguardian.*;resolution:=\"optional\",
            junit.runner;version=\"[4.12,5)\",
            org.junit;version=\"[4.12,5)\",
            org.junit.experimental.categories;version=\"[4.12,5)\",
            org.junit.internal.builders;version=\"[4.12,5)\",
            org.junit.platform.commons.logging;status=INTERNAL,
            org.junit.runner.*;version=\"[4.12,5)\",
            org.junit.runners.model;version=\"[4.12,5)\",
            *
          </Import-Package>
          <Provide-Capability>
            org.junit.platform.engine;
            org.junit.platform.engine=junit-vintage;
            version:Version=\"\${version_cleanup;\${project.version}}\"
          </Provide-Capability>
          <Require-Capability>
            org.junit.platform.launcher;
            filter:='(&amp;(org.junit.platform.launcher=junit-platform-launcher)(version&gt;=\${version_cleanup;%{platform_version}})(!(version&gt;=\${versionmask;+;\${version_cleanup;%{platform_version}}})))';
            effective:=active
          </Require-Capability>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>" junit-vintage-engine

%{mvn_package} :junit-bom bom
%{mvn_package} :aggregator __noinstall

%build
%if %{with bootstrap}
mkdir -p lib
build-jar-repository -s lib opentest4j/opentest4j apiguardian/apiguardian-api
%{ant} package javadoc
%else
%{mvn_build} -f -- \
    -Dencoding=utf-8 -DlegacyMode=true -Dverbose=true -Dsource=8
%endif

%install
%if %{with bootstrap}

install -dm 0755 %{buildroot}%{_javadir}/%{base_name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{base_name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for i in junit-platform-commons junit-platform-engine junit-platform-launcher junit-jupiter-api; do
    install -pm 0644 ${i}/target/${i}*.jar %{buildroot}%{_javadir}/%{base_name}/${i}.jar
    %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}/${i}.pom
    %add_maven_depmap %{base_name}/${i}.pom %{base_name}/${i}.jar
    cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
done

%else

%mvn_install
%jpackage_script org/junit/platform/console/ConsoleLauncher "" "" junit5:opentest4j:picocli:junit:hamcrest %{name} true
%fdupes -s documentation/src/docs/

%endif

%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.md NOTICE.md

%if %{without bootstrap}

%{_bindir}/%{name}

%files bom -f .mfiles-bom
%license LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md

%else

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.md NOTICE.md

%endif

%changelog
