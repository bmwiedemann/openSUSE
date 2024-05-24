#
# spec file for package junit5
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global platform_version 1.10.2
%global jupiter_version %{version}
%global vintage_version %{version}
%global base_name junit5
# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Version:        5.10.2
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
Source205:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-launcher/%{platform_version}/junit-platform-launcher-%{platform_version}.pom
Source206:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-runner/%{platform_version}/junit-platform-runner-%{platform_version}.pom
Source207:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-api/%{platform_version}/junit-platform-suite-api-%{platform_version}.pom
Source208:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-reporting/%{platform_version}/junit-platform-reporting-%{platform_version}.pom
Source209:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-testkit/%{platform_version}/junit-platform-testkit-%{platform_version}.pom
Source210:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-commons/%{platform_version}/junit-platform-suite-commons-%{platform_version}.pom
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
Patch3:         0003-Bump-open-test-reporting-to-0.1.0-M2.patch
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
BuildRequires:  asciidoc
BuildRequires:  maven-local
BuildRequires:  mvn(com.univocity:univocity-parsers)
BuildRequires:  mvn(info.picocli:picocli)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.jopt-simple:jopt-simple)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.opentest4j.reporting:open-test-reporting-events)
BuildRequires:  mvn(org.opentest4j:opentest4j)
Requires:       %{base_name}-minimal >= %{version}
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

%package guide
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Requires:       %{name}-javadoc = %{version}-%{release}

%description guide
JUnit 5 User Guide.

%prep
%setup -q -n %{base_name}-r%{version} -a1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
find -name \*.jar -delete

cp -p %{SOURCE100} pom.xml
cp -p %{SOURCE200} junit-platform-commons/pom.xml
cp -p %{SOURCE201} junit-platform-console/pom.xml
cp -p %{SOURCE202} junit-platform-console-standalone/pom.xml
cp -p %{SOURCE203} junit-platform-engine/pom.xml
cp -p %{SOURCE205} junit-platform-launcher/pom.xml
cp -p %{SOURCE206} junit-platform-runner/pom.xml
cp -p %{SOURCE207} junit-platform-suite-api/pom.xml
cp -p %{SOURCE208} junit-platform-reporting/pom.xml
cp -p %{SOURCE209} junit-platform-testkit/pom.xml
cp -p %{SOURCE210} junit-platform-suite-commons/pom.xml
cp -p %{SOURCE300} junit-jupiter/pom.xml
cp -p %{SOURCE301} junit-jupiter-api/pom.xml
cp -p %{SOURCE302} junit-jupiter-engine/pom.xml
cp -p %{SOURCE303} junit-jupiter-migrationsupport/pom.xml
cp -p %{SOURCE304} junit-jupiter-params/pom.xml
cp -p %{SOURCE400} junit-vintage-engine/pom.xml
cp -p %{SOURCE500} junit-bom/pom.xml

for pom in $(find -mindepth 2 -name pom.xml | grep -v tests/); do
    module=$(dirname $pom)
    if [ -d ${module}/src/module ]; then
      mkdir -p ${module}/src/main/java
      mv ${module}/src/module/*/module-info.java ${module}/src/main/java/
    fi
    # Set parent to aggregator
    %pom_add_parent org.fedoraproject.xmvn.junit5:aggregator:any $pom
    # OSGi BSN
    bsn=$(sed 's|/pom.xml$||;s|.*/|org.|;s|-|.|g' <<<"$pom")
    %pom_xpath_inject pom:project "<properties><osgi.bsn>${bsn}</osgi.bsn></properties>" $pom
    # Incorrect scope - API guardian is just annotation, needed only during compilation
    %pom_xpath_set -f "pom:dependency[pom:artifactId='apiguardian-api']/pom:scope" provided $pom
    %pom_xpath_set -f "pom:dependency[pom:scope='runtime']/pom:scope" compile $pom
done

%pom_remove_parent junit-bom

# Add deps which are shaded by upstream and therefore not present in POMs.
%pom_add_dep net.sf.jopt-simple:jopt-simple:5.0.4 junit-platform-console
%pom_add_dep com.univocity:univocity-parsers:2.5.4 junit-jupiter-params
%pom_add_dep org.opentest4j.reporting:open-test-reporting-events:0.1.0-M2 junit-platform-reporting
%pom_add_dep info.picocli:picocli:4.7.5 junit-platform-console

# Disable the standalone console (just jar with shaded dependencies)
%pom_disable_module junit-platform-console-standalone
# Disable the modules built in -minimal package
%pom_disable_module junit-platform-commons
%pom_disable_module junit-jupiter-api

%{mvn_package} :junit-bom bom
%{mvn_package} :aggregator __noinstall

%build
%if %{with bootstrap}
mkdir -p lib
build-jar-repository -s lib opentest4j/opentest4j apiguardian/apiguardian-api
%{ant} package javadoc
%else
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dencoding=utf-8 -Dsource=8

# Build docs.  Ignore exit asciidoc -- it fails for some reason, but
# still produces readable docs.
asciidoc documentation/src/docs/asciidoc/index.adoc || :
ln -s ../../javadoc/junit5 documentation/src/docs/api
%endif

%install
%if %{with bootstrap}

install -dm 0755 %{buildroot}%{_javadir}/%{base_name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{base_name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for i in junit-platform-commons junit-jupiter-api; do
    install -pm 0644 ${i}/target/${i}*.jar %{buildroot}%{_javadir}/%{base_name}/${i}.jar
    %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}/${i}.pom
    %add_maven_depmap %{base_name}/${i}.pom %{base_name}/${i}.jar
    cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
done

%else

%mvn_install
%jpackage_script org/junit/platform/console/ConsoleLauncher "" "" junit5:junit:hamcrest:opentest4j:open-test-reporting:picocli:jopt-simple:assertj-core %{name} true
%fdupes -s documentation/src/docs/

%endif

%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.md LICENSE-notice.md

%if %{without bootstrap}

%{_bindir}/%{name}

%files bom -f .mfiles-bom
%license LICENSE.md LICENSE-notice.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md LICENSE-notice.md

%files guide
%doc documentation/src/docs/*

%else

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.md LICENSE-notice.md

%endif

%changelog
