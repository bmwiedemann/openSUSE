#
# spec file for package regexp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2008, JPackage Project
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


%define full_name       jakarta-%{name}
%define section         free
Name:           regexp
Version:        1.5
Release:        0
Summary:        Simple regular expressions API
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://jakarta.apache.org/%{name}/
Source0:        http://www.apache.org/dist/jakarta/regexp/jakarta-regexp-%{version}.tar.gz
Source1:        regexp-%{version}.pom
BuildRequires:  ant
BuildRequires:  ant >= 1.6
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  xml-commons-apis-bootstrap
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#!BuildIgnore:  xml-commons-apis xml-commons-resolver xml-commons xerces-j2
#!BuildIgnore:  xml-commons-jaxp-1.3-apis
BuildArch:      noarch

%description
Regexp is a 100% Pure Java Regular Expression package that was
graciously donated to the Apache Software Foundation by Jonathan Locke.
He originally wrote this software back in 1996 and it has stood up
quite well to the test of time. It includes complete Javadoc
documentation as well as a simple Applet for visual debugging and
testing suite for compatibility.

%prep
%setup -q -n %{full_name}-%{version}
# remove all binary libs
find . -type f -name "*.jar" | xargs -t rm

%build
export OPT_JAR_LIST=:
export CLASSPATH=
mkdir lib
ant -Djakarta-site2.dir=. -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6  jar

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/*.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
[ -d docs/api ] && rm -rf docs/api
# pom
mkdir -p %{buildroot}%{_mavenpomdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a %{full_name}:%{full_name}

%files
%defattr(0644,root,root,0755)
%doc LICENSE
%{_javadir}/*.jar
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml*

%changelog
