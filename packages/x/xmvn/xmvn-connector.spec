#
# spec file for package xmvn-connector
#
# Copyright (c) 2025 SUSE LLC
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


%global parent xmvn
%global subname connector
%bcond_with tests
Name:           %{parent}-%{subname}
Version:        4.3.0
Release:        0
Summary:        XMvn Connector for Maven Resolver
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        https://github.com/fedora-java/%{parent}/releases/download/%{version}/%{parent}-%{version}.tar.xz
Source1:        %{parent}-build.tar.xz
BuildRequires:  %{parent}-api = %{version}
BuildRequires:  %{parent}-core = %{version}
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  maven-lib
BuildRequires:  maven-resolver-api
BuildRequires:  objectweb-asm
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
Provides:       %{name}-aether = %{version}
Obsoletes:      %{name}-aether < %{version}
BuildArch:      noarch

%description
This package provides XMvn Connector for Maven Resolver, which
provides integration of Maven Resolver with XMvn.  It provides an
adapter which allows XMvn resolver to be used as Maven workspace
reader.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{parent}-%{version} -a1

%autopatch -p1

# Resolver IT won't work either - it tries to execute JAR file, which
# relies on Class-Path in manifest, which is forbidden in Fedora...
find -name ResolverIntegrationTest.java -delete

%pom_remove_plugin -r :maven-site-plugin

%{mvn_package} ":xmvn{,-it}" __noinstall

# Upstream code quality checks, not relevant when building RPMs
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
# FIXME pom macros don't seem to support submodules in profile
%pom_remove_plugin :jacoco-maven-plugin xmvn-it

# remove dependency plugin maven-binaries execution
# we provide apache-maven by symlink
%pom_xpath_remove "pom:executions/pom:execution[pom:id[text()='maven-binaries']]"

# Don't put Class-Path attributes in manifests
%pom_remove_plugin :maven-jar-plugin xmvn-tools

pushd %{name}
  %{mvn_file} :{*} %{parent}/@1
popd

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven/maven-model-builder \
    maven/maven-plugin-api \
    maven-resolver/maven-resolver-api \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    %{parent}/%{parent}-api

pushd %{name}
  %{ant} \
%if %{without tests}
  -Dtest.skip=true \
%endif
  package javadoc

%{mvn_artifact} pom.xml target/%{name}-%{version}.jar

popd

%install
pushd %{name}
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f %{name}/.mfiles
%license LICENSE NOTICE
%doc AUTHORS README.md

%files javadoc -f %{name}/.mfiles-javadoc
%license LICENSE NOTICE

%changelog
