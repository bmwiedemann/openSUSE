#
# spec file for package javaparser
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


Name:           javaparser
Version:        3.3.5
Release:        0
Summary:        Java 1 to 9 Parser and Abstract Syntax Tree for Java
License:        LGPL-3.0-or-later OR Apache-2.0
URL:            https://javaparser.org
Source0:        https://github.com/javaparser/javaparser/archive/%{name}-parent-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildArch:      noarch

%description
This package contains a Java 1 to 9 Parser with AST generation and
visitor support. The AST records the source code structure, javadoc
and comments. It is also possible to change the AST nodes or create new
ones to modify the source code.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-parent-%{version}

sed -i 's/\r//' readme.md

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin :animal-sniffer-maven-plugin javaparser-core
%pom_remove_plugin :maven-enforcer-plugin javaparser-core
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :coveralls-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin . javaparser-testing

# Compatibility alias
%{mvn_alias} :javaparser-core com.google.code.javaparser:javaparser

# Fix javacc plugin name
sed -i \
  -e 's/ph-javacc-maven-plugin/javacc-maven-plugin/' \
  -e 's/com.helger.maven/org.codehaus.mojo/' \
  javaparser-core/pom.xml

# Missing plugin
%pom_remove_plugin :templating-maven-plugin javaparser-core

# Missing dep on jbehave for testing
%pom_disable_module javaparser-testing

# Only need to ship the core module
%{mvn_package} ":javaparser-core-generators" __noinstall
%{mvn_package} ":javaparser-metamodel-generator" __noinstall
%{mvn_package} ":javaparser-testing" __noinstall

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc readme.md changelog.md
%license LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%files javadoc -f .mfiles-javadoc
%license LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%changelog
