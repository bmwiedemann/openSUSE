#
# spec file for package maven-scm
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2000-2005, JPackage Project
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


Name:           maven-scm
Version:        1.12.0
Release:        0
Summary:        Common API for doing SCM operations
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/scm
Source0:        http://archive.apache.org/dist/maven/scm/%{name}-%{version}-source-release.zip
# Patch to migrate to new plexus default container
# This has been sent upstream: https://issues.apache.org/jira/browse/SCM-731
Patch0:         maven-scm-1.12.0-sec-dispatcher-2.0.patch
Patch1:         0001-Port-maven-scm-to-latest-version-of-plexus-default.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings:2.2.1)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit.ssh.jsch)
BuildRequires:  mvn(org.sonatype.plexus:plexus-sec-dispatcher)
%ifarch %{ix86}
BuildConflicts: java >= 12
BuildConflicts: java-devel >= 12
BuildConflicts: java-headless >= 12
%endif
#!BuildRequires: jgit
BuildArch:      noarch

%description
Maven SCM supports Maven plugins (e.g. maven-release-plugin) and other
tools (e.g. Continuum) in providing them a common API for doing SCM operations.

%package test
Summary:        Tests for %{name}
Group:          Development/Libraries/Java
Requires:       maven-scm = %{version}-%{release}

%description test
Tests for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

# Remove unnecessary animal sniffer
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%pom_remove_plugin :maven-enforcer-plugin

%pom_change_dep -r :maven-project :maven-compat

# Remove providers-integrity from build (we don't have mks-api)
%pom_disable_module maven-scm-provider-integrity maven-scm-providers

# Partially remove cvs support for removal of netbeans-cvsclient
# It still works with cvsexe provider
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-cvsjava maven-scm-client
%pom_disable_module maven-scm-provider-cvsjava maven-scm-providers/maven-scm-providers-cvs
sed -i s/cvsjava.CvsJava/cvsexe.CvsExe/ maven-scm-client/src/main/resources/META-INF/plexus/components.xml

# Port to commons-lang3
%pom_change_dep -r :commons-lang org.apache.commons:commons-lang3:3.8.1
sed -i "s/org\.apache\.commons\.lang\./org.apache.commons.lang3./" \
    maven-scm-providers/maven-scm-providers-git/maven-scm-provider-gitexe/src/main/java/org/apache/maven/scm/provider/git/gitexe/command/status/GitStatusConsumer.java \
    maven-scm-providers/maven-scm-providers-svn/maven-scm-provider-svnexe/src/main/java/org/apache/maven/scm/provider/svn/svnexe/command/checkout/SvnCheckOutConsumer.java \
    maven-scm-providers/maven-scm-providers-svn/maven-scm-provider-svnexe/src/main/java/org/apache/maven/scm/provider/svn/svnexe/command/remoteinfo/SvnRemoteInfoCommand.java

# Tests are skipped anyways, so remove dependency on mockito.
%pom_remove_dep org.mockito: maven-scm-providers/maven-scm-provider-jazz
%pom_remove_dep org.mockito: maven-scm-providers/maven-scm-provider-accurev

%pom_add_dep org.eclipse.jgit:org.eclipse.jgit.ssh.jsch maven-scm-providers/maven-scm-providers-git/maven-scm-provider-jgit

# Put TCK tests into a separate sub-package
%{mvn_package} :%{name}-provider-cvstest test
%{mvn_package} :%{name}-provider-gittest test
%{mvn_package} :%{name}-provider-svntest test
%{mvn_package} :%{name}-test test

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc NOTICE

%files test -f .mfiles-test
%license LICENSE
%doc NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
