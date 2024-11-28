#
# spec file for package prometheus-simpleclient-java
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


%global version_id parent
%global upstream_name client_java
Name:           prometheus-simpleclient-java
Version:        0.16.0
Release:        0
Summary:        Prometheus Java Suite
License:        Apache-2.0 AND CC0-1.0
URL:            https://github.com/prometheus/client_java/
Source0:        https://github.com/prometheus/client_java/archive/%{version_id}-%{version}.tar.gz
Patch1:         remove_opentelemetry_tracer.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(com.github.ben-manes.caffeine:caffeine) >= 2.7.0
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildArch:      noarch

%description
The Prometheus Java Suite: Client Metrics, Exposition, and Examples.

%package parent
Summary:        Prometheus Java Suite parent pom

%description parent
The Prometheus Java Suite: Client Metrics, Exposition, and Examples.

%package bom
Summary:        Prometheus Java Simpleclient BOM

%description bom
Bill of Materials for the Simpleclient.

%package caffeine
Summary:        Prometheus Java Simpleclient Caffeine

%description caffeine
Metrics collector for caffeine based caches.

%package common
Summary:        Prometheus Java Simpleclient Common

%description common
Common code used by various modules of the Simpleclient.

%package graphite_bridge
Summary:        Prometheus Java Simpleclient Graphite Bridge

%description graphite_bridge
Graphite bridge for the Prometheus Java Simpleclient.

%package guava
Summary:        Prometheus Java Simpleclient guava

%description guava
Metrics collector for guava based caches.

%package hotspot
Summary:        Prometheus Java Simpleclient Hotspot

%description hotspot
Collectors of data from Java Hotspot.

%package httpserver
Summary:        Prometheus Java Simpleclient Httpserver

%description httpserver
Httpserver exposition for the simpleclient.

%package jetty
Summary:        Prometheus Java Simpleclient Jetty

%description jetty
Collector of data from Jetty StatisticsHandler.

%package jetty_jdk8
Summary:        Prometheus Java Simpleclient Jetty JDK 8

%description jetty_jdk8
Collector of data from Jetty Statistics for Jetty versions which require JDK 8.

%package log4j
Summary:        Prometheus Java Simpleclient log4j

%description log4j
Metrics collector for log4j appender logging.

%package log4j2
Summary:        Prometheus Java Simpleclient log4j2

%description log4j2
Metrics collector for log4j2 appender logging.

%package logback
Summary:        Prometheus Java Simpleclient logback

%description logback
Metrics collector for logback appender logging.

%package pushgateway
Summary:        Prometheus Java Simpleclient Pushgateway

%description pushgateway
Pushgateway exporter for the simpleclient.

%package servlet
Summary:        Prometheus Java Simpleclient Servlet (javax)

%description servlet
HTTP servlet exporter for the simpleclient (Javax API).

%package servlet-common
Summary:        Prometheus Java Simpleclient Servlet

%description servlet-common
HTTP servlet exporter for the simpleclient.

%package servlet-jakarta
Summary:        Prometheus Java Simpleclient Servlet (jakarta)

%description servlet-jakarta
HTTP servlet exporter for the simpleclient (Jakarta API).

%package tracer
Summary:        Prometheus Java Span Context Supplier - Parent

%description tracer
Prometheus Java Span Context Supplier - Parent POM.

%package tracer-common
Summary:        Prometheus Java Span Context Supplier - Common

%description tracer-common
Prometheus Java Span Context Supplier - Common.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{upstream_name}-%{version_id}-%{version}

# Remove included jar files
find . -name \*.jar -print0 | xargs -0 rm

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :versions-maven-plugin

for m in simpleclient_dropwizard \
         simpleclient_hibernate \
         simpleclient_spring_web \
         simpleclient_spring_boot \
         simpleclient_vertx \
         simpleclient_vertx4 \
         integration_tests \
         benchmarks; do
%pom_disable_module $m
done
# Only build simpleclient_tracer_common as it's being used by an Examplar class
%pom_disable_module simpleclient_tracer_otel_agent simpleclient_tracer
%pom_disable_module simpleclient_tracer_otel simpleclient_tracer

# remove OpenTelemetry stuff, which we don't support
%patch -P1 -p2
%pom_remove_dep io.prometheus:simpleclient_tracer_otel simpleclient
%pom_remove_dep io.prometheus:simpleclient_tracer_otel_agent simpleclient
%pom_add_dep io.prometheus:simpleclient_tracer_common:%{version} simpleclient

# Change compiler source/target version to JDK 8 level
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8" . simpleclient_hotspot
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8" . simpleclient_hotspot

%build
%{mvn_build} -f -s

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-simpleclient
%license LICENSE
%doc NOTICE

%files parent -f .mfiles-parent

%files bom -f .mfiles-simpleclient_bom

%files caffeine -f .mfiles-simpleclient_caffeine

%files common -f .mfiles-simpleclient_common

%files graphite_bridge -f .mfiles-simpleclient_graphite_bridge

%files guava -f .mfiles-simpleclient_guava

%files hotspot -f .mfiles-simpleclient_hotspot

%files httpserver -f .mfiles-simpleclient_httpserver

%files jetty -f .mfiles-simpleclient_jetty

%files jetty_jdk8 -f .mfiles-simpleclient_jetty_jdk8

%files log4j -f .mfiles-simpleclient_log4j

%files log4j2 -f .mfiles-simpleclient_log4j2

%files logback -f .mfiles-simpleclient_logback

%files pushgateway -f .mfiles-simpleclient_pushgateway

%files servlet -f .mfiles-simpleclient_servlet

%files servlet-common -f .mfiles-simpleclient_servlet_common

%files servlet-jakarta -f .mfiles-simpleclient_servlet_jakarta

%files tracer -f .mfiles-simpleclient_tracer

%files tracer-common -f .mfiles-simpleclient_tracer_common

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
