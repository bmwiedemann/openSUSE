#
# spec file for package log4j
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
%bcond_without extra_modules
Name:           log4j
Version:        2.17.2
Release:        0
Summary:        Java logging package
License:        Apache-2.0
URL:            http://logging.apache.org/%{name}
Source0:        http://archive.apache.org/dist/logging/%{name}/%{version}/apache-%{name}-%{version}-src.tar.gz
Source1:        http://archive.apache.org/dist/logging/%{name}/%{version}/apache-%{name}-%{version}-src.tar.gz.asc
Source2:        https://www.apache.org/dist/logging/KEYS#/%{name}.keyring
Patch0:         log4j-java8compat.patch
Patch1:         logging-log4j-Remove-unsupported-EventDataConverter.patch
Patch2:         log4j-jackson-databind.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.lmax:disruptor)
BuildRequires:  mvn(com.sun.mail:javax.mail)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(javax.activation:javax.activation-api)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.logging:logging-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-ext)
Requires:       java-headless >= 1.8
Obsoletes:      log4j-mini
BuildArch:      noarch
%if %{with extra_modules}
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.commons:commons-csv)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires:  mvn(org.lightcouch:lightcouch)
BuildRequires:  mvn(org.zeromq:jeromq)
%endif

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package slf4j
Summary:        Binding between LOG4J 2 API and SLF4J
Requires:       java-headless >= 1.8

%description slf4j
Binding between LOG4J 2 API and SLF4J.

%package jcl
Summary:        Apache Log4j Commons Logging Bridge
Requires:       java-headless >= 1.8

%description jcl
Apache Log4j Commons Logging Bridge.

%if %{with extra_modules}
%package taglib
Summary:        Apache Log4j Tag Library
Requires:       java-headless >= 1.8

%description taglib
Apache Log4j Tag Library for Web Applications.

%package jmx-gui
Summary:        Apache Log4j JMX GUI
Requires:       java-devel
Requires:       java-headless >= 1.8

%description jmx-gui
Swing-based client for remotely editing the log4j configuration and remotely
monitoring StatusLogger output. Includes a JConsole plug-in.

%package web
Summary:        Apache Log4j Web
Requires:       java-headless >= 1.8

%description web
Support for Log4j in a web servlet container.

%package bom
Summary:        Apache Log4j BOM

%description bom
Apache Log4j 2 Bill of Material

%package nosql
Summary:        Apache Log4j NoSql
Requires:       java-headless >= 1.8

%description nosql
Use NoSQL databases such as MongoDB and CouchDB to append log messages.
%endif

%package        javadoc
Summary:        API documentation for %{name}
Obsoletes:      %{name}-manual < %{version}

%description    javadoc
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}-src
%autopatch -p1

%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-remote-resources-plugin
%pom_remove_plugin -r :maven-doap-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-toolchains-plugin
%pom_remove_plugin -r :revapi-maven-plugin

# remove all the stuff we'll build ourselves
find -name "*.jar" -o -name "*.class" -delete
rm -rf docs/api

%pom_disable_module %{name}-distribution
%pom_disable_module %{name}-samples

# Apache Flume is not in openSUSE yet
%pom_disable_module %{name}-flume-ng

# artifact for upstream testing of log4j itself, shouldn't be distributed
%pom_disable_module %{name}-perf

# unavailable com.conversantmedia:disruptor
rm log4j-core/src/main/java/org/apache/logging/log4j/core/async/DisruptorBlockingQueueFactory.java
%pom_remove_dep -r com.conversantmedia:disruptor

# kafka not available
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/mom/kafka
%pom_remove_dep -r :kafka-clients

# liquibase not available
%pom_disable_module %{name}-liquibase

# we don't have slf4j 1.8 yet
%pom_disable_module %{name}-slf4j18-impl

# we don't have commons-dbcp2
%pom_disable_module %{name}-jdbc-dbcp2

# We do not have mongodb
%pom_disable_module %{name}-mongodb3
%pom_disable_module %{name}-mongodb4

# System scoped dep provided by JDK
%pom_remove_dep :jconsole %{name}-jmx-gui

# old AID is provided by felix, we want osgi-core
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core

# BOM package shouldn't require Apache RAT
%pom_remove_plugin :apache-rat-plugin %{name}-bom

# tests are disabled
%pom_remove_plugin -r :maven-failsafe-plugin

%pom_disable_module %{name}-core-its
%pom_disable_module %{name}-jpa
%pom_disable_module %{name}-cassandra
%pom_disable_module %{name}-appserver
%pom_disable_module %{name}-spring-boot
%pom_disable_module %{name}-spring-cloud-config
%pom_disable_module %{name}-kubernetes
%if %{without extra_modules}
%pom_disable_module %{name}-bom
%pom_disable_module %{name}-taglib
%pom_disable_module %{name}-jmx-gui
%pom_disable_module %{name}-web
%pom_disable_module %{name}-couchdb
%endif

%pom_remove_dep -r :javax.persistence
%if %{without extra_modules}
%pom_remove_dep -r :jackson-dataformat-yaml
%pom_remove_dep -r :jackson-dataformat-xml
%pom_remove_dep -r :woodstox-core
%pom_remove_dep -r :jboss-jms-api_1.1_spec
%pom_remove_dep -r :jeromq
%pom_remove_dep -r :commons-csv
%else
%pom_change_dep -r :jboss-jms-api_1.1_spec org.apache.geronimo.specs:geronimo-jms_1.1_spec
%endif

%pom_add_dep javax.activation:javax.activation-api %{name}-core

%if %{without extra_modules}
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/{jackson,config/yaml,parser}
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/{db,mom,nosql}
rm log4j-core/src/main/java/org/apache/logging/log4j/core/layout/*{Csv,Jackson,Xml,Yaml,Json,Gelf}*.java
rm log4j-1.2-api/src/main/java/org/apache/log4j/builders/layout/*Xml*.java
rm -r log4j-1.2-api/src/main/java/org/apache/log4j/or/jms
%endif

%{mvn_package} ':%{name}-slf4j-impl' slf4j
%{mvn_package} ':%{name}-to-slf4j' slf4j
%{mvn_package} ':%{name}-taglib' taglib
%{mvn_package} ':%{name}-jcl' jcl
%{mvn_package} ':%{name}-jmx-gui' jmx-gui
%{mvn_package} ':%{name}-web' web
%{mvn_package} ':%{name}-bom' bom
%{mvn_package} ':%{name}-cassandra' nosql
%{mvn_package} ':%{name}-couchdb' nosql

%{mvn_package} :log4j-core-its __noinstall
%{mvn_package} ::zip: __noinstall

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%if %{with extra_modules}
%jpackage_script org.apache.logging.log4j.jmx.gui.ClientGUI '' '' %{name}/%{name}-jmx-gui:%{name}/%{name}-core %{name}-jmx false
%endif

%files -f .mfiles
%dir %{_javadir}/%{name}
%license LICENSE.txt
%doc NOTICE.txt

%files slf4j -f .mfiles-slf4j

%files jcl -f .mfiles-jcl

%if %{with extra_modules}
%files taglib -f .mfiles-taglib

%files web -f .mfiles-web

%files bom -f .mfiles-bom

%files nosql -f .mfiles-nosql

%files jmx-gui -f .mfiles-jmx-gui
%{_bindir}/%{name}-jmx
%endif

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt
%doc NOTICE.txt

%changelog
