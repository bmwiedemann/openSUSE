#
# spec file for package maven-shade-plugin
#
# Copyright (c) 2024 SUSE LLC
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


Name:           maven-shade-plugin
Version:        3.6.0
Release:        0
Summary:        Capability to package the artifact in an uber-jar
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/plugins/%{name}
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.commons:commons-collections4)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.vafer:jdependency)
BuildArch:      noarch

%description
This plugin provides the capability to package the artifact in an
uber-jar, including its dependencies and to shade, i.e. rename, the
packages of some of the dependencies.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q
rm src/test/jars/plexus-utils-1.4.1.jar

%pom_change_dep :plexus-utils ::4.0.2
%pom_add_dep org.codehaus.plexus:plexus-xml:3.0.1

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=8
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
