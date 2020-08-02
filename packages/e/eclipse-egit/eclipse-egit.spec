#
# spec file for package eclipse-egit
#
# Copyright (c) 2020 SUSE LLC
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


%global gittag 5.8.0.202006091008-r
Name:           eclipse-egit
Version:        5.8.0
Release:        0
Summary:        Eclipse Git Integration
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/egit
# Use github mirror for now, see: https://bugs.eclipse.org/bugs/show_bug.cgi?id=522144
Source0:        https://github.com/eclipse/egit/archive/v%{gittag}/egit-v%{gittag}.tar.gz
BuildRequires:  eclipse-jdt-bootstrap
BuildRequires:  eclipse-jgit >= %{version}
BuildRequires:  eclipse-license2
BuildRequires:  eclipse-platform-bootstrap
BuildRequires:  maven-antrun-plugin
BuildRequires:  tycho
#!BuildIgnore:  eclipse-jdt
#!BuildIgnore:  eclipse-platform
#!BuildIgnore:  tycho-bootstrap
#!BuildRequires: log4j eclipse-emf-core eclipse-ecf-core
BuildArch:      noarch
# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch:    s390 %{arm} %{ix86}
%if 0
Requires:       eclipse-jgit >= %{version}
Requires:       eclipse-platform
%endif

%description
The eclipse-egit package contains Eclipse plugins for
interacting with Git repositories.

%prep
%setup -q -n egit-%{gittag}

# Disable unnecessary plugins for RPM builds
%pom_remove_plugin :maven-enforcer-plugin

%pom_xpath_remove "pom:repositories"
%pom_xpath_remove "pom:dependencies"
%pom_xpath_remove "pom:profiles"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin/pom:configuration/pom:target"
%pom_xpath_remove "*[local-name() ='plugin' and (child::*[text()='tycho-packaging-plugin'])]"
%pom_xpath_remove "pom:dependencies" org.eclipse.egit.doc/pom.xml
%pom_disable_module org.eclipse.egit.repository
%pom_disable_module org.eclipse.egit.source-feature
%pom_disable_module org.eclipse.egit.target

# Don't build mylyn feature
%pom_disable_module org.eclipse.egit.mylyn.ui
%pom_disable_module org.eclipse.egit.mylyn-feature

# Ensure correct apache sshd bundle gets symlinked
sed -i -e '/jsch/a<import plugin="org.apache.sshd.osgi"/>' org.eclipse.egit-feature/feature.xml

# Disable tests
%pom_disable_module org.eclipse.egit.core.test
%pom_disable_module org.eclipse.egit.ui.test
%pom_disable_module org.eclipse.egit.gitflow.test
%pom_disable_module org.eclipse.egit.mylyn.ui.test

%{mvn_package} "::pom::" __noinstall
%{mvn_package} :* egit

%build
%{mvn_build} -j -f

%install
%mvn_install

%files -f .mfiles-egit
%license LICENSE
%doc README.md

%if %{with mylyn}
%files mylyn -f .mfiles-mylyn
%license LICENSE
%doc README.md
%endif

%changelog
