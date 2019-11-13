#
# spec file for package os-maven-plugin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global vertag Final
Name:           os-maven-plugin
Version:        1.2.3
Release:        0
Summary:        Maven plugin for generating platform-dependent properties
License:        Apache-2.0
URL:            https://github.com/trustin/os-maven-plugin/
Source0:        https://github.com/trustin/%{name}/archive/%{name}-%{version}.Final.tar.gz
Patch0:         0001-Port-to-current-plexus-utils.patch
Patch1:         0002-Don-t-fail-on-unknown-arch.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
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
%setup -q -n %{name}-%{name}-%{version}.%{vertag}

%patch0 -p1
%patch1 -p1

# Remove Eclipse plugin
%pom_remove_dep org.eclipse:ui
%pom_remove_plugin :maven-jar-plugin
find -name EclipseStartup.java -delete
find -name plugin.xml -delete

%build
%{mvn_build} -f -- -Dsource=6

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
