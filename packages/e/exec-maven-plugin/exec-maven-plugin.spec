#
# spec file for package exec-maven-plugin
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


Name:           exec-maven-plugin
Version:        1.6.0
Release:        0
Summary:        Maven plugin to allow execution of system and Java programs
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://www.mojohaus.org/exec-maven-plugin/
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/%{version}/exec-maven-plugin-%{version}-source-release.zip
Patch1:         exec-maven-plugin-1.6.0-Port-to-Maven-3.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  unzip
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

dos2unix LICENSE.txt
find . -name *.jar -delete

%pom_remove_dep :maven-project
%pom_remove_dep :maven-toolchain
%pom_remove_dep :maven-artifact-manager

%pom_add_dep org.apache.maven:maven-compat
%pom_add_dep junit:junit::test

%pom_remove_plugin :animal-sniffer-maven-plugin

%patch1 -p1

%build
%{mvn_build} -f -- -DmavenVersion=3 -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
