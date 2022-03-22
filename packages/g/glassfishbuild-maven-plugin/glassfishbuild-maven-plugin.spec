#
# spec file for package glassfishbuild-maven-plugin
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


Name:           glassfishbuild-maven-plugin
Version:        3.2.26
Release:        0
Summary:        GlassFishBuild Maven Plugin
License:        CDDL-1.1 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Documentation/HTML
URL:            https://javaee.github.io/glassfish
Source0:        https://github.com/javaee/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         glassfishbuild-maven-plugin-3.2.26-maven-resolver-3.5.0.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildArch:      noarch

%description
This plugin provides custom goals used by the GlassFish project build.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q
%patch0 -p1
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin

%pom_xpath_set "pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.8
%pom_xpath_set "pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.8

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
