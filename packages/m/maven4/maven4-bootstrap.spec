#
# spec file for package maven4-bootstrap
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
%global file_version 4.0.0-rc-5
Name:           %{base_name}%{?maven_version_suffix}-bootstrap
Version:        4.0.0~rc5
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
Patch3:         0001-Fix-a-ConcurrentModificationException-11429.patch
Patch4:         0002-Fix-field-accessibility-leak-in-EnhancedCompositeBea.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local
BuildRequires:  plexus-xml
BuildRequires:  sisu-plexus
BuildRequires:  stax2-api
BuildRequires:  woodstox-core
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%prep
%setup -q -n apache-%{base_name}-%{file_version} -a10

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

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
    org.eclipse.sisu.plexus \
    plexus/xml \
    stax2-api \
    woodstox-core

%{ant} -f build-bootstrap.xml \
  package

%{mvn_artifact} pom.xml
%{mvn_package} :maven __noinstall
%{mvn_artifact} api/pom.xml
%{mvn_package} :maven-api __noinstall
%{mvn_artifact} impl/pom.xml
%{mvn_package} :maven-impl-modules __noinstall

%{mvn_artifact} api/maven-api-annotations/pom.xml api/maven-api-annotations/target/maven-api-annotations-%{file_version}.jar
%{mvn_artifact} api/maven-api-xml/pom.xml api/maven-api-xml/target/maven-api-xml-%{file_version}.jar
%{mvn_artifact} impl/maven-xml/pom.xml impl/maven-xml/target/maven-xml-%{file_version}.jar

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
