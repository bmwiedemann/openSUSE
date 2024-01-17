#
# spec file for package os-maven-plugin
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


Name:           os-maven-plugin
Version:        1.7.0
Release:        0
Summary:        Maven plugin for generating platform-dependent properties
License:        Apache-2.0
URL:            https://github.com/trustin/os-maven-plugin/
Source0:        https://github.com/trustin/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:         0001-Don-t-fail-on-unknown-arch.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
os-maven-plugin is a Maven extension/plugin that generates various
useful platform-dependent project properties normalized from
${os.name} and ${os.arch}.

${os.name} and ${os.arch} are often subtly different between JVM and
operating system versions or they sometimes contain machine-unfriendly
characters such as whitespaces. This plugin tries to remove such
fragmentation so that you can determine the current operating system
and architecture reliably.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch0 -p1

# Remove Eclipse plugin
%pom_remove_dep org.eclipse:ui
%pom_remove_plugin :maven-jar-plugin
find -name EclipseStartup.java -delete
find -name plugin.xml -delete

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

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
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
