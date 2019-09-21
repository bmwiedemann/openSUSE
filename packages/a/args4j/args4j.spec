#
# spec file for package args4j
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           args4j
Version:        2.0.9
Release:        0
Summary:        Java commandline parser
License:        MIT
Group:          Development/Libraries/Java
Url:            http://args4j.kohsuke.org/
Source0:        %{name}-%{version}.tar.bz2
Source1:        http://central.maven.org/maven2/args4j/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  ant >= 1.7.0
BuildRequires:  ant-apache-regexp
BuildRequires:  ant-contrib
BuildRequires:  ant-junit
BuildRequires:  ant-nodeps
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Requires:       java >= 1.8
BuildArch:      noarch

%description
args4j is a small Java class library that makes it easy
to parse command line options/arguments in your CUI application.
- It makes the command line parsing very easy by using annotations
- You can generate the usage screen very easily
- You can generate HTML/XML that lists all options for your documentation
- Fully supports localization
- It is designed to parse javac like options (as opposed to GNU-style
  where ls -lR is considered to have two options l and R)

%package        javadoc
Summary:        Javadoc for Java commandline parser
Group:          Development/Libraries/Java

%description    javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} pom.xml
%pom_remove_parent
%pom_xpath_inject pom:project "
  <groupId>args4j</groupId>
  <version>%{version}</version>"

%build
mkdir -p build/generated-sources
ant -Djavac.source=8 -Djavac.target=8 -Dsource.encoding="ISO-8859-1"

%install
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 dist/%{name}.jar  %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -sf %{_javadir}/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}-%{version}.pom
%add_maven_depmap %{name}-%{version}.pom %{name}-%{version}.jar

# Java doc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/javadoc %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files javadoc
%{_javadocdir}/%{name}

%changelog
