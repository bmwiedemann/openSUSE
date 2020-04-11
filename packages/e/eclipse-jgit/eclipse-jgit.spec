#
# spec file for package eclipse-jgit
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


%global gittag 5.1.3.201810200350-r
Name:           eclipse-jgit
Version:        5.1.3
Release:        0
Summary:        Eclipse JGit
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/egit/
# Use github mirror for now, see: https://bugs.eclipse.org/bugs/show_bug.cgi?id=522144
Source0:        https://github.com/eclipse/jgit/archive/v%{gittag}/jgit-v%{gittag}.tar.gz
Patch0:         fix_jgit_sh.patch
# Change how feature deps are specified, to avoid embedding versions
Patch1:         jgit-feature-deps.patch
BuildRequires:  apache-commons-compress
BuildRequires:  args4j
BuildRequires:  eclipse-platform-bootstrap
BuildRequires:  google-gson
BuildRequires:  hamcrest-core
BuildRequires:  javaewah
BuildRequires:  jgit = %{version}
BuildRequires:  junit
BuildRequires:  jzlib
BuildRequires:  slf4j
BuildRequires:  tycho
BuildRequires:  xml-commons-apis
#!BuildRequires: log4j eclipse-emf-core eclipse-ecf-core
#!BuildIgnore:  eclipse-platform
#!BuildIgnore:  tycho-bootstrap
Requires:       apache-commons-compress
Requires:       args4j
Requires:       eclipse-platform
Requires:       google-gson
Requires:       hamcrest-core
Requires:       javaewah
Requires:       jgit = %{version}
Requires:       junit
Requires:       jzlib
Requires:       slf4j
Requires:       xml-commons-apis
BuildArch:      noarch

%description
A pure Java implementation of the Git version control system.

%prep
%setup -q -n jgit-%{gittag}

%patch0
%patch1

# Disable multithreaded build
rm .mvn/maven.config

# Javaewah change
sed -i -e "s/javaewah/com.googlecode.javaewah.JavaEWAH/g" org.eclipse.jgit.packaging/org.eclipse.jgit{,.pgm}.feature/feature.xml

# Don't try to get deps from local *maven* repo, use tycho resolved ones
%pom_remove_dep com.googlecode.javaewah:JavaEWAH
for p in $(find org.eclipse.jgit.packaging -name pom.xml) ; do
  grep -q dependencies $p && %pom_xpath_remove "pom:dependencies" $p
done

# Don't need target platform or repository modules with xmvn
%pom_disable_module org.eclipse.jgit.target org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.repository org.eclipse.jgit.packaging
%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin/pom:configuration/pom:target" org.eclipse.jgit.packaging

# Don't build source features
%pom_disable_module org.eclipse.jgit.source.feature org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.pgm.source.feature org.eclipse.jgit.packaging

# Remove unnecessary plugins for RPM builds
%pom_remove_plugin :maven-enforcer-plugin org.eclipse.jgit.packaging

# org.slf4j.api -> slf4j.api
# org.slf4j.impl.log4j12 -> slf4j.simple
sed -i 's/org\.slf4j\.api/slf4j\.api/
        s/org\.slf4j\.impl\.log4j12/slf4j\.simple/' \
org.eclipse.jgit.packaging/org.eclipse.jgit.feature/feature.xml

pushd org.eclipse.jgit.packaging
%{mvn_package} "::pom::" __noinstall
popd

%build
pushd org.eclipse.jgit.packaging
%{mvn_build} -j -f
popd

%install
pushd org.eclipse.jgit.packaging
%mvn_install
popd

%files -f org.eclipse.jgit.packaging/.mfiles
%license LICENSE
%doc README.md

%changelog
