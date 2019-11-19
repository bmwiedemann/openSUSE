#
# spec file for package groovy
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


Name:           groovy
Version:        2.4.8
Release:        0
Summary:        Dynamic language for the Java Platform
License:        Apache-2.0 AND BSD-3-Clause AND EPL-1.0 AND SUSE-Public-Domain AND CC-BY-2.5
Group:          Development/Libraries/Java
URL:            http://groovy-lang.org
Source0:        https://dl.bintray.com/groovy/maven/apache-groovy-src-%{version}.zip
Source1:        groovy-script.sh
Source3:        groovy.desktop
Source4:        cpl-v10.txt
Source5:        epl-v10.txt
Source6:        http://central.maven.org/maven2/org/codehaus/groovy/groovy-all/%{version}/groovy-all-%{version}.pom
Patch0:         0001-Port-to-Servlet-API-3.1.patch
Patch1:         0002-Gradle-local-mode.patch
Patch2:         0003-Bintray.patch
Patch3:         0004-Remove-android-support.patch
Patch4:         0005-Update-to-QDox-2.0.patch
Patch5:         0006-Disable-artifactory-publish.patch
Patch6:         0007-Fix-missing-extension-definitions.patch
Patch7:         groovy-overview.patch
BuildRequires:  ant
BuildRequires:  ant-antlr
BuildRequires:  antlr
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-collections
BuildRequires:  apache-ivy
BuildRequires:  apache-parent
BuildRequires:  aqute-bnd
BuildRequires:  asm3
BuildRequires:  bsf
BuildRequires:  desktop-file-utils
BuildRequires:  glassfish-el-api
BuildRequires:  glassfish-jsp-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  gradle-local >= 2.1-0.9
BuildRequires:  jansi
BuildRequires:  jarjar
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  jline
BuildRequires:  junit
BuildRequires:  multiverse
BuildRequires:  qdox
BuildRequires:  testng
BuildRequires:  unzip
BuildRequires:  xmvn-subst
BuildRequires:  xstream
BuildRequires:  mvn(javax.servlet:jsp-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.codehaus.gpars:gpars)
Requires:       %{name}-ant = %{version}-%{release}
Requires:       %{name}-bsf = %{version}-%{release}
Requires:       %{name}-console = %{version}-%{release}
Requires:       %{name}-docgenerator = %{version}-%{release}
Requires:       %{name}-groovydoc = %{version}-%{release}
Requires:       %{name}-groovysh = %{version}-%{release}
Requires:       %{name}-jmx = %{version}-%{release}
Requires:       %{name}-json = %{version}-%{release}
Requires:       %{name}-jsr223 = %{version}-%{release}
Requires:       %{name}-lib = %{version}-%{release}
Requires:       %{name}-nio = %{version}-%{release}
Requires:       %{name}-servlet = %{version}-%{release}
Requires:       %{name}-sql = %{version}-%{release}
Requires:       %{name}-swing = %{version}-%{release}
Requires:       %{name}-templates = %{version}-%{release}
Requires:       %{name}-test = %{version}-%{release}
Requires:       %{name}-testng = %{version}-%{release}
Requires:       %{name}-xml = %{version}-%{release}
# optional in pom.xml, but present in upstream binary tarball
Requires:       xpp3-minimal
BuildConflicts: java-devel >= 9
#!BuildRequires: eclipse-platform gradle-bootstrap groovy-bootstrap gpars
BuildArch:      noarch

%description
Groovy is an agile and dynamic language for the Java Virtual Machine,
built upon Java with features inspired by languages like Python, Ruby and
Smalltalk.  It seamlessly integrates with all existing Java objects and
libraries and compiles straight to Java bytecode so you can use it anywhere
you can use Java.

%package lib
Summary:        Groovy JAR artifact
Group:          Development/Libraries/Java
Obsoletes:      %{name}-bootstrap
Requires:       gpars

%description lib
This package contains Groovy JAR artifact.

%package ant
Summary:        ant module for %{name}
Group:          Development/Libraries/Java

%description ant
ant module for %{name}.

%package bsf
Summary:        bsf module for %{name}
Group:          Development/Libraries/Java

%description bsf
bsf module for %{name}.

%package console
Summary:        console module for %{name}
Group:          Development/Libraries/Java

%description console
console module for %{name}.

%package docgenerator
Summary:        docgenerator module for %{name}
Group:          Development/Libraries/Java

%description docgenerator
docgenerator module for %{name}.

%package groovydoc
Summary:        groovydoc module for %{name}
Group:          Development/Libraries/Java

%description groovydoc
groovydoc module for %{name}.

%package groovysh
Summary:        groovysh module for %{name}
Group:          Development/Libraries/Java

%description groovysh
groovysh module for %{name}.

%package jmx
Summary:        jmx module for %{name}
Group:          Development/Libraries/Java

%description jmx
jmx module for %{name}.

%package json
Summary:        json module for %{name}
Group:          Development/Libraries/Java

%description json
json module for %{name}.

%package jsr223
Summary:        jsr223 module for %{name}
Group:          Development/Libraries/Java

%description jsr223
jsr223 module for %{name}.

%package nio
Summary:        nio module for %{name}
Group:          Development/Libraries/Java

%description nio
nio module for %{name}.

%package servlet
Summary:        servlet module for %{name}
Group:          Development/Libraries/Java

%description servlet
servlet module for %{name}.

%package sql
Summary:        sql module for %{name}
Group:          Development/Libraries/Java

%description sql
sql module for %{name}.

%package swing
Summary:        swing module for %{name}
Group:          Development/Libraries/Java

%description swing
swing module for %{name}.

%package templates
Summary:        templates module for %{name}
Group:          Development/Libraries/Java

%description templates
templates module for %{name}.

%package test
Summary:        test module for %{name}
Group:          Development/Libraries/Java

%description test
test module for %{name}.

%package testng
Summary:        testng module for %{name}
Group:          Development/Libraries/Java

%description testng
testng module for %{name}.

%package xml
Summary:        xml module for %{name}
Group:          Development/Libraries/Java

%description xml
xml module for %{name}.

%prep
%setup -q
cp %{SOURCE4} %{SOURCE5} .
# Remove bundled JARs and classes
find \( -name *.jar -o -name *.class \) -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%{mvn_package} ':groovy::indy:'
%{mvn_package} ':groovy-{*}' @1
%{mvn_package} ':groovy-{*}::indy:' @1

%build
%{gradle_build} -f -G jarAll -- -x javadoc -Pindy=true
%{gradle_build} -f -G distBin -- -x javadoc -x jarAllWithIndy

%install
%{mvn_artifact} %{SOURCE6} target/libs/groovy-all-%{version}-indy.jar
%mvn_install

unzip -o target/distributions/apache-groovy-binary-%{version}.zip
rm -rf groovy-%{version}/{*LICENSE.txt,NOTICE.txt,bin/*.bat,META-INF}
install -d -m 755 %{buildroot}%{_datadir}/
cp -a groovy-%{version} %{buildroot}%{_datadir}/%{name}

for mod in groovy groovy-ant groovy-bsf groovy-console groovy-docgenerator \
           groovy-groovydoc groovy-groovysh groovy-jmx groovy-json \
           groovy-jsr223 groovy-nio groovy-servlet groovy-sql groovy-swing \
           groovy-templates groovy-test groovy-testng groovy-xml; do
    ln -sf ../../java/%{name}/$mod.jar %{buildroot}%{_datadir}/%{name}/lib/$mod-%{version}.jar
    ln -sf ../../java/%{name}/$mod-indy.jar %{buildroot}%{_datadir}/%{name}/indy/$mod-%{version}.jar
done

ln -sf ../../java/%{name}/groovy-all.jar %{buildroot}%{_datadir}/%{name}/embeddable/groovy-all-%{version}.jar
ln -sf ../../java/%{name}/groovy-all.jar %{buildroot}%{_datadir}/%{name}/embeddable/groovy-all-%{version}-indy.jar

find %{buildroot}%{_datadir}/%{name}/lib/ ! -name "groovy*" -type f -print -delete
xmvn-subst %{buildroot}%{_datadir}/%{name}/

# $GROOVY_HOME/lib probably contains much more JARs (optional deps?) than is actually needed.
# These extra JARs can cause problems, e.g. rhbz#1184269.
# From that reason, let's symlink needed JARs manually for now.
ln -sf `build-classpath ant/ant` %{buildroot}%{_datadir}/%{name}/lib/ant.jar
ln -sf `build-classpath ant/ant-antlr` %{buildroot}%{_datadir}/%{name}/lib/ant-antlr.jar
ln -sf `build-classpath ant/ant-junit` %{buildroot}%{_datadir}/%{name}/lib/ant-junit.jar
ln -sf `build-classpath ant/ant-launcher` %{buildroot}%{_datadir}/%{name}/lib/ant-launcher.jar
ln -sf `build-classpath bsf` %{buildroot}%{_datadir}/%{name}/lib/bsf.jar
ln -sf `build-classpath commons-cli` %{buildroot}%{_datadir}/%{name}/lib/commons-cli.jar
ln -sf `build-classpath commons-logging` %{buildroot}%{_datadir}/%{name}/lib/commons-logging.jar
#ln -sf `build-classpath gpars/gpars` %{buildroot}%{_datadir}/%{name}/lib/gpars.jar
ln -sf `build-classpath hamcrest/core` %{buildroot}%{_datadir}/%{name}/lib/hamcrest-core.jar
ln -sf `build-classpath apache-ivy/ivy` %{buildroot}%{_datadir}/%{name}/lib/ivy.jar
ln -sf `build-classpath jansi/jansi` %{buildroot}%{_datadir}/%{name}/lib/jansi.jar
ln -sf `build-classpath beust-jcommander` %{buildroot}%{_datadir}/%{name}/lib/jcommander.jar
ln -sf `build-classpath jline/jline` %{buildroot}%{_datadir}/%{name}/lib/jline.jar
ln -sf `build-classpath glassfish-jsp-api` %{buildroot}%{_datadir}/%{name}/lib/jsp-api.jar
# part of JDK7+ (?)
#ln -sf `build-classpath jsr166y` %{buildroot}%{_datadir}/%{name}/lib/jsr166y.jar
ln -sf `build-classpath junit` %{buildroot}%{_datadir}/%{name}/lib/junit.jar
ln -sf `build-classpath multiverse/multiverse-core` %{buildroot}%{_datadir}/%{name}/lib/multiverse-core.jar
# Android support, removed by patch
#ln -sf `build-classpath openbeans` %{buildroot}%{_datadir}/%{name}/lib/openbeans.jar
ln -sf `build-classpath qdox` %{buildroot}%{_datadir}/%{name}/lib/qdox.jar
ln -sf `build-classpath glassfish-servlet-api` %{buildroot}%{_datadir}/%{name}/lib/servlet-api.jar
ln -sf `build-classpath testng` %{buildroot}%{_datadir}/%{name}/lib/testng.jar
ln -sf `build-classpath xpp3-minimal` %{buildroot}%{_datadir}/%{name}/lib/xpp3-minimal.jar
ln -sf `build-classpath xstream/xstream` %{buildroot}%{_datadir}/%{name}/lib/xstream.jar
# upstream bundles extra166y in gpars
#ln -sf `build-classpath extra166y` %{buildroot}%{_datadir}/%{name}/lib/extra166y.jar

# Startup scripts
install -d -m 755 %{buildroot}%{_bindir}/
for cmd in grape groovy groovyc groovyConsole groovydoc groovysh java2groovy; do
    class=$(awk '/^startGroovy/{print$2}' %{buildroot}%{_datadir}/%{name}/bin/$cmd)
    install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/$cmd
    sed -i "s/@CLASS@/$class/" %{buildroot}%{_bindir}/$cmd
    ln -sf %{_bindir}/$cmd %{buildroot}%{_datadir}/%{name}/bin/$cmd
done

# Configuration
install -d -m 755 %{buildroot}%{_sysconfdir}/
mv %{buildroot}%{_datadir}/%{name}/conf/groovy-starter.conf %{buildroot}%{_sysconfdir}/
ln -s %{_sysconfdir}/groovy-starter.conf %{buildroot}%{_datadir}/%{name}/conf/

# Desktop icon
install -d %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/applications
install -p -m644 subprojects/groovy-console/src/main/resources/groovy/ui/ConsoleIcon.png \
        %{buildroot}%{_datadir}/pixmaps/groovy.png
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE3}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
SentUpstream: No public bugtracker
-->
<application>
  <id type="desktop">groovy.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Interactive console for the Groovy programming language</summary>
  <description>
    <p>
      Groovy is a dynamic programming language that is commonly used as a
      scripting language for the Java platform. This application provides an
      interactive console for evaluating scripts in the Groovy language.
    </p>
  </description>
  <url type="homepage">http://groovy-lang.org/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/groovy/a.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
  -->
</application>
EOF

%files
%{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%config(noreplace) %{_sysconfdir}/*

%files lib -f .mfiles -f .mfiles-all
%license LICENSE
%doc NOTICE README.adoc

%files ant -f .mfiles-ant

%files bsf -f .mfiles-bsf

%files console -f .mfiles-console

%files docgenerator -f .mfiles-docgenerator

%files groovydoc -f .mfiles-groovydoc

%files groovysh -f .mfiles-groovysh

%files jmx -f .mfiles-jmx

%files json -f .mfiles-json

%files jsr223 -f .mfiles-jsr223

%files nio -f .mfiles-nio

%files servlet -f .mfiles-servlet

%files sql -f .mfiles-sql

%files swing -f .mfiles-swing

%files templates -f .mfiles-templates

%files test -f .mfiles-test

%files testng -f .mfiles-testng

%files xml -f .mfiles-xml

%changelog
