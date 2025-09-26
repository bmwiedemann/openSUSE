#
# spec file for package maven-scm
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        2.2.1
Release:        0
Summary:        Common API for doing SCM operations
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/scm
Source0:        http://archive.apache.org/dist/maven/scm/%{name}-%{version}-source-release.zip
Patch0:         0001-Don-t-depend-on-apache-sshd-test-jars.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(com.google.inject:guice::no_aop:)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-text)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.sshd:sshd-git)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interactivity-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-sec-dispatcher)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit.ssh.apache)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
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
%patch -P 0 -p1

%pom_remove_plugin -r :animal-sniffer-maven-plugin

# Put TCK tests into a separate sub-package
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
