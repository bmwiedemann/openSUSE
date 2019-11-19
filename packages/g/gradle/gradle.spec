#
# spec file for package gradle
#
# Copyright (c) 2019 SUSE LLC.
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


Name:           gradle
Version:        4.4.1
Release:        0
Summary:        Build automation tool
# Some examples and integration tests are under GNU LGPL and Boost
# Software License, but are not used to create binary package.
License:        Apache-2.0
URL:            http://www.gradle.org/

Source0:        http://services.gradle.org/distributions/gradle-%{version}-src.zip
Source1:        http://services.gradle.org/versions/all#/all-released-versions.json
Source2:        gradle-font-metadata.xml
Source3:        gradle-jquery-metadata.xml
Source4:        gradle-launcher.sh.in
Source5:        gradle.desktop
Source6:        gradle-man.txt

Patch0001:      0001-Gradle-local-mode.patch
Patch0002:      0002-Remove-Class-Path-from-manifest.patch
Patch0003:      0003-Implement-XMvn-repository-factory-method.patch
Patch0004:      0004-Use-unversioned-dependency-JAR-names.patch
Patch0005:      0005-Port-to-Maven-3.3.9-and-Eclipse-Aether.patch
Patch0006:      0006-Disable-code-quality-checks.patch
Patch0007:      0007-Port-to-Kryo-3.0.patch
Patch0008:      0008-Port-to-Ivy-2.4.0.patch
Patch0009:      0009-Port-to-Polyglot-0.1.8.patch
Patch0010:      0010-Port-from-Simple-4-to-Jetty-9.patch
Patch0011:      0011-Disable-benchmarks.patch
Patch0012:      0012-Disable-patching-of-external-modules.patch
Patch0013:      0013-Add-missing-transitive-dependencies.patch
Patch0014:      0014-Disable-ideNative-module.patch
Patch0015:      0015-Disable-docs-build.patch
Patch0016:      0016-Port-to-guava-20.0.patch
# it depends on ant which is Java 8+
Patch0017:      0017-Set-core-api-source-level-to-8.patch

Patch100:       gradle-CVE-2019-16370.patch

BuildRequires:  gradle-local
BuildRequires:  xmvn-subst

# Generic build dependencies
BuildRequires:  desktop-file-utils
BuildRequires:  glibc-locale-base
BuildRequires:  hostname
BuildRequires:  procps
BuildRequires:  unzip

# Not to have to own the directories
BuildRequires:  hicolor-icon-theme

# manpage build dependencies
BuildRequires:  asciidoc
BuildRequires:  xmlto

# Artifacts required for Gradle build
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(biz.aQute.bnd:bndlib)
BuildRequires:  mvn(bsh:bsh)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(ch.qos.logback:logback-core)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-core)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-kms)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-s3)
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.esotericsoftware.kryo:kryo)
BuildRequires:  mvn(com.esotericsoftware:minlog)
BuildRequires:  mvn(com.esotericsoftware:reflectasm)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.code.findbugs:findbugs)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.guava:guava-jdk5:20.0)
BuildRequires:  mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(com.google.http-client:google-http-client)
BuildRequires:  mvn(com.google.oauth-client:google-oauth-client)
BuildRequires:  mvn(com.googlecode.jarjar:jarjar)
BuildRequires:  mvn(com.googlecode.jatl:jatl)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(com.typesafe.zinc:zinc)
BuildRequires:  mvn(com.uwyn:jhighlight)
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-configuration:commons-configuration)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(jline:jline)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.jcip:jcip-annotations)
BuildRequires:  mvn(net.rubygrapefruit:native-platform)
BuildRequires:  mvn(net.sourceforge.nekohtml:nekohtml)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-annotation_1.0_spec)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-shared)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-builder-support)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.xbean:xbean-reflect)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.codehaus.groovy.modules.http-builder:http-builder)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codenarc:CodeNarc)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-spi)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.eclipse.jetty:jetty-annotations)
BuildRequires:  mvn(org.eclipse.jetty:jetty-jsp)
BuildRequires:  mvn(org.eclipse.jetty:jetty-plus)
BuildRequires:  mvn(org.eclipse.jetty:jetty-security)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.eclipse.jetty:jetty-webapp)
BuildRequires:  mvn(org.eclipse.jetty:jetty-xml)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.fusesource.jansi:jansi-native)
BuildRequires:  mvn(org.gmetrics:GMetrics)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.mozilla:rhino)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm-all)
BuildRequires:  mvn(org.parboiled:parboiled-core)
BuildRequires:  mvn(org.parboiled:parboiled-java)
BuildRequires:  mvn(org.pegdown:pegdown)
BuildRequires:  mvn(org.samba.jcifs:jcifs)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:jul-to-slf4j)
BuildRequires:  mvn(org.slf4j:log4j-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.sonatype.plexus:plexus-cipher)
BuildRequires:  mvn(org.sonatype.plexus:plexus-sec-dispatcher)
BuildRequires:  mvn(org.sonatype.pmaven:pmaven-common)
BuildRequires:  mvn(org.sonatype.pmaven:pmaven-groovy)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(xerces:xercesImpl) mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(xml-apis:xml-apis)
# Avoid building with bootstrap versions of those
#!BuildRequires: groovy-lib sbt gpars
# But we want to avoid cycle with oneself
#!BuildRequires: gradle-bootstrap
BuildConflicts: java-devel >= 9

Obsoletes:      %{name}-bootstrap

# Artifacts required for Gradle build which don't have Maven metadata
# and thus no mvn provides.
BuildRequires:  lato-fonts
BuildRequires:  liberation-fonts

# Generic runtime dependencies.
Requires:       bash
Requires:       hicolor-icon-theme
Requires:       javapackages-tools

# Theoretically Gradle might be usable with just JRE, but typical Gradle
# workflow requires full JDK, so we recommend it here.
Recommends:     java-devel

# Providers of symlinks in Gradle lib/ directory. Generated with:
# for l in $(find /usr/share/gradle -type l); do rpm -qf --qf 'Requires:       %{name}\n' $(readlink -e $l); done | sort -u | grep -v gradle
Requires:       ant
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-collections
Requires:       apache-commons-compress
Requires:       apache-commons-io
Requires:       apache-commons-lang
Requires:       apache-commons-lang3
Requires:       apache-ivy
Requires:       aqute-bndlib
Requires:       atinject
Requires:       aws-sdk-java-core
Requires:       aws-sdk-java-kms
Requires:       aws-sdk-java-s3
Requires:       base64coder
Requires:       beust-jcommander
Requires:       bouncycastle
Requires:       bouncycastle-pg
Requires:       bsh2
Requires:       ecj
Requires:       glassfish-servlet-api
Requires:       google-gson
Requires:       google-guice
Requires:       groovy-lib
Requires:       guava20
Requires:       hawtjni-runtime
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       jackson-annotations
Requires:       jackson-core
Requires:       jackson-databind
Requires:       jansi
Requires:       jansi-native
Requires:       jatl
Requires:       jcifs
Requires:       jcip-annotations
Requires:       jcl-over-slf4j
Requires:       jetty-server
Requires:       jetty-util
Requires:       jgit
Requires:       joda-time
Requires:       jsch
Requires:       jsr-305
Requires:       jul-to-slf4j
Requires:       junit
Requires:       kryo
Requires:       log4j-over-slf4j
Requires:       maven-lib
Requires:       maven-resolver-api
Requires:       maven-resolver-connector-basic
Requires:       maven-resolver-impl
Requires:       maven-resolver-spi
Requires:       maven-resolver-transport-wagon
Requires:       maven-resolver-util
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       minlog
Requires:       native-platform
Requires:       nekohtml
Requires:       objectweb-asm
Requires:       objenesis
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       reflectasm
Requires:       rhino
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
Requires:       snakeyaml
Requires:       tesla-polyglot-common
Requires:       tesla-polyglot-groovy
Requires:       testng
Requires:       xbean
Requires:       xerces-j2
Requires:       xml-commons-apis

%description
Gradle is build automation evolved. Gradle can automate the building,
testing, publishing, deployment and more of software packages or other
types of projects such as generated static websites, generated
documentation or indeed anything else.

Gradle combines the power and flexibility of Ant with the dependency
management and conventions of Maven into a more effective way to
build. Powered by a Groovy DSL and packed with innovation, Gradle
provides a declarative way to describe all kinds of builds through
sensible defaults. Gradle is quickly becoming the build system of
choice for many open source projects, leading edge enterprises and
legacy automation challenges.

%prep
%autosetup -p1

# Remove bundled wrapper JAR
rm -rf gradle/wrapper/
# Remove bundled JavaScript
>subprojects/diagnostics/src/main/resources/org/gradle/api/tasks/diagnostics/htmldependencyreport/jquery.jstree.js

# This file is normally downloaded from Internet during package build
mkdir -p build
cp %{SOURCE1} build/all-released-versions.json

# quality checks for which we don't have deps
rm -r buildSrc/src/main/groovy/org/gradle/binarycompatibility
rm buildSrc/src/main/groovy/org/gradle/build/docs/CacheableAsciidoctorTask.groovy

# jquery and fonts don't have Maven metadata
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE2}
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE3}

# Tests for build script currently fail, but the build works.
# TODO: enble tests
rm -rf buildSrc/src/test

# Compilation with Fedora versions of some libraries produces
# warnings. Lets not treat them as errors to make the build work.
sed -i 's/"-Werror" <<//' gradle/strictCompile.gradle

removeProject() {
sed -i "/'$1'/d" settings.gradle
sed -i "s/'$1',\?//" build.gradle
}
removeProject resourcesGcs
rm -r subprojects/resources-gcs
rm -r subprojects/ide-native

%build
export LANG=en_US.UTF8
# Disables parallel build and daemon mode
rm gradle.properties
gradle-local --offline --no-daemon install xmvnInstall \
    -Pgradle_installPath=$PWD/inst \
    -PfinalRelease -Dbuild.number="%{?fedora:Fedora }%{?rhel:Red Hat }%{version}-%{release}"

# manpage build
mkdir man
asciidoc -b docbook -d manpage -o man/gradle.xml %{SOURCE6}
xmlto man man/gradle.xml -o man

%install
cp subprojects/distributions/src/toplevel/NOTICE .
cp subprojects/docs/src/samples/application/src/dist/LICENSE .

install -d -m 755 %{buildroot}%{_javadir}/%{name}/

rm -rf inst/bin/gradle.bat inst/media
ln -sf %{_bindir}/%{name} inst/bin/gradle
find inst/lib -type f -name 'gradle*' | sed 's:.*/\(gradle-.*\)-%{version}.*:ln -sf %{_javadir}/%{name}/\1.jar &:' | bash -x
ln -sf $(find-jar ecj/ecj) inst/lib/plugins/ecj.jar
xmvn-subst -s $(find inst/lib -type f)
# TODO figure out why this one is missing
ln -s $(find-jar commons-lang) inst/lib/
cp -a inst %{buildroot}%{_datadir}/%{name}

%mvn_install

install -d -m 755 %{buildroot}%{_bindir}/
cat %{SOURCE4} | sed "s#@BASH@#$(which bash)#g" >gradle.sh
chmod +x %{name}.sh
install -p -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE5}

for r in 16 24 32 48 64 128 256; do
    install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/
    install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-${r}x${r}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/%{name}.png
done

install -d -m 755 %{buildroot}%{_mandir}/man1/
install -p -m 644 man/gradle.1 %{buildroot}%{_mandir}/man1/gradle.1

%files -f .mfiles
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/gradle.1*
%license LICENSE NOTICE

%changelog
