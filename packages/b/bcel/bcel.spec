#
# spec file for package bcel
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


Name:           bcel
Version:        6.8.0
Release:        0
Summary:        Byte Code Engineering Library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-bcel/
Source0:        https://archive.apache.org/dist/commons/bcel/source/%{name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-lang3
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
#!BuildIgnore:  xalan-j2 xerces-j2 xml-apis xml-resolver
BuildArch:      noarch

%description
The Byte Code Engineering Library is intended to give users a
convenient way to analyze, create, and manipulate (binary) Java class
files (those ending with .class). Classes are represented by objects
that contain all the symbolic information of the given class: methods,
fields, and byte code instructions, in particular.

Such objects can be read from an existing file, transformed by a
program (such as a class loader at runtime), and dumped to a file
again. An even more interesting application is the creation of classes
from scratch at runtime. The Byte Code Engineering Library (BCEL) may
also be useful if you want to learn about the Java Virtual Machine
(JVM) and the format of Java .class files.

BCEL is already being used successfully in several projects, such as
compilers, optimizers, obfuscators, code generators, and analysis
tools.

It contains a byte code verifier named JustIce, which usually gives you
much better information about what is wrong with your code than the
standard JVM message.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
cp %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib apache-commons-lang3
%ant jar javadoc

%install
# jar
mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
mkdir -p %{buildroot}%{_mavenpomdir}
%mvn_install_pom pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a "bcel:bcel"
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
