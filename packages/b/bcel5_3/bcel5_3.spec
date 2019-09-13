#
# spec file for package bcel5_3
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define section free
Name:           bcel5_3
Version:        5.3
Release:        0
Summary:        Byte Code Engineering Library
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://jakarta.apache.org/bcel/
# svn co -r417157 http://svn.apache.org/repos/asf/jakarta/bcel/trunk bcel
Source0:        http://www.apache.org/dist/jakarta/bcel/source/bcel.tar.bz2
# from bcel package
Source1000:     build.xml
Source1001:     manifest.txt
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  junit
Provides:       bcel5.3 = %{version}-%{release}
BuildArch:      noarch

%description
The Byte Code Engineering Library (formerly known as JavaClass) is
intended to give users a convenient possibility to analyze, create, and
manipulate (binary) Java class files (those ending with .class). Classes
are represented by objects which contain all the symbolic information of
the given class: methods, fields and byte code instructions, in
particular.  Such objects can be read from an existing file, be
transformed by a program (e.g. a class loader at run-time) and dumped to
a file again. An even more interesting application is the creation of
classes from scratch at run-time. The Byte Code Engineering Library
(BCEL) may be also useful if you want to learn about the Java Virtual
Machine (JVM) and the format of Java .class files.  BCEL is already
being used successfully in several projects such as compilers,
optimizers, obsfuscators and analysis tools, the most popular probably
being the Xalan XSLT processor at Apache.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
The Byte Code Engineering Library (formerly known as JavaClass) is
intended to give users a convenient possibility to analyze, create, and
manipulate (binary) Java class files (those ending with .class). Classes
are represented by objects which contain all the symbolic information of
the given class: methods, fields and byte code instructions, in
particular.  Such objects can be read from an existing file, be
transformed by a program (e.g. a class loader at run-time) and dumped to
a file again. An even more interesting application is the creation of
classes from scratch at run-time. The Byte Code Engineering Library
(BCEL) may be also useful if you want to learn about the Java Virtual
Machine (JVM) and the format of Java .class files.  BCEL is already
being used successfully in several projects such as compilers,
optimizers, obsfuscators and analysis tools, the most popular probably
being the Xalan XSLT processor at Apache.

%prep
%setup -q -n bcel
chmod -x NOTICE.txt

cp %{SOURCE1000} %{SOURCE1001} .

%build
ant -Dbuild.dest=target/classes -Dbuild.dir=target -Dsrc.dir=src/main/java \
    -Dexamples.dir=src/examples -Dname=bcel-%{version} -Dapidocs.dir=target/site/apidocs \
        -Ddocs.src=xdocs -Djakarta.site2=jakarta-site2 -Djdom.jar=jdom.jar \
        -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
        compile jar apidocs

%install
# jars
mkdir -p %{buildroot}%{_javadir}
install -m 644 target/bcel-%{version}*.jar %{buildroot}%{_javadir}/bcel5.3-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -a target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -s %{name}-%{version} %{name})
# FIXME: (dwalluck): breaks --short-circuit
rm -rf docs/api
%fdupes %{buildroot}%{_javadocdir}

%files
%doc LICENSE.txt NOTICE.txt README.txt RELEASE-NOTES.txt TODO.JustIce
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
