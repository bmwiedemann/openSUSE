#
# spec file for package jetty
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%global addver  .v20190610
Name:           %{base_name}-minimal
Version:        9.4.19
Release:        0
Summary:        Java Webserver and Servlet Container
License:        Apache-2.0 OR EPL-1.0
URL:            https://www.eclipse.org/jetty/
Source0:        https://github.com/eclipse/%{base_name}.project/archive/%{base_name}-%{version}%{addver}.tar.gz
Patch0:         jetty-annotations-asm6.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(javax.transaction:javax.transaction-api)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.apache.tomcat:tomcat-jasper)
BuildRequires:  mvn(org.apache.tomcat:tomcat-util-scan)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-schemas)
BuildArch:      noarch

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
%{desc}

%package        -n %{base_name}-annotations
Summary:        annotations module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-annotations
%{extdesc} %{summary}.

%package        -n %{base_name}-client
Summary:        client module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-client
%{extdesc} %{summary}.

%package        -n %{base_name}-continuation
Summary:        continuation module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-continuation
%{extdesc} %{summary}.

%package        -n %{base_name}-http
Summary:        http module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-http
%{extdesc} %{summary}.

%package        -n %{base_name}-http-spi
Summary:        http-spi module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-http-spi
%{extdesc} %{summary}.

%package        -n %{base_name}-io
Summary:        io module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-io
%{extdesc} %{summary}.

%package        -n %{base_name}-jaas
Summary:        jaas module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-jaas
%{extdesc} %{summary}.

%package        -n %{base_name}-jndi
Summary:        jndi module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-jndi
%{extdesc} %{summary}.


%package        -n %{base_name}-jsp
Summary:        jsp module for Jetty
License:        Apache-2.0 OR EPL-1.0
Requires:       glassfish-el

%description    -n %{base_name}-jsp
%{extdesc} %{summary}.

%package        -n %{base_name}-security
Summary:        security module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-security
%{extdesc} %{summary}.

%package        -n %{base_name}-server
Summary:        server module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-server
%{extdesc} %{summary}.

%package        -n %{base_name}-servlet
Summary:        servlet module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-servlet
%{extdesc} %{summary}.

%package        -n %{base_name}-util
Summary:        util module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-util
%{extdesc} %{summary}.

%package        -n %{base_name}-webapp
Summary:        webapp module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-webapp
%{extdesc} %{summary}.

%package        -n %{base_name}-jmx
Summary:        jmx module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-jmx
%{extdesc} %{summary}.

%package        -n %{base_name}-xml
Summary:        xml module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-xml
%{extdesc} %{summary}.

%package        -n %{base_name}-plus
Summary:        plus module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-plus
%{extdesc} %{summary}.

%package        -n %{base_name}-proxy
Summary:        proxy module for Jetty
License:        Apache-2.0 OR EPL-1.0

%description    -n %{base_name}-proxy
%{extdesc} %{summary}.

%package        javadoc
Summary:        Javadoc for %{name}
License:        Apache-2.0 OR EPL-1.0

%description    javadoc
%{summary}.

%prep
%setup -q -n %{base_name}.project-%{base_name}-%{version}%{addver}

%patch0 -p1

find . -name "*.?ar" -exec rm {} \;
find . -name "*.class" -exec rm {} \;

# Plugins irrelevant or harmful to building the package
%pom_remove_plugin -r :findbugs-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :clirr-maven-plugin
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :maven-pmd-plugin
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

# Use proper groupId for apache ant
%pom_xpath_replace "pom:groupId[text()='ant']" "<groupId>org.apache.ant</groupId>" jetty-ant/pom.xml

%pom_remove_dep "com.sun.net.httpserver:http" jetty-http-spi

%pom_change_dep -r org.mortbay.jasper:apache-jsp org.apache.tomcat:tomcat-jasper

%pom_add_dep 'org.junit.jupiter:junit-jupiter-engine:${junit.version}' tests/test-sessions/test-sessions-common

# Old version of jetty not available for tests, so use this version
%pom_change_dep 'org.eclipse.jetty:jetty-util' 'org.eclipse.jetty:jetty-util:${project.version}' tests/test-webapps/test-servlet-spec/test-spec-webapp

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
%pom_xpath_remove "pom:execution[pom:id[text()='copy-setuid-deps']]" jetty-home/pom.xml

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

# missing conscrypt
%pom_disable_module jetty-alpn-conscrypt-server jetty-alpn
%pom_disable_module jetty-alpn-conscrypt-client jetty-alpn
%pom_remove_dep -r :jetty-alpn-conscrypt-server
%pom_remove_dep -r :jetty-alpn-conscrypt-client
rm -fr examples/embedded/src/main/java/org/eclipse/jetty/embedded/ManyConnectors.java

# the default location is not allowed by SELinux
sed -i '/<SystemProperty name="jetty.state"/d' \
    jetty-home/src/main/resources/etc/jetty-started.xml

# remote-resources only copies about.html
%pom_remove_plugin :maven-remote-resources-plugin
# packages module configs, we don't need those in minimal
%pom_remove_plugin -r :maven-assembly-plugin
# only useful when tests are enabled (copies test deps)
%pom_remove_plugin :maven-dependency-plugin jetty-client

%pom_disable_module jetty-ant
%pom_disable_module jetty-http2
%pom_disable_module jetty-fcgi
%pom_disable_module jetty-websocket
%pom_disable_module jetty-servlets
%pom_disable_module jetty-util-ajax
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
%pom_disable_module jetty-alpn
%pom_disable_module jetty-home

%mvn_file :{*} %{base_name}/@1

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

%{mvn_package} org.eclipse.jetty.cdi: jetty-cdi

%{mvn_package} ':jetty-alpn*-client' jetty-alpn-client
%{mvn_package} ':jetty-alpn*-server' jetty-alpn-server

%{mvn_package} :apache-jsp jetty-jsp
%{mvn_alias} :apache-jsp :jetty-jsp

# we don't have all necessary dependencies to run tests
# missing test dep: org.eclipse.jetty.toolchain:jetty-perf-helper
%{mvn_build} -f -s

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -n %{base_name}-annotations -f .mfiles-jetty-annotations

%files -n %{base_name}-client -f .mfiles-jetty-client

%files -n %{base_name}-continuation -f .mfiles-jetty-continuation

%files -n %{base_name}-jaas -f .mfiles-jetty-jaas

%files -n %{base_name}-jndi -f .mfiles-jetty-jndi

%files -n %{base_name}-jsp -f .mfiles-jetty-jsp

%files -n %{base_name}-io -f .mfiles-jetty-io

%files -n %{base_name}-server -f .mfiles-jetty-server

%files -n %{base_name}-servlet -f .mfiles-jetty-servlet

%files -n %{base_name}-util -f .mfiles-jetty-util

%files -n %{base_name}-webapp -f .mfiles-jetty-webapp

%files -n %{base_name}-jmx -f .mfiles-jetty-jmx

%files -n %{base_name}-xml -f .mfiles-jetty-xml

%files -n %{base_name}-http -f .mfiles-jetty-http

%files -n %{base_name}-security -f .mfiles-jetty-security

%files -n %{base_name}-proxy -f .mfiles-jetty-proxy

%files -n %{base_name}-plus -f .mfiles-jetty-plus

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE.txt

%changelog
