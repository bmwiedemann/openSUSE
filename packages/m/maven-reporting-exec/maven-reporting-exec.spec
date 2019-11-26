#
# spec file for package maven-reporting-exec
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


Name:           maven-reporting-exec
Version:        1.4
Release:        0
Summary:        Classes to manage report plugin executions with Maven 3
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/shared/maven-reporting-exec/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/reporting/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0001:      0001-Port-to-Eclipse-Aether-and-Eclipse-Sisu.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
Requires:       java-headless
BuildArch:      noarch

%description
Classes to manage and configure report plugin executions with Maven 3.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
The API documentation of %{name}.

%prep
%setup -q
%patch0001 -p1

# convert CR+LF to LF
sed -i 's/\r//g' pom.xml src/main/java/org/apache/maven/reporting/exec/*

%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin

# Build against Maven 3.x, Eclipse Aether and Eclipse Sisu
%pom_remove_dep org.sonatype.aether:aether-api
%pom_remove_dep org.sonatype.aether:aether-util
%pom_change_dep org.sonatype.aether:aether-connector-wagon org.eclipse.aether:aether-transport-wagon
%pom_change_dep org.sonatype.sisu:sisu-inject-plexus org.eclipse.sisu:org.eclipse.sisu.plexus

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
