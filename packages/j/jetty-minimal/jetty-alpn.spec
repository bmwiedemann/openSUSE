#
# spec file for package jetty-alpn
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2000-2007, JPackage Project
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


%global base_name jetty
%global addver  .v20241219
%define src_name %{base_name}.project-%{base_name}-%{version}%{addver}
Name:           %{base_name}-alpn
Version:        9.4.57
Release:        0
Summary:        The alpn modules for Jetty
License:        Apache-2.0 OR EPL-1.0
URL:            https://www.eclipse.org/jetty/
Source0:        https://github.com/eclipse/%{base_name}.project/archive/%{base_name}-%{version}%{addver}.tar.gz#/%{src_name}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.conscrypt:conscrypt-openjdk-uber)
BuildRequires:  mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires:  mvn(org.eclipse.jetty:jetty-io) >= %{version}
BuildRequires:  mvn(org.eclipse.jetty:jetty-server) >= %{version}
BuildArch:      noarch
# missing gcc13 to build conscrypt's dependencies
%if 0%{?sle_version} && 0%{?sle_version} < 150400
ExclusiveArch:  do-not-build
%endif

%description

%global desc \
Jetty is a 100% Java HTTP Server and Servlet Container. This means that you\
do not need to configure and run a separate web server (like Apache) in order\
to use Java, servlets and JSPs to generate dynamic content. Jetty is a fully\
featured web server for static and dynamic content. Unlike separate\
server/container solutions, this means that your web server and web\
application run in the same process, without interconnection overheads\
and complications. Furthermore, as a pure java component, Jetty can be simply\
included in your application for demonstration, distribution or deployment.\
Jetty is available on all Java supported platforms.
%global extdesc %{desc}\
\
This package contains
%{extdesc} %{summary}

%package client
Summary:        The alpn modules for Jetty (client components)

%description client
%{extdesc} %{summary}

%package server
Summary:        The alpn modules for Jetty (server components)

%description server
%{extdesc} %{summary}

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
%{summary}.

%prep
%setup -q -n %{src_name}

find . -name "*.?ar" -exec rm {} \;
find . -name "*.class" -exec rm {} \;

%pom_remove_dep :::import

# Plugins irrelevant or harmful to building the package
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :license-maven-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :h2spec-maven-plugin

# Unnecessary pom flattening can be skipped
%pom_remove_plugin -r :flatten-maven-plugin jetty-bom

%pom_disable_module aggregates/jetty-all

%pom_xpath_inject "pom:configuration/pom:instructions" \
"<Import-Package>sun.misc;resolution:=optional,com.sun.nio.file;resolution:=optional,*</Import-Package>"

%pom_remove_dep "com.sun.net.httpserver:http" jetty-http-spi

%pom_change_dep -r org.mortbay.jasper:apache-jsp org.apache.tomcat:tomcat-jasper

%pom_add_dep 'org.junit.jupiter:junit-jupiter-engine:${junit.version}' tests/test-sessions/test-sessions-common

# provided by glassfish-jsp-api that has newer version
%pom_change_dep -r javax.servlet.jsp:jsp-api javax.servlet.jsp:javax.servlet.jsp-api

# txt artifact - not installable
%pom_remove_plugin ":jetty-version-maven-plugin"
%pom_xpath_remove "pom:artifactItem[pom:classifier='version']" jetty-home

# Disable building source release
%pom_xpath_remove 'pom:execution[pom:id="sources"]' jetty-home

# Unwanted JS in javadoc
sed -i '/^\s*\*.*<script>/d' jetty-util/src/main/java/org/eclipse/jetty/util/resource/Resource.java

# only used for integration tests
%pom_remove_plugin :maven-invoker-plugin jetty-jspc-maven-plugin

# These bundles have a dep on Eclipse that is not available on every arch
%pom_disable_module jetty-osgi

# We don't have asciidoctor-maven-plugin
%pom_disable_module jetty-documentation
%pom_remove_dep -r :jetty-documentation
%pom_xpath_remove 'pom:execution[pom:id="unpack-documentation"]' jetty-distribution

%pom_xpath_remove 'pom:artifactItem[pom:artifactId="libsetuid-osx"]' jetty-home/pom.xml

# TODO remove when jetty-setuid is packaged
%pom_xpath_remove "pom:execution[pom:id='copy-setuid-deps']" jetty-home/pom.xml

# We don't have gcloud-java-datastore
%pom_disable_module jetty-gcloud
%pom_disable_module test-gcloud-sessions tests/test-sessions
%pom_remove_dep :jetty-gcloud-session-manager jetty-home

# we don't have com.googlecode.xmemcached:xmemcached yet
%pom_disable_module jetty-memcached
%pom_disable_module test-memcached-sessions tests/test-sessions
%pom_remove_dep :jetty-memcached-sessions jetty-home

# We don't have hazelcast
%pom_disable_module jetty-hazelcast
%pom_disable_module test-hazelcast-sessions tests/test-sessions
%pom_remove_dep :jetty-hazelcast jetty-home

# We don't have infinispan
%pom_disable_module jetty-infinispan
%pom_disable_module test-infinispan-sessions tests/test-sessions
%pom_remove_dep :infinispan-embedded jetty-home
%pom_remove_dep :infinispan-embedded-query jetty-home
%pom_remove_dep :infinispan-remote jetty-home
%pom_remove_dep :infinispan-remote-query jetty-home
%pom_xpath_remove "pom:execution[pom:id='unpack-infinispan-config']" jetty-home

# Not currently able to build tests, so can't build benchmarks
%pom_disable_module jetty-jmh

# Distribution tests require internet access, so disable
%pom_disable_module test-distribution tests

# the default location is not allowed by SELinux
sed -i '/<SystemProperty name="jetty.state"/d' \
    jetty-home/src/main/resources%{_sysconfdir}/jetty-started.xml

# remote-resources only copies about.html
%pom_remove_plugin :maven-remote-resources-plugin
# packages module configs, we don't need those in minimal
%pom_remove_plugin -r :maven-assembly-plugin
# only useful when tests are enabled (copies test deps)
%pom_remove_plugin :maven-dependency-plugin jetty-client

# all modules besides the current jetty-alpn
%pom_disable_module jetty-ant
%pom_disable_module jetty-http2
%pom_disable_module jetty-fcgi
%pom_disable_module jetty-servlets
%pom_disable_module apache-jstl
%pom_disable_module jetty-maven-plugin
%pom_disable_module jetty-jspc-maven-plugin
%pom_disable_module jetty-deploy
%pom_disable_module jetty-start
%pom_disable_module jetty-cdi
%pom_disable_module jetty-spring
%pom_disable_module jetty-jaspi
%pom_disable_module jetty-rewrite
%pom_disable_module jetty-nosql
%pom_disable_module jetty-unixsocket
%pom_disable_module tests
%pom_disable_module examples
%pom_disable_module jetty-quickstart
%pom_disable_module jetty-distribution
%pom_disable_module jetty-runner
%pom_disable_module jetty-http-spi
%pom_disable_module jetty-home
%pom_disable_module jetty-websocket

# minimal modules built in jetty-minimal package
%pom_disable_module jetty-annotations
%pom_disable_module jetty-client
%pom_disable_module jetty-continuation
%pom_disable_module jetty-http
%pom_disable_module jetty-io
%pom_disable_module jetty-jaas
%pom_disable_module jetty-jmx
%pom_disable_module jetty-jndi
%pom_disable_module apache-jsp
%pom_disable_module jetty-openid
%pom_disable_module jetty-plus
%pom_disable_module jetty-proxy
%pom_disable_module jetty-security
%pom_disable_module jetty-server
%pom_disable_module jetty-servlet
%pom_disable_module jetty-util
%pom_disable_module jetty-util-ajax
%pom_disable_module jetty-xml
%pom_disable_module jetty-webapp

%pom_xpath_remove "pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:additionalJOption"

%{mvn_file} :{*} %{base_name}/@1

%build

%{mvn_package} :jetty-home __noinstall
%{mvn_package} :jetty-distribution __noinstall

# Separate package for POMs
%{mvn_package} ':*-project' __noinstall
%{mvn_package} ':*-parent' __noinstall
%{mvn_package} ':*-bom' __noinstall

# artifact used by demo
%{mvn_package} :test-mock-resources

%{mvn_package} ':test-*' __noinstall
%{mvn_package} ':*-tests' __noinstall
%{mvn_package} ':*-it' __noinstall
%{mvn_package} ':example-*' __noinstall
%{mvn_package} org.eclipse.jetty.tests: __noinstall
%{mvn_package} ::war: __noinstall
%{mvn_package} :jetty-runner __noinstall
%{mvn_package} :build-resources __noinstall

%{mvn_package} org.eclipse.jetty.cdi: jetty-cdi

%{mvn_package} ':jetty-alpn*-client' jetty-alpn-client
%{mvn_package} ':jetty-alpn*-server' jetty-alpn-server

%{mvn_package} :apache-jsp jetty-jsp
%{mvn_alias} :apache-jsp :jetty-jsp

%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files client -f .mfiles-%{name}-client

%files server -f .mfiles-%{name}-server

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE.txt

%changelog
