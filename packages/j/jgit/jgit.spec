#
# spec file for package jgit
#
# Copyright (c) 2025 SUSE LLC
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


%global gittag 5.11.0.202103091610-r
Name:           jgit
Version:        5.11.0
Release:        0
Summary:        Eclipse JGit
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/egit/
# Use github mirror for now, see: https://bugs.eclipse.org/bugs/show_bug.cgi?id=522144
Source0:        https://git.eclipse.org/c/jgit/jgit.git/snapshot/jgit-%{gittag}.tar.xz
# Set the correct classpath for the command line tools
# Switch to feature requirements for third-party bundles, also makes the following changes:
#  javaewah -> com.googlecode.javaewah.JavaEWAH
#  org.slf4j.api -> slf4j.api
#  org.slf4j.impl.log4j12 -> slf4j.simple
Patch1:         0002-Don-t-embed-versions-of-third-party-libs-use-feature.patch
Patch2:         jgit-shade.patch
Patch3:         jgit-5.11.0-java8.patch
Patch4:         jgit-apache-sshd.patch
Patch5:         jgit-jsch.patch
Patch6:         jgit-CVE-2023-4759.patch
Patch7:         jgit-bc-179.patch
Patch8:         javax-servlet-api-4.patch
Patch9:         jgit-CVE-2025-4949.patch
# For main build
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.googlecode.javaewah:JavaEWAH)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.i2p.crypto:eddsa)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.sshd:sshd-osgi) >= 2.4
BuildRequires:  mvn(org.apache.sshd:sshd-sftp) >= 2.4
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.tukaani:xz)
# All the jars that need to be on the classpath for the script to work
Requires:       apache-commons-codec
Requires:       apache-commons-compress
Requires:       apache-commons-logging
Requires:       apache-sshd
Requires:       args4j
Requires:       ed25519-java
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       javaewah
Requires:       javapackages-tools
Requires:       jsch
Requires:       jzlib
Requires:       slf4j
Requires:       xz-java
Obsoletes:      %{name}-bootstrap
BuildArch:      noarch

%description
Command line Git tool built entirely in Java.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n jgit-%{gittag}

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1

# Disable multithreaded build
rm .mvn/maven.config

# Don't try to get deps from local *maven* repo, use tycho resolved ones
for p in $(find org.eclipse.jgit.packaging -name pom.xml) ; do
  grep -q dependencies $p && %pom_xpath_remove "pom:dependencies" $p
done

# Disable "errorprone" compiler
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:compilerArgs" pom.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:annotationProcessorPaths" pom.xml

# Don't need target platform or repository modules with xmvn
%pom_disable_module org.eclipse.jgit.target org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.repository org.eclipse.jgit.packaging
%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin/pom:configuration/pom:target" org.eclipse.jgit.packaging/pom.xml

# Don't build source features
%pom_disable_module org.eclipse.jgit.source.feature org.eclipse.jgit.packaging

# Don't build benchmark and coverage
%pom_disable_module org.eclipse.jgit.benchmarks
%pom_disable_module org.eclipse.jgit.coverage

# Use newer Felix dep
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core

# Remove unnecessary plugins for RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-enforcer-plugin org.eclipse.jgit.packaging
%pom_remove_plugin -r :japicmp-maven-plugin

# Don't attach shell script artifact
%pom_remove_plugin org.codehaus.mojo:build-helper-maven-plugin org.eclipse.jgit.pgm

# Remove org.apache.log4j
%pom_remove_dep log4j:log4j . org.eclipse.jgit.pgm
%pom_change_dep org.slf4j:slf4j-log4j12 org.slf4j:slf4j-simple . org.eclipse.jgit.pgm

%{mvn_package} ":*.test" __noinstall

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Pjavac

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

# Binary
%jpackage_script org.eclipse.jgit.pgm.Main "" "" javaewah:jzlib:jsch:jgit:slf4j/api:slf4j/simple:args4j:commons-compress:httpcomponents/httpcore:httpcomponents/httpclient:commons-logging:commons-codec:eddsa:apache-sshd/sshd-osgi:apache-sshd/sshd-sftp %{name}

# Ant task configuration
install -dm 755 %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/jgit <<EOF
javaewah jzlib jsch jgit/org.eclipse.jgit jgit/org.eclipse.jgit.ant slf4j/slf4j-api slf4j/slf4j-simple httpcomponents/httpcore httpcomponents/httpclient commons-logging commons-codec
EOF

%files -f .mfiles
%license LICENSE
%doc README.md
%{_bindir}/jgit
%config(noreplace) %{_sysconfdir}/ant.d/jgit

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
