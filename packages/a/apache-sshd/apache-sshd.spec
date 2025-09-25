#
# spec file for package apache-sshd
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "extras"
%bcond_without extras
%else
%bcond_with extras
%endif
%global homedir %{_datadir}/apache-sshd
Version:        2.16.0
Release:        0
Summary:        Apache SSHD
# One file has ISC licensing:
#   sshd-common/src/main/java/org/apache/sshd/common/config/keys/loader/openssh/kdf/BCrypt.java
License:        Apache-2.0 AND ISC
Group:          Development/Libraries/Java
URL:            https://mina.apache.org/sshd-project
Source0:        https://archive.apache.org/dist/mina/sshd/%{version}/apache-sshd-%{version}-src.tar.gz
Patch0:         file-name-mapping.patch
Patch1:         password-no-echo.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(net.i2p.crypto:eddsa)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.tomcat:tomcat-jni)
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)
BuildRequires:  mvn(org.apache:apache:pom:) >= 30
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk18on)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk18on)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch
%if %{with extras}
Name:           apache-sshd-%{flavor}
BuildRequires:  xmvn-subst
BuildRequires:  mvn(io.netty:netty-handler)
BuildRequires:  mvn(io.netty:netty-transport)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.sshd:sshd-common) = %{version}
BuildRequires:  mvn(org.apache.sshd:sshd-core) = %{version}
BuildRequires:  mvn(org.apache.sshd:sshd-osgi) = %{version}
BuildRequires:  mvn(org.apache.sshd:sshd-putty) = %{version}
BuildRequires:  mvn(org.apache.sshd:sshd-scp) = %{version}
BuildRequires:  mvn(org.apache.sshd:sshd-sftp) = %{version}
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk18on)
BuildRequires:  mvn(org.bouncycastle:bcutil-jdk18on)
BuildRequires:  mvn(org.c02e.jpgpj:jpgpj)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit.pgm)
BuildRequires:  mvn(org.slf4j:slf4j-jdk14)
#!BuildRequires: jgit
%else
Name:           apache-sshd
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

%description
Apache SSHD is a 100% pure java library to support the SSH protocols on both
the client and server side.

%if %{with extras}
%package -n apache-sshd-standalone
Summary:        Standalone installation of apache-sshd
Requires:       apache-sshd
Requires:       apache-sshd-extras
Requires:       assertj-core
Requires:       bouncycastle
Requires:       bouncycastle-pg
Requires:       bouncycastle-pkix
Requires:       bouncycastle-util
Requires:       byte-buddy
Requires:       ed25519-java
Requires:       javaewah
Requires:       jcl-over-slf4j
Requires:       jctools
Requires:       jgit
Requires:       jpgpj
Requires:       netty
Requires:       objectweb-asm
Requires:       slf4j
Requires:       slf4j-jdk14
Requires:       tomcat-lib

%description -n apache-sshd-standalone
This package provides standalone installation of apache-sshd
%endif

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{name}.

%prep
%setup -q -n apache-sshd-%{version}

%patch -P 0 -p1
%patch -P 1 -p1

%pom_change_dep -r tomcat:tomcat-apr org.apache.tomcat:tomcat-jni

# Avoid unnecessary dep on spring framework
%pom_remove_dep :spring-framework-bom
%pom_remove_dep :testcontainers-bom sshd-sftp sshd-core

# We don't have dependencies for these modules
%pom_disable_module sshd-benchmarks
%pom_disable_module sshd-mina
%pom_remove_dep -r org.apache.sshd:sshd-mina
%pom_disable_module sshd-spring-sftp
%pom_remove_dep -r org.apache.sshd:sshd-spring-sftp
# don't require bom that we don't package
%pom_remove_dep org.testcontainers:testcontainers-bom sshd-scp
%pom_remove_dep :netty-bom sshd-netty

%pom_remove_dep :shared-dsml-parser sshd-ldap

%if %{with extras}
%pom_disable_module sshd-common
%pom_disable_module sshd-core
%pom_disable_module sshd-osgi
%pom_disable_module sshd-putty
%pom_disable_module sshd-scp
%pom_disable_module sshd-sftp
%else
%pom_disable_module sshd-openpgp
%pom_disable_module sshd-netty
%pom_disable_module sshd-ldap
%pom_disable_module sshd-git
%pom_disable_module sshd-contrib
%pom_disable_module sshd-cli
%pom_disable_module assembly
%endif

# Disable plugins we don't need for RPM builds
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :impsort-maven-plugin
%pom_remove_plugin :maven-clean-plugin
%pom_remove_plugin :formatter-maven-plugin . sshd-core

# We only need the unix-bin execution
%pom_xpath_remove "pom:executions/pom:execution[pom:id='unix-src']" assembly
%pom_xpath_remove "pom:executions/pom:execution[pom:id='windows-bin']" assembly
%pom_xpath_remove "pom:executions/pom:execution[pom:id='windows-src']" assembly

# Suppress generation of uses clauses
%pom_xpath_inject "pom:configuration/pom:instructions" "<_nouses>true</_nouses>" .

%pom_remove_plugin :maven-antrun-plugin sshd-osgi

%{mvn_file} :{*} apache-sshd/@1

%{mvn_package} :sshd __noinstall
%{mvn_package} :apache-sshd __noinstall

%build
# Can't run tests, they require ch.ethz.ganymed:ganymed-ssh2
%{mvn_build} -f -- -Dworkspace.root.dir=$(pwd) \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%if %{with extras}
mkdir sshd_home
(cd sshd_home
    tar --delay-directory-restore -xvf \
        ../assembly/target/apache-sshd-%{version}.tar.gz
)
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%if %{with extras}
export SSHD_HOME=$(pwd)/sshd_home/apache-sshd-%{version}
rm $SSHD_HOME/bin/*.bat

install -d -m 0755 %{buildroot}%{homedir}
cp -a $SSHD_HOME/{bin,dependencies,extras,lib} %{buildroot}%{homedir}/
xmvn-subst -s -R %{buildroot} %{buildroot}%{homedir}
%endif

%files -f .mfiles
%doc CHANGES.md
%license LICENSE.txt NOTICE.txt assembly/src/main/legal/licenses/jbcrypt.txt

%if %{with extras}
%files -n apache-sshd-standalone
%{homedir}
%endif

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt assembly/src/main/legal/licenses/jbcrypt.txt

%changelog
