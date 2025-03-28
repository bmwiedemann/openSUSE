#
# spec file for package cbi-plugins
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


Name:           cbi-plugins
Version:        1.1.5
Release:        0
Summary:        A set of helpers for Eclipse CBI
License:        EPL-1.0
Group:          Development/Libraries/Java
URL:            https://github.com/eclipse-cbi/org.eclipse.cbi/blob/main/maven-plugins/README.md
Source0:        https://github.com/eclipse-cbi/org.eclipse.cbi/archive/refs/tags/org.eclipse.cbi.maven.plugins_maven-plugin-parent_%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  tycho-bootstrap
BuildRequires:  xz
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.auto.value:auto-value)
BuildRequires:  mvn(com.google.auto.value:auto-value-annotations)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava)
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
# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch:    s390 %{arm} %{ix86}

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
%pom_remove_dep com.google.code.findbugs:findbugs-annotations maven-plugins/eclipse-flatpak-packager
sed -i -e '/SuppressFBWarnings/d' maven-plugins/eclipse-flatpak-packager/src/main/java/org/eclipse/cbi/maven/plugins/flatpakager/model/Source.java

# Build the common module
%pom_xpath_inject pom:modules "<module>../common/</module>" maven-plugins
%pom_remove_dep org.eclipse.cbi:checkstyle common
%pom_add_dep com.google.auto.value:auto-value-annotations:1.6 common

# Parent pom and common module are "released" independently, but actually nothing changed yet since last releases
sed -i -e 's/1\.0\.5-SNAPSHOT/1.0.4/' pom.xml
sed -i -e 's/1\.2\.3-SNAPSHOT/1.2.2/' common/pom.xml

for i in eclipse-winsigner eclipse-jarsigner eclipse-macsigner eclipse-cbi;
do
  %pom_add_plugin org.apache.maven.plugins:maven-plugin-plugin maven-plugins/${i}-plugin "
    <configuration>
      <goalPrefix>${i}</goalPrefix>
    </configuration>"
done
for i in eclipse-dmg-packager eclipse-flatpak-packager;
do
  %pom_add_plugin org.apache.maven.plugins:maven-plugin-plugin maven-plugins/${i} "
    <configuration>
      <goalPrefix>${i}</goalPrefix>
    </configuration>"
done

%build
pushd maven-plugins
%{mvn_build} -f -- \
    -Dproject.build.sourceEncoding=UTF-8 -Dsource=1.8
popd

%install
pushd maven-plugins
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f maven-plugins/.mfiles

%files javadoc -f maven-plugins/.mfiles-javadoc

%changelog
