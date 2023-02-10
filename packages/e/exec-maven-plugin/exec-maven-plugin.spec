#
# spec file for package exec-maven-plugin
#
# Copyright (c) 2022 SUSE LLC
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


Name:           exec-maven-plugin
Version:        3.0.0
Release:        0
Summary:        Exec Maven Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.mojohaus.org/exec-maven-plugin/
Source0:        https://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/%{version}/exec-maven-plugin-%{version}-source-release.zip
Patch0:         exec-maven-plugin-ioexception.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
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
%patch0 -p1

sed -i 's/\r$//' LICENSE.txt
find . -name *.jar -delete

%pom_remove_plugin :animal-sniffer-maven-plugin

#Drop test part. sonatype-aerther not available
%pom_remove_dep :mockito-core
%pom_remove_dep :maven-plugin-testing-harness
%pom_remove_dep :plexus-interpolation

rm -rf src/test/

%build
%{mvn_build} -f

# The tooling generates Java 9+ require, but it a multi-release jar that works with Java 8 just fine
sed -i 's|compilerTarget=9|compilerTarget=1\.8|' .xmvn/properties
sed -i 's|<requiresJava>9</requiresJava>|<requiresJava>1\.8</requiresJava>|' .xmvn-reactor

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
