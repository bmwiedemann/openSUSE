#
# spec file for package string-template-maven-plugin
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


Name:           string-template-maven-plugin
Version:        1.1
Release:        0
Summary:        StringTemplate Maven Plugin
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/kevinbirch/%{name}
Source0:        https://github.com/kevinbirch/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/kevinbirch/%{name}/master/LICENSE
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.twdata.maven:mojo-executor)
#!BuildRequires: stringtemplate4
BuildArch:      noarch

%description
This plugin allows to execute StringTemplate template files during build.
The values for templates can come from static declarations or from a Java
class specified to be executed.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} .
%pom_change_dep :stringtemplate :ST4
%pom_change_dep org.sonatype.aether: org.eclipse.aether:
perl -pi -e 's#org\.sonatype\.aether#org.eclipse.aether#g' \
	src/main/java/com/webguys/maven/plugin/st/Controller.java

%build
%mvn_build -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
