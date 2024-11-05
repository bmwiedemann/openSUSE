#
# spec file for package maven-surefire-plugins
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


%global base_name maven-surefire
Name:           %{base_name}-plugins
Version:        3.5.2
Release:        0
Summary:        Test framework project
License:        Apache-2.0 AND CPL-1.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/surefire/
Source0:        %{base_name}-%{version}.tar.xz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        https://www.eclipse.org/legal/cpl-v10.html
Patch0:         0001-Port-to-TestNG-7.4.0.patch
Patch1:         0002-Unshade-surefire.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.surefire:maven-surefire-common)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-api)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-booter)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-extensions-api)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-logger-api)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-report-parser)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
#!BuildRequires: maven-compiler-plugin-bootstrap
#!BuildRequires: maven-jar-plugin-bootstrap
#!BuildRequires: maven-plugin-plugin-bootstrap
#!BuildRequires: maven-resources-plugin-bootstrap
#!BuildRequires: maven-surefire-plugin-bootstrap
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
%setup -q -n %{base_name}-%{version}
cp -p %{SOURCE1} %{SOURCE2} .

%patch -P 0 -p1
%patch -P 1 -p1

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

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-its

# We don't need site-source
%pom_remove_plugin :maven-assembly-plugin maven-surefire-plugin

# Disable all modules besides the 3 plugins
for module in \
    maven-surefire-common \
    surefire-api \
    surefire-booter \
    surefire-grouper \
    surefire-extensions-api \
    surefire-extensions-spi \
    surefire-its \
    surefire-logger-api \
    surefire-providers \
    surefire-report-parser; do
  %pom_disable_module ${module}
done

%build
%{mvn_package} ":*tests*" __noinstall
%{mvn_package} ":{surefire,surefire-providers}" __noinstall
%{mvn_package} ":*{surefire-plugin,report-plugin}*" @1
%{mvn_package} ":*junit-platform*" junit5
%{mvn_package} ":*{junit,testng,failsafe-plugin,report-parser}*"  @1

%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -n maven-surefire-plugin -f .mfiles-surefire-plugin

%files -n maven-surefire-report-plugin -f .mfiles-report-plugin

%files -n maven-failsafe-plugin -f .mfiles-failsafe-plugin

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt cpl-v10.html

%changelog
