#
# spec file for package java-cup
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


%global _without_bootstrap 1
%define cvs_version        11a
%define real_name   java-cup
%bcond_with                bootstrap
Name:           java-cup
Version:        0.11
Release:        0
Summary:        LALR Parser Generator in Java
License:        HPND
Group:          Development/Libraries/Java
Url:            http://www2.cs.tum.edu/projects/cup/
# https://www2.in.tum.de/WebSVN/dl.php?repname=CUP&path=/develop/&rev=0&isdir=1
Source0:        develop.tar.bz2
Source1:        java-cup.script
Source2:        java-cup-generated-files.tar.bz2
# From          http://www2.cs.tum.edu/projects/cup/
Source3:        java-cup.license
Patch1:         java-cup-no-classpath-in-manifest.patch
Patch2:         java-cup-no-cup-no-jflex.patch
Patch3:         java-cup-classpath.patch
# Missing symbolFactory initialization in lr_parser, causes sinjdoc to crash
Patch4:         java-cup-lr_parser-constructor.patch
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  xml-commons-apis-bootstrap
BuildRequires:  xml-commons-resolver-bootstrap
#!BuildIgnore:  xml-commons-apis xml-commons-resolver xalan-j2 xerces-j2
Obsoletes:      java_cup < %{version}-%{release}
Provides:       java_cup = %{version}-%{release}
BuildArch:      noarch
%if %without bootstrap
BuildRequires:  java-cup-bootstrap
BuildRequires:  jflex
%endif
# bootstrap variant is just stripped down java-cup, so it conflicts
%if %without bootstrap
Conflicts:      java-cup-bootstrap
%else
Conflicts:      java-cup
%endif

%description
java-cup is a LALR Parser Generator in Java. With v0.11, you can: *
   use CUP in an Ant-Target

* start CUP by a simple command like java -jar java-cup-11a.jar
   myGrammar.cup

* use generic parametrized classes (since Java 1.5) as datatypes for
   non terminals and terminals

* have Your own symbol classes

%if %without bootstrap
%package manual
Summary:        LALR Parser Generator in Java
Group:          Development/Libraries/Java

%description manual
java-cup is a LALR Parser Generator in Java. With v0.11, you can: *
   use CUP in an Ant-Target

* start CUP by a simple command like java -jar java-cup-11a.jar
   myGrammar.cup

* use generic parametrized classes (since Java 1.5) as datatypes for
   non

* terminals and terminals

* have Your own symbol classes

%endif

%prep
%setup -q -n develop
%patch1 -p1
%if %with bootstrap
%setup -q -T -D -a 2 -n develop
%patch2 -p1
%else
%{_bindir}/find . -name '*.jar' | %{_bindir}/xargs rm
%patch3 -p1
%endif
%patch4 -p1
perl -pi -e 's/1\.2/1.6/g' build.xml
mkdir -p classes dist
cp %{SOURCE3} license.txt

%build
%if %with bootstrap
export CLASSPATH=
%else
export CLASSPATH=$(build-classpath java-cup jflex)
%endif
export OPT_JAR_LIST=:
ant

%install
# jar
mkdir -p %{buildroot}%{_javadir}
cp -a dist/%{real_name}-%{cvs_version}.jar %{buildroot}%{_javadir}/%{real_name}-%{version}.jar
cp -a dist/%{real_name}-%{cvs_version}-runtime.jar %{buildroot}%{_javadir}/%{real_name}-runtime-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)
# compatibility symlinks
(cd %{buildroot}%{_javadir} && ln -s %{real_name}.jar java_cup.jar && ln -s %{real_name}-runtime.jar java_cup-runtime.jar)
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/%{real_name}

%files
%doc changelog.txt license.txt
%attr(0755,root,root) %{_bindir}/%{real_name}
%{_javadir}/*
%if %without bootstrap
%files manual
%doc manual.html

%endif

%changelog
