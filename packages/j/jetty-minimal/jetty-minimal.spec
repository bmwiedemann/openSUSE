#
# spec file for package jetty-minimal
#
# Copyright (c) 2024 SUSE LLC
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
%global addver  .v20240826
%define src_name %{base_name}.project-%{base_name}-%{version}%{addver}
Name:           %{base_name}-minimal
Version:        9.4.56
Release:        0
Summary:        Java Webserver and Servlet Container
License:        Apache-2.0 OR EPL-1.0
Group:          Productivity/Networking/Web/Servers
URL:            https://www.eclipse.org/jetty/
Source0:        https://github.com/eclipse/%{base_name}.project/archive/%{base_name}-%{version}%{addver}.tar.gz#/%{src_name}.tar.gz
Patch0:         jetty-port-to-servlet-4.0.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.transaction:javax.transaction-api)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.tomcat:tomcat-jasper)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty.orbit:javax.mail.glassfish)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-schemas)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.slf4j:slf4j-api)
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
Summary:        The annotations module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-annotations
%{extdesc} %{summary}.

%package        -n %{base_name}-ant
Summary:        The ant module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-ant
%{extdesc} %{summary}.

%package        -n %{base_name}-cdi
Summary:        The cdi module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-cdi
%{extdesc} %{summary}.

%package        -n %{base_name}-client
Summary:        The client module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-client
%{extdesc} %{summary}.

%package        -n %{base_name}-continuation
Summary:        The continuation module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-continuation
%{extdesc} %{summary}.

%package        -n %{base_name}-deploy
Summary:        The deploy module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-deploy
%{extdesc} %{summary}.

%package        -n %{base_name}-fcgi
Summary:        The fcgi module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-fcgi
%{extdesc} %{summary}.

%package        -n %{base_name}-http
Summary:        The http module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-http
%{extdesc} %{summary}.

%package        -n %{base_name}-http-spi
Summary:        The http-spi module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-http-spi
%{extdesc} %{summary}.

%package        -n %{base_name}-io
Summary:        The io module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-io
%{extdesc} %{summary}.

%package        -n %{base_name}-jaas
Summary:        The jaas module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-jaas
%{extdesc} %{summary}.

%package        -n %{base_name}-jmx
Summary:        The jmx module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-jmx
%{extdesc} %{summary}.

%package        -n %{base_name}-jndi
Summary:        The jndi module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-jndi
%{extdesc} %{summary}.

%package        -n %{base_name}-jsp
Summary:        The jsp module for Jetty
Group:          Productivity/Networking/Web/Servers
Requires:       glassfish-el

%description    -n %{base_name}-jsp
%{extdesc} %{summary}.

%package        -n %{base_name}-openid
Summary:        The openid module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-openid
%{extdesc} %{summary}.

%package        -n %{base_name}-plus
Summary:        The plus module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-plus
%{extdesc} %{summary}.

%package        -n %{base_name}-proxy
Summary:        The proxy module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-proxy
%{extdesc} %{summary}.

%package        -n %{base_name}-quickstart
Summary:        The quickstart module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-quickstart
%{extdesc} %{summary}.

%package        -n %{base_name}-rewrite
Summary:        The rewrite module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-rewrite
%{extdesc} %{summary}.

%package        -n %{base_name}-security
Summary:        The security module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-security
%{extdesc} %{summary}.

%package        -n %{base_name}-server
Summary:        The server module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-server
%{extdesc} %{summary}.

%package        -n %{base_name}-servlet
Summary:        The servlet module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-servlet
%{extdesc} %{summary}.

%package        -n %{base_name}-servlets
Summary:        The servlets module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-servlets
%{extdesc} %{summary}.

%package        -n %{base_name}-start
Summary:        The start module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-start
%{extdesc} %{summary}.

%package        -n %{base_name}-util
Summary:        The util module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-util
%{extdesc} %{summary}.

%package        -n %{base_name}-util-ajax
Summary:        The util-ajax module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-util-ajax
%{extdesc} %{summary}.

%package        -n %{base_name}-webapp
Summary:        The webapp module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-webapp
%{extdesc} %{summary}.

%package        -n %{base_name}-xml
Summary:        The xml module for Jetty
Group:          Productivity/Networking/Web/Servers

%description    -n %{base_name}-xml
%{extdesc} %{summary}.

%package        -n %{base_name}-project
Summary:        POM files for Jetty

%description    -n %{base_name}-project
%{extdesc} %{summary}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Productivity/Networking/Web/Servers

%description    javadoc
%{summary}.

%prep
%setup -q -n %{src_name}
%patch -P 0 -p1

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

%pom_change_dep org.apache.directory.api: :::test jetty-jaas

# the default location is not allowed by SELinux
sed -i '/<SystemProperty name="jetty.state"/d' \
    jetty-home/src/main/resources%{_sysconfdir}/jetty-started.xml

# remote-resources only copies about.html
%pom_remove_plugin :maven-remote-resources-plugin
# packages module configs, we don't need those in minimal
%pom_remove_plugin -r :maven-assembly-plugin
# only useful when tests are enabled (copies test deps)
%pom_remove_plugin :maven-dependency-plugin jetty-client

%pom_disable_module jetty-http2
%pom_disable_module jetty-websocket
%pom_disable_module apache-jstl
%pom_disable_module jetty-maven-plugin
%pom_disable_module jetty-jspc-maven-plugin
%pom_disable_module jetty-spring
%pom_disable_module jetty-jaspi
%pom_disable_module jetty-nosql
%pom_disable_module tests
%pom_disable_module examples
%pom_disable_module jetty-distribution
%pom_disable_module jetty-runner
%pom_disable_module jetty-unixsocket
%pom_disable_module jetty-alpn
%pom_disable_module jetty-home

%pom_xpath_remove "pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:additionalJOption"

%{mvn_file} :{*} %{base_name}/@1

%build

%{mvn_package} :jetty-home __noinstall
%{mvn_package} :jetty-distribution __noinstall

# Separate package for POMs
%{mvn_package} ':*-project' project
%{mvn_package} ':*-parent' project
%{mvn_package} ':*-bom' project

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

# we don't have all necessary dependencies to run tests
# missing test dep: org.eclipse.jetty.toolchain:jetty-perf-helper
%{mvn_build} -f -s -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

# Apache Ant stuff
install -dm0755 %{buildroot}%{_sysconfdir}/ant.d
install -dm0755 %{buildroot}%{_datadir}/ant/lib
echo $(for jar in %{buildroot}%{_javadir}/%{base_name}/*.jar; do echo %{base_name}/$(basename $jar .jar); done) \
	>%{buildroot}%{_sysconfdir}/ant.d/%{base_name}
ln -s %{_javadir}/%{base_name}/%{base_name}-ant.jar %{buildroot}%{_datadir}/ant/lib/

%files -n %{base_name}-annotations -f .mfiles-jetty-annotations

%files -n %{base_name}-ant -f .mfiles-jetty-ant
%config %{_sysconfdir}/ant.d/%{base_name}
%{_datadir}/ant/lib/%{base_name}-ant.jar

%files -n %{base_name}-cdi -f .mfiles-jetty-cdi

%files -n %{base_name}-client -f .mfiles-jetty-client

%files -n %{base_name}-continuation -f .mfiles-jetty-continuation

%files -n %{base_name}-deploy -f .mfiles-jetty-deploy

%files -n %{base_name}-fcgi -f .mfiles-fcgi-server -f .mfiles-fcgi-client

%files -n %{base_name}-http-spi -f .mfiles-jetty-http-spi

%files -n %{base_name}-jaas -f .mfiles-jetty-jaas

%files -n %{base_name}-jndi -f .mfiles-jetty-jndi

%files -n %{base_name}-jsp -f .mfiles-jetty-jsp

%files -n %{base_name}-io -f .mfiles-jetty-io

%files -n %{base_name}-openid -f .mfiles-jetty-openid

%files -n %{base_name}-server -f .mfiles-jetty-server

%files -n %{base_name}-servlet -f .mfiles-jetty-servlet

%files -n %{base_name}-start -f .mfiles-jetty-start

%files -n %{base_name}-util -f .mfiles-jetty-util

%files -n %{base_name}-util-ajax -f .mfiles-jetty-util-ajax

%files -n %{base_name}-webapp -f .mfiles-jetty-webapp

%files -n %{base_name}-jmx -f .mfiles-jetty-jmx

%files -n %{base_name}-xml -f .mfiles-jetty-xml

%files -n %{base_name}-http -f .mfiles-jetty-http

%files -n %{base_name}-proxy -f .mfiles-jetty-proxy

%files -n %{base_name}-plus -f .mfiles-jetty-plus

%files -n %{base_name}-project -f .mfiles-project

%files -n %{base_name}-quickstart -f .mfiles-jetty-quickstart

%files -n %{base_name}-rewrite -f .mfiles-jetty-rewrite

%files -n %{base_name}-security -f .mfiles-jetty-security

%files -n %{base_name}-servlets -f .mfiles-jetty-servlets

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE.txt

%changelog
