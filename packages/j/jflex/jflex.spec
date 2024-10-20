#
# spec file for package jflex
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%if %{with bootstrap}
Name:           jflex-bootstrap
%else
Name:           jflex
%endif
Version:        1.9.1
Release:        0
Summary:        Lexical Analyzer Generator for Java
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.jflex.de/
Source0:        jflex-%{version}.tar.xz
Source1:        jflex-%{version}-generated-files.tar.xz
Source2:        jflex-build.xml
Patch0:         jflex-1.9.1-no-auto-value.patch
BuildRequires:  ant
BuildRequires:  glassfish-annotation-api
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  jsr-305
Requires:       java_cup
Requires:       javapackages-tools
BuildArch:      noarch
%if %{without bootstrap}
BuildRequires:  fdupes
BuildRequires:  java-cup
BuildRequires:  jflex-bootstrap
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.auto.value:auto-value)
BuildRequires:  mvn(com.google.auto.value:auto-value-annotations)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
Conflicts:      jflex-bootstrap
%else
BuildRequires:  java-cup-bootstrap
Conflicts:      jflex
%endif

%description
JFlex is a lexical analyzer generator for Java written in Java. It is
also a rewrite of the very useful tool JLex which was developed by
Elliot Berk at Princeton University. As Vern Paxson states for his C/C++
tool flex: they do not share any code though.

Design goals The main design goals of JFlex are:

    * Full unicode support
    * Fast generated scanners
    * Fast scanner generation
    * Convenient specification syntax
    * Platform independence
    * JLex compatibility

%if %without bootstrap
%package maven-plugin
Summary:        JFlex Maven Plugin

%description maven-plugin
This is a Maven 3 plugin to generate Lexer code in Java from
a Lexer specification, using JFlex.

%package -n cup-maven-plugin
Summary:        CUP Maven plugin

%description -n cup-maven-plugin
A plugin to generate Java parsers with CUP.

%package javadoc
Summary:        API documentation for %{name}
Provides:       %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < %{version}-%{release}

%description javadoc
This package provides %{summary}.

%endif

%prep
%setup -q -n jflex-%{version}
find . -name '*.jar' -print -delete
find . -name '.gitignore' -print -delete
rm -rf src/generated
%pom_remove_plugin :jflex-maven-plugin jflex
%pom_remove_plugin -r :cup-maven-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :fmt-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%pom_xpath_set pom:project/pom:properties/pom:jflex.jdk.version 1.8

%pom_disable_module benchmark
%pom_disable_module testsuite

%if %{with bootstrap}
%setup -q -T -D -a 1 -n jflex-%{version}
cp %{SOURCE2} jflex/build.xml
mkdir -p lib
%patch -P 0 -p1
build-jar-repository -s lib jsr-305 java-cup-runtime glassfish-annotation-api
%else
%{mvn_file} :jflex %{name} JFlex
%{mvn_package} :jflex-parent __noinstall
%endif

%build
%if %{with bootstrap}
ant -Dproject.version=%{version} -f jflex/build.xml package
%else
java-cup -parser LexParse -interface -destdir jflex/src/main/java jflex/src/main/cup/LexParse.cup
jflex -d jflex/src/main/java/jflex --skel jflex/src/main/jflex/skeleton.nested jflex/src/main/jflex/LexScan.flex
%{mvn_build} -fs
%endif

%install

%if %{with bootstrap}
# jar
mkdir -p %{buildroot}%{_javadir}
cp -a jflex/target/jflex-%{version}.jar %{buildroot}%{_javadir}/jflex.jar

# compatibility symlink
(cd %{buildroot}%{_javadir} && ln -s jflex.jar JFlex.jar)
%else
%mvn_install
%fdupes -s %{buildroot}/%{_javadocdir}/%{name}
%endif

%jpackage_script jflex.Main "" "" jflex:java-cup jflex true

%if %{with bootstrap}
%files
%{_javadir}/jflex.jar
%{_javadir}/JFlex.jar
%else

%files -f .mfiles-jflex
%endif
%license LICENSE.md
%doc README.md
%attr(0755,root,root) %{_bindir}/jflex

%if %without bootstrap
%files maven-plugin -f .mfiles-jflex-maven-plugin
%doc jflex-maven-plugin/README.md

%files -n cup-maven-plugin -f .mfiles-cup-maven-plugin

%files javadoc -f .mfiles-javadoc
%license LICENSE.md
%endif

%changelog
