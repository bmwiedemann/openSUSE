#
# spec file for package maven-resolver
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


%define _buildshell /bin/bash
Name:           maven-resolver
Version:        2.0.20
Release:        0
Summary:        Apache Maven Artifact Resolver library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/resolver/
Source0:        https://archive.apache.org/dist/maven/resolver/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  bouncycastle
BuildRequires:  bouncycastle-pg
BuildRequires:  fdupes
BuildRequires:  google-gson
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-wagon-provider-api
BuildRequires:  methanol
BuildRequires:  objectweb-asm
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  unzip
Obsoletes:      %{name}-supplier
Obsoletes:      %{name}2
BuildArch:      noarch

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%package api
Summary:        Maven Artifact Resolver API
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-api

%description api
The application programming interface for the repository system.

%package spi
Summary:        Maven Artifact Resolver SPI
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-spi

%description spi
The service provider interface for repository system implementations and
repository connectors.

%package util
Summary:        Maven Artifact Resolver Utilities
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-util

%description util
A collection of utility classes to ease usage of the repository system.

%package named-locks
Summary:        Maven Artifact Resolver Named Locks
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-named-locks

%description named-locks
A synchronization utility implementation using Named locks

%package named-locks-ipc
Summary:        Maven Artifact Resolver Named Locks using IPC
Group:          Development/Libraries/Java
Obsoletes:      %{name}2-named-locks-ipc

%description named-locks-ipc
A synchronization utility implementation using IPC.

%package impl
Summary:        Maven Artifact Resolver Implementation
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-impl

%description impl
An implementation of the repository system.

%package generator-gnupg
Summary:        Maven Artifact Resolver GnuPG Signer Generator
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-generator-gnupg

%description generator-gnupg
A generator implementation for GnuPG signatures.

%package test-util
Summary:        Maven Artifact Resolver Test Utilities
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-test-util

%description test-util
A collection of utility classes to ease testing of the repository system.

%package connector-basic
Summary:        Maven Artifact Resolver Connector Basic
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-connector-basic

%description connector-basic
A repository connector implementation for repositories using URI-based layouts.

%package transport-apache
Summary:        Maven Artifact Resolver Transport Apache
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}-transport-http
Obsoletes:      %{name}2-transport-apache

%description transport-apache
A transport implementation for repositories using http:// and https:// URLs.

%package transport-classpath
Summary:        Maven Artifact Resolver Transport Classpath
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-transport-classpath

%description transport-classpath
A transport implementation for repositories using classpath:// URLs.

%package transport-file
Summary:        Maven Artifact Resolver Transport File
Group:          Development/Libraries/Java
Obsoletes:      %{name}2-transport-file

%description transport-file
A transport implementation for repositories using file:// URLs.

%package transport-jdk11
Summary:        Maven Artifact Resolver Transport JDK 11
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-transport-jdk-11
Obsoletes:      %{name}2-transport-jdk11

%description transport-jdk11
Maven Artifact Transport JDK Java 11+.

%package transport-jdk8
Summary:        Maven Artifact Resolver Transport JDK 8
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-transport-jdk-8
Obsoletes:      %{name}2-transport-jdk8

%description transport-jdk8
Maven Artifact Transport JDK Java 8+.

%package transport-jdk
Summary:        Maven Artifact Resolver Transport JDK (mr)
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-transport-jdk

%description transport-jdk
Maven Artifact Transport JDK - Multi Release.

%package transport-wagon
Summary:        Maven Artifact Resolver Transport Wagon
Group:          Development/Libraries/Java
Obsoletes:      %{name}
Obsoletes:      %{name}2-transport-wagon

%description transport-wagon
A transport implementation based on Maven Wagon.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
Obsoletes:      %{name}2-javadoc

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -a1

%pom_remove_dep :jetty-bom

%build
mkdir -p lib
build-jar-repository -s lib \
  atinject \
  bcpg \
  bcprov \
  google-gson/gson \
  httpcomponents/httpclient \
  httpcomponents/httpcore \
  maven-wagon/provider-api \
  methanol \
  objectweb-asm/asm \
  org.eclipse.sisu.inject \
  org.eclipse.sisu.plexus \
  plexus-classworlds \
  plexus/xml \
  slf4j/api

ant \
  -Dtest.skip=true \
  package javadoc

%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
  for module in named-locks-ipc generator-gnupg; do
    ant -f %{name}-${module} \
%if %{without tests}
      -Dtest.skip=true \
%endif
      package javadoc
  done
%endif

%install
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for i in \
    api \
    connector-basic \
    impl \
    named-locks \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    named-locks-ipc \
    generator-gnupg \
%endif
    spi \
    test-util \
    transport-apache \
    transport-classpath \
    transport-file \
    transport-wagon \
    util; do
  cp -r %{name}-${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}
  install -pm 0644 %{name}-${i}/target/%{name}-${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${i}.jar
  %{mvn_install_pom} %{name}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${i}.pom
  if [ "${i}" == transport-wagon ]; then
    %add_maven_depmap %{name}/%{name}-${i}.pom %{name}/%{name}-${i}.jar -f ${i} -a org.eclipse.aether:aether-${i}:org.eclipse.aether:aether-connector-wagon
  else
    %add_maven_depmap %{name}/%{name}-${i}.pom %{name}/%{name}-${i}.jar -f ${i} -a org.eclipse.aether:aether-${i}
  fi
done

for i in \
    transport-jdk11 \
    transport-jdk8 \
    transport-jdk; do
  if [ -e %{name}-transport-jdk-parent/%{name}-${i}/site/apidocs ]; then
    cp -r %{name}-transport-jdk-parent/%{name}-${i}/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}
  fi
  install -pm 0644 %{name}-transport-jdk-parent/%{name}-${i}/target/%{name}-${i}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}/%{name}-${i}.jar
  %{mvn_install_pom} %{name}-transport-jdk-parent/%{name}-${i}/pom.xml \
    %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${i}.pom
  %add_maven_depmap %{name}/%{name}-${i}.pom %{name}/%{name}-${i}.jar -f ${i}
done

%fdupes -s %{buildroot}%{_javadocdir}

%files api -f .mfiles-api
%license LICENSE NOTICE

%files spi -f .mfiles-spi

%files util -f .mfiles-util

%files named-locks -f .mfiles-named-locks

%files impl -f .mfiles-impl

%files test-util -f .mfiles-test-util

%files connector-basic -f .mfiles-connector-basic

%files transport-classpath -f .mfiles-transport-classpath

%files transport-file -f .mfiles-transport-file

%files transport-wagon -f .mfiles-transport-wagon

%files transport-apache -f .mfiles-transport-apache

%files transport-jdk11 -f .mfiles-transport-jdk11

%files transport-jdk8 -f .mfiles-transport-jdk8

%files transport-jdk -f .mfiles-transport-jdk

%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
%files named-locks-ipc -f .mfiles-named-locks-ipc

%files generator-gnupg -f .mfiles-generator-gnupg

%endif

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE NOTICE

%changelog
