#
# spec file for package maven-plugin-plugin-bootstrap
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


%global base_name maven-plugin-tools
%global artifactId maven-plugin-plugin
Name:           %{artifactId}-bootstrap
Version:        3.15.2
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
BuildRequires:  atinject
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-tools-annotations
BuildRequires:  maven-plugin-tools-api
BuildRequires:  maven-plugin-tools-generators
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-util
BuildRequires:  plexus-build-api0
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildArch:      noarch

%description
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%prep
%setup -q -n %{base_name}-%{version} -a1
%patch -P 0 -p1
%patch -P 20

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

%pom_remove_dep org.junit:junit-bom
%pom_remove_dep :maven-plugin-tools-ant maven-plugin-plugin
%pom_remove_dep :maven-plugin-tools-beanshell maven-plugin-plugin

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
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
    maven-resolver/maven-resolver-util \
    org.eclipse.sisu.plexus \
    plexus/plexus-build-api0 \
    plexus/utils \
    plexus-velocity/plexus-velocity

%{mvn_file} :%{artifactId} %{base_name}/%{artifactId}
pushd %{artifactId}
%{ant} \
    -Dtest.skip=true \
    jar
popd

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{base_name}
install -pm 0644 %{artifactId}/target/%{artifactId}-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/%{artifactId}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{base_name}
%{mvn_install_pom} %{artifactId}/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}/%{artifactId}.pom
%add_maven_depmap %{base_name}/%{artifactId}.pom %{base_name}/%{artifactId}.jar

%files -f .mfiles
%license LICENSE NOTICE

%changelog
