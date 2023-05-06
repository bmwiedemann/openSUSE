#
# spec file for package jflex-bootstrap
#
# Copyright (c) 2023 SUSE LLC
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


##### WARNING: please do not edit this auto generated spec file. Use the jflex.spec! #####
%global with_bootstrap 1
%bcond_with                bootstrap
Name:           jflex-bootstrap
Version:        1.8.2
Release:        0
Summary:        Lexical Analyzer Generator for Java
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.jflex.de/
Source0:        http://www.jflex.de/release/jflex-%{version}.tar.gz
Source1:        jflex-%{version}-generated-files.tar.xz
Source2:        jflex-build.xml
Patch0:         jflex-1.8.2-no-auto-value.patch
BuildRequires:  ant
BuildRequires:  glassfish-annotation-api
BuildRequires:  java-devel
BuildRequires:  javapackages-local
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
%pom_remove_plugin :jflex-maven-plugin
%pom_remove_plugin :cup-maven-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :jacoco-maven-plugin

%pom_xpath_remove "pom:plugin[pom:artifactId='maven-site-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='fmt-maven-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='cup-maven-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-shade-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='jacoco-maven-plugin']" parent.xml

%if %{with bootstrap}
%setup -q -T -D -a 1 -n jflex-%{version}
cp %{SOURCE2} build.xml
mkdir -p lib
%patch0 -p1
build-jar-repository -s lib java-cup-runtime glassfish-annotation-api
%else
%{mvn_file} : %{name} JFlex
%endif

%build
%if %{with bootstrap}
%{ant} package
%else
java-cup -parser LexParse -interface -destdir src/main/java src/main/cup/LexParse.cup
jflex -d src/main/java/jflex --skel src/main/jflex/skeleton.nested src/main/jflex/LexScan.flex
%{mvn_build} -f
%endif

%install

%if %{with bootstrap}
# jar
mkdir -p %{buildroot}%{_javadir}
cp -a target/jflex-%{version}.jar %{buildroot}%{_javadir}/jflex.jar

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

%files -f .mfiles
%endif
%license src/main/resources/LICENSE_JFLEX
%doc README.md changelog.md
%attr(0755,root,root) %{_bindir}/jflex

%if %without bootstrap
%files javadoc -f .mfiles-javadoc
%license src/main/resources/LICENSE_JFLEX
%endif

%changelog
