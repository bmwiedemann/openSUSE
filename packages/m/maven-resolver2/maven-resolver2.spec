#
# spec file for package maven-resolver2
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


%define base_name maven-resolver
%define version_suffix 2
%define _buildshell /bin/bash
Name:           %{base_name}%{version_suffix}
Version:        2.0.16
Release:        0
Summary:        Apache Maven Artifact Resolver library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/resolver/
Source0:        https://archive.apache.org/dist/maven/resolver/%{base_name}-%{version}-source-release.zip
Source1:        %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  bouncycastle
BuildRequires:  bouncycastle-pg
BuildRequires:  fdupes
BuildRequires:  google-gson
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-wagon-provider-api
BuildRequires:  methanol
BuildRequires:  objectweb-asm
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j2
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.bouncycastle:bcutil-jdk18on)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j:2)
BuildArch:      noarch

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%package api
Summary:        Maven Artifact Resolver API
Group:          Development/Libraries/Java

%description api
The application programming interface for the repository system.

%package spi
Summary:        Maven Artifact Resolver SPI
Group:          Development/Libraries/Java

%description spi
The service provider interface for repository system implementations and
repository connectors.

%package util
Summary:        Maven Artifact Resolver Utilities
Group:          Development/Libraries/Java

%description util
A collection of utility classes to ease usage of the repository system.

%package named-locks
Summary:        Maven Artifact Resolver Named Locks
Group:          Development/Libraries/Java

%description named-locks
A synchronization utility implementation using Named locks

%package named-locks-ipc
Summary:        Maven Artifact Resolver Named Locks using IPC
Group:          Development/Libraries/Java

%description named-locks-ipc
A synchronization utility implementation using IPC.

%package impl
Summary:        Maven Artifact Resolver Implementation
Group:          Development/Libraries/Java

%description impl
An implementation of the repository system.

%package generator-gnupg
Summary:        Maven Artifact Resolver GnuPG Signer Generator
Group:          Development/Libraries/Java

%description generator-gnupg
A generator implementation for GnuPG signatures.

%package test-util
Summary:        Maven Artifact Resolver Test Utilities
Group:          Development/Libraries/Java

%description test-util
A collection of utility classes to ease testing of the repository system.

%package connector-basic
Summary:        Maven Artifact Resolver Connector Basic
Group:          Development/Libraries/Java

%description connector-basic
A repository connector implementation for repositories using URI-based layouts.

%package transport-apache
Summary:        Maven Artifact Resolver Transport Apache
Group:          Development/Libraries/Java

%description transport-apache
A transport implementation for repositories using http:// and https:// URLs.

%package transport-classpath
Summary:        Maven Artifact Resolver Transport Classpath
Group:          Development/Libraries/Java

%description transport-classpath
A transport implementation for repositories using classpath:// URLs.

%package transport-file
Summary:        Maven Artifact Resolver Transport File
Group:          Development/Libraries/Java

%description transport-file
A transport implementation for repositories using file:// URLs.

%package transport-jdk11
Summary:        Maven Artifact Resolver Transport JDK 11
Group:          Development/Libraries/Java
Provides:       %{name}-transport-jdk-11 = %{version}
Obsoletes:      %{name}-transport-jdk-11 < %{version}

%description transport-jdk11
Maven Artifact Transport JDK Java 11+.

%package transport-jdk8
Summary:        Maven Artifact Resolver Transport JDK 8
Group:          Development/Libraries/Java
Provides:       %{name}-transport-jdk-8 = %{version}
Obsoletes:      %{name}-transport-jdk-8 < %{version}

%description transport-jdk8
Maven Artifact Transport JDK Java 8+.

%package transport-jdk
Summary:        Maven Artifact Resolver Transport JDK (mr)
Group:          Development/Libraries/Java

%description transport-jdk
Maven Artifact Transport JDK - Multi Release.

%package transport-wagon
Summary:        Maven Artifact Resolver Transport Wagon
Group:          Development/Libraries/Java

%description transport-wagon
A transport implementation based on Maven Wagon.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n %{base_name}-%{version} -a1

%pom_remove_dep :jetty-bom

# Use newer maven4 version
%pom_xpath_set pom:project/pom:properties/pom:maven4Version 4

# Normalize slf4j version to 2
%pom_xpath_set pom:project/pom:properties/pom:slf4jVersion 2

%{mvn_file} :{*} %{base_name}/@1

%{mvn_compat_version} :maven-resolver-api %{version_suffix} %{version}
%{mvn_compat_version} :maven-resolver-connector-basic %{version_suffix} %{version}
%{mvn_compat_version} :maven-resolver-impl %{version_suffix} %{version}
%{mvn_compat_version} :maven-resolver-named-locks %{version_suffix} %{version}
%{mvn_compat_version} :maven-resolver-spi %{version_suffix} %{version}
%{mvn_compat_version} :maven-resolver-test-util %{version_suffix} %{version}
%{mvn_compat_version} :maven-resolver-transport-classpath %{version_suffix} %{version}
%{mvn_compat_version} :maven-resolver-transport-file %{version_suffix} %{version}
%{mvn_compat_version} :maven-resolver-transport-wagon %{version_suffix} %{version}
%{mvn_compat_version} :maven-resolver-util %{version_suffix} %{version}

%{mvn_package} :%{base_name} __noinstall
%{mvn_package} :%{base_name}-transport-jdk-parent __noinstall
%{mvn_package} :%{base_name}-{*}  @1

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
  slf4j/api-2

%{ant} \
%if %{without tests}
  -Dtest.skip=true \
%endif
  package javadoc

%{mvn_artifact} pom.xml
%{mvn_artifact} %{base_name}-transport-jdk-parent/pom.xml

mkdir -p target/site/apidocs

for i in \
    api \
    connector-basic \
    generator-gnupg \
    impl \
    named-locks \
    named-locks-ipc \
    spi \
    test-util \
    transport-apache \
    transport-classpath \
    transport-file \
    transport-wagon \
    util; do
  cp -r %{base_name}-${i}/target/site/apidocs target/site/apidocs/%{name}-${i}
  %{mvn_artifact} %{base_name}-${i}/pom.xml %{base_name}-${i}/target/%{base_name}-${i}-%{version}.jar
done

for i in \
    transport-jdk11 \
    transport-jdk8 \
    transport-jdk; do
  if [ -e %{base_name}-transport-jdk-parent/%{base_name}-${i}/site/apidocs ]; then
    cp -r %{base_name}-transport-jdk-parent/%{base_name}-${i}/site/apidocs target/site/apidocs/%{name}-${i}
  fi
  %{mvn_artifact} \
    %{base_name}-transport-jdk-parent/%{base_name}-${i}/pom.xml \
    %{base_name}-transport-jdk-parent/%{base_name}-${i}/target/%{base_name}-${i}-%{version}.jar
done

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files api -f .mfiles-api
%license LICENSE NOTICE

%files spi -f .mfiles-spi

%files util -f .mfiles-util

%files named-locks -f .mfiles-named-locks

%files named-locks-ipc -f .mfiles-named-locks-ipc

%files impl -f .mfiles-impl

%files test-util -f .mfiles-test-util

%files connector-basic -f .mfiles-connector-basic

%files generator-gnupg -f .mfiles-generator-gnupg

%files transport-classpath -f .mfiles-transport-classpath

%files transport-file -f .mfiles-transport-file

%files transport-wagon -f .mfiles-transport-wagon

%files transport-apache -f .mfiles-transport-apache

%files transport-jdk11 -f .mfiles-transport-jdk11

%files transport-jdk8 -f .mfiles-transport-jdk8

%files transport-jdk -f .mfiles-transport-jdk

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
