#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global base_name maven-plugin-tools
%global artifactId maven-plugin-plugin
Name:           %{artifactId}-bootstrap
Version:        3.9.0
Release:        0
Summary:        Maven Plugin Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugin-tools/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/%{base_name}/%{version}/%{base_name}-%{version}-source-release.zip
Source1:        %{base_name}-build.tar.xz
Patch0:         0002-Remove-dependency-on-jtidy.patch
# The maven-plugin-plugin is used to generate those descriptors, which
# creates a circular dependency of maven-plugin-plugin on itself.
# We generated those ones outside the rpm build for a bootstrap package.
Patch20:        maven-plugin-plugin-bootstrap-resouces.patch
BuildRequires:  ant
BuildRequires:  javapackages-local
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-tools-api
BuildRequires:  maven-plugin-tools-generators
BuildRequires:  maven-resolver-api
BuildRequires:  plexus-build-api
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-annotations)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-java)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildArch:      noarch

%description
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%prep
%setup -q -n %{base_name}-%{version} -a1
%patch0 -p1
%patch20

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

# Remove test dependencies because tests are skipped anyways.
%pom_xpath_remove "pom:dependency[pom:scope='test']"

%pom_remove_dep org.junit:junit-bom
%pom_remove_dep :maven-plugin-tools-ant maven-plugin-plugin
%pom_remove_dep :maven-plugin-tools-beanshell maven-plugin-plugin

%{mvn_package} :maven-plugin-tools __noinstall

%build
mkdir -p lib
build-jar-repository -s lib \
	maven/maven-artifact \
	maven/maven-core \
	maven/maven-model \
	maven/maven-plugin-api \
	maven/maven-repository-metadata \
	maven/maven-settings \
	maven-plugin-tools/maven-plugin-annotations \
	maven-plugin-tools/maven-plugin-tools-api \
	maven-plugin-tools/maven-plugin-tools-generators \
    maven-resolver/maven-resolver-api \
	org.eclipse.sisu.inject \
	org.eclipse.sisu.plexus \
    plexus/plexus-build-api \
	plexus/utils \
	plexus-velocity/plexus-velocity

%{mvn_file} :%{artifactId} %{base_name}/%{artifactId}
pushd %{artifactId}
%{ant} \
	-Dtest.skip=true \
	jar
popd
%{mvn_artifact} pom.xml
%{mvn_artifact} %{artifactId}/pom.xml %{artifactId}/target/%{artifactId}-%{version}.jar

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
