#
# spec file for package xmvn5-connector
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


%global parent xmvn
%global version_suffix 5
%global subname connector
Name:           %{parent}%{version_suffix}-%{subname}
Version:        5.1.0
Release:        0
Summary:        XMvn Connector for Maven Resolver
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        %{parent}-%{version}.tar.xz
Source1:        %{parent}-build.tar.xz
BuildRequires:  %{parent}%{version_suffix}-api = %{version}
BuildRequires:  %{parent}%{version_suffix}-core = %{version}
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local
BuildRequires:  maven-resolver2-api
BuildRequires:  maven4-lib
BuildRequires:  objectweb-asm
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
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
%pom_remove_plugin -r :spotless-maven-plugin

# remove dependency plugin maven-binaries execution
# we provide apache-maven by symlink
%pom_xpath_remove "pom:executions/pom:execution[pom:id[text()='maven-binaries']]"

# Don't put Class-Path attributes in manifests
%pom_remove_plugin :maven-jar-plugin xmvn-tools

pushd %{parent}-%{subname}
  %{mvn_compat_version} : %{version_suffix} %{version}
  %{mvn_file} :{*} %{parent}/@1
popd

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    maven/maven-api-core \
    maven/maven-api-model \
    maven/maven-api-spi \
    maven/maven-api-toolchain \
    maven/maven-artifact-4 \
    maven/maven-core-4 \
    maven/maven-model-4 \
    maven/maven-plugin-api-4 \
    maven-resolver/maven-resolver-api-2 \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    %{parent}/%{parent}-api-%{version_suffix}

pushd %{parent}-%{subname}
  ant package javadoc

%{mvn_artifact} pom.xml target/%{parent}-%{subname}-%{version}.jar

popd

%install
pushd %{parent}-%{subname}
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f %{parent}-%{subname}/.mfiles
%license LICENSE NOTICE
%doc AUTHORS README.md

%files javadoc -f %{parent}-%{subname}/.mfiles-javadoc
%license LICENSE NOTICE

%changelog
