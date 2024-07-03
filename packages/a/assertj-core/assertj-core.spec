#
# spec file for package assertj-core
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           assertj-core
Version:        3.25.3
Release:        0
Summary:        Library of assertions similar to fest-assert
License:        Apache-2.0
URL:            https://joel-costigliola.github.io/assertj/
Source0:        https://github.com/joel-costigliola/assertj-core/archive/assertj-build-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.opentest4j:opentest4j)
Requires:       java-headless >= 1.8
#!BuildRequires: junit5-minimal
BuildArch:      noarch

%description
A set of strongly-typed assertions to use for unit testing
(either with JUnit or TestNG).

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides API documentation for %{name}.

%prep
%setup -q -n assertj-assertj-build-%{version}

%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :spotless-maven-plugin
#pom_remove_plugin -r :bnd-maven-plugin
%pom_remove_plugin -r :bnd-resolver-maven-plugin
%pom_remove_plugin -r :bnd-testing-maven-plugin
%pom_remove_plugin -r :nexus-staging-maven-plugin
%pom_remove_plugin -r :license-maven-plugin
%pom_remove_plugin -r :flatten-maven-plugin
%pom_remove_dep -r :mockito-bom
%pom_remove_dep -r :junit-bom

%pom_disable_module assertj-core-kotlin assertj-tests/assertj-integration-tests
%pom_disable_module assertj-core-groovy assertj-tests/assertj-integration-tests

%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:provided

%build
%{mvn_build} -f -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.release=8 -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md CONTRIBUTING.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc CONTRIBUTING.md
%license LICENSE.txt

%changelog
