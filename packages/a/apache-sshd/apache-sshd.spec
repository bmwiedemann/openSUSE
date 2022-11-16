#
# spec file for package apache-sshd
#
# Copyright (c) 2022 SUSE LLC
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


Name:           apache-sshd
Version:        2.9.2
Release:        0
Summary:        Apache SSHD
# One file has ISC licensing:
#   sshd-common/src/main/java/org/apache/sshd/common/config/keys/loader/openssh/kdf/BCrypt.java
License:        Apache-2.0 AND ISC
URL:            https://mina.apache.org/sshd-project
Source0:        https://archive.apache.org/dist/mina/sshd/%{version}/apache-sshd-%{version}-src.tar.gz
# Avoid optional dep on tomcat native APR library
Patch0:         0001-Avoid-optional-dependency-on-native-tomcat-APR-libra.patch
Patch1:         apache-sshd-javadoc.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.i2p.crypto:eddsa)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit47)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
Apache SSHD is a 100% pure java library to support the SSH protocols on both
the client and server side.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{name}.

%prep
%setup -q

# Avoid optional dep on tomcat native APR library
%patch0 -p1
%patch1 -p1

rm -rf sshd-core/src/main/java/org/apache/sshd/agent/unix

# Avoid unnecessary dep on spring framework
%pom_remove_dep :spring-framework-bom
%pom_remove_dep :testcontainers-bom sshd-sftp sshd-core

# Build the core modules only
%pom_disable_module assembly
%pom_disable_module sshd-mina
%pom_disable_module sshd-netty
%pom_disable_module sshd-ldap
%pom_disable_module sshd-git
%pom_disable_module sshd-contrib
%pom_disable_module sshd-spring-sftp
%pom_disable_module sshd-cli
%pom_disable_module sshd-openpgp

# Disable plugins we don't need for RPM builds
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :gmavenplus-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :impsort-maven-plugin
%pom_remove_plugin :formatter-maven-plugin . sshd-core

# Suppress generation of uses clauses
%pom_xpath_inject "pom:configuration/pom:instructions" "<_nouses>true</_nouses>" .

%pom_remove_plugin :maven-antrun-plugin sshd-osgi

%build
# Can't run tests, they require ch.ethz.ganymed:ganymed-ssh2
%{mvn_build} -f -- -Dworkspace.root.dir=$(pwd) \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGES.md
%license LICENSE.txt NOTICE.txt assembly/src/main/legal/licenses/jbcrypt.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt assembly/src/main/legal/licenses/jbcrypt.txt

%changelog
