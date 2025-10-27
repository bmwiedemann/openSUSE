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


Name:           maven-plugin-tools
Version:        3.15.2
Release:        0
Summary:        Maven Plugin Tools
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugin-tools/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.tar.xz
Patch0:         0002-Remove-dependency-on-jtidy.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  bsh2
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
BuildRequires:  modello >= 2.0.0
BuildRequires:  objectweb-asm >= 9.7
BuildRequires:  plexus-ant-factory
BuildRequires:  plexus-archiver
BuildRequires:  plexus-bsh-factory
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

%package ant
Summary:        Maven Plugin Tool for Ant
Group:          Development/Libraries/Java

%description ant
Descriptor extractor for plugins written in Ant.

%package api
Summary:        Maven Plugin Tools APIs
Group:          Development/Libraries/Java

%description api
The Maven Plugin Tools API provides an API to extract information from
and generate documentation for Maven Plugins.

%package beanshell
Summary:        Maven Plugin Tool for Beanshell
Group:          Development/Libraries/Java

%description beanshell
Descriptor extractor for plugins written in Beanshell.

%package generators
Summary:        Maven Plugin Tools Generators
Group:          Development/Libraries/Java

%description generators
The Maven Plugin Tools Generators provides content generation
(documentation, help) from plugin descriptor.

%package java
Summary:        Maven Plugin Tool for Java
Group:          Development/Libraries/Java

%description java
Descriptor extractor for plugins written in Java.

%package model
Summary:        Maven Plugin Metadata Model
Group:          Development/Libraries/Java

%description model
The Maven Plugin Metadata Model provides an API to play with the Metadata
model.

%package -n maven-script-ant
Summary:        Maven Ant Mojo Support
Group:          Development/Libraries/Java

%description -n maven-script-ant
This package provides %{summary}, which write Maven plugins with
Ant scripts.

%package -n maven-script-beanshell
Summary:        Maven Beanshell Mojo Support
Group:          Development/Libraries/Java

%description -n maven-script-beanshell
This package provides %{summary}, which write Maven plugins with
Beanshell scripts.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java
Provides:       %{name}-javadocs = %{version}-%{release}
Obsoletes:      %{name}-javadocs < %{version}-%{release}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -a1
%patch -P 0 -p1

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

%pom_remove_dep net.sf.jtidy:jtidy maven-plugin-tools-generators

%build
mkdir -p lib
build-jar-repository -s lib \
    ant \
    atinject \
    bsh2/bsh \
    httpcomponents/httpclient \
    httpcomponents/httpcore \
    jsoup/jsoup \
    maven/maven-artifact \
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
    plexus/ant-factory \
    plexus/archiver \
    plexus/bsh-factory \
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

%install
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for i in \
    maven-plugin-annotations \
    maven-plugin-tools-annotations \
    maven-plugin-tools-api \
    maven-plugin-tools-generators \
    maven-plugin-tools-java; do
  install -pm 0644 ${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
  %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f ${i}
  if [ -d ${i}/target/site/apidocs ]; then
    cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
  fi
done
for i in \
    maven-plugin-tools-ant \
    maven-plugin-tools-beanshell \
    maven-plugin-tools-model \
    maven-script-ant \
    maven-script-beanshell; do
  install -pm 0644 maven-script/${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
  %{mvn_install_pom} maven-script/${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f ${i}
  if [ -d maven-script/${i}/target/site/apidocs ]; then
    cp -r maven-script/${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
  fi
done
%fdupes -s %{buildroot}%{_javadocdir}

%files -n maven-plugin-annotations -f .mfiles-maven-plugin-annotations

%files annotations -f .mfiles-maven-plugin-tools-annotations
%license LICENSE NOTICE

%files ant -f .mfiles-maven-plugin-tools-ant

%files api -f .mfiles-maven-plugin-tools-api
%license LICENSE NOTICE

%files beanshell -f .mfiles-maven-plugin-tools-beanshell

%files generators -f .mfiles-maven-plugin-tools-generators

%files java -f .mfiles-maven-plugin-tools-java

%files model -f .mfiles-maven-plugin-tools-model
%license LICENSE NOTICE

%files -n maven-script-ant -f .mfiles-maven-script-ant
%license LICENSE NOTICE

%files -n maven-script-beanshell -f .mfiles-maven-script-beanshell
%license LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE NOTICE

%changelog
