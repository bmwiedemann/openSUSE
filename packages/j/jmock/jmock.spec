#
# spec file for package jmock
#
# Copyright (c) 2024 SUSE LLC
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
URL:            http://jmock.codehaus.org/license.html
Source0:        %{name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source2:        https://repo1.maven.org/maven2/jmock/%{name}-cglib/%{version}/%{name}-cglib-%{version}.pom
Patch0:         jmock-1.2.0-AssertMo.patch
Patch1:         jmock-1.2.0-build_xml.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit
BuildRequires:  cglib-nohook >= 2.1.3
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  junit >= 3.8.1
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
%patch -P 0
%patch -P 1

# needs net.sf.cglib.asm. classes fron dropped cglib-nohook
rm -rf src/test src/atest

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=`pwd`/build/classes:$(build-classpath cglib)
ant \
    -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
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
%{mvn_install_pom} %{SOURCE1} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%{mvn_install_pom} %{SOURCE2} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}-cglib.pom
%add_maven_depmap JPP-%{name}-cglib.pom %{name}-cglib.jar

#
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc-%{version}/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}
#
install -dm 755 %{buildroot}%{_datadir}/%{name}-%{version}
cp -pr examples/* %{buildroot}%{_datadir}/%{name}-%{version}
%fdupes -s %{buildroot}%{_datadir}/%{name}-%{version}

%files -f .mfiles
%license LICENSE.txt
%doc overview.html
%{_javadir}/%{name}-tests.jar

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
