#
# spec file for package objenesis
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2009, JPackage Project
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


%global major 2
%global minor 6
%global micro 0
%global fullversion %{major}.%{minor}.%{micro}
%global specversion %{major}.%{minor}
Name:           objenesis
%if %{micro}
Version:        %{fullversion}
Release:        0
%else
Version:        %{specversion}
Release:        0
%endif
Summary:        A library for instantiating Java objects
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://objenesis.org/
Source0:        https://github.com/easymock/%{name}/archive/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
# uses sun.misc.Unsafe
BuildConflicts: java-devel >= 9
BuildArch:      noarch

%description
Objenesis is a small Java library that serves one purpose: to instantiate
a new object of a particular class.
Java supports dynamic instantiation of classes using Class.newInstance();
however, this only works if the class has an appropriate constructor. There
are many times when a class cannot be instantiated this way, such as when
the class contains constructors that require arguments, that have side effects,
and/or that throw exceptions. As a result, it is common to see restrictions
in libraries stating that classes must require a default constructor.
Objenesis aims to overcome these restrictions by bypassing the constructor
on object instantiation. Needing to instantiate an object without calling
the constructor is a fairly specialized task, however there are certain cases
when this is useful:
* Serialization, Remoting and Persistence - Objects need to be instantiated
  and restored to a specific state, without invoking code.
* Proxies, AOP Libraries and Mock Objects - Classes can be sub-classed without
  needing to worry about the super() constructor.
* Container Frameworks - Objects can be dynamically instantiated in
  non-standard ways.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# Enable generation of pom.properties (rhbz#1017850)
%pom_xpath_remove pom:addMavenDescriptor

%pom_remove_plugin :maven-timestamp-plugin
%pom_remove_plugin :maven-license-plugin
%pom_xpath_remove "pom:dependency[pom:scope='test']" tck

%pom_xpath_remove pom:build/pom:extensions

for i in main tck; do
  %pom_remove_parent ${i}
  %pom_xpath_inject "pom:project" "<groupId>org.objenesis</groupId><version>%{version}</version>" ${i}
done

%build
mkdir -p main/build/classes
javac -d main/build/classes -source 6 -target 6 -encoding utf-8 \
  $(find main/src/main/java -name *.java | xargs)
jar cf %{name}-%{version}.jar -C main/build/classes .

touch manifest.txt
echo "Bundle-Description: A library for instantiating Java objects" >> manifest.txt
echo "Bundle-License: http://www.apache.org/licenses/LICENSE-2.0.txt" >> manifest.txt
echo "Bundle-Name: Objenesis" >> manifest.txt
echo "Bundle-SymbolicName: org.objenesis" >> manifest.txt
echo "Bundle-Version: %{fullversion}" >> manifest.txt
echo "Export-Package: org.objenesis;uses:=\"org.objenesis.instantiator,org.objenesis.strategy\";version=\"%{fullversion}\",\
org.objenesis.instantiator.android;uses:=\"org.objenesis.instantiator,\
org.objenesis.instantiator.annotations\";version=\"%{fullversion}\",\
org.objenesis.instantiator.basic;uses:=\"org.objenesis.instantiator,org.objenesis.instantiator.annotations\";version=\"%{fullversion}\",\
org.objenesis.instantiator;version=\"%{fullversion}\",\
org.objenesis.instantiator.gcj;uses:=\"org.objenesis.instantiator,org.objenesis.instantiator.annotations\";version=\"%{fullversion}\",\
org.objenesis.instantiator.util;uses:=\"sun.misc\";version=\"%{fullversion}\",org.objenesis.instantiator.annotations;version=\"%{fullversion}\",org.objenesis.instantiator.perc;uses:=\"org.objenesis.instantiator,org.objenesis.instantiator.annotations\";version=\"%{fullversion}\",\
org.objenesis.instantiator.sun;uses:=\"org.objenesis.instantiator,\
org.objenesis.instantiator.annotations\";version=\"%{fullversion}\",\
org.objenesis.strategy;uses:=\"org.objenesis.instantiator\";version=\"%{fullversion}\"" | sed 's/.\{71\}/&\n /g' >> manifest.txt
echo "Import-Package: sun.misc;resolution:=optional,\
COM.newmonics.PercClassloader;resolution:=optional,\
sun.reflect;resolution:=optional" | sed 's/.\{71\}/&\n /g' >> manifest.txt
echo "Require-Capability: osgi.ee;filter:=\"(&(osgi.ee=JavaSE)(version=1.6))\"" >> manifest.txt
jar ufm %{name}-%{version}.jar manifest.txt

mkdir -p tck/build/classes
javac -d tck/build/classes -source 6 -target 6 -encoding utf-8 \
  -cp %{name}-%{version}.jar \
  $(find tck/src/main/java -name *.java | xargs)
jar cf %{name}-tck-%{version}.jar -C tck/build/classes .
jar uf %{name}-tck-%{version}.jar -C tck/src/main/resources .
jar ufe %{name}-tck-%{version}.jar org.objenesis.tck.Main

mkdir -p build/apidoc
javadoc -d build/apidoc -source 6 -encoding utf-8 \
  $(find main/src/main/java -name *.java && \
    find tck/src/main/java -name *.java | xargs)

%install
# jars
install -dm 755 %{buildroot}%{_javadir}/%{name}
install -m 0644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -m 0644 %{name}-tck-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-tck.jar

# poms
install -dm 755 %{buildroot}%{_mavenpomdir}/%{name}
install -m 0644 main/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
install -m 0644 tck/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-tck.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
%add_maven_depmap %{name}/%{name}-tck.pom %{name}/%{name}-tck.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -aL build/apidoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
