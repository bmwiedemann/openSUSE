#
# spec file for package maven4-testing
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


%global maven_version_suffix 4
%global base_name maven
%global file_version 4.0.0-SNAPSHOT
Name:           %{base_name}%{?maven_version_suffix}-testing
Version:        4.0.0~20260724.2b1209f9a3
Release:        0
Summary:        Maven Plugin Testing Mechanism
# maven itself is ASL 2.0
# bundled slf4j is MIT
License:        Apache-2.0 AND MIT
Group:          Development/Tools/Building
URL:            https://maven.apache.org/
Source0:        %{base_name}-%{version}.tar.xz
Source1:        maven-bash-completion
Source2:        mvn.1
Source10:       %{base_name}-build.tar.xz
Patch1:         0001-Adapt-mvn-script.patch
Patch2:         0002-Invoke-logback-via-reflection.patch
BuildRequires:  ant
BuildRequires:  apiguardian
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local
BuildRequires:  junit5-minimal
BuildRequires:  maven-resolver-api >= 2.0.17
BuildRequires:  maven-resolver-connector-basic
BuildRequires:  maven-resolver-impl
BuildRequires:  maven-resolver-spi
BuildRequires:  maven-resolver-transport-apache
BuildRequires:  maven-resolver-transport-file
BuildRequires:  maven4-lib
BuildRequires:  mockito
BuildRequires:  opentest4j
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-sec-dispatcher4
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml4
BuildRequires:  slf4j
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)

%description
The Maven Plugin Testing Harness provides mechanisms to manage tests
on Mojo.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{base_name}-%{version} -a10

%patch -P 1 -p1
%patch -P 2 -p1

%pom_xpath_set pom:project/pom:properties/pom:plexusXmlVersion 4

%pom_remove_dep -r :junit-bom
%pom_remove_dep -r :mockito-bom
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin :bom-builder3 apache-maven

%pom_remove_dep :jline-terminal-ffm impl/maven-jline
%pom_remove_dep :jline-terminal-ffm apache-maven
%pom_remove_dep -r :logback-classic

find -name '*.java' -exec sed -i 's/\r//' {} +
find -name 'pom.xml' -exec sed -i 's/\r//' {} +

sed -i "s/@{maven_version_suffix}/%{?maven_version_suffix}/" apache-maven/src/assembly/maven/bin/mvn

# not really used during build, but a precaution
find -name '*.jar' -not -path '*/test/*' -delete
find -name '*.class' -delete
find -name '*.bat' -delete

#sed -i 's:\r::' apache-maven/src/conf/settings.xml

# Downloads dependency licenses from the Internet and aggregates them.
# We already ship the licenses in their respective packages.
rm apache-maven/src/main/appended-resources/META-INF/LICENSE.vm

# Disable plugins which are not useful for us
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin

%{mvn_package} :apache-maven __noinstall
%{mvn_package} ::mdo: __noinstall

%{mvn_file} :{*} %{base_name}/@1

%build

mkdir -p lib
build-jar-repository -s lib \
  apiguardian/apiguardian-api \
  junit5/junit-jupiter-api \
  junit5/junit-platform-commons \
  maven/maven-api-annotations \
  maven/maven-api-core \
  maven/maven-api-di \
  maven/maven-api-model \
  maven/maven-api-plugin \
  maven/maven-api-settings \
  maven/maven-api-spi \
  maven/maven-api-toolchain \
  maven/maven-api-xml \
  maven/maven-core-4 \
  maven/maven-di \
  maven/maven-impl \
  maven/maven-model-4 \
  maven/maven-plugin-api-4 \
  maven/maven-support \
  maven/maven-xml \
  maven-resolver/maven-resolver-api \
  maven-resolver/maven-resolver-connector-basic \
  maven-resolver/maven-resolver-impl \
  maven-resolver/maven-resolver-named-locks \
  maven-resolver/maven-resolver-spi \
  maven-resolver/maven-resolver-util \
  maven-resolver/maven-resolver-transport-apache \
  maven-resolver/maven-resolver-transport-file \
  mockito/mockito-core \
  opentest4j/opentest4j \
  org.eclipse.sisu.plexus \
  plexus-classworlds \
  plexus/sec-dispatcher-4 \
  plexus/utils \
  plexus/xml-4 \
  slf4j/api

%{ant} -f impl/maven-testing/build.xml \
  package javadoc

%{mvn_artifact} pom.xml
%{mvn_package} :maven __noinstall
%{mvn_artifact} impl/pom.xml
%{mvn_package} :maven-impl-modules __noinstall

%{mvn_artifact} impl/maven-testing/pom.xml impl/maven-testing/target/maven-testing-%{file_version}.jar

%install
%mvn_install -J impl/maven-testing/target/site/apidocs

%fdupes %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
