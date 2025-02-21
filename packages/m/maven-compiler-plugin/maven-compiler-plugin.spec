#
# spec file for package maven-compiler-plugin
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global base_name maven-compiler-plugin
Version:        3.14.0
Release:        0
Summary:        Maven Compiler Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugins/maven-compiler-plugin
Source0:        https://archive.apache.org/dist/maven/plugins/%{base_name}-%{version}-source-release.zip
Source1:        %{base_name}-build.xml
Patch0:         %{base_name}-bootstrap-resources.patch
BuildRequires:  javapackages-local
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-util
BuildRequires:  maven-shared-incremental
BuildRequires:  maven-shared-utils
BuildRequires:  objectweb-asm
BuildRequires:  plexus-compiler >= 2.13
BuildRequires:  plexus-languages
BuildRequires:  plexus-utils
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{base_name}-bootstrap
BuildRequires:  ant
%else
Name:           %{base_name}
BuildRequires:  fdupes
BuildRequires:  xmvn
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
Obsoletes:      %{base_name}-bootstrap
#!BuildRequires: maven-compiler-plugin-bootstrap
#!BuildRequires: maven-jar-plugin-bootstrap
#!BuildRequires: maven-javadoc-plugin-bootstrap
#!BuildRequires: maven-plugin-plugin-bootstrap
#!BuildRequires: maven-resources-plugin-bootstrap
#!BuildRequires: maven-surefire-plugin-bootstrap
%endif

%description
The Compiler Plugin is used to compile the sources of your project.

%if %{without bootstrap}
%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.
%endif

%prep
%setup -q -n %{base_name}-%{version}
%if %{with bootstrap}
cp %{SOURCE1} build.xml
%patch -P 0 -p1
%endif

%pom_remove_dep :::test

# There is nothing to index and this creates a cycle
%pom_remove_plugin org.eclipse.sisu:sisu-maven-plugin

%pom_xpath_remove pom:project/pom:parent/pom:relativePath

%build
%if %{with bootstrap}
mkdir -p lib
build-jar-repository -s lib \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven/maven-plugin-api \
    maven-plugin-tools/maven-plugin-annotations \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-util \
    maven-shared-incremental/maven-shared-incremental \
    maven-shared-utils/maven-shared-utils \
    objectweb-asm/asm-all \
    plexus-compiler/plexus-compiler-api \
    plexus-compiler/plexus-compiler-manager \
    plexus-languages/plexus-java \
    plexus/utils
%{ant} -Dtest.skip=true jar
%else
xmvn --batch-mode --offline \
    -Dmaven.test.skip=true \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    package org.apache.maven.plugins:maven-javadoc-plugin:aggregate
%endif

%{mvn_artifact} pom.xml target/%{base_name}-%{version}.jar

%install
%mvn_install
%if %{without bootstrap}
%fdupes -s %{buildroot}%{_javadocdir}
%endif

%files -f .mfiles
%license LICENSE NOTICE

%if %{without bootstrap}
%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE
%endif

%changelog
