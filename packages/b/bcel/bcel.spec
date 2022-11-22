#
# spec file for package bcel
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


Name:           bcel
Version:        5.2
Release:        0
Summary:        Byte Code Engineering Library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/proper/commons-bcel/
Source0:        http://archive.apache.org/dist/commons/bcel/source/%{name}-%{version}-src.tar.gz
Source1:        http://archive.apache.org/dist/commons/bcel/source/%{name}-%{version}-src.tar.gz.asc
Source2:        http://repo.maven.apache.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source3:        bcel.keyring
Patch0:         bcel-5.2-encoding.patch
#PATCH-FIX-UPSTREAM bsc#1205125 CVE-2022-42920 Out-of-bounds writing issue
Patch1:         bcel-CVE-2022-42920.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  regexp
#!BuildIgnore:  xalan-j2 xerces-j2 xml-apis xml-resolver
Requires:       regexp
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

%prep
%autosetup -p1

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
# very broken build
perl -p -i -e 's| depends=\"examples\"||g;' build.xml
touch manifest.txt

%build
export CLASSPATH=%(build-classpath regexp)
export OPT_JAR_LIST="ant/ant-nodeps"
ant \
    -Dant.build.javac.target=8 -Dant.build.javac.source=8 \
    -Dbuild.dest=./build -Dbuild.dir=./build -Dname=%{name} \
    compile jar

%install
# jars
mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

mkdir -p %{buildroot}%{_mavenpomdir}
install -m 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}-%{version}.pom

%add_maven_depmap %{name}-%{version}.pom %{name}-%{version}.jar -a "bcel:bcel"

%files -f .mfiles
%license LICENSE.txt
%{_javadir}/*

%changelog
