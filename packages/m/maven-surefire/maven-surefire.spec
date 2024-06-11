#
# spec file for package maven-surefire
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


Name:           maven-surefire
Version:        3.2.5
Release:        0
Summary:        Test framework project
License:        Apache-2.0 AND CPL-1.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/surefire/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        https://www.eclipse.org/legal/cpl-v10.html
Source10:       %{name}-build.tar.xz
Patch0:         0001-Port-to-TestNG-7.4.0.patch
Patch10:        %{name}-bootstrap-resources.patch
BuildRequires:  ant
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javacc
BuildRequires:  javapackages-local
BuildRequires:  jdom
BuildRequires:  jsr-305
BuildRequires:  junit
BuildRequires:  maven-common-artifact-filters
BuildRequires:  maven-doxia-core
BuildRequires:  maven-doxia-logging-api
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-reporting-api
BuildRequires:  maven-reporting-impl
BuildRequires:  maven-resolver
BuildRequires:  maven-shared-utils
BuildRequires:  plexus-i18n
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-languages
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  testng
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
# PpidChecker relies on /usr/bin/ps to check process uptime
Requires:       procps
BuildArch:      noarch

%description
Surefire is a test framework project.

%package plugin-bootstrap
Summary:        Surefire plugin for maven
Group:          Development/Libraries/Java

%description plugin-bootstrap
Maven surefire plugin for running tests via the surefire framework.

%package report-plugin-bootstrap
Summary:        Surefire reports plugin for maven
Group:          Development/Libraries/Java

%description report-plugin-bootstrap
Plugin for generating reports from surefire test runs.

%package provider-junit
Summary:        JUnit provider for Maven Surefire
Group:          Development/Libraries/Java

%description provider-junit
JUnit provider for Maven Surefire.

%package provider-testng
Summary:        TestNG provider for Maven Surefire
Group:          Development/Libraries/Java

%description provider-testng
TestNG provider for Maven Surefire.

%package report-parser
Summary:        Parses report output files from surefire
Group:          Development/Libraries/Java

%description report-parser
Plugin for parsing report output files from surefire.

%package -n maven-failsafe-plugin-bootstrap
Summary:        Maven plugin for running integration tests
Group:          Development/Libraries/Java

%description -n maven-failsafe-plugin-bootstrap
The Failsafe Plugin is designed to run integration tests while the
Surefire Plugins is designed to run unit. The name (failsafe) was
chosen both because it is a synonym of surefire and because it implies
that when it fails, it does so in a safe way.

If you use the Surefire Plugin for running tests, then when you have a
test failure, the build will stop at the integration-test phase and
your integration test environment will not have been torn down
correctly.

The Failsafe Plugin is used during the integration-test and verify
phases of the build lifecycle to execute the integration tests of an
application. The Failsafe Plugin will not fail the build during the
integration-test phase thus enabling the post-integration-test phase
to execute.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -a10
cp -p %{SOURCE1} %{SOURCE2} .

%patch -P 0 -p1
#patch -P 1 -p1
%patch -P 10 -p1

# Disable strict doclint
sed -i /-Xdoclint:all/d pom.xml

%pom_remove_dep org.junit:junit-bom

%pom_disable_module surefire-shadefire
%pom_remove_dep -r org.apache.maven.surefire:surefire-shadefire

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-its

# QA plugin useful only for upstream
%pom_remove_plugin -r :jacoco-maven-plugin
# Not wanted
%pom_remove_plugin -r :maven-shade-plugin

find -name *.java -exec sed -i -e s/org.apache.maven.surefire.shared.utils/org.apache.maven.shared.utils/ -e s/org.apache.maven.surefire.shared.io/org.apache.commons.io/ -e s/org.apache.maven.surefire.shared.lang3/org.apache.commons.lang3/ -e s/org.apache.maven.surefire.shared.compress/org.apache.commons.compress/ {} \;

# Not packaged
%pom_remove_plugin -r :animal-sniffer-maven-plugin
# Complains
%pom_remove_plugin -r :apache-rat-plugin
# We don't need site-source
%pom_remove_plugin :maven-assembly-plugin maven-surefire-plugin
%pom_remove_dep -r ::::site-source

%build
%{mvn_package} ":*tests*" __noinstall
%{mvn_package} ":{surefire,surefire-providers}" __noinstall
%{mvn_package} ":*{surefire-plugin,report-plugin}*" @1
%{mvn_package} ":*junit-platform*" junit5
%{mvn_package} ":*{junit,testng,failsafe-plugin,report-parser}*"  @1

mkdir -p lib
build-jar-repository -s -p lib \
    atinject \
    apache-commons-lang3 \
    commons-compress \
    commons-io \
    javacc \
    jsr-305 \
    junit \
    maven-common-artifact-filters/maven-common-artifact-filters \
    maven-doxia/doxia-core \
    maven-doxia/doxia-logging-api \
    maven-doxia/doxia-sink-api \
    maven-doxia-sitetools/doxia-site-renderer \
    maven/maven-artifact \
    maven/maven-compat \
    maven/maven-core \
    maven/maven-model \
    maven/maven-plugin-api \
    maven/maven-settings \
    maven-plugin-tools/maven-plugin-annotations \
    maven-reporting-api/maven-reporting-api \
    maven-reporting-impl/maven-reporting-impl \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-util \
    maven-shared-utils/maven-shared-utils \
    org.eclipse.sisu.plexus \
    org.eclipse.sisu.inject \
    plexus-containers/plexus-component-annotations \
    plexus-i18n/plexus-i18n \
    plexus/interpolation \
    plexus-languages/plexus-java \
    plexus/utils \
    plexus/xml \
    testng

%{ant} \
    -Dtest.skip=true \
    package javadoc

%{mvn_artifact} pom.xml
%{mvn_artifact} surefire-providers/pom.xml

mkdir -p target/site/apidocs

for module in \
    surefire-logger-api \
    surefire-api \
    surefire-booter \
    surefire-grouper \
    surefire-extensions-api \
    surefire-extensions-spi \
    surefire-shared-utils \
    maven-surefire-common \
    surefire-report-parser \
    maven-surefire-plugin \
    maven-failsafe-plugin \
    maven-surefire-report-plugin; do
  %{mvn_artifact} ${module}/pom.xml ${module}/target/${module}-%{version}.jar
  if [ -d ${module}/target/site/apidocs ]; then
    cp -r ${module}/target/site/apidocs target/site/apidocs/${module}
  fi
done
for module in \
    common-junit3 \
    common-java5 \
    common-junit4 \
    common-junit48 \
    surefire-junit3 \
    surefire-junit4 \
    surefire-junit47 \
    surefire-testng-utils \
    surefire-testng; do
  %{mvn_artifact} surefire-providers/${module}/pom.xml \
    surefire-providers/${module}/target/${module}-%{version}.jar
  if [ -d surefire-providers/${module}/target/site/apidocs ]; then
    cp -r surefire-providers/${module}/target/site/apidocs target/site/apidocs/${module}
  fi
done

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE-2.0.txt cpl-v10.html

%files plugin-bootstrap -f .mfiles-surefire-plugin

%files report-plugin-bootstrap -f .mfiles-report-plugin

%files report-parser -f .mfiles-report-parser

%files provider-junit -f .mfiles-junit

%files provider-testng -f .mfiles-testng

%files -n maven-failsafe-plugin-bootstrap -f .mfiles-failsafe-plugin

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt cpl-v10.html

%changelog
