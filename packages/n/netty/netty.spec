#
# spec file for package netty
#
# Copyright (c) 2021 SUSE LLC
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


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:           netty
Version:        4.1.60
Release:        0
Summary:        An asynchronous event-driven network application framework and tools for Java
License:        Apache-2.0
URL:            https://netty.io/
Source0:        https://github.com/netty/netty/archive/netty-%{namedversion}.tar.gz
# Upsteam uses a simple template generator script written in groovy and run with gmaven
# We don't have the plugin and want to avoid groovy dependency
# This script is written in bash+sed and performs the same task
Source1:        codegen.bash
Patch0:         0001-Remove-optional-dep-Blockhound.patch
Patch1:         0002-Remove-optional-dep-conscrypt.patch
Patch2:         0003-Remove-optional-deps-jetty-alpn-and-npn.patch
Patch3:         0004-Remove-optional-dep-tcnative.patch
Patch4:         0005-Remove-optional-dep-log4j.patch
Patch5:         0006-revert-Fix-native-image-build.patch
Patch6:         0007-Revert-Support-session-cache-for-client-and-server-w.patch
Patch7:         no-werror.patch
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(io.netty:netty-jni-util::sources:)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.fusesource.hawtjni:maven-hawtjni-plugin)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)

%description
Netty is a NIO client server framework which enables quick and easy
development of network applications such as protocol servers and
clients. It greatly simplifies and streamlines network programming
such as TCP and UDP socket server.

'Quick and easy' doesn't mean that a resulting application will suffer
from a maintainability or a performance issue. Netty has been designed
carefully with the experiences earned from the implementation of a lot
of protocols such as FTP, SMTP, HTTP, and various binary and
text-based legacy protocols. As a result, Netty has succeeded to find
a way to achieve ease of development, performance, stability, and
flexibility without a compromise.

%package poms
Summary:        POM-only artifacts for %{name}
BuildArch:      noarch

%description poms
%{summary}.

%package javadoc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description javadoc
%{summary}.

%prep
%setup -q -n netty-netty-%{namedversion}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# remove unnecessary dependency on parent POM
%pom_remove_parent . bom dev-tools

# Disable all in one jar
%pom_disable_module all

# Not needed for RPM builds
%pom_disable_module "example"
%pom_disable_module "tarball"
%pom_disable_module "microbench"

%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-remote-resources-plugin"]' '
<dependencies>
<dependency>
<groupId>io.netty</groupId>
<artifactId>netty-dev-tools</artifactId>
<version>${project.version}</version>
</dependency>
</dependencies>'

%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :xml-maven-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-clean-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-jxr-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :forbiddenapis

cp %{SOURCE1} common/codegen.bash
chmod +x common/codegen.bash
%pom_add_plugin org.codehaus.mojo:exec-maven-plugin common '
<executions>
    <execution>
        <id>generate-collections</id>
        <phase>generate-sources</phase>
        <goals>
            <goal>exec</goal>
        </goals>
        <configuration>
            <executable>common/codegen.bash</executable>
        </configuration>
    </execution>
</executions>
'
%pom_remove_plugin :groovy-maven-plugin common

# We don't have com.oracle.substratevm
%pom_remove_dep "com.oracle.substratevm:" common
rm common/src/main/java/io/netty/util/internal/svm/*

# The protobuf-javanano API was discontinued upstream
# so disable support for protobuf in the codecs module
%pom_remove_dep -r "com.google.protobuf:protobuf-java"
%pom_remove_dep -r "com.google.protobuf.nano:protobuf-javanano"
rm codec/src/main/java/io/netty/handler/codec/protobuf/*
sed -i '/import.*protobuf/d' codec/src/main/java/io/netty/handler/codec/DatagramPacket*.java

%pom_remove_dep -r "org.jboss.marshalling:jboss-marshalling"
rm codec/src/main/java/io/netty/handler/codec/marshalling/*

# Various compression codecs
%pom_remove_dep -r com.github.jponge:lzma-java
rm codec/src/*/java/io/netty/handler/codec/compression/Lzma*.java
%pom_remove_dep -r com.ning:compress-lzf
rm codec/src/*/java/io/netty/handler/codec/compression/Lzf*.java
%pom_remove_dep -r net.jpountz.lz4:lz4
rm codec/src/*/java/io/netty/handler/codec/compression/Lz4*.java

# Disable other codecs with extra dependencies
%pom_remove_dep -r com.fasterxml:aalto-xml
%pom_disable_module codec-xml

# Disable unneeded transport artifacts
%pom_disable_module transport-native-epoll
%pom_disable_module transport-native-kqueue
%pom_disable_module transport-rxtx
%pom_disable_module transport-sctp
%pom_disable_module transport-udt

# Disable macos native bit
%pom_disable_module resolver-dns-native-macos

# Disable test suites
%pom_disable_module testsuite
%pom_disable_module testsuite-autobahn
%pom_disable_module testsuite-http2
%pom_disable_module testsuite-native
%pom_disable_module testsuite-native-image
%pom_disable_module testsuite-osgi
%pom_disable_module testsuite-shading
%pom_disable_module transport-native-unix-common-tests

# Upstream has jctools bundled.
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution[pom:id = 'generate-manifest']/pom:configuration/pom:instructions/pom:Import-Package" common/pom.xml

# Tell xmvn to install attached artifact, which it does not
# do by default. In this case install all attached artifacts with
# the linux classifier.
%{mvn_package} ":::linux*:"

%{mvn_package} ":netty-parent" poms
%{mvn_package} ":netty-bom" poms

%{mvn_package} ':*-tests' __noinstall

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files poms -f .mfiles-poms
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
