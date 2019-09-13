#
# spec file for package xmvn
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%global subname connector-aether
%bcond_with tests
Name:           %{parent}-%{subname}
Version:        3.0.0
Release:        0
Summary:        XMvn Connector for Maven Resolver
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        https://github.com/fedora-java/%{parent}/releases/download/%{version}/%{parent}-%{version}.tar.xz
Source1:        %{parent}-build.tar.xz
Patch0:         0001-Fix-installer-plugin-loading.patch
Patch1:         0001-Port-to-Gradle-4.2.patch
Patch2:         0001-Port-to-Gradle-4.3.1.patch
Patch3:         0001-Support-setting-Xdoclint-none-in-m-javadoc-p-3.0.0.patch
Patch4:         0001-Fix-configuration-of-aliased-plugins.patch
Patch5:         0001-Don-t-use-JAXB-for-converting-bytes-to-hex-string.patch
Patch6:         0001-Use-apache-commons-compress-for-manifest-injection-a.patch
Patch7:         0001-port-to-gradle-4.4.1.patch
Patch8:         0001-Replace-JAXB-parser.patch
BuildRequires:  %{parent}-api = %{version}
BuildRequires:  %{parent}-core = %{version}
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  maven-lib
BuildRequires:  maven-resolver-api
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# Bisect IT has no chances of working in local, offline mode, without
# network access - it needs to access remote repositories.
find -name BisectIntegrationTest.java -delete

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
    commons-cli \
    guava20/guava-20.0 \
    guice/google-guice-no_aop \
    jdom2/jdom2 \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven/maven-model-builder \
    maven/maven-plugin-api \
    maven-resolver/maven-resolver-api \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus-classworlds \
    plexus/cli \
    plexus-containers/plexus-component-annotations \
    plexus-metadata-generator \
    plexus/utils \
    qdox \
    xbean/xbean-reflect \
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
