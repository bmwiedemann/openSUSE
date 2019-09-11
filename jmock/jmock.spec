#
# spec file for package jmock
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define section   free
Name:           jmock
Version:        1.2.0
Release:        0
Summary:        Test Java code using mock objects
License:        BSD-3-Clause
Group:          Development/Libraries/Java
Url:            http://jmock.codehaus.org/license.html
Source0:        jmock-1.2.0.tar.gz
# svn export http://svn.codehaus.org/jmock/tags/1.2.0/ jmock-1.2.0
Source1:        jmock-1.2.0.pom
Source2:        jmock-cglib-1.2.0.pom
Patch0:         jmock-1.2.0-AssertMo.patch
Patch1:         jmock-1.2.0-build_xml.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit
BuildRequires:  cglib-nohook >= 2.1.3
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit >= 3.8.1
BuildRequires:  objectweb-asm >= 5
Requires:       cglib >= 2.1.3
Requires:       objectweb-asm >= 5
BuildArch:      noarch

%description
jMock is a library for testing Java code using mock objects. Mock
   objects help you design and test the interactions between the
   objects in your programs. The jMock package: * makes it quick and
   easy to define mock objects, so you don't break the rhythm of
   programming.

* lets you define flexible constraints over object interactions,
   reducing the brittleness of your tests.

* is easy to extend.

%package        javadoc
Summary:        Test Java code using mock objects
Group:          Development/Libraries/Java

%description    javadoc
jMock is a library for testing Java code using mock objects. Mock
   objects help you design and test the interactions between the
   objects in your programs. The jMock package: * makes it quick and
   easy to define mock objects, so you don't break the rhythm of
   programming.

* lets you define flexible constraints over object interactions,
   reducing the brittleness of your tests.

* is easy to extend.

%package        demo
Summary:        Test Java code using mock objects
Group:          Development/Libraries/Java

%description    demo
jMock is a library for testing Java code using mock objects. Mock
   objects help you design and test the interactions between the
   objects in your programs. The jMock package: * makes it quick and
   easy to define mock objects, so you don't break the rhythm of
   programming.

* lets you define flexible constraints over object interactions,
   reducing the brittleness of your tests.

* is easy to extend.

%prep
%setup -q
find . -name "*.jar" | xargs rm
%patch0
%patch1

# needs net.sf.cglib.asm. classes fron dropped cglib-nohook
rm -rf src/test src/atest

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=`pwd`/build/classes:$(build-classpath objectweb-asm cglib)
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    -Dbuild.sysclasspath=only \
    package

%install
install -Dpm 644 build/%{name}-core-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 build/%{name}-cglib-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-cglib.jar
install -pm 644 build/%{name}-tests-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-tests.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
#install -pm 644 %{SOURCE2} \
#    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cglib.pom
%add_maven_depmap

#
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc-%{version}/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}
#
install -dm 755 %{buildroot}%{_datadir}/%{name}-%{version}
cp -pr examples/* %{buildroot}%{_datadir}/%{name}-%{version}

%files
%doc LICENSE.txt overview.html
%{_javadir}/*.jar
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml*

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
