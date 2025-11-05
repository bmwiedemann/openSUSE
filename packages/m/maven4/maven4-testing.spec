#
# spec file for package maven4-testing
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%global file_version 4.0.0-rc-4
Name:           %{base_name}%{?maven_version_suffix}-testing
Version:        4.0.0~rc4
Release:        0
Summary:        Maven Plugin Testing Mechanism
# maven itself is ASL 2.0
# bundled slf4j is MIT
License:        Apache-2.0 AND MIT
Group:          Development/Tools/Building
URL:            https://maven.apache.org/
Source0:        https://archive.apache.org/dist/%{base_name}/%{base_name}-4/%{file_version}/source/apache-%{base_name}-%{file_version}-src.tar.gz
Source1:        maven-bash-completion
Source2:        mvn.1
Source10:       apache-%{base_name}-build.tar.xz
Patch1:         0001-Adapt-mvn-script.patch
# Downstream-specific, avoids dependency on logback
Patch2:         0002-Invoke-logback-via-reflection.patch
Patch3:         0001-Resolver-2.0.11-11043-11115.patch
Patch4:         maven4-resolver-2.0.13.patch
Patch5:         0001-Set-Guice-class-loading-to-CHILD-avoid-using-termina.patch
BuildRequires:  ant
BuildRequires:  apiguardian
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local
BuildRequires:  junit5-minimal
BuildRequires:  maven-resolver2-api
BuildRequires:  maven-resolver2-connector-basic
BuildRequires:  maven-resolver2-impl
BuildRequires:  maven-resolver2-spi
BuildRequires:  maven-resolver2-transport-apache
BuildRequires:  maven-resolver2-transport-file
BuildRequires:  maven4-lib
BuildRequires:  mockito
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml4
BuildRequires:  slf4j2
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
%setup -q -n apache-%{base_name}-%{file_version} -a10

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1

%pom_remove_dep -r :junit-bom
%pom_remove_dep -r :mockito-bom
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin :bom-builder3 apache-maven

%pom_remove_dep :jline-terminal-ffm impl/maven-jline
%pom_remove_dep :jline-terminal-ffm apache-maven
%pom_remove_dep -r :logback-classic

%pom_disable_module maven-executor impl

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
sed -i "
/buildNumber=/ d
/timestamp=/ d
" `find -name build.properties`
sed -i "s/version=.*/version=%{file_version}/" `find -name build.properties`
sed -i "s/distributionId=.*/distributionId=apache-maven/" `find -name build.properties`
sed -i "s/distributionShortName=.*/distributionShortName=Maven/" `find -name build.properties`
sed -i "s/distributionName=.*/distributionName=Apache\ Maven/" `find -name build.properties`

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
  maven-resolver/maven-resolver-api-2 \
  maven-resolver/maven-resolver-connector-basic-2 \
  maven-resolver/maven-resolver-impl-2 \
  maven-resolver/maven-resolver-named-locks-2 \
  maven-resolver/maven-resolver-spi-2 \
  maven-resolver/maven-resolver-util-2 \
  maven-resolver/maven-resolver-transport-apache \
  maven-resolver/maven-resolver-transport-file-2 \
  mockito/mockito-core \
  org.eclipse.sisu.plexus \
  plexus-classworlds \
  plexus/utils \
  plexus/xml-4 \
  slf4j/api-2

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
