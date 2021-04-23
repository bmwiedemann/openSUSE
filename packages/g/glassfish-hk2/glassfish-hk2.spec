#
# spec file for package glassfish-hk2
#
# Copyright (c) 2020 SUSE LLC
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


%global extra_version 1.0.3
%bcond_without jp_minimal
Name:           glassfish-hk2
Version:        2.5.0
Release:        0
Summary:        Glassfish Hundred Kilobytes Kernel
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://github.com/eclipse-ee4j/glassfish-hk2/
Source0:        https://github.com/eclipse-ee4j/glassfish-hk2/archive/%{version}-RELEASE/%{name}-%{version}.tar.gz
Source1:        https://github.com/eclipse-ee4j/glassfish-hk2-extra/archive/%{extra_version}-RELEASE/%{name}-extra-%{extra_version}.tar.gz
Source2:        hk2-inhabitant-generator-osgi.bundle
# unbundles tiger-types from hk2-utils osgi metadata and
# fixes invalid whitespace in hk2-core osgi metadata
Patch0:         0001-OSGi-metadata-fixes.patch
# fixed some test failures
Patch1:         0002-Fixed-tests.patch
# Module ambiguous in java 11
Patch2:         hk2-jdk11.patch
BuildRequires:  maven-local
BuildRequires:  mvn(aopalliance:aopalliance)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-osgi)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm-all)
BuildArch:      noarch
%if %{without jp_minimal}
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(javax.el:javax.el-api)
BuildRequires:  mvn(javax.json:javax.json-api)
BuildRequires:  mvn(javax.validation:validation-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(org.apache.bcel:bcel)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.bundlerepository)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.glassfish:javax.json)
BuildRequires:  mvn(org.hibernate:hibernate-validator)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.springframework:spring-context)
BuildRequires:  mvn(org.testng:testng)
%endif
%if %{with jp_minimal}
Obsoletes:      glassfish-hk2-dependency-verifier < %{version}-%{release}
Obsoletes:      glassfish-hk2-dependency-visualizer < %{version}-%{release}
Obsoletes:      glassfish-hk2-guice-bridge < %{version}-%{release}
Obsoletes:      glassfish-hk2-osgi < %{version}-%{release}
Obsoletes:      glassfish-hk2-spring-bridge < %{version}-%{release}
%endif

%description
HK2 for Hundred Kilobytes Kernel is an abstraction to
a module subsystem coupled with a simple yet powerful
component model to build server side software.

%package hk2
Summary:        HK2 module of HK2 itself

%description hk2
This is so that other modules can depend on HK2 as an HK2 module.

%package api
Summary:        HK2 API module

%description api
Hundred Kilobytes Kernel API module.

%package core
Summary:        HK2 core module

%description core
Hundred Kilobytes Kernel core module.

%package configuration
Summary:        HK2 configuration modules

%description configuration
Hundred Kilobytes Kernel configuration modules.

%package extras
Summary:        HK2 extras module

%description extras
Default implementations for HK2 services.

%package jmx
Summary:        HK2 JMX module

%description jmx
Hundred Kilobytes Kernel JMX module.

%package locator
Summary:        HK2 ServiceLocator Default Implementation

%description locator
Hundred Kilobytes Kernel ServiceLocator Default Implementation.

%package metadata-generator
Summary:        HK2 Metadata Generator

%description metadata-generator
HK2 Metadata Generator Subsystem.

%package runlevel
Summary:        HK2 Run Level Service

%description runlevel
Hundred Kilobytes Kernel Run Level Service.

%package utils
Summary:        HK2 Implementation Utilities

%description utils
Hundred Kilobytes Kernel Implementation Utilities.

%package class-model
Summary:        Class Model for Hk2

%description class-model
Hundred Kilobytes Kernel Class Model.

%package osgi-resource-locator
Summary:        HK2 OSGi resource locator bundle
Obsoletes:      osgi-resource-locator < %{version}-%{release}
Provides:       osgi-resource-locator = %{version}-%{release}

%description osgi-resource-locator
Hundred Kilobytes Kernel - OSGi resource locator bundle. Used by
various API providers that rely on META-INF/services mechanism to
locate providers.

%if %{without jp_minimal}
%package dependency-verifier
Summary:        HK2 Static Analyser for verifying module dependency

%description dependency-verifier
HK2 Static Analyser for verifying module dependency.

%package dependency-visualizer
Summary:        HK2 Tool to visualize the dependencies

%description dependency-visualizer
Tool to visualize the dependencies generated by HK2's dependency-verifier.

%package guice-bridge
Summary:        HK2 Guice Bridge

%description guice-bridge
Hundred Kilobytes Kernel Guice Bridge.

%package spring-bridge
Summary:        HK2 Spring Bridge

%description spring-bridge
Hundred Kilobytes Kernel Spring Bridge.

%package osgi
Summary:        HK2 OSGi Adapter

%description osgi
Hundred Kilobytes Kernel OSGi Adapter.
%endif

%package testing
Summary:        Utilities for testing with HK2
Obsoletes:      %{name}-locator-extras < %{version}-%{release}
Provides:       %{name}-locator-extras = %{version}-%{release}
Obsoletes:      %{name}-locator-no-proxies < %{version}-%{release}
Provides:       %{name}-locator-no-proxies = %{version}-%{release}
Obsoletes:      %{name}-locator-no-proxies2 < %{version}-%{release}
Provides:       %{name}-locator-no-proxies2 = %{version}-%{release}
Obsoletes:      %{name}-runlevel-extras < %{version}-%{release}
Provides:       %{name}-runlevel-extras = %{version}-%{release}
Obsoletes:      %{name}-testng < %{version}-%{release}
Provides:       %{name}-testng = %{version}-%{release}

%description testing
Hundred Kilobytes Kernel utilities for testing.

%package maven-plugins
Summary:        HK2 Maven Plug-ins
Obsoletes:      %{name}-maven < %{version}-%{release}
Provides:       %{name}-maven < %{version}-%{release}
Obsoletes:      %{name}-inhabitant-generator < %{version}-%{release}
Provides:       %{name}-inhabitant-generator < %{version}-%{release}

%description maven-plugins
This package provides various maven plug-ins:
* consolidatedbundle-maven-plugin
* osgiversion-maven-plugin
* hk2-inhabitant-generator

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n glassfish-hk2-%{version}-RELEASE
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Disable tests that intermittently fail on ARM arches
sed -i -e '/org\.junit\.Ignore/s/\/\///' \
  hk2-locator/src/test/java/org/glassfish/hk2/tests/locator/multithreaded1/MultiThreaded1Test.java

# Explode extra bundles and insert into the build
tar xf %{SOURCE1} --strip-components=1 \
  %{name}-extra-%{extra_version}-RELEASE/osgi-resource-locator \
  %{name}-extra-%{extra_version}-RELEASE/dependency-{verifier,visualizer}
%pom_xpath_set "pom:dependency[pom:groupId ='org.glassfish.hk2']/pom:version" %{version} dependency-verifier
for mod in osgi-resource-locator dependency-verifier dependency-visualizer ; do
  %pom_xpath_inject "pom:modules" "<module>$mod</module>"
  %pom_remove_parent $mod
  %pom_add_parent "org.glassfish.hk2:hk2-parent:%{version}" $mod
done

# Do not remove test resources
find . -name '*.jar' ! -name "gendir.jar" -type f -print -delete
find . -name '*.class' -print -delete

# EE4j parent pom contains only release/nexus related stuff, we won't miss it
%pom_remove_parent bom .

# Some Glassfish APIs that moved to the EE4j project are not yet updated in openSUSE
# provide the new Jakarta maven coords, so continue to use the old javax coords for now
%pom_change_dep -r jakarta.servlet:jakarta.servlet-api javax.servlet:javax.servlet-api
%pom_change_dep -r jakarta.annotation:jakarta.annotation-api javax.annotation:javax.annotation-api
%pom_change_dep -r jakarta.el:jakarta.el-api javax.el:javax.el-api
%pom_change_dep -r jakarta.json:jakarta.json-api javax.json:javax.json-api
%pom_change_dep -r org.glassfish:jakarta.json org.glassfish:javax.json
%pom_change_dep -r org.glassfish.hk2.external:jakarta.inject javax.inject:javax.inject

# Use system libraries, not bundled versions
%pom_change_dep -r org.glassfish.hk2.external:asm-repackaged org.ow2.asm:asm-all:'${asm.version}'
%pom_change_dep -r org.glassfish.hk2.external:aopalliance-repackaged aopalliance:aopalliance:'${aopalliance.version}'
find class-model maven-plugins/hk2-inhabitant-generator hk2-testing/hk2-junitrunner \
   -name "*.java" -exec sed -i "s/org.glassfish.hk2.external.org.objectweb.asm/org.objectweb.asm/g" {} +

# Fix version of deps from hk2 extra
%pom_change_dep :osgi-resource-locator ::%{extra_version}

# Enterprise APIs are a subset of those provided by the Compendium APIs
%pom_remove_dep org.osgi:org.osgi.enterprise
%pom_change_dep :org.osgi.enterprise org.osgi:osgi.cmpn:6.0.0 class-model

# Remove plugins not necessary for RPM builds
%pom_remove_plugin :maven-download-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-eclipse-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_dep :jacoco-maven-plugin
%pom_remove_plugin :maven-jar-plugin osgi-resource-locator
%pom_remove_plugin :maven-source-plugin osgi-resource-locator
%pom_remove_plugin :maven-javadoc-plugin osgi-resource-locator
%pom_remove_plugin :maven-release-plugin osgi-resource-locator
%pom_remove_plugin :maven-gpg-plugin osgi-resource-locator
%pom_xpath_remove "pom:plugin[pom:artifactId ='maven-jar-plugin']/pom:executions" hk2

# Don't ship re-packaged external deps or examples
%pom_disable_module external
%pom_disable_module examples

# Disable modules and tests that require org.ops4j.*
# These are not available in Fedora
%pom_disable_module osgi-adapter-test osgi/adapter-tests
%pom_remove_dep org.ops4j.pax.exam:
%pom_remove_dep org.ops4j.pax.url:
%pom_remove_dep org.ops4j.pax.logging:

# Disable test that would introduce circular deps
%pom_disable_module jersey hk2-testing

%if %{with jp_minimal}
# Disable modules with extra deps when building with jp_minimal
%pom_disable_module dependency-verifier
%pom_disable_module dependency-visualizer
%pom_disable_module osgi
%pom_disable_module guice-bridge
%pom_disable_module spring-bridge
%pom_remove_dep :osgi-adapter bom
%pom_remove_dep :guice-bridge bom
%pom_remove_dep :spring-bridge bom
%pom_disable_module hk2-xml hk2-configuration/persistence
# Build minimal testing utilities when building with jp_minimal
%pom_xpath_set "pom:modules" "<module>hk2-junitrunner</module>" hk2-testing
# Avoid dep on hibernate when building with jp_minimal
%pom_remove_dep javax.validation:validation-api hk2-utils
%pom_remove_dep org.hibernate:hibernate-validator hk2-utils
%pom_remove_dep javax.el:javax.el-api hk2-utils
rm hk2-utils/src/main/java/org/glassfish/hk2/utilities/general/ValidatorUtilities.java \
   hk2-utils/src/main/java/org/glassfish/hk2/utilities/general/internal/MessageInterpolatorImpl.java \
   hk2-utils/src/test/java/org/glassfish/hk2/utilities/test/ValidatorTest.java
%endif

# FIXME remove a broken test
rm hk2-runlevel/src/test/java/org/glassfish/hk2/runlevel/tests/listener/ListenerErrorTest.java

# Remove pointless unused dependencies
# Patch submitted upstream, see https://github.com/eclipse-ee4j/glassfish-hk2/pull/445
%pom_remove_dep org.osgi:osgi_R4_core
%pom_remove_dep :com.springsource.org.junit

# Remove some optional deps
%pom_remove_dep -r :jboss-logging
%pom_remove_dep -r :classmate

# Disable security policy that interferes with tests
%pom_xpath_remove "pom:plugin[pom:artifactId ='maven-surefire-plugin']/pom:configuration" hk2-api
%pom_xpath_remove "pom:plugin[pom:artifactId ='maven-surefire-plugin']/pom:configuration" hk2-locator

# Fix reference to JDK tools jar
%pom_xpath_set "pom:dependency[pom:groupId ='com.sun']/pom:artifactId" tools hk2-testing/ant
%pom_xpath_remove "pom:dependency[pom:groupId ='com.sun']/pom:scope" hk2-testing/ant
%pom_xpath_remove "pom:dependency[pom:groupId ='com.sun']/pom:systemPath" hk2-testing/ant
%pom_xpath_remove "pom:profiles/pom:profile[pom:id ='mac']" hk2-testing/ant

# Don't put classpath in jar manifest
%pom_xpath_set "pom:addClasspath" false dependency-verifier

mkdir -p hk2/target/classes

# Drop pre-existent OSGI manifest file
rm maven-plugins/hk2-inhabitant-generator/src/main/resources/META-INF/MANIFEST.MF
%pom_add_plugin org.apache.felix:maven-bundle-plugin maven-plugins/hk2-inhabitant-generator '
<configuration>
  <supportedProjectTypes>
   <supportedProjectType>maven-plugin</supportedProjectType>
  </supportedProjectTypes>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

# Add configuration file for osgiversion plugin
cp -p %{SOURCE2} maven-plugins/hk2-inhabitant-generator/osgi.bundle
%pom_add_plugin org.glassfish.hk2:osgiversion-maven-plugin:'${project.version}' maven-plugins/hk2-inhabitant-generator

# Inject manifest file
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin:2.4 maven-plugins/hk2-inhabitant-generator "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <manifestEntries>
      <service>foo</service>
    </manifestEntries>
  </archive>
</configuration>"

# fix build failure. 'useDefaultManifestFile' has been removed from the maven-jar-plugin >= 3.0.0
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:configuration/pom:useDefaultManifestFile" . hk2-utils
%pom_xpath_inject "pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:configuration/pom:archive" \
  "<manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>" hk2-utils

# For every module that generates a OSGi manifest, add it to the jar
# Remove this when upstream moves to maven-jar-plugin >= 3.0.0
for mod in $(grep -l maven-bundle-plugin $(find */ -name pom.xml) ) ; do
  if [ "$(dirname $mod)" = "hk-utils" ] ; then
    continue
  fi
  %pom_add_plugin org.apache.maven.plugins:maven-jar-plugin $mod "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"
done

# This causes the plugin not to try to build with source/target 1.5
%pom_remove_plugin :maven-compiler-plugin maven-plugins/consolidatedbundle-maven-plugin

# Don't package unit test jars
%{mvn_package} ":::tests:" __noinstall

# Create subpackages
%{mvn_package} ":hk2-bom" %{name}
%{mvn_package} ":hk2-parent" %{name}
%{mvn_package} ":hk2" hk2
%{mvn_package} ":hk2-api" api
%{mvn_package} ":hk2-core" core
%{mvn_package} ":hk2-configuration" configuration
%{mvn_package} ":hk2-configuration-hub" configuration
%{mvn_package} ":hk2-configuration-integration" configuration
%{mvn_package} ":hk2-configuration-persistence" configuration
%{mvn_package} ":hk2-property-file" configuration
%{mvn_package} ":hk2-xml-parent" configuration
%{mvn_package} ":hk2-xml-schema" configuration
%{mvn_package} ":hk2-xml-integration-test" __noinstall
%{mvn_package} ":hk2-xml-test" __noinstall
%{mvn_package} ":hk2-json" configuration
%{mvn_package} ":hk2-pbuf" configuration
%{mvn_package} ":hk2-xml" configuration
%{mvn_package} ":hk2-extras" extras
%{mvn_package} ":hk2-jmx" jmx
%{mvn_package} ":hk2-locator" locator
%{mvn_package} ":hk2-metadata-generator" metadata-generator
%{mvn_package} ":hk2-metadata-generator-parent" metadata-generator
%{mvn_package} ":hk2-metadata-generator-test1" __noinstall
%{mvn_package} ":hk2-runlevel" runlevel
%{mvn_package} ":hk2-utils" utils
%{mvn_package} ":class-model" class-model
%{mvn_package} ":osgi-resource-locator" osgi-resource-locator
%{mvn_package} ":hk2-dependency-verifier" dependency-verifier
%{mvn_package} ":hk2-dependency-visualizer" dependency-visualizer
%{mvn_package} ":guice-bridge" guice-bridge
%{mvn_package} ":spring-bridge" spring-bridge
%{mvn_package} ":osgi" osgi
%{mvn_package} ":osgi-adapter" osgi
%{mvn_package} ":osgi-adapter-tests-parent" __noinstall
%{mvn_package} ":contract-bundle" __noinstall
%{mvn_package} ":faux-sdp-bundle" __noinstall
%{mvn_package} ":no-hk2-bundle" __noinstall
%{mvn_package} ":osgi-adapter-test" __noinstall
%{mvn_package} ":sdp-management-bundle" __noinstall
%{mvn_package} ":test-module-startup" __noinstall

# Testing modules
%{mvn_package} ":hk2-testing" testing
%{mvn_package} ":hk2-ant-test" testing
%{mvn_package} ":hk2-collections-tests" testing
%{mvn_package} ":hk2-junitrunner" testing
%{mvn_package} ":hk2-locator-extras" testing
%{mvn_package} ":hk2-locator-no-proxies" testing
%{mvn_package} ":hk2-locator-no-proxies2" testing
%{mvn_package} ":hk2-mockito" testing
%{mvn_package} ":hk2-runlevel-extras" testing
%{mvn_package} ":hk2-testng" testing
%{mvn_package} ":interceptor-events" testing

# Maven plug-ins
%{mvn_package} ":maven-plugins" maven-plugins
%{mvn_package} ":consolidatedbundle-maven-plugin" maven-plugins
%{mvn_package} ":hk2-inhabitant-generator" maven-plugins
%{mvn_package} ":osgiversion-maven-plugin" maven-plugins

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=7 \
%endif
	-Dhk2.mvn.plugins.version=%{version}

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%license LICENSE.md NOTICE.md

%files hk2 -f .mfiles-hk2
%license LICENSE.md NOTICE.md

%files api -f .mfiles-api
%license LICENSE.md NOTICE.md

%files core -f .mfiles-core
%license LICENSE.md NOTICE.md

%files configuration -f .mfiles-configuration
%license LICENSE.md NOTICE.md

%files extras -f .mfiles-extras
%license LICENSE.md NOTICE.md

%files jmx -f .mfiles-jmx
%license LICENSE.md NOTICE.md

%files locator -f .mfiles-locator
%license LICENSE.md NOTICE.md

%files metadata-generator -f .mfiles-metadata-generator
%license LICENSE.md NOTICE.md

%files runlevel -f .mfiles-runlevel
%license LICENSE.md NOTICE.md

%files utils -f .mfiles-utils
%license LICENSE.md NOTICE.md

%files class-model -f .mfiles-class-model
%license LICENSE.md NOTICE.md

%files osgi-resource-locator -f .mfiles-osgi-resource-locator
%license LICENSE.md NOTICE.md

%if %{without jp_minimal}
%files dependency-verifier -f .mfiles-dependency-verifier
%license LICENSE.md NOTICE.md

%files dependency-visualizer -f .mfiles-dependency-visualizer
%doc dependency-visualizer/README
%license LICENSE.md NOTICE.md

%files guice-bridge -f .mfiles-guice-bridge
%license LICENSE.md NOTICE.md

%files spring-bridge -f .mfiles-spring-bridge
%license LICENSE.md NOTICE.md

%files osgi -f .mfiles-osgi
%license LICENSE.md NOTICE.md
%endif

%files testing -f .mfiles-testing
%license LICENSE.md NOTICE.md

%files maven-plugins -f .mfiles-maven-plugins
%license LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
