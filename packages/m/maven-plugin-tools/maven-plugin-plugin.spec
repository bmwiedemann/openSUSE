#
# spec file for package maven-plugin-plugin
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


%global base_name maven-plugin-tools
Name:           maven-plugin-plugin
Version:        3.15.2
Release:        0
Summary:        Maven Plugin Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugin-tools/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/%{base_name}/%{version}/%{base_name}-%{version}-source-release.zip
Patch0:         0002-Remove-dependency-on-jtidy.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-annotations)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-generators)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-java)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
Obsoletes:      %{name}-bootstrap
#!BuildRequires: maven-compiler-plugin-bootstrap
#!BuildRequires: maven-jar-plugin-bootstrap
#!BuildRequires: maven-plugin-plugin-bootstrap
#!BuildRequires: maven-resources-plugin-bootstrap
#!BuildRequires: maven-surefire-plugin-bootstrap
BuildArch:      noarch

%description
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{version}
%patch -P 0 -p1

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin :sisu-maven-plugin

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

%pom_remove_dep org.junit:junit-bom
%pom_remove_dep :maven-plugin-tools-ant maven-plugin-plugin
%pom_remove_dep :maven-plugin-tools-beanshell maven-plugin-plugin

%build
pushd %{name}
%{mvn_file} :%{name} %{base_name}/%{name}
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

popd

%install
pushd %{name}
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f %{name}/.mfiles
%license LICENSE NOTICE

%files javadoc -f %{name}/.mfiles-javadoc
%license LICENSE NOTICE

%changelog
