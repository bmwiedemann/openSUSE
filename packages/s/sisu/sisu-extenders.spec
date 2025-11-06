#
# spec file for package sisu-extenders
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           sisu-extenders
Version:        0.9.0.M4
Release:        0
Summary:        Sisu Extenders
License:        EPL-1.0 AND EPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/sisu
Source0:        https://github.com/eclipse-sisu/sisu-project/archive/refs/tags/%{reltype}/%{version}.tar.gz#/sisu-project-%{version}.tar.gz
Patch1:         sisu-no-dependency-on-glassfish-servlet-api.patch
Patch3:         sisu-osgi-api.patch
Patch4:         sisu-reproducible-index.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildArch:      noarch

%description
Java dependency injection framework with backward support for
plexus and bean style dependency injection.

%package -n sisu-inject-extender
Summary:        Sisu Inject Extender
Group:          Development/Libraries/Java

%description -n sisu-inject-extender
Automatically discovers and wires JSR-330 annotated Sisu
components contained in OSGi bundles

%package -n sisu-plexus-extender
Summary:        Sisu Plexus Extender
Group:          Development/Libraries/Java

%description -n sisu-plexus-extender
Plexus-JSR330 adapter; adds Plexus support to the Sisu-Inject
container

%prep
%setup -q -n sisu-project-%{reltype}-%{version}

%patch -P 1 -p1
%patch -P 3 -p1
%patch -P 4 -p2

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-invoker-plugin
# it is scope "import" but used only for tests that we don't run
%pom_remove_dep :junit-bom
%pom_xpath_remove pom:project/pom:build/pom:extensions

%pom_disable_module org.eclipse.sisu.inject
%pom_disable_module org.eclipse.sisu.plexus
%pom_disable_module org.eclipse.sisu.mojos

%{mvn_package} :sisu-inject __noinstall

%build
%{mvn_build} -fjs

%install
%mvn_install

%files -n sisu-inject-extender -f .mfiles-org.eclipse.sisu.inject.extender
%license LICENSE.txt

%files -n sisu-plexus-extender -f .mfiles-org.eclipse.sisu.plexus.extender
%license LICENSE.txt

%changelog
