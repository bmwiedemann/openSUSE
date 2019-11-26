#
# spec file for package maven-plugin-plugin
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


%global base_name maven-plugin-tools
Name:           maven-plugin-plugin
Version:        3.5.1
Release:        0
Summary:        Maven Plugin Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/plugin-tools/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugin-tools/%{base_name}/%{version}/%{base_name}-%{version}-source-release.zip
Patch0:         0001-Avoid-duplicate-MOJO-parameters.patch
Patch1:         0002-Deal-with-nulls-from-getComment.patch
Patch2:         0003-Port-to-plexus-utils-3.0.24.patch
Patch10:        fix-getPluginsAsMap.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-annotations)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-generators)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-java)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.surefire:maven-surefire-common)
BuildRequires:  mvn(org.apache.maven:maven-artifact:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-model:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
Obsoletes:      %{name}-bootstrap
#!BuildRequires: maven-compiler-plugin-bootstrap
#!BuildRequires: maven-jar-plugin-bootstrap
#!BuildRequires: maven-javadoc-plugin-bootstrap
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch10 -p1

%pom_remove_plugin -r :maven-enforcer-plugin

# For com.sun:tools use scope "compile" instead of "system"
%pom_remove_dep com.sun:tools maven-plugin-tools-javadoc
%pom_add_dep com.sun:tools maven-plugin-tools-javadoc

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

# Remove test dependencies because tests are skipped anyways.
%pom_xpath_remove "pom:dependency[pom:scope='test']"

# Use Maven 3.1.1 APIs
%pom_remove_dep :maven-project maven-plugin-plugin
%pom_remove_dep :maven-plugin-descriptor maven-plugin-plugin
%pom_remove_dep :maven-plugin-registry maven-plugin-plugin
%pom_remove_dep :maven-artifact-manager maven-plugin-plugin

# Why on the earth is this dependency there ???
%pom_remove_dep :maven-surefire-common maven-plugin-plugin

%pom_change_dep :maven-project :maven-core maven-plugin-tools-annotations
%pom_change_dep :maven-plugin-descriptor :maven-compat maven-plugin-tools-annotations

%pom_remove_dep :maven-plugin-descriptor maven-script/maven-plugin-tools-ant
%pom_change_dep :maven-project :maven-core maven-script/maven-plugin-tools-ant

%pom_remove_dep :maven-plugin-descriptor maven-plugin-tools-api
%pom_change_dep :maven-project :maven-core maven-plugin-tools-api

%pom_remove_dep :maven-plugin-descriptor maven-script/maven-plugin-tools-beanshell

%pom_remove_dep :maven-project maven-plugin-tools-generators
%pom_remove_dep :maven-plugin-descriptor maven-plugin-tools-generators

%pom_change_dep :maven-project :maven-core maven-plugin-tools-java
%pom_remove_dep :maven-plugin-descriptor maven-plugin-tools-java

%pom_change_dep :maven-plugin-descriptor :maven-plugin-api maven-script/maven-plugin-tools-model

%pom_remove_dep :maven-project maven-script/maven-script-ant
%pom_remove_dep :maven-plugin-descriptor maven-script/maven-script-ant

%pom_remove_dep :maven-project
%pom_remove_dep :maven-plugin-descriptor
%pom_add_dep org.apache.maven:maven-compat
%pom_add_dep org.apache.maven:maven-plugin-registry

%build
pushd %{name}
%{mvn_file} :%{name} %{base_name}/%{name}
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

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
