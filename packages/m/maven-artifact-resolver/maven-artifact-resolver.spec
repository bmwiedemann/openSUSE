#
# spec file for package maven-artifact-resolver
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


Name:           maven-artifact-resolver
Version:        1.0
Release:        0
Summary:        Maven Artifact Resolution API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/shared/%{name}
Source0:        http://central.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Replaced plexus-maven-plugin with plexus-component-metadata
Patch0:         %{name}-plexus.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  unzip
BuildArch:      noarch

%description
Provides a component for plugins to easily resolve project dependencies.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

%pom_xpath_inject pom:project/pom:dependencies "
<dependency>
  <groupId>org.apache.maven</groupId>
  <artifactId>maven-compat</artifactId>
  <version>1.0</version>
</dependency>" pom.xml

# Incompatible method invocation
rm src/test/java/org/apache/maven/shared/artifact/resolver/DefaultProjectDependenciesResolverIT.java

%build
%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc DEPENDENCIES NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
