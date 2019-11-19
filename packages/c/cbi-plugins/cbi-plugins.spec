#
# spec file for package cbi-plugins
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


Name:           cbi-plugins
Version:        1.1.5
Release:        0
Summary:        A set of helpers for Eclipse CBI
License:        EPL-1.0
Group:          Development/Libraries/Java
URL:            https://git.eclipse.org/c/cbi/org.eclipse.cbi.git/tree/maven-plugins/README.md
Source0:        https://git.eclipse.org/c/cbi/org.eclipse.cbi.git/snapshot/org.eclipse.cbi-org.eclipse.cbi.maven.plugins_maven-plugin-parent_%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  tycho-bootstrap
BuildRequires:  xz
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.auto.value:auto-value)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(de.pdark:decentxml)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpmime)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
#!BuildIgnore:  tycho
BuildArch:      noarch

%description
A set of helpers for Eclipse CBI.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n org.eclipse.cbi-org.eclipse.cbi.maven.plugins_maven-plugin-parent_%{version}
%pom_disable_module eclipse-macsigner-plugin maven-plugins
%pom_disable_module eclipse-winsigner-plugin maven-plugins

# Disable plugins not needed for RPM builds
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-enforcer-plugin

# We don't have findbugs annotations
%pom_change_dep com.google.code.findbugs: com.google.code.findbugs:jsr305 . maven-plugins/eclipse-flatpak-packager
sed -i -e '/SuppressFBWarnings/d' maven-plugins/eclipse-flatpak-packager/src/main/java/org/eclipse/cbi/maven/plugins/flatpakager/model/Source.java

# Build the common module
%pom_xpath_inject pom:modules "<module>../common/</module>" maven-plugins
%pom_remove_dep org.eclipse.cbi:checkstyle common

# Parent pom and common module are "released" independently, but actually nothing changed yet since last releases
sed -i -e 's/1\.0\.5-SNAPSHOT/1.0.4/' pom.xml
sed -i -e 's/1\.2\.3-SNAPSHOT/1.2.2/' common/pom.xml

%build
# Tests require jimfs which we don't have
%{mvn_build} -f -- -f maven-plugins/pom.xml -Dproject.build.sourceEncoding=UTF-8 -Dsource=1.8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
