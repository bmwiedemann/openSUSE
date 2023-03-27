#
# spec file for package eclipse-jgit
#
# Copyright (c) 2023 SUSE LLC
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
%define __provides_exclude osgi*
Name:           eclipse-jgit
Version:        5.11.0
Release:        0
Summary:        Eclipse JGit
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/egit/
Source0:        https://git.eclipse.org/c/jgit/jgit.git/snapshot/jgit-%{gittag}.tar.xz
# Set the correct classpath for the command line tools
Patch0:         0001-Ensure-the-correct-classpath-is-set-for-the-jgit-com.patch
# Switch to feature requirements for third-party bundles, also makes the following changes:
#  javaewah -> com.googlecode.javaewah.JavaEWAH
#  org.slf4j.api -> slf4j.api
#  org.slf4j.impl.log4j12 -> slf4j.simple
Patch1:         0002-Don-t-embed-versions-of-third-party-libs-use-feature.patch
Patch2:         jgit-shade.patch
Patch3:         jgit-5.11.0-java8.patch
Patch4:         jgit-apache-sshd-2.7.0.patch
# For main build
BuildRequires:  ant
BuildRequires:  apache-commons-compress
BuildRequires:  apache-sshd >= 2.7
BuildRequires:  args4j
BuildRequires:  bouncycastle
BuildRequires:  bouncycastle-pg
BuildRequires:  bouncycastle-pkix
BuildRequires:  eclipse-platform-bootstrap
BuildRequires:  ed25519-java
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  google-gson
BuildRequires:  hamcrest-core
BuildRequires:  javaewah
BuildRequires:  jgit = %{version}
BuildRequires:  junit
BuildRequires:  jzlib
BuildRequires:  maven-local
BuildRequires:  slf4j
BuildRequires:  tycho
BuildRequires:  xml-commons-apis
BuildRequires:  xmvn-subst
BuildConflicts: java >= 12
BuildConflicts: java-devel >= 12
BuildConflicts: java-headless >= 12
#!BuildIgnore:  eclipse-platform
#!BuildIgnore:  tycho-bootstrap
#!BuildRequires: eclipse-emf-core eclipse-ecf-core
Requires:       apache-commons-compress
Requires:       apache-sshd >= 2.7
Requires:       args4j
Requires:       bouncycastle
Requires:       bouncycastle-pg
Requires:       bouncycastle-pkix
Requires:       ed25519-java
Requires:       google-gson
Requires:       hamcrest-core
Requires:       javaewah
Requires:       jgit = %{version}
Requires:       junit
Requires:       jzlib
Requires:       slf4j
Requires:       xml-commons-apis
BuildArch:      noarch
# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch:    s390 %{arm} %{ix86}

%description
A pure Java implementation of the Git version control system.

%prep
%setup -q -n jgit-%{gittag}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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

pushd org.eclipse.jgit.packaging
%{mvn_package} "::pom::" __noinstall
popd

%build
pushd org.eclipse.jgit.packaging
%{mvn_build} -j -f
popd

%install
pushd org.eclipse.jgit.packaging
%mvn_install
popd
xmvn-subst -R %{buildroot} %{_datadir}/eclipse/droplets/jgit
#%fdupes -s %{buildroot}%{_datadir}

%files -f org.eclipse.jgit.packaging/.mfiles
%license LICENSE
%doc README.md

%changelog
