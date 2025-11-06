#
# spec file for package xmvn5-mojo
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
%global subname mojo
Name:           %{parent}%{version_suffix}-%{subname}
Version:        5.1.0
Release:        0
Summary:        XMvn MOJO
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        %{parent}-%{version}.tar.xz
BuildRequires:  %{parent}%{version_suffix}-api = %{version}
BuildRequires:  %{parent}%{version_suffix}-core = %{version}
BuildRequires:  %{parent}%{version_suffix}-minimal
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(io.kojan:kojan-xml)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven:maven-api-core)
BuildRequires:  mvn(org.apache.maven:maven-api-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
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
%setup -q -n %{parent}-%{version}

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

# Remove all dependencies with scope test, since a raw xmvn does not hide them
%pom_remove_dep -r :::test:

pushd %{parent}-%{subname}
  %{mvn_compat_version} : %{version_suffix} %{version}
  %{mvn_file} :{*} %{parent}/@1
popd

%build
pushd %{parent}-%{subname}
  mkdir -p .mvn
  %{parent}%{version_suffix} \
    --batch-mode --offline \
    -Dmaven.test.skip=true -Dsource=8 \
    package org.apache.maven.plugins:maven-javadoc-plugin:aggregate

%{mvn_artifact} pom.xml target/%{parent}-%{subname}-%{version}.jar

popd

%install
pushd %{parent}-%{subname}
%mvn_install -J target/reports/apidocs
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f %{parent}-%{subname}/.mfiles
%license LICENSE NOTICE
%doc AUTHORS README.md

%files javadoc -f %{parent}-%{subname}/.mfiles-javadoc
%license LICENSE NOTICE

%changelog
