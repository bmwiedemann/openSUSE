#
# spec file for package logback
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


Name:           logback
Version:        1.2.3
Release:        0
Summary:        A Java logging library
License:        LGPL-2.1-or-later OR EPL-1.0
URL:            https://logback.qos.ch/
Source0:        %{name}-%{version}.tar.xz
# Remove deprecated methods
Patch0:         %{name}-1.1.11-jetty.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  maven-local
BuildRequires:  mvn(javax.mail:mail)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:  mvn(org.apache.tomcat:tomcat-coyote)
BuildRequires:  mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.codehaus.janino:janino)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-ext)
BuildConflicts: java-devel >= 9
#!BuildRequires: groovy-lib
BuildArch:      noarch

%description
Logback is intended as a successor to the popular log4j project. At present
time, logback is divided into three modules, logback-core, logback-classic
and logback-access.

The logback-core module lays the groundwork for the other two modules. The
logback-classic module can be assimilated to a significantly improved
version of log4j. Moreover, logback-classic natively implements the SLF4J
API so that you can readily switch back and forth between logback and other
logging frameworks such as log4j or java.util.logging (JUL).

The logback-access module integrates with Servlet containers, such as
Tomcat and Jetty, to provide HTTP-access log functionality. Note that you
could easily build your own module on top of logback-core.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for the Logback library

%package access
Summary:        Logback-access module for Servlet integration

%description access
The logback-access module integrates with Servlet containers, such as Tomcat
and Jetty, to provide HTTP-access log functionality. Note that you could
easily build your own module on top of logback-core.

%package examples
Summary:        Logback Examples Module

%description examples
logback-examples module.

%prep
%setup -q
chmod -x README.md LICENSE.txt
find . -type f -exec chmod -x {} \;
chmod +x %{name}-examples/src/main/resources/setClasspath.sh

%patch0 -p1

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :cobertura-maven-plugin

rm -r %{name}-*/src/test/java/*
# remove test deps
# ch.qos.logback:logback-core:test-jar
%pom_xpath_remove -r "pom:dependency[pom:type = 'test-jar']"
%pom_xpath_remove -r "pom:dependency[pom:scope = 'test']"

# bundle-test-jar
%pom_xpath_remove -r "pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:executions"

# com.oracle:ojdbc14:10.2.0.1 com.microsoft.sqlserver:sqljdbc4:2.0
%pom_xpath_remove "pom:project/pom:profiles/pom:profile[pom:id = 'host-orion']" %{name}-access
%pom_xpath_remove "pom:project/pom:profiles" %{name}-classic

%pom_xpath_remove "pom:project/pom:profiles/pom:profile[pom:id = 'javadocjar']"

# disable for now
%pom_disable_module logback-site

%pom_xpath_remove "pom:build/pom:extensions"

%{mvn_package} ":%{name}-access" access
%{mvn_package} ":%{name}-examples" examples

%build

# unavailable test dep maven-scala-plugin
# slf4jJAR and org.apache.felix.main are required by logback-examples modules for maven-antrun-plugin
%{mvn_build} -f -- \
  -Dorg.slf4j:slf4j-api:jar=$(build-classpath slf4j/api) \
  -Dorg.apache.felix:org.apache.felix.main:jar=$(build-classpath felix/org.apache.felix.main)

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

install -d -m 755 %{buildroot}%{_datadir}/%{name}/examples
cp -r %{name}-examples/src %{buildroot}%{_datadir}/%{name}/examples
ln -sf %{_mavenpomdir}/%{name}/%{name}-examples.pom %{buildroot}%{_datadir}/%{name}/examples/pom.xml
%fdupes -s %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%files access -f .mfiles-access
%license LICENSE.txt

%files examples -f .mfiles-examples
%license LICENSE.txt
%{_datadir}/%{name}

%changelog
