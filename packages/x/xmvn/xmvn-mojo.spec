#
# spec file for package xmvn-mojo
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


%global parent xmvn
%global subname mojo
Name:           %{parent}-%{subname}
Version:        4.3.0
Release:        0
Summary:        XMvn MOJO
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        https://github.com/fedora-java/%{parent}/releases/download/%{version}/%{parent}-%{version}.tar.xz
Source1:        %{parent}-build.tar.xz
Patch0:         xmvn-mojo-sisu110.patch
BuildRequires:  %{parent}-api = %{version}
BuildRequires:  %{parent}-core = %{version}
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-util
BuildRequires:  objectweb-asm
BuildRequires:  xmvn-install
BuildRequires:  xmvn-minimal
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
This package provides XMvn MOJO, which is a Maven plugin that consists
of several MOJOs.  Some goals of these MOJOs are intended to be
attached to default Maven lifecycle when building packages, others can
be called directly from Maven command line.

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

# Remove all dependencies with scope test, since a raw xmvn does not hide them
%pom_remove_dep -r :::test:

%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-plugin-plugin']/pom:configuration" '
    <goalPrefix>${project.artifactId}</goalPrefix>' xmvn-mojo

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
    maven/maven-plugin-api \
    maven-plugin-tools/maven-plugin-annotations \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-util \
    objectweb-asm/asm-all \
    xmvn

pushd %{name}
  ant \
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
