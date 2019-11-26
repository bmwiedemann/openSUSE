#
# spec file for package gmavenplus-plugin
#
# Copyright (c) 2019 SUSE LLC
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


Name:           gmavenplus-plugin
Version:        1.5
Release:        0
Summary:        Integrates Groovy into Maven projects
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://groovy.github.io/GMavenPlus/
Source0:        https://github.com/groovy/GMavenPlus/archive/%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(jline:jline)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-plugin-registry)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus:codehaus-parent:pom:)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildArch:      noarch

%description
GMavenPlus is a rewrite of GMaven, a Maven plugin
that allows you to integrate Groovy into your
Maven projects.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n GMavenPlus-%{version}

%pom_remove_plugin :maven-clean-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-help-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-site-plugin

%pom_xpath_remove "pom:build/pom:extensions"
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

# Mockito cannot mock this class: class org.codehaus.gmavenplus.mojo.AbstractGroovyMojoTest$TestGroovyMojo
rm -r src/test/java/org/codehaus/gmavenplus/mojo/AbstractGroovyMojoTest.java

# Convert from dos to unix line ending
dos2unix README.markdown

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- -Pnonindy \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.markdown
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
