#
# spec file for package maven-surefire-plugins
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


%global base_name maven-surefire
Name:           %{base_name}-plugins
Version:        3.6.0
Release:        0
Summary:        Test framework project
License:        Apache-2.0 AND CPL-1.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/surefire/
Source0:        %{base_name}-%{version}.tar.xz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        https://www.eclipse.org/legal/cpl-v10.html
Source10:       %{base_name}-build.tar.xz
Patch0:         0001-Unshade-surefire.patch
BuildRequires:  ant
BuildRequires:  apache-commons-lang3
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-doxia-core
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-reporting-impl
BuildRequires:  maven-resolver-api
BuildRequires:  maven-shared-utils
BuildRequires:  maven-surefire
BuildRequires:  maven-surefire-report-parser
BuildRequires:  plexus-i18n
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-xml
BuildRequires:  sisu-plexus
BuildRequires:  xmvn-install
BuildRequires:  xmvn-minimal
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildArch:      noarch

%description
Surefire is a test framework project.

%package -n maven-surefire-plugin
Summary:        Surefire plugin for maven
Group:          Development/Libraries/Java

%description -n maven-surefire-plugin
Maven surefire plugin for running tests via the surefire framework.

%package -n maven-surefire-report-plugin
Summary:        Surefire reports plugin for maven
Group:          Development/Libraries/Java

%description -n maven-surefire-report-plugin
Plugin for generating reports from surefire test runs.

%package -n maven-failsafe-plugin
Summary:        Maven plugin for running integration tests
Group:          Development/Libraries/Java

%description -n maven-failsafe-plugin
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
Group:          Development/Libraries/Java

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{base_name}-%{version} -a10
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

# Remove all dependencies with scope test, since a raw xmvn does not hide them
%pom_remove_dep -r :::test:

%build
%{mvn_package} ":*tests*" __noinstall
%{mvn_package} ":{surefire,surefire-providers}" __noinstall
%{mvn_package} ":*{surefire-plugin,report-plugin}*" @1
%{mvn_package} ":*junit-platform*" junit5
%{mvn_package} ":*{failsafe-plugin,report-parser}*"  @1

%{mvn_file} ":{*}" %{base_name}/@1

mkdir -p lib
build-jar-repository -s -p lib \
    apache-commons-lang3 \
    atinject \
    commons-compress \
    commons-io \
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
    maven-surefire/maven-surefire-common \
    maven-surefire/surefire-api \
    maven-surefire/surefire-booter \
    maven-surefire/surefire-extensions-api \
    maven-surefire/surefire-logger-api \
    maven-surefire/surefire-report-parser \
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
    -f build-plugins.xml \
    package javadoc

%{mvn_artifact} pom.xml
%{mvn_artifact} surefire-providers/pom.xml

mkdir -p target/site/apidocs

for module in \
    maven-surefire-plugin \
    maven-failsafe-plugin \
    maven-surefire-report-plugin; do
  %{mvn_artifact} ${module}/pom.xml ${module}/target/${module}-%{version}.jar
  if [ -d ${module}/target/site/apidocs ]; then
    cp -r ${module}/target/site/apidocs target/site/apidocs/${module}
  fi
done

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -n maven-surefire-plugin -f .mfiles-surefire-plugin

%files -n maven-surefire-report-plugin -f .mfiles-report-plugin

%files -n maven-failsafe-plugin -f .mfiles-failsafe-plugin

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt cpl-v10.html

%changelog
