#
# spec file for package jflex-maven-plugin
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


Name:           jflex-maven-plugin
Version:        1.8.2
Release:        0
Summary:        JFlex Maven Plugin
License:        BSD-3-Clause
URL:            https://github.com/jflex-de/jflex
Source0:        %{name}-%{version}.tar.xz
Source1:        https://raw.githubusercontent.com/jflex-de/jflex/v%{version}/pom.xml#/%{name}-%{version}-parent.xml
Source2:        https://raw.githubusercontent.com/jflex-de/jflex/v%{version}/LICENSE.md
Patch0:         0001-jflex-maven-plugin-updates-for-guava-26.0-jre.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(de.jflex:jflex)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildArch:      noarch

%description
This is a Maven 3 plugin to generate Lexer code in Java from
a Lexer specification, using JFlex.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q
cp %{SOURCE1} parent.xml
cp %{SOURCE2} LICENSE.md
%pom_xpath_set pom:parent/pom:relativePath parent.xml

%patch0 -p2

%pom_remove_plugin :maven-enforcer-plugin

%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:annotationProcessorPaths" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-site-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='fmt-maven-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='cup-maven-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-shade-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='jacoco-maven-plugin']" parent.xml


%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md

%changelog
