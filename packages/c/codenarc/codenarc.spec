#
# spec file for package codenarc
#
# Copyright (c) 2019 SUSE LLC.
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


%global oname CodeNarc
Name:           codenarc
Version:        1.4
Release:        0
Summary:        Groovy library that provides static analysis features for Groovy code
License:        Apache-2.0
URL:            http://codenarc.sourceforge.net/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires:  mvn(org.codehaus.groovy:groovy)
BuildRequires:  mvn(org.codehaus.groovy:groovy-ant)
BuildRequires:  mvn(org.codehaus.groovy:groovy-xml)
BuildRequires:  mvn(org.gmetrics:GMetrics)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
CodeNarc is a static analysis tool for Groovy source code,
enabling monitoring and enforcement of many coding standards
and best practices. CodeNarc applies a set of Rules
(predefined and/or custom) that are applied to each Groovy
file, and generates an HTML report of the results, including
a list of rules violated for each source file, and a count
of the number of violations per package and for the whole
project.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

cp -p site-pom.xml pom.xml

dos2unix README.md

mkdir -p src/main/java/org/codenarc/analyzer
cp -p src/main/groovy/org/codenarc/analyzer/SuppressionAnalyzer.java \
 src/main/java/org/codenarc/analyzer/

# Set encoding
%pom_xpath_inject pom:project/pom:properties '
  <antVersion>1.9.6</antVersion>
  <gmetricsVersion>0.7</gmetricsVersion>
  <junitVersion>4.12</junitVersion>
  <slf4jVersion>1.7.25</slf4jVersion>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>'

%pom_xpath_set pom:properties/pom:targetJdk 1.6
%pom_xpath_set pom:properties/pom:groovyVersion 2.4.5

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.5.1 . "
<configuration>
    <source>\${targetJdk}</source>
    <target>\${targetJdk}</target>
</configuration>"

%pom_add_plugin org.codehaus.gmavenplus:gmavenplus-plugin:1.5 . "
 <executions>
  <execution>
   <goals>
    <goal>generateStubs</goal>
    <!--goal>testCompile</goal-->
    <goal>testGenerateStubs</goal>
   </goals>
  </execution>
 </executions>"

%pom_add_dep org.apache.ant:ant:'${antVersion}' . "<optional>true</optional>"
%pom_add_dep org.codehaus.groovy:groovy:'${groovyVersion}'
%pom_add_dep org.codehaus.groovy:groovy-ant:'${groovyVersion}'
%pom_add_dep org.codehaus.groovy:groovy-xml:'${groovyVersion}'
%pom_add_dep org.gmetrics:GMetrics:'${gmetricsVersion}'
%pom_add_dep junit:junit:'${junitVersion}'
%pom_add_dep org.slf4j:slf4j-api:'${slf4jVersion}'

%{mvn_file} org.%{name}:%{oname} %{name} %{oname}

%build

%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGELOG.md README.md
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
