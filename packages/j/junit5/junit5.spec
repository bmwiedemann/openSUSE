#
# spec file for package junit5
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global platform_version 1.5.2
%global jupiter_version %{version}
%global vintage_version %{version}
%bcond_without console
Name:           junit5
Version:        5.5.2
Release:        0
Summary:        Java regression testing framework
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://junit.org/junit5/
Source0:        https://github.com/junit-team/junit5/archive/r%{version}/junit5-%{version}.tar.gz
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
# Jupiter POMs
Source301:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-api/%{jupiter_version}/junit-jupiter-api-%{jupiter_version}.pom
Source302:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-engine/%{jupiter_version}/junit-jupiter-engine-%{jupiter_version}.pom
Source303:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-migrationsupport/%{jupiter_version}/junit-jupiter-migrationsupport-%{jupiter_version}.pom
Source304:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-params/%{jupiter_version}/junit-jupiter-params-%{jupiter_version}.pom
Source305:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter/%{jupiter_version}/junit-jupiter-%{jupiter_version}.pom
# Vintage POM
Source400:      https://repo1.maven.org/maven2/org/junit/vintage/junit-vintage-engine/%{vintage_version}/junit-vintage-engine-%{vintage_version}.pom
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.univocity:univocity-parsers)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.opentest4j:opentest4j)
BuildArch:      noarch
%if %{with console}
BuildRequires:  mvn(info.picocli:picocli)
# Explicit requires for javapackages-tools since junit5 script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
%endif

%description
JUnit is a popular regression testing framework for Java platform.

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
%setup -q -n %{name}-r%{version}
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
cp -p %{SOURCE301} junit-jupiter-api/pom.xml
cp -p %{SOURCE302} junit-jupiter-engine/pom.xml
cp -p %{SOURCE303} junit-jupiter-migrationsupport/pom.xml
cp -p %{SOURCE304} junit-jupiter-params/pom.xml
cp -p %{SOURCE305} junit-jupiter/pom.xml
cp -p %{SOURCE400} junit-vintage-engine/pom.xml

for pom in $(find -mindepth 2 -name pom.xml); do
    # Set parent to aggregator
    %pom_xpath_inject pom:project "<parent><groupId>org.fedoraproject.xmvn.junit5</groupId><artifactId>aggregator</artifactId><version>1.0.0</version></parent>" $pom
    # OSGi BSN
    bsn=$(sed 's|/pom.xml$||;s|.*/|org.|;s|-|.|g' <<<"$pom")
    %pom_xpath_inject pom:project "<properties><osgi.bsn>${bsn}</osgi.bsn></properties>" $pom
    # Incorrect scope - API guardian is just annotation, needed only during compilation
    %pom_xpath_set -f "pom:dependency[pom:artifactId='apiguardian-api']/pom:scope" provided $pom
done

# Add deps which are shaded by upstream and therefore not present in POMs.
%pom_add_dep info.picocli:picocli:4.0.4 junit-platform-console
%pom_add_dep com.univocity:univocity-parsers:2.5.4 junit-jupiter-params

# Incorrect scope - Junit4 is needed for compilation too, not only runtime.
%pom_xpath_set "pom:dependency[pom:artifactId='junit']/pom:scope" compile junit-vintage-engine

%if %{without console}
# Disable the console modules
%pom_disable_module junit-platform-console
%pom_disable_module junit-platform-console-standalone
%endif

%{mvn_package} :aggregator __noinstall

%build
%{mvn_build} -f -- -Dencoding=utf-8 -Dsource=8

# Build docs.  Ignore exit asciidoc -- it fails for some reason, but
# still produces readable docs.
asciidoc documentation/src/docs/asciidoc/index.adoc || :
ln -s ../../javadoc/junit5 documentation/src/docs/api

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
%fdupes -s documentation/src/docs/

%if %{with console}
%jpackage_script org/junit/platform/console/ConsoleLauncher "" "" junit5:junit:opentest4j:jopt-simple %{name} true
%endif

%files -f .mfiles
%if %{with console}
%{_bindir}/%{name}
%endif
%license LICENSE.md LICENSE-notice.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md LICENSE-notice.md

%files guide
%doc documentation/src/docs/*

%changelog
