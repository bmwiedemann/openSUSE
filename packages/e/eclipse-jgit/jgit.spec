#
# spec file for package jgit
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


%global gittag 5.1.3.201810200350-r
Name:           jgit
Version:        5.1.3
Release:        0
Summary:        Java-based command line Git interface
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/egit/
# Use github mirror for now, see: https://bugs.eclipse.org/bugs/show_bug.cgi?id=522144
Source0:        https://github.com/eclipse/jgit/archive/v%{gittag}/jgit-v%{gittag}.tar.gz
Patch0:         fix_jgit_sh.patch
# Change how feature deps are specified, to avoid embedding versions
Patch1:         jgit-feature-deps.patch
# For main build
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.googlecode.javaewah:JavaEWAH)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.tukaani:xz)
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
%setup -q -n %{name}-%{gittag}

%patch0
%patch1

# Disable multithreaded build
rm .mvn/maven.config

# Disable "errorprone" compiler
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution[pom:id='compile-with-errorprone']" pom.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution[pom:id='default-compile']/pom:configuration" pom.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:dependencies" pom.xml

# Use newer Felix dep
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core

# Remove unnecessary plugins for RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-enforcer-plugin
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
install -dm 755 %{buildroot}%{_bindir}
install -m 755 org.eclipse.jgit.pgm/jgit.sh %{buildroot}%{_bindir}/jgit

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
