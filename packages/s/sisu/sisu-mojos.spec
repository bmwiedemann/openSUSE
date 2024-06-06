#
# spec file for package sisu-mojos
#
# Copyright (c) 2024 SUSE LLC
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


%global reltype milestones
Name:           sisu-mojos
Version:        0.9.0.M3
Release:        0
Summary:        Sisu plugin for Apache Maven
License:        EPL-1.0 AND EPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/sisu
Source0:        https://github.com/eclipse-sisu/sisu-project/archive/refs/tags/%{reltype}/%{version}.tar.gz#/sisu-project-%{version}.tar.gz
Patch1:         sisu-no-dependency-on-glassfish-servlet-api.patch
Patch3:         sisu-osgi-api.patch
Patch4:         sisu-reproducible-index.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject) >= %{version}
BuildRequires:  mvn(org.slf4j:slf4j-nop)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
#!BuildIgnore:  maven-javadoc-plugin
#!BuildIgnore:  maven-javadoc-plugin-bootstrap
BuildArch:      noarch

%description
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n sisu-project-%{reltype}-%{version}

%patch -P 1 -p1
%patch -P 3 -p1
%patch -P 4 -p2

%pom_remove_plugin -r :maven-enforcer-plugin
# it is scope "import" but used only for tests that we don't run
%pom_remove_dep :junit-bom

pushd org.eclipse.sisu.mojos
%pom_add_dep org.eclipse.sisu:org.eclipse.sisu.plexus:%{version}
%pom_add_plugin org.apache.maven.plugins:maven-resources-plugin:3.3.1
%{mvn_alias} : org.sonatype.plugins:
popd

%build
pushd org.eclipse.sisu.mojos
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8
popd

%install
pushd org.eclipse.sisu.mojos
%mvn_install
popd
%fdupes -s %{buildroot}%{_javadocdir}

%files -f org.eclipse.sisu.mojos/.mfiles
%dir %{_javadir}/%{name}
%license LICENSE.txt

%files javadoc -f org.eclipse.sisu.mojos/.mfiles-javadoc
%license LICENSE.txt

%changelog
