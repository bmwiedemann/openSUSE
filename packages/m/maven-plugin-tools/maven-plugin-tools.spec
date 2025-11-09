#
# spec file for package maven-plugin-tools
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


%global base_ver 4.0.0
%global beta_ver 2
%global file_ver %{base_ver}-beta-%{beta_ver}
Name:           maven-plugin-tools
Version:        %{base_ver}~beta%{beta_ver}
Release:        0
Summary:        Maven Plugin Tools
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugin-tools/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{file_ver}/%{name}-%{file_ver}-source-release.zip
Source1:        %{name}-build.tar.xz
Patch0:         0002-Remove-dependency-on-jtidy.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsoup
BuildRequires:  maven-lib
BuildRequires:  maven-reporting-api
BuildRequires:  maven-resolver-api
BuildRequires:  maven-wagon-provider-api
BuildRequires:  objectweb-asm >= 9.9
BuildRequires:  plexus-archiver
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-languages
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  plexus-xml
BuildRequires:  qdox
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  unzip
BuildRequires:  velocity
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildArch:      noarch

%description
The Maven Plugin Tools contains the necessary tools to be able to produce Maven
Plugins in a variety of languages.

%package -n maven-plugin-annotations
Summary:        Maven Plugin Java 5 Annotations
Group:          Development/Libraries/Java

%description -n maven-plugin-annotations
This package contains Java 5 annotations to use in Mojos.

%package annotations
Summary:        Maven Plugin Tool for Annotations
Group:          Development/Libraries/Java

%description annotations
This package provides Java 5 annotation tools for use with Apache Maven.

%package api
Summary:        Maven Plugin Tools APIs
Group:          Development/Libraries/Java
# Packages removed between 3.x and 4.x
Obsoletes:      %{name}-ant
Obsoletes:      %{name}-beanshell
Obsoletes:      %{name}-java
Obsoletes:      %{name}-model
Obsoletes:      maven-script-ant
Obsoletes:      maven-script-beanshell

%description api
The Maven Plugin Tools API provides an API to extract information from
and generate documentation for Maven Plugins.

%package generators
Summary:        Maven Plugin Tools Generators
Group:          Development/Libraries/Java

%description generators
The Maven Plugin Tools Generators provides content generation
(documentation, help) from plugin descriptor.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -a1 -n %{name}-%{file_ver}
%patch -P 0 -p1

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

%pom_remove_dep net.sf.jtidy:jtidy maven-plugin-tools-generators

%{mvn_package} :maven-plugin-tools __noinstall
%{mvn_package} :maven-script __noinstall
%{mvn_package} :{*} @1

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    httpcomponents/httpclient \
    httpcomponents/httpcore \
    jsoup/jsoup \
    maven/maven-api-plugin \
    maven/maven-artifact \
    maven/maven-compat \
    maven/maven-core \
    maven/maven-model \
    maven/maven-plugin-api \
    maven/maven-settings \
    maven-reporting-api/maven-reporting-api \
    maven-resolver/maven-resolver-api \
    maven-wagon/provider-api \
    objectweb-asm/asm \
    objectweb-asm/asm-commons \
    objectweb-asm/asm-util \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus/archiver \
    plexus-classworlds \
    plexus-languages/plexus-java \
    plexus/utils \
    plexus/xml \
    plexus-velocity/plexus-velocity \
    qdox \
    slf4j/api \
    velocity

%{ant} \
    -Dtest.skip=true \
    package javadoc

%{mvn_artifact} pom.xml
mkdir -p target/site/apidocs
for i in \
    maven-plugin-annotations \
    maven-plugin-tools-annotations \
    maven-plugin-tools-api \
    maven-plugin-tools-generators; do
  %{mvn_artifact} ${i}/pom.xml ${i}/target/${i}-%{file_ver}.jar
  if [ -d ${i}/target/site/apidocs ]; then
    cp -r ${i}/target/site/apidocs target/site/apidocs/${i}
  fi
done

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -n maven-plugin-annotations -f .mfiles-maven-plugin-annotations

%files annotations -f .mfiles-maven-plugin-tools-annotations
%license LICENSE NOTICE

%files api -f .mfiles-maven-plugin-tools-api
%license LICENSE NOTICE

%files generators -f .mfiles-maven-plugin-tools-generators

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
