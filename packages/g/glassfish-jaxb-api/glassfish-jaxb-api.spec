#
# spec file for package glassfish-jaxb-api
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


%global oname jaxb-spec
%global bundle jaxb-api
# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           glassfish-jaxb-api
Version:        2.4.0
Release:        0
Summary:        Java Architecture for XML Binding
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://jaxb.java.net/
Source0:        https://github.com/javaee/%{oname}/archive/%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  glassfish-activation-api
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Glassfish - JAXB (JSR 222) API.

%package javadoc
Summary:        Javadoc for %{oname}
Group:          Documentation/HTML

%description javadoc
Glassfish - JAXB (JSR 222) API.

This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}
cp %{SOURCE1} jaxb-api/build.xml

%pom_disable_module jaxb-api-test

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin jaxb-api
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin jaxb-api
%pom_remove_plugin org.glassfish.build:gfnexus-maven-plugin jaxb-api
%pom_remove_plugin :findbugs-maven-plugin jaxb-api
%pom_remove_plugin :maven-enforcer-plugin jaxb-api
%pom_remove_plugin :cobertura-maven-plugin jaxb-api
%pom_remove_plugin :maven-dependency-plugin jaxb-api

%build
pushd jaxb-api
mkdir -p lib
build-jar-repository -s lib glassfish-activation-api
%{ant} jar javadoc
popd

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 %{bundle}/target/%{bundle}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{bundle}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -r %{bundle}/target/site/apidocs/* %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
