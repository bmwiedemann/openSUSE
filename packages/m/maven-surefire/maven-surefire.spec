#
# spec file for package maven-surefire
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


Name:           maven-surefire
Version:        3.6.0
Release:        0
Summary:        Test framework project
License:        Apache-2.0 AND CPL-1.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/surefire/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        https://www.eclipse.org/legal/cpl-v10.html
Source10:       %{name}-build.tar.xz
Patch0:         0001-Unshade-surefire.patch
BuildRequires:  ant
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javacc
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsr-305
BuildRequires:  junit5-minimal
BuildRequires:  maven-common-artifact-filters
BuildRequires:  maven-doxia-core
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-reporting-api
BuildRequires:  maven-reporting-impl
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-impl
BuildRequires:  maven-resolver-named-locks
BuildRequires:  maven-resolver-util
BuildRequires:  maven-shared-utils
BuildRequires:  objectweb-asm
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-i18n
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-languages
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
# PpidChecker relies on /usr/bin/ps to check process uptime
Requires:       procps
Obsoletes:      %{name}-provider-junit
Obsoletes:      %{name}-provider-testng
BuildArch:      noarch

%description
Surefire is a test framework project.

%package provider-junit5
Summary:        JUnit 5 provider for Maven Surefire
Group:          Development/Libraries/Java

%description provider-junit5
JUnit 5 provider for Maven Surefire.

%package report-parser
Summary:        Parses report output files from surefire
Group:          Development/Libraries/Java

%description report-parser
Plugin for parsing report output files from surefire.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Provides:       %{name}-provider-junit5-javadoc
Obsoletes:      %{name}-provider-junit5-javadoc

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -a10
cp -p %{SOURCE1} %{SOURCE2} .

%patch -P 0 -p1

# Disable strict doclint
sed -i /-Xdoclint:all/d pom.xml

# QA plugin useful only for upstream
%pom_remove_plugin -r :jacoco-maven-plugin
# Not wanted
%pom_remove_plugin -r :maven-shade-plugin
# Not packaged
%pom_remove_plugin -r :animal-sniffer-maven-plugin
# Complains
%pom_remove_plugin -r :apache-rat-plugin

%pom_disable_module surefire-shadefire
%pom_remove_dep -r :surefire-shadefire

%pom_remove_dep -r :mockito-bom
%pom_remove_dep -r :junit-bom

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-its

# We don't need site-source
%pom_remove_plugin :maven-assembly-plugin maven-surefire-plugin

%build
%{mvn_package} ":*tests*" __noinstall
%{mvn_package} ":{surefire,surefire-providers}" __noinstall
%{mvn_package} ":*{surefire-plugin,report-plugin}*" @1
%{mvn_package} ":*junit-platform*" junit5
%{mvn_package} ":*{failsafe-plugin,report-parser}*"  @1

mkdir -p lib
build-jar-repository -s -p lib \
    apache-commons-lang3 \
    atinject \
    commons-compress \
    commons-io \
    jsr-305 \
    junit5/junit-jupiter-api \
    junit5/junit-platform-commons \
    junit5/junit-platform-engine \
    junit5/junit-platform-launcher \
    maven-common-artifact-filters/maven-common-artifact-filters \
    maven-doxia/doxia-core \
    maven-doxia/doxia-sink-api \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven/maven-plugin-api \
    maven/maven-settings \
    maven-plugin-tools/maven-plugin-annotations \
    maven-reporting-api/maven-reporting-api \
    maven-reporting-impl/maven-reporting-impl \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-impl \
    maven-resolver/maven-resolver-named-locks \
    maven-resolver/maven-resolver-util \
    maven-shared-utils/maven-shared-utils \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus-containers/plexus-component-annotations \
    plexus-i18n/plexus-i18n \
    plexus/interpolation \
    plexus-languages/plexus-java \
    plexus/utils \
    plexus/xml \
    slf4j/api

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
    surefire-extensions-api \
    surefire-extensions-spi \
    maven-surefire-common \
    surefire-report-parser; do
  %{mvn_artifact} ${module}/pom.xml ${module}/target/${module}-%{version}.jar
  if [ -d ${module}/target/site/apidocs ]; then
    cp -r ${module}/target/site/apidocs target/site/apidocs/${module}
  fi
done
for module in \
    common-java5 \
    surefire-junit-platform; do
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

%files report-parser -f .mfiles-report-parser

%files provider-junit5 -f .mfiles-junit5

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt cpl-v10.html

%changelog
