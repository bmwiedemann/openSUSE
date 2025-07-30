#
# spec file for package eclipse-collections
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


Name:           eclipse-collections
Version:        12.0.0
Release:        0
Summary:        Collections framework for Java
License:        BSD-3-Clause AND EPL-1.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/collections
Source0:        https://github.com/eclipse/%{name}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 11
BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bnd.annotation)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.platform:junit-platform-engine)
BuildRequires:  mvn(org.junit.vintage:junit-vintage-engine)
BuildArch:      noarch

%description
Eclipse Collections is a comprehensive collections library for Java. The
library enables productivity and performance by delivering an expressive and
efficient set of APIs and types. The iteration protocol was inspired by the
Smalltalk collection framework, and the collections are compatible with the
Java Collection Framework types.

Eclipse Collections is compatible with Java 8+. Eclipse Collections is a part
of the OpenJDK Quality Outreach program, and it is validated for different
versions of the OpenJDK.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup

%pom_remove_plugin -r org.jacoco:jacoco-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_disable_module jcstress-tests
%pom_disable_module test-coverage
%pom_disable_module unit-tests-java8

%{mvn_package} :*-tests __noinstall

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE-*.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE-*.txt

%changelog
