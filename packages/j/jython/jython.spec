#
# spec file for package jython
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


%global pyver %(python3 -c 'import sys;print(sys.version[0:3])')
%global cpython_version    %{pyver}
%global pyxml_version      %{pyver}
%global _python_bytecompile_errors_terminate_build 0
Name:           jython
Version:        2.7.3
Release:        0
Summary:        A Java implementation of the Python language
License:        Apache-2.0 AND Python-2.0
Group:          Development/Languages/Python
URL:            https://www.jython.org/
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-build.patch
Patch1:         %{name}-dont-validate-pom.patch
Patch2:         %{name}-cachedir.patch
Patch3:         %{name}-fix-tty-detection.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  antlr3-java
BuildRequires:  antlr3-tool
BuildRequires:  apache-commons-compress
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  guava
BuildRequires:  jansi
BuildRequires:  jarjar
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  jffi
BuildRequires:  jline
BuildRequires:  jnr-constants
BuildRequires:  jnr-ffi
BuildRequires:  jnr-posix
BuildRequires:  lucene-core
BuildRequires:  objectweb-asm
BuildRequires:  python3 >= %{cpython_version}
BuildRequires:  python3-xml >= %{pyxml_version}
BuildRequires:  stringtemplate4
Requires:       antlr3-java
Requires:       antlr3-tool
Requires:       apache-commons-compress
Requires:       glassfish-servlet-api
Requires:       guava
Requires:       jansi
Requires:       jarjar
Requires:       jffi
Requires:       jline
Requires:       jnr-constants
Requires:       jnr-ffi
Requires:       jnr-posix
Requires:       junit
Requires:       lucene-core
Requires:       objectweb-asm
Requires:       stringtemplate4
Obsoletes:      %{name}-manual

%description
Jython is an implementation of the high-level, dynamic, object-oriented
language Python seamlessly integrated with the Java platform. The
predecessor to Jython, JPython, is certified as 100% Pure Java. Jython
is freely available for both commercial and noncommercial use and is
distributed with source code. Jython is complementary to Java and is
especially suited for the following tasks: Embedded scripting--Java
programmers can add the Jython libraries to their system to allow end
users to write simple or complicated scripts that add functionality to
the application. Interactive experimentation--Jython provides an
interactive interpreter that can be used to interact with Java packages
or with running Java applications. This allows programmers to
experiment and debug any Java system using Jython. Rapid application
development--Python programs are typically 2-10X shorter than the
equivalent Java program. This translates directly to increased
programmer productivity. The seamless interaction between Python and
Java allows developers to freely mix the two languages both during
development and in shipping products.

%package javadoc
Summary:        Javadoc for jython
Group:          Development/Libraries/Java
Provides:       jython-manual = %{version}
Obsoletes:      jython-manual < %{version}
BuildArch:      noarch

%description javadoc
API documentation for %{name}.

%package demo
Summary:        Demonstration and samples for jython
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description demo
Demonstrations and samples for %{name}.

%prep
%autosetup -p1

%build
build-jar-repository -s -p extlibs \
    jffi/jffi \
    antlr3 \
    antlr3-runtime \
    commons-compress \
    glassfish-servlet-api \
    guava/guava \
    jansi/jansi \
    jarjar \
    jline/jline \
    jnr/jnr-constants \
    jnr/jnr-ffi \
    jnr/jnr-posix \
    junit \
    lucene/lucene-core \
    objectweb-asm/asm \
    objectweb-asm/asm-commons \
    objectweb-asm/asm-util \
    stringtemplate4/ST4

%{ant} -Djython.version=%{version}

pushd maven
%{ant} -Djython.version=%{version} bundle
popd

# Symlink run-time libs
rm dist/javalib/*.jar
build-jar-repository -s -p dist/javalib \
    jffi/jffi \
    antlr3 \
    antlr3-runtime \
    commons-compress \
    glassfish-servlet-api \
    guava/guava \
    jansi/jansi \
    jarjar \
    jline/jline \
    jnr/jnr-constants \
    jnr/jnr-ffi \
    jnr/jnr-posix \
    junit \
    lucene/lucene-core \
    objectweb-asm/asm \
    objectweb-asm/asm-commons \
    objectweb-asm/asm-util \
    stringtemplate4/ST4

# remove shebangs from python files
find dist -type f -name '*.py' | xargs sed -i "s:#!\s*/usr.*::"

# fix env-script-interpreter
sed -i 's/env bash/bash/' dist/bin/%{name}{,.py}

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 build/maven/%{name}-%{version}.pom %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a org.python:jython-standalone,jython:jython

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/Doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# jython home dir
install -d -m 755 %{buildroot}%{_libdir}/%{name}
ln -s %{_javadir}/%{name}.jar %{buildroot}%{_libdir}/%{name}
ln -s %{_javadir}/%{name}.jar %{buildroot}%{_libdir}/%{name}/%{name}-dev.jar
cp -pr dist/javalib %{buildroot}%{_libdir}/%{name}
rm dist/bin/jython_regrtest.bat
rm dist/bin/jython.exe
cp -pr dist/bin %{buildroot}%{_libdir}/%{name}
install -m 644 dist/registry %{buildroot}%{_libdir}/%{name}

# libs without tests
rm -rf dist/Lib/{distutils/tests,email/test,json/tests,test,unittest/test}
cp -pr dist/Lib %{buildroot}%{_libdir}/%{name}
%fdupes -s %{buildroot}%{_libdir}/%{name}/Lib

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr Demo %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}/Demo

# javadoc
install -d -m 755 %{buildroot}%{_datadir}/%{name}/Doc
ln -s %{_javadocdir}/%{name} %{buildroot}%{_datadir}/%{name}/Doc/javadoc

# scripts
install -d %{buildroot}%{_bindir}
ln -s %{_libdir}/%{name}/bin/jython %{buildroot}%{_bindir}

%files -f .mfiles
%doc ACKNOWLEDGMENTS NEWS README.txt
%license LICENSE.txt
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/bin
%{_libdir}/%{name}/javalib
%{_libdir}/%{name}/jython.jar
%{_libdir}/%{name}/jython-dev.jar
%{_libdir}/%{name}/Lib
%{_libdir}/%{name}/registry

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/Doc

%files demo
%license LICENSE.txt
%{_datadir}/%{name}/Demo

%changelog
