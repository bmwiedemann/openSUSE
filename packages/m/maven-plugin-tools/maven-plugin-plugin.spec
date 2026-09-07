#
# spec file for package maven-plugin-plugin
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


%global base_ver 4.0.0
%global beta_ver 2
%global file_ver %{base_ver}-beta-%{beta_ver}
%global base_name maven-plugin-tools
Name:           maven-plugin-plugin
Version:        %{base_ver}~beta%{beta_ver}
Release:        0
Summary:        Maven Plugin Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugin-tools/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/%{base_name}/%{file_ver}/%{base_name}-%{file_ver}-source-release.zip
Source1:        %{base_name}-build.tar.xz
Patch0:         0001-A-standalone-generator-of-HelpMojo.java-and-plugin-d.patch
Patch1:         0002-Remove-dependency-on-jtidy.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-tools-annotations
BuildRequires:  maven-plugin-tools-api
BuildRequires:  maven-plugin-tools-generators
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-util
BuildRequires:  objectweb-asm >= 9.9
BuildRequires:  plexus-build-api0
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-minimal
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
Obsoletes:      %{name}-bootstrap
BuildArch:      noarch

%description
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{file_ver} -a1
%patch -P 0 -p1
%patch -P 1 -p1

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

# Remove all dependencies with scope test, since a raw xmvn does not hide them
%pom_remove_dep -r :::test:

%build
mkdir -p lib
build-jar-repository -s lib \
    apache-commons-lang3 \
    atinject \
    jsoup/jsoup \
    maven/maven-artifact \
    maven/maven-builder-support \
    maven/maven-core \
    maven/maven-model \
    maven/maven-model-builder \
    maven/maven-plugin-api \
    maven/maven-repository-metadata \
    maven/maven-resolver-provider \
    maven/maven-settings \
    maven-plugin-tools/maven-plugin-annotations \
    maven-plugin-tools/maven-plugin-tools-api \
    maven-plugin-tools/maven-plugin-tools-generators \
    maven-plugin-tools/maven-plugin-tools-annotations \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-util \
    objectweb-asm/asm-all \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus/archiver \
    plexus-classworlds \
    plexus/interpolation \
    plexus/io \
    plexus/plexus-build-api0 \
    plexus/utils \
    plexus/xml \
    plexus-velocity/plexus-velocity \
    qdox \
    slf4j/api \
    velocity-engine/velocity-engine-core \
    xmvn

%{mvn_file} :%{name} %{base_name}/%{name}
%{mvn_package} :%{base_name} __noinstall
pushd %{name}
ant \
    -Dtest.skip=true \
    jar
ant \
    -f build-stage2.xml \
    -Dtest.skip=true \
    jar javadoc
%{mvn_artifact} ../pom.xml
%{mvn_artifact} pom.xml target/%{name}-%{file_ver}.jar
popd

%install
pushd %{name}
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f %{name}/.mfiles
%license LICENSE NOTICE

%files javadoc -f %{name}/.mfiles-javadoc
%license LICENSE NOTICE

%changelog
