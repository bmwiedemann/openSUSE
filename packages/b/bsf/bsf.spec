#
# spec file for package bsf
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


Name:           bsf
Version:        2.4.0
Release:        0
Summary:        Bean Scripting Framework
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/bsf/
Source0:        http://www.apache.org/dist/commons/bsf/source/%{name}-src-%{version}.tar.gz
Source1:        bsf-pom.xml
Source1000:     http://www.apache.org/dist/commons/bsf/source/%{name}-src-%{version}.tar.gz.asc
Source1001:     bsf.keyring
Patch0:         build-file.patch
Patch1:         build.properties.patch
BuildRequires:  ant
BuildRequires:  apache-commons-logging
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  rhino
BuildRequires:  xalan-j2
#!BuildIgnore:  jline
Requires:       mvn(commons-logging:commons-logging)
BuildArch:      noarch

%description
Bean Scripting Framework (BSF) is a set of Java classes that provides
scripting language support within Java applications and access to Java
objects and methods from scripting languages. BSF allows writing JSPs
in languages other than Java while providing access to the Java class
library. In addition, BSF permits any Java application to be
implemented in part (or dynamically extended) by a language that is
embedded within it. This is achieved by providing an API that permits
calling scripting language engines from within Java as well as an
object registry that exposes Java objects to these scripting language
engines.

This BSF package currently supports several scripting languages: *
   Javascript (using Rhino ECMAScript, from the Mozilla project)
* XSLT Stylesheets (as a component of Apache XML project's Xalan and
   Xerces)

In addition, the following languages are supported with their own
   BSF engines: * Java (using BeanShell, from the BeanShell project)
* JRuby
* JudoScript

%package javadoc
Summary:        Javadoc for bsf
Group:          Development/Libraries/Java

%description javadoc
Bean Scripting Framework (BSF) is a set of Java classes which provides
scripting language support within Java applications, and access to Java
objects and methods from scripting languages. BSF allows one to write
JSPs in languages other than Java while providing access to the Java
class library. In addition, BSF permits any Java application to be
implemented in part (or dynamically extended) by a language that is
embedded within it. This is achieved by providing an API that permits
calling scripting language engines from within Java, as well as an
object registry that exposes Java objects to these scripting language
engines.

This package contains the javadoc documentation for the Bean Scripting
Framework.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
find -name \*.jar -delete

%build
mkdir -p lib
build-jar-repository -s -p lib apache-commons-logging rhino xalan-j2
%{ant} -Dant.build.javac.source=8 -Dant.build.javac.target=8 jar javadocs

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/lib/%{name}.jar \
            %{buildroot}%{_javadir}/%{name}.jar

# pom and depmap frag
install -DTm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.bsf:%{name}"

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc AUTHORS.txt CHANGES.txt README.txt TODO.txt RELEASE-NOTE.txt

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
