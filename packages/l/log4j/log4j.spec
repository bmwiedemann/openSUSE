#
# spec file for package log4j
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


%bcond_with extras
Name:           log4j
Version:        2.11.1
Release:        0
Summary:        Java logging package
License:        Apache-2.0
URL:            http://logging.apache.org/%{name}
Source0:        http://archive.apache.org/dist/logging/%{name}/%{version}/apache-%{name}-%{version}-src.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.lmax:disruptor)
BuildRequires:  mvn(com.sun.mail:javax.mail)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.logging:logging-parent:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-ext)
BuildArch:      noarch
%if %{with extras}
BuildRequires:  mvn(com.datastax.cassandra:cassandra-driver-core)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.commons:commons-csv)
BuildRequires:  mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.eclipse.persistence:javax.persistence)
BuildRequires:  mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
BuildRequires:  mvn(org.lightcouch:lightcouch)
BuildRequires:  mvn(org.zeromq:jeromq)
BuildRequires:  mvn(sun.jdk:jconsole)
# Explicit requires for javapackages-tools since log4j-jmx script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
%endif

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package slf4j
Summary:        Binding between LOG4J 2 API and SLF4J

%description slf4j
Binding between LOG4J 2 API and SLF4J.

%package jcl
Summary:        Apache Log4j Commons Logging Bridge

%description jcl
Apache Log4j Commons Logging Bridge.

%if %{with extras}
%package osgi
Summary:        Apache Log4J Core OSGi Bundles

%description osgi
Apache Log4J Core OSGi Bundles.

%package taglib
Summary:        Apache Log4j Tag Library

%description taglib
Apache Log4j Tag Library for Web Applications.

%package jmx-gui
Summary:        Apache Log4j JMX GUI
Requires:       java-devel

%description jmx-gui
Swing-based client for remotely editing the log4j configuration and remotely
monitoring StatusLogger output. Includes a JConsole plug-in.

%package web
Summary:        Apache Log4j Web

%description web
Support for Log4j in a web servlet container.

%package bom
Summary:        Apache Log4j BOM

%description bom
Apache Log4j 2 Bill of Material

%package nosql
Summary:        Apache Log4j NoSql

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

%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-remote-resources-plugin
%pom_remove_plugin -r :maven-doap-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-toolchains-plugin

# remove all the stuff we'll build ourselves
find -name "*.jar" -o -name "*.class" -delete
rm -rf docs/api

%pom_disable_module %{name}-samples
%pom_disable_module %{name}-distribution

# Apache Flume is not in Fedora yet
%pom_disable_module %{name}-flume-ng

# artifact for upstream testing of log4j itself, shouldn't be distributed
%pom_disable_module %{name}-perf

# needs java 9 to build
%pom_disable_module %{name}-api-java9
%pom_disable_module %{name}-core-java9
%pom_remove_dep -r :%{name}-api-java9
%pom_remove_dep -r :%{name}-core-java9
%pom_remove_plugin -r :maven-dependency-plugin

# unavailable com.conversantmedia:disruptor
rm log4j-core/src/main/java/org/apache/logging/log4j/core/async/DisruptorBlockingQueueFactory.java
%pom_remove_dep -r com.conversantmedia:disruptor

# kafka not available
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/mom/kafka
%pom_remove_dep -r :kafka-clients

# not compatible with fedora's version
%pom_disable_module %{name}-liquibase

# we don't have slf4j 1.8 yet
%pom_disable_module %{name}-slf4j18-impl

# we don't have commons-dbcp2
%pom_disable_module %{name}-jdbc-dbcp2

# We have mongodb 4
%pom_disable_module %{name}-mongodb2
%pom_disable_module %{name}-mongodb3

# System scoped dep provided by JDK
%pom_remove_dep :jconsole %{name}-jmx-gui
%pom_add_dep sun.jdk:jconsole %{name}-jmx-gui

# old AID is provided by felix, we want osgi-core
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core

# BOM package shouldn't require Apache RAT
%pom_remove_plugin :apache-rat-plugin %{name}-bom

# tests are disabled
%pom_remove_plugin :maven-failsafe-plugin

%if %{without extras}
%pom_disable_module %{name}-taglib
%pom_disable_module %{name}-jmx-gui
%pom_disable_module %{name}-bom
%pom_disable_module %{name}-web
%pom_disable_module %{name}-iostreams
%pom_disable_module %{name}-jul
%pom_disable_module %{name}-core-its
%pom_disable_module %{name}-jpa
%pom_disable_module %{name}-couchdb
%pom_disable_module %{name}-cassandra
%pom_disable_module %{name}-appserver

%pom_remove_dep -r :jackson-dataformat-yaml
%pom_remove_dep -r :jackson-dataformat-xml
%pom_remove_dep -r :woodstox-core
%pom_remove_dep -r :javax.persistence
%pom_remove_dep -r :jboss-jms-api_1.1_spec
%pom_remove_dep -r :jeromq
%pom_remove_dep -r :commons-csv

rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/{jackson,config/yaml,parser}
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/{db,mom,nosql}
rm log4j-core/src/main/java/org/apache/logging/log4j/core/layout/*{Csv,Jackson,Xml,Yaml,Json,Gelf}*.java
rm log4j-api/src/main/java/org/apache/logging/log4j/util/Activator.java
%endif

%{mvn_alias} :%{name}-1.2-api %{name}:%{name}

# Note that packages using the compatibility layer still need to have log4j-core
# on the classpath to run. This is there to prevent build-classpath from putting
# whole dir on the classpath which results in loading incorrect provider
%{mvn_file} ':{%{name}-1.2-api}' %{name}/@1 %{name}

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

%build
# missing test deps (mockejb)
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%if %{with extras}
%jpackage_script org.apache.logging.log4j.jmx.gui.ClientGUI '' '' %{name}/%{name}-jmx-gui:%{name}/%{name}-core %{name}-jmx false
%endif

%files -f .mfiles
%dir %{_javadir}/%{name}
%license LICENSE.txt
%doc NOTICE.txt

%files slf4j -f .mfiles-slf4j

%files jcl -f .mfiles-jcl

%if %{with extras}
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
