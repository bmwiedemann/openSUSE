#
# spec file for package log4j
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
%bcond_without extra_modules
Name:           log4j
Version:        2.26.0
Release:        0
Summary:        Java logging package
License:        Apache-2.0
URL:            http://logging.apache.org/%{name}
Source0:        https://archive.apache.org/dist/logging/%{name}/%{version}/apache-%{name}-%{version}-src.zip
Source1:        https://archive.apache.org/dist/logging/%{name}/%{version}/apache-%{name}-%{version}-src.zip.asc
Source2:        https://www.apache.org/dist/logging/KEYS#/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bnd.annotation)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.lmax:disruptor)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.jms:jakarta.jms-api)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.jspecify:jspecify)
BuildRequires:  mvn(org.osgi:osgi.annotation)
Requires:       java-headless >= 1.8
Obsoletes:      log4j-mini
BuildArch:      noarch
%if %{with extra_modules}
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(javax.servlet.jsp:javax.servlet.jsp-api)
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

%package bom
Summary:        Apache Log4j BOM

%description bom
Apache Log4j 2 Bill of Material

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
monitoring StatusLogger output.

%package web
Summary:        Apache Log4j Web
Requires:       java-headless >= 1.8

%description web
Support for Log4j in a web servlet container.

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
%setup -q -c -n apache-%{name}-%{version}-src

find . -name .log4j-plugin-processing-activator -print -delete
find . -name package-info.java -print -delete

%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin -r org.ops4j.pax.exam:exam-maven-plugin
%pom_remove_plugin -r org.gradlex:gradle-module-metadata-maven-plugin
%pom_remove_plugin -r org.apache.maven.plugins:maven-clean-plugin
%pom_remove_plugin -r org.apache.logging.log4j:log4j-docgen-maven-plugin

# remove all the stuff we'll build ourselves
find -name "*.jar" -o -name "*.class" -delete
rm -rf docs/api

# artifact for upstream testing of log4j itself, shouldn't be distributed
%pom_disable_module %{name}-perf-test

%pom_remove_dep -r org.apache.groovy:groovy-bom
%pom_remove_dep -r com.fasterxml.jackson:jackson-bom
%pom_remove_dep -r jakarta.platform:jakarta.jakartaee-bom
%pom_remove_dep -r org.junit:junit-bom
%pom_remove_dep -r org.springframework:spring-framework-bom
%pom_remove_dep -r org.mockito:mockito-bom

# unavailable com.conversantmedia:disruptor
rm log4j-core/src/main/java/org/apache/logging/log4j/core/async/DisruptorBlockingQueueFactory.java
%pom_remove_dep -r com.conversantmedia:disruptor

# kafka not available
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/mom/kafka
%pom_remove_dep -r :kafka-clients

# we don't have commons-dbcp2
%pom_disable_module %{name}-jdbc-dbcp2

# We do not have mongodb
%pom_disable_module %{name}-mongodb
%pom_disable_module %{name}-mongodb4

# old AID is provided by felix, we want osgi-core
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core
%pom_change_dep -r org.osgi:org.osgi.annotation.bundle org.osgi:osgi.annotation
%pom_remove_dep -r org.osgi:org.osgi.annotation.versioning

%pom_remove_plugin :maven-resources-plugin

# tests are disabled
%pom_remove_plugin -r :maven-failsafe-plugin
%pom_remove_plugin -r :maven-surefire-plugin

%pom_remove_parent

%pom_disable_module %{name}-api-test
%pom_disable_module %{name}-core-test
%pom_disable_module %{name}-core-fuzz-test
%pom_disable_module %{name}-fuzz-test
%pom_disable_module %{name}-layout-template-json-test
%pom_disable_module %{name}-layout-template-json-fuzz-test
%pom_disable_module %{name}-slf4j2-impl-fuzz-test

%pom_disable_module %{name}-core-its
%pom_disable_module %{name}-jpa
%pom_disable_module %{name}-cassandra
%pom_disable_module %{name}-appserver
%pom_disable_module %{name}-spring-boot
%pom_disable_module %{name}-spring-cloud-config-client
%if %{without extra_modules}
%pom_disable_module %{name}-taglib
%pom_disable_module %{name}-web
%pom_disable_module %{name}-couchdb

%pom_remove_dep -r :jackson-dataformat-yaml
%pom_remove_dep -r javax.jms:javax.jms-api
%pom_remove_dep -r :jeromq
%pom_remove_dep -r :commons-csv
%else
%pom_change_dep -r javax.jms:javax.jms-api org.apache.geronimo.specs:geronimo-jms_1.1_spec
%endif

%if %{without extra_modules}
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/{jackson,config/yaml,parser}
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/{db,mom,nosql}
rm log4j-core/src/main/java/org/apache/logging/log4j/core/layout/*{Csv,Jackson,Xml,Yaml,Json,Gelf}*.java
rm log4j-1.2-api/src/main/java/org/apache/log4j/builders/layout/*Xml*.java
rm -r log4j-1.2-api/src/main/java/org/apache/log4j/or/jms
%endif

%pom_remove_dep com.sun.mail:javax.mail log4j-core
%pom_remove_dep javax.mail:javax.mail-api log4j-core
%pom_remove_dep javax.activation:javax.activation-api log4j-core
rm log4j-core/src/main/java/org/apache/logging/log4j/core/net/MimeMessageBuilder.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/net/SmtpManager.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/appender/SmtpAppender.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/filter/MutableThreadContextMapFilter.java

%pom_remove_dep org.eclipse.angus:angus-activation log4j-jakarta-smtp
%pom_remove_dep org.eclipse.angus:jakarta.mail log4j-jakarta-smtp

%if %{?pkg_vcmp:%pkg_vcmp slf4j >= 2}%{!?pkg_vcmp:0}
%pom_disable_module %{name}-slf4j-impl
%{mvn_alias} :%{name}-slf4j2-impl :%{name}-slf4j-impl
%else
%pom_disable_module %{name}-slf4j2-impl
%{mvn_alias} :%{name}-slf4j-impl :%{name}-slf4j2-impl
%endif

%{mvn_package} ':%{name}-slf4j-impl' slf4j
%{mvn_package} ':%{name}-slf4j2-impl' slf4j
%{mvn_package} ':%{name}-to-slf4j' slf4j
%{mvn_package} ':%{name}-taglib' taglib
%{mvn_package} ':%{name}-jcl' jcl
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

%files -f .mfiles
%dir %{_javadir}/%{name}
%license LICENSE.txt
%doc NOTICE.txt

%files slf4j -f .mfiles-slf4j

%files jcl -f .mfiles-jcl

%files bom -f .mfiles-bom

%if %{with extra_modules}
%files taglib -f .mfiles-taglib

%files web -f .mfiles-web

%files nosql -f .mfiles-nosql
%endif

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt
%doc NOTICE.txt

%changelog
