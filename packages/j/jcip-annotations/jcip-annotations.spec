#
# spec file for package jcip-annotations
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jcip-annotations
Version:        1.0
Release:        0
Summary:        Java Concurrency in Practice
License:        CC-BY-2.5
Group:          Development/Libraries/Java
Url:            http://www.jcip.net/
Source0:        http://www.jcip.net/jcip-annotations-src.jar
Source1:        http://repo1.maven.org/maven/livetribe/maven/m2/net/jcip/jcip-annotations/1.0/jcip-annotations-1.0.pom
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  unzip
Requires:       java >= 1.6.0
BuildArch:      noarch

%description
Class, field, and method level annotations for describing thread-safety
policies.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
Class, field, and method level annotations for describing thread-safety
policies.

%prep
%setup -q -c
mkdir -p target/site/apidocs/
mkdir -p target/classes/
mkdir -p src/main/java/
mv net src/main/java

%build
export JAVA_HOME=%{_jvmdir}/java
$JAVA_HOME/bin/javac -source 1.6 -target 1.6 -d target/classes $(find src/main/java -name "*.java")
$JAVA_HOME/bin/javadoc -source 1.6 -d target/site/apidocs -sourcepath src/main/java net.jcip.annotations
for f in $(find aQute/ -type f -not -name "*.class"); do
    cp $f target/classes/$f
done
pushd target/classes
$JAVA_HOME/bin/jar cmf ../../META-INF/MANIFEST.MF ../%{name}-%{version}.jar *
popd

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
