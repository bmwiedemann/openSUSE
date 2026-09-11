#
# spec file for package javaparser
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        3.28.2
Release:        0
Summary:        Java Parser and Abstract Syntax Tree for Java
License:        Apache-2.0 OR LGPL-3.0-or-later
Group:          Development/Libraries/Java
URL:            https://javaparser.org
Source0:        https://github.com/javaparser/javaparser/archive/%{name}-parent-%{version}.tar.gz
Source1:        %{name}-build.tar.xz
BuildRequires:  aqute-bnd
BuildRequires:  checker-qual
BuildRequires:  fdupes
BuildRequires:  guava
BuildRequires:  java-devel >= 1.8
BuildRequires:  javacc
BuildRequires:  javapackages-local >= 6
BuildRequires:  javassist
BuildArch:      noarch

%description
A set of libraries implementing a Java 1.0 - Java 17 Parser with advanced
analysis functionalities.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%autosetup -n %{name}-%{name}-parent-%{version} -a1

sed -i 's/\r//' readme.md

# Missing dep on jbehave for testing
%pom_disable_module javaparser-core-testing
%pom_disable_module javaparser-core-testing-bdd
%pom_disable_module javaparser-symbol-solver-testing

# Only need to ship the core module
%pom_disable_module javaparser-core-metamodel-generator
%pom_disable_module javaparser-core-serialization

echo "-reproducible: true" >> javaparser-core/bnd.bnd
echo "-noextraheaders: true" >> javaparser-core/bnd.bnd
echo "-snapshot: SNAPSHOT" >> javaparser-core/bnd.bnd

%build
mkdir -p lib
build-jar-repository -s -p lib \
    aqute-bnd/biz.aQute.bnd.ant \
    checker-qual \
    guava \
    javacc \
    javassist
ant -Dtest.skip=true package javadoc

%install
# dirs
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}

# jars
install -pm 0644 %{name}-core/target/%{name}-core-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}/%{name}-core.jar
install -pm 0644 %{name}-symbol-solver-core/target/%{name}-symbol-solver-core-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}/%{name}-symbol-solver-core.jar
# poms
%{mvn_install_pom} %{name}-core/pom.xml \
  %{buildroot}%{_mavenpomdir}/%{name}/%{name}-core.pom
%add_maven_depmap %{name}/%{name}-core.pom %{name}/%{name}-core.jar -a com.google.code.javaparser:javaparser
%{mvn_install_pom} %{name}-symbol-solver-core/pom.xml \
  %{buildroot}%{_mavenpomdir}/%{name}/%{name}-symbol-solver-core.pom
%add_maven_depmap %{name}/%{name}-symbol-solver-core.pom %{name}/%{name}-symbol-solver-core.jar

# javadoc
cp -r %{name}-core/target/site/apidocs \
  %{buildroot}%{_javadocdir}/%{name}/%{name}-core
cp -r  %{name}-symbol-solver-core/target/site/apidocs \
  %{buildroot}%{_javadocdir}/%{name}/%{name}-symbol-solver-core
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc readme.md changelog.md
%license LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%changelog
