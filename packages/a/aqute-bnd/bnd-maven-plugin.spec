#
# spec file for package bnd-maven-plugin
#
# Copyright (c) 2023 SUSE LLC
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


Name:           bnd-maven-plugin
Version:        6.3.1
Release:        0
Summary:        BND Maven plugin
# Part of jpm is under BSD, but jpm is not included in binary RPM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://bnd.bndtools.org/
Source0:        bnd-%{version}.tar.xz
Patch1:         0001-Disable-removed-commands.patch
Patch2:         0002-Port-to-OSGI-7.0.0.patch
Patch3:         0003-Remove-unmet-dependencies.patch
Patch4:         reproducible-timestamps.patch
Patch5:         reproducible-packages-list.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib) >= %{version}
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-mapping)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildArch:      noarch

%description
Collection of various Maven plugins provided by the Bnd project.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n bnd-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

cp -r biz.aQute.bnd.maven/src/aQute/bnd/maven/lib/configuration maven/bnd-maven-plugin/src/main/java/aQute/bnd/maven/lib
cp -r biz.aQute.bnd.maven/src/aQute/bnd/maven/lib/executions maven/bnd-maven-plugin/src/main/java/aQute/bnd/maven/lib
pushd maven
%pom_remove_dep -r :biz.aQute.bnd.maven
# Unavailable reactor dependency - org.osgi.impl.bundle.repoindex.cli
%pom_disable_module bnd-indexer-maven-plugin
# Requires unbuilt parts of bnd
%pom_disable_module bnd-export-maven-plugin
%pom_disable_module bnd-reporter-maven-plugin
%pom_disable_module bnd-resolver-maven-plugin
%pom_disable_module bnd-run-maven-plugin
%pom_disable_module bnd-testing-maven-plugin
# Integration tests require Internet access
%pom_remove_plugin -r :maven-invoker-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_plugin -r :flatten-maven-plugin

%pom_remove_dep -r org.junit:junit-bom

%{mvn_package} biz.aQute.bnd:bnd-plugin-parent __noinstall
popd

%build
pushd maven
%{mvn_build} -f -- -Dproject.build.sourceEncoding=UTF-8 -Dsource=8
popd

%install
pushd maven
%mvn_install
popd
%fdupes -s %{buildroot}%{_javadocdir}

%files -f maven/.mfiles
%license LICENSE

%files javadoc -f maven/.mfiles-javadoc
%license LICENSE

%changelog
