#
# spec file for package maven-resolver2-supplier-mvn4
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
%define fragment_name supplier-mvn4
%define _buildshell /bin/bash
Name:           %{base_name}%{version_suffix}-%{fragment_name}
Version:        2.0.16
Release:        0
Summary:        Maven Artifact Resolver Instance Supplier Maven4
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/resolver/
Source0:        https://archive.apache.org/dist/maven/resolver/%{base_name}-%{version}-source-release.zip
Source1:        %{base_name}%{version_suffix}-build.tar.xz
BuildRequires:  %{base_name}%{version_suffix}-api
BuildRequires:  %{base_name}%{version_suffix}-connector-basic
BuildRequires:  %{base_name}%{version_suffix}-impl
BuildRequires:  %{base_name}%{version_suffix}-named-locks
BuildRequires:  %{base_name}%{version_suffix}-spi
BuildRequires:  %{base_name}%{version_suffix}-transport-apache
BuildRequires:  %{base_name}%{version_suffix}-transport-file
BuildRequires:  %{base_name}%{version_suffix}-util
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven4-lib
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildArch:      noarch

%description
A helper module to provide RepositorySystem instances.

Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

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

%{mvn_package} :%{base_name} __noinstall

%{mvn_file} :{*} %{base_name}/@1

%build
mkdir -p lib
build-jar-repository -s lib \
    maven/maven-api-core-4 \
    maven/maven-api-spi-4 \
    maven/maven-model-builder-4 \
    maven/maven-resolver-provider-4 \
    %{base_name}/maven-resolver-api-%{version_suffix} \
    %{base_name}/maven-resolver-connector-basic-%{version_suffix} \
    %{base_name}/maven-resolver-impl-%{version_suffix} \
    %{base_name}/maven-resolver-named-locks-%{version_suffix} \
    %{base_name}/maven-resolver-spi-%{version_suffix} \
    %{base_name}/maven-resolver-transport-apache \
    %{base_name}/maven-resolver-transport-file-%{version_suffix} \
    %{base_name}/maven-resolver-util-%{version_suffix}

%{ant} -f %{base_name}-%{fragment_name} \
%if %{without tests}
  -Dtest.skip=true \
%endif
  package javadoc

%{mvn_artifact} pom.xml

%{mvn_artifact} \
    %{base_name}-%{fragment_name}/pom.xml \
    %{base_name}-%{fragment_name}/target/%{base_name}-%{fragment_name}-%{version}.jar

%install
%mvn_install -J %{base_name}-%{fragment_name}/target/site/apidocs
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
