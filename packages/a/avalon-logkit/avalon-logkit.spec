#
# spec file for package avalon-logkit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2005, JPackage Project
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


%define     short_name      logkit
%define     camelcase_short_name      LogKit
Name:           avalon-logkit
Version:        2.1
Release:        0
Summary:        Java logging toolkit
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://avalon.apache.org/%{short_name}/
#Source0:       http://www.apache.org/dist/excalibur/%{name}/source/%{name}-%{version}-src.zip
#Source1:       http://repo1.maven.org/maven2/avalon-logkit/avalon-logkit/%{version}/%{name}-%{version}.pom
Source0:        %{name}-%{version}-src.zip
Source1:        %{name}-%{version}.pom
Patch0:         fix-java6-compile.patch
Patch1:         avalon-logkit-pom-deps.patch
Patch2:         avalon-logkit-encoding.patch
Patch3:         fix-java7-compile.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  geronimo-jms-1_1-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javamail
BuildRequires:  javapackages-local
BuildRequires:  jdbc-stdext
BuildRequires:  log4j
BuildRequires:  unzip
Requires:       mvn(javax.jms:jms)
Requires:       mvn(javax.mail:mail)
Requires:       mvn(javax.servlet:servlet-api)
BuildArch:      noarch

%description
LogKit is a logging toolkit designed for secure performance oriented
logging in applications. To get started using LogKit, it is recomended
that you read the whitepaper and browse the API docs.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0
cp %{SOURCE1} pom.xml
%patch1
%patch2 -p1
%patch3

# remove all binary libs
find . -name "*.jar" -delete

%build
ant clean
mkdir -p target/lib
build-jar-repository -s -p target/lib \
                   log4j \
                   javamail/mailapi \
                   geronimo-jms-1.1-api \
                   glassfish-servlet-api

ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dencoding=ISO-8859-1 -Dnoget=true -lib %{_datadir}/java \
    jar javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

#pom
install -d -m 755 %{buildroot}/%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{short_name}:%{short_name},org.apache.avalon.logkit:%{name}"

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/*
%{_datadir}/maven-metadata/%{name}.xml
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/*

%changelog
