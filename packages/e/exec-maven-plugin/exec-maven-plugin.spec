#
# spec file for package exec-maven-plugin
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           exec-maven-plugin
Version:        3.5.1
Release:        0
Summary:        Exec Maven Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.mojohaus.org/exec-maven-plugin/
Source0:        https://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/%{version}/exec-maven-plugin-%{version}-source-release.zip
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-jdk14)
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
A plugin to allow execution of system and Java programs.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n exec-maven-plugin-%{version}

sed -i 's/\r$//' LICENSE.txt
find . -name *.jar -delete

%pom_remove_plugin :animal-sniffer-maven-plugin

#Drop test part. sonatype-aerther not available
%pom_remove_dep :mockito-core
%pom_remove_dep :maven-plugin-testing-harness

rm -rf src/test/

%pom_xpath_set pom:project/pom:properties/pom:mavenVersion 3

%build
%{mvn_build} -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
