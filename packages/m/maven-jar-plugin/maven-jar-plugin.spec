#
# spec file for package maven-jar-plugin
#
# Copyright (c) 2019 SUSE LLC
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
%global base_name maven-jar-plugin
Version:        3.2.0
Release:        0
Summary:        Maven JAR Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/plugins/maven-jar-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{base_name}/%{version}/%{base_name}-%{version}-source-release.zip
Source1:        %{base_name}-build.xml
Patch0:         %{base_name}-bootstrap-resources.patch
Patch1:         01-allow-replacing-artifacts.patch
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  maven-archiver >= 3.5.0
BuildRequires:  maven-file-management
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  plexus-archiver >= 4.2.0
BuildRequires:  plexus-utils >= 3.3.0
BuildRequires:  sisu-plexus
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
BuildRequires:  xmvn
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
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
Builds a Java Archive (JAR) file from the compiled
project classes and resources.

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
%patch0 -p1
%endif
%patch1 -p1

%build
# Test class MockArtifact doesn't override method getMetadata
%if %{with bootstrap}
mkdir -p lib
build-jar-repository -s lib \
	maven-file-management/file-management \
	maven-archiver/maven-archiver \
	maven/maven-artifact \
	maven/maven-core \
	maven/maven-plugin-api \
	maven-plugin-tools/maven-plugin-annotations \
	org.eclipse.sisu.plexus \
	plexus/archiver \
	plexus/utils
%{ant} -Dtest.skip=true jar
%else
xmvn --batch-mode --offline \
	-Dmaven.test.skip=true -DmavenVersion=3.1.1 \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=7 \
%endif
	package org.apache.maven.plugins:maven-javadoc-plugin:aggregate
%endif

%{mvn_artifact} pom.xml target/%{base_name}-%{version}.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%dir %{_javadir}/%{name}
%license LICENSE
%doc NOTICE

%if %{without bootstrap}
%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE
%endif

%changelog
