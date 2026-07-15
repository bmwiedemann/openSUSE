#
# spec file for package logback
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.5.38
Release:        0
Summary:        A Java logging library
License:        EPL-1.0 OR LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            https://logback.qos.ch/
Source0:        %{name}-%{version}.tar.xz
Patch0:         filtering.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 11
BuildRequires:  maven-local
BuildRequires:  mvn(ch.qos.reload4j:reload4j)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-ext)
BuildRequires:  mvn(org.tukaani:xz)
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
Group:          Documentation/HTML

%description javadoc
API documentation for the Logback library

%package access
Summary:        Logback-access module for Servlet integration
Group:          Development/Libraries/Java

%description access
The logback-access module integrates with Servlet containers, such as Tomcat
and Jetty, to provide HTTP-access log functionality. Note that you could
easily build your own module on top of logback-core.

%package examples
Summary:        Logback Examples Module
Group:          Development/Libraries/Java

%description examples
logback-examples module.

%prep
%autosetup -p1

chmod -x README.md LICENSE.txt
find . -type f -exec chmod -x {} \;
chmod +x %{name}-examples/src/main/resources/setClasspath.sh

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :central-publishing-maven-plugin
# needed for tests only
%pom_remove_plugin -r :maven-antrun-plugin

rm -r %{name}-*/src/test/java/*
# remove test deps
# ch.qos.logback:logback-core:test-jar
%pom_xpath_remove -r "pom:dependency[pom:type = 'test-jar']"
%pom_xpath_remove -r "pom:dependency[pom:scope = 'test']"

%pom_disable_module %{name}-classic-blackbox
%pom_disable_module %{name}-core-blackbox

# bundle-test-jar
%pom_xpath_remove -r "pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:executions"

%pom_xpath_remove "pom:project/pom:profiles/pom:profile[pom:id = 'javadocjar']"

%pom_xpath_remove "pom:build/pom:extensions"
%pom_xpath_remove "pom:profiles"

%{mvn_package} ":%{name}-access" access
%{mvn_package} ":%{name}-examples" examples

%build

%{mvn_build} -fj -- javadoc:aggregate

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
