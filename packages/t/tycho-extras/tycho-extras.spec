#
# spec file for package tycho-extras
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


%global snap %{nil}
Name:           tycho-extras
Version:        1.2.0
Release:        0
Summary:        Additional plugins for Tycho
License:        EPL-1.0
Group:          Development/Libraries/Java
URL:            http://eclipse.org/tycho/
Source0:        http://git.eclipse.org/c/tycho/org.eclipse.tycho.extras.git/snapshot/org.eclipse.tycho.extras-tycho-extras-%{version}.tar.xz
Patch0:         %{name}-fix-build.patch
Patch1:         %{name}-use-custom-resolver.patch
Patch2:         tycho-maven-archiver-3.0.1.patch
#https://git.eclipse.org/r/#/c/75453/
Patch3:         fix-xmvn-pomless-builddep.patch
BuildRequires:  fdupes
BuildRequires:  jgit-bootstrap
BuildRequires:  maven-local
BuildRequires:  tycho-bootstrap
BuildRequires:  xz
BuildRequires:  mvn(io.takari.polyglot:polyglot-common)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
#!BuildIgnore:  tycho jgit
BuildArch:      noarch

%description
A small set of plugins that work with Tycho to provide additional functionality
when building projects of an OSGi nature.

%package javadoc
Summary:        Java docs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n org.eclipse.tycho.extras-tycho-extras-%{version}
%patch0 -p1
%patch1 -p1
%patch2
%patch3 -p1

# maven-properties-plugin is only needed for tests
%pom_remove_plugin org.eclipse.m2e:lifecycle-mapping
%pom_remove_plugin org.sonatype.plugins:maven-properties-plugin tycho-p2-extras-plugin
# remove org.apache.maven:apache-maven zip
%pom_remove_dep org.apache.maven:apache-maven tycho-p2-extras-plugin
%pom_add_dep org.fedoraproject.p2:org.fedoraproject.p2 tycho-eclipserun-plugin/pom.xml

%{mvn_alias} :{*} org.eclipse.tycho:@1

%build
# To run tests, we need :
# maven-properties-plugin (unclear licensing)
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

# Install extension JAR with deps into XMvn ext directory
install -d -m 755 %{buildroot}%{_datadir}/xmvn/lib/ext/
ln -s %{_javadir}/%{name}/tycho-pomless.jar %{buildroot}%{_datadir}/xmvn/lib/ext/
ln -s %{_javadir}/tesla-polyglot/polyglot-common.jar %{buildroot}%{_datadir}/xmvn/lib/ext/

%files -f .mfiles
%{_datadir}/xmvn/lib/ext/*

%files javadoc -f .mfiles-javadoc

%changelog
