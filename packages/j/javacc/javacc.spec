#
# spec file for package javacc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2005, JPackage Project
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global base_name javacc
Version:        7.0.4
Release:        0
Summary:        A Parser and Scanner Generator for Java
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://javacc.org
Source0:        https://github.com/javacc/javacc/archive/%{version}.tar.gz
BuildRequires:  ant
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{base_name}-bootstrap
BuildRequires:  javapackages-tools
Provides:       %{base_name}
%else
Name:           %{base_name}
BuildRequires:  %{base_name}
BuildRequires:  fdupes
BuildRequires:  javapackages-local
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Provides:       %{base_name}-bootstrap
Obsoletes:      %{base_name}-bootstrap
%endif

%description
Java Compiler Compiler (JavaCC) is the most popular parser generator
for use with Java applications. A parser generator is a tool that reads
a grammar specification and converts it to a Java program that can
recognize matches to the grammar. In addition to the parser generator
itself, JavaCC provides other standard capabilities related to parser
generation such as tree building (via a tool called JJTree included
with JavaCC), actions, debugging, etc.

%package manual
Summary:        Manual for %{name}
Group:          Documentation/Other

%description manual
Manual for %{name}.

%package demo
Summary:        Examples for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description demo
Examples for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{version}
rm -f lib/*.jar
%if %{without bootstrap}
rm -f bootstrap/javacc.jar
build-jar-repository -s -p bootstrap javacc

find ./examples -type f -exec sed -i 's/\r//' {} \;

# The pom dependencies are wrong
%pom_xpath_remove pom:project/pom:dependencies
%endif

%build
%{ant} \
  -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
%if %{with bootstrap}
  jar
%else
  jar javadoc
%endif

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{base_name}-%{version}.jar %{buildroot}%{_javadir}/%{base_name}.jar

%if %{without bootstrap}

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}.pom
%add_maven_depmap %{base_name}.pom %{base_name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}
%fdupes -s www
%fdupes -s examples

%jpackage_script javacc '' '' javacc javacc true
ln -s %{_bindir}/javacc %{buildroot}%{_bindir}/javacc.sh
%jpackage_script jjdoc '' '' javacc jjdoc true
%jpackage_script jjtree '' '' javacc jjtree true

%endif

%if %{with bootstrap}
%files
%{_javadir}/%{base_name}.jar
%else
%files -f .mfiles
%{_bindir}/javacc
%{_bindir}/javacc.sh
%{_bindir}/jjdoc
%{_bindir}/jjtree
%endif
%license LICENSE
%doc README

%if %{without bootstrap}
%files manual
%doc www/*

%files demo
%doc examples

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}
%endif

%changelog
