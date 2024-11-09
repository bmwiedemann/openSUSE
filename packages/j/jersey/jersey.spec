#
# spec file for package jersey
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


%bcond_without jp_minimal
Name:           jersey
Version:        2.28
Release:        0
Summary:        JAX-RS (JSR 311) production quality Reference Implementation
# Some files in core-server are under ASL 2.0 license
License:        Apache-2.0 AND (EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0) AND BSD-2-Clause
URL:            https://github.com/eclipse-ee4j/jersey
Source0:        https://github.com/eclipse-ee4j/jersey/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
# Support fo servlet 3.1 apis
Patch0:         jersey-2.17-mvc-jsp-servlet31.patch
# Keep working with old deps in Fedora
Patch2:         0002-Port-to-glassfish-jsonp-1.0.patch
Patch3:         0003-Port-to-hibernate-validation-5.x.patch
Patch4:         jersey-2.28-contended.patch
Patch5:         java-util-concurrent-ThreadFactory-newThread.patch
Patch6:         jersey-asm-version.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.sun.istack:istack-commons-maven-plugin)
BuildRequires:  mvn(javax.activation:javax.activation-api)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.persistence:persistence-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.validation:validation-api)
BuildRequires:  mvn(javax.ws.rs:javax.ws.rs-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-client)
BuildRequires:  mvn(org.eclipse.jetty:jetty-continuation)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.eclipse.jetty:jetty-webapp)
BuildRequires:  mvn(org.glassfish.hk2:hk2-bom:pom:)
BuildRequires:  mvn(org.glassfish.hk2:hk2-locator)
BuildRequires:  mvn(org.glassfish.hk2:osgi-resource-locator)
BuildRequires:  mvn(org.jvnet.mimepull:mimepull)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.simpleframework:simple-common)
BuildRequires:  mvn(org.simpleframework:simple-http)
BuildRequires:  mvn(org.simpleframework:simple-transport)
BuildRequires:  mvn(xerces:xercesImpl)
#!BuildRequires: istack-commons-maven-plugin
BuildArch:      noarch
%if %{without jp_minimal}
BuildRequires:  mvn(com.github.spullara.mustache.java:compiler)
BuildRequires:  mvn(io.reactivex:rxjava)
BuildRequires:  mvn(javax.el:javax.el-api)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.json:javax.json-api)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(javax.transaction:javax.transaction-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.jettison:jettison)
BuildRequires:  mvn(org.freemarker:freemarker)
BuildRequires:  mvn(org.glassfish.grizzly:grizzly-http-server)
BuildRequires:  mvn(org.glassfish.grizzly:grizzly-http-servlet)
BuildRequires:  mvn(org.glassfish:javax.el)
BuildRequires:  mvn(org.glassfish:javax.json)
BuildRequires:  mvn(org.glassfish:jsonp-jaxrs)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.hibernate:hibernate-validator)
BuildRequires:  mvn(org.hibernate:hibernate-validator-cdi)
BuildRequires:  mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires:  mvn(org.jboss.weld.se:weld-se-core)
BuildRequires:  mvn(org.jboss:jboss-vfs)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(org.testng:testng)
%endif

%description
Jersey is the open source JAX-RS (JSR 311)
production quality Reference Implementation
for building RESTful Web services.

%if %{without jp_minimal}
%package test-framework
Summary:        Jersey Test Framework

%description test-framework
%{summary}.
%endif

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%autosetup -p1

find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

# Additional license file
cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt CONTRIBUTING.md README.md

# Remove repackaged bundled deps: guava, objectweb-asm
rm -r core-server/src/main/java/jersey
find core-server -name "*.java" -exec sed -i "s|jersey.repackaged.||" {} +
rm -r core-common/src/main/java/org/glassfish/jersey/internal/guava
grep -rl --include=*.java org.glassfish.jersey.internal.guava | xargs sed -i "s|org\.glassfish\.jersey\.internal\.guava|com.google.common.base|"
find core-* containers/{grizzly2,jdk,jetty}-http media/sse ext/{entity-filtering,bean-validation,rx} -name "*.java" -exec sed -i \
  -e "/base\.Cache/s/common\.base/common.cache/" \
  -e "/base\.LoadingCache/s/common\.base/common.cache/" \
  -e "/base\.Multimap/s/common\.base/common.collect/" \
  -e "/base\.....Multimap/s/common\.base/common.collect/" \
  -e "/base\.HashBasedTable/s/common\.base/common.collect/" \
  -e "/base\.Table/s/common\.base/common.collect/" \
  -e "/base\.ThreadFactoryBuilder/s/common\.base/common.util.concurrent/" \
  -e "/base\.InetAddresses/s/common\.base/common.net/" \
  -e "/base\.Primitives/s/common\.base/common.primitives/" {} +
%pom_add_dep 'com.google.guava:guava:${guava.version}' core-common inject/hk2
%pom_xpath_set "pom:dependency[pom:artifactId = 'guava']/pom:scope" provided containers/jdk-http
%pom_add_dep 'org.ow2.asm:asm:${asm.version}' core-server

# EE4j parent pom contains only release/nexus related stuff, we won't miss it
%pom_remove_parent bom .

# Some Glassfish APIs that moved to the EE4j project are not yet updated in Fedora to
# provide the new Jakarta maven coords, so continue to use the old javax coords for now
%pom_change_dep -r jakarta.servlet:jakarta.servlet-api javax.servlet:javax.servlet-api . test-framework
%pom_change_dep -r jakarta.servlet.jsp:jakarta.servlet.jsp-api javax.servlet.jsp:jsp-api
%pom_change_dep -r jakarta.xml.bind:jakarta.xml.bind-api javax.xml.bind:jaxb-api
%pom_change_dep -r jakarta.annotation:jakarta.annotation-api javax.annotation:javax.annotation-api
%pom_change_dep -r jakarta.persistence:jakarta.persistence-api javax.persistence:persistence-api
%pom_change_dep -r org.glassfish.hk2.external:jakarta.inject javax.inject:javax.inject
%pom_change_dep -r jakarta.el:jakarta.el-api javax.el:javax.el-api
%pom_change_dep -r org.glassfish:jakarta.el org.glassfish:javax.el
%pom_change_dep -r org.glassfish:jakarta.json org.glassfish:javax.json
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core
%pom_change_dep -r org.osgi:org.osgi.compendium org.osgi:osgi.cmpn
%pom_change_dep -r jakarta.ws.rs:jakarta.ws.rs-api javax.ws.rs:javax.ws.rs-api

# Fix NoClassDefFound in tests
%pom_add_dep javax.json:javax.json-api:1.0 media/json-processing

# Fix misc EE API references
%pom_change_dep javax:javaee-api javax.enterprise:cdi-api:'${cdi.api.version}':provided ext/cdi/jersey-cdi1x-transaction
%pom_add_dep javax.transaction:javax.transaction-api:1.3:provided ext/cdi/jersey-cdi1x-transaction
#pom_add_dep org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec:1.0.0.Alpha3:provided ext/cdi/jersey-cdi1x-validation

# uses com.sun.javadoc apis removed in JDK 13
%pom_disable_module wadl-doclet ext

# Don't use obsolete servlet API version
%pom_remove_dep -r org.mortbay.jetty:servlet-api-2.5

# JMockit is unavailable in Fedora
%pom_remove_dep -r org.jmockit:jmockit

# Disable plugins/extensions not needed for RPM builds
%pom_xpath_remove pom:build/pom:extensions
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin core-common
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-jflex-plugin media/moxy
%pom_remove_plugin :maven-jflex-plugin media/jaxb

# Prevent duplicate javadoc invokation
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions"

# No need to ship archetypes (these are pulled from maven central
# when a user invokes the archetype generator command line tool)
%pom_disable_module archetypes

# Disable incubating projects (not generally production ready)
%pom_disable_module incubator

# Don't ship support for netty that doesn't build
%pom_disable_module netty-http containers
%pom_remove_dep :jersey-container-netty-http bom
%pom_disable_module netty-connector connectors
%pom_remove_dep :jersey-netty-connector bom
%pom_disable_module netty test-framework/providers
%pom_remove_dep :jersey-test-framework-provider-netty test-framework/providers/bundle

# Don't ship support for obsolete Jersey 1.x
%pom_disable_module servlet-portability ext
%pom_remove_dep :jersey-servlet-portability bom

# Don't ship support for obsolete jackson 1.x
%pom_disable_module json-jackson1 media
%pom_remove_dep :jersey-media-json-jackson1 bom

# Requires unavailable dep on eclipse yasson
%pom_disable_module json-binding media
%pom_remove_dep :jersey-media-json-binding bom

# Requires unavailable dep eclipselink moxy
%pom_disable_module moxy media
%pom_remove_dep :jersey-media-moxy bom

# Requires unavailable dep on Spring Framework 4.x
%pom_disable_module spring4 ext
%pom_remove_dep :jersey-spring4 bom

# Requires unavailable dep grizzly-http-client
%pom_disable_module grizzly-connector connectors
%pom_remove_dep :jersey-grizzly-connector bom
%pom_remove_dep org.glassfish.jersey.connectors:jersey-grizzly-connector media/multipart
rm media/multipart/src/test/java/org/glassfish/jersey/media/multipart/internal/MultiPartHeaderModificationTest.java

# Requires unavailable dep ejb-container
%pom_disable_module glassfish containers
%pom_remove_dep :jersey-gf-ejb bom

# Requires unavailable dep on cdi-api 2
%pom_disable_module cdi2-se inject
%pom_remove_dep :jersey-cdi2-se bom

# Requires unavailable dep on rxjava2
%pom_disable_module rx-client-rxjava2 ext/rx
%pom_remove_dep :jersey-rx-client-rxjava2 bom

# Requires unavailable groovy-eclipse-compiler plugin
%pom_disable_module maven test-framework

# Don't bother regenerating wadl sources, we don't have the plugin
%pom_remove_plugin com.sun.tools.xjc.maven2: core-server

# Additional modules to disable when jp_minimal is activated
%if %{with jp_minimal}
%pom_disable_module grizzly2-http containers
%pom_disable_module grizzly2-servlet containers
%pom_disable_module json-jettison media
%pom_disable_module json-processing media
%pom_disable_module sse media
%pom_disable_module bean-validation ext
%pom_disable_module cdi ext
%pom_disable_module mvc ext
%pom_disable_module mvc-bean-validation ext
%pom_disable_module mvc-freemarker ext
%pom_disable_module mvc-jsp ext
%pom_disable_module mvc-mustache ext
%pom_disable_module rx ext
%endif

# Ensure HK2-based InjectionManagerFactory implementation can be discovered under OSGi
%pom_xpath_inject "pom:plugin/pom:configuration/pom:instructions" \
  '<Require-Bundle>org.glassfish.jersey.inject.jersey-hk2;bundle-version="%{version}"</Require-Bundle>' core-common
cp -p inject/hk2/src/main/resources/META-INF/services/org.glassfish.jersey.internal.inject.InjectionManagerFactory \
  core-common/src/main/resources/META-INF/services

# Allow versioned dep on javax.annotation
sed -i -e 's/javax\.annotation\.\*;version="!"/javax.annotation.*/' $(find -name pom.xml)
# Make optional dep on javax.activation
sed -i -e 's/javax\.activation\.\*;/javax.activation.*;resolution:=optional;/' core-common/pom.xml
%pom_add_dep javax.activation:javax.activation-api::provided core-common
%pom_add_dep javax.xml.bind:jaxb-api::provided core-server ext/entity-filtering

# All aggregation poms conflict because they have the same aId
%mvn_package :project __noinstall

# Package test framework separately
%{mvn_package} "org.glassfish.jersey.test-framework*:" test-framework

%build
%mvn_build -f -- \
%if %{with jp_minimal}
    -Dtest-framework.excluded \
%endif
    -PsecurityOff -Dasm.version=6.2.1 -Dmaven.test.failure.ignore=true \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dexamples.excluded -Dtests.excluded -Dbundles.excluded -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md CONTRIBUTING.md
%license LICENSE.md NOTICE.md LICENSE-2.0.txt

%if %{without jp_minimal}
%files test-framework -f .mfiles-test-framework
%license LICENSE.md NOTICE.md LICENSE-2.0.txt
%endif

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md LICENSE-2.0.txt

%changelog
