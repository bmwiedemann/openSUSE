#
# spec file for package jboss-modules
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


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:           jboss-modules
Version:        1.5.2
Release:        0
Summary:        A Modular Classloading System
License:        Apache-2.0 AND xpp
Group:          Development/Libraries/Java
URL:            https://github.com/jbossas/jboss-modules
Source0:        https://github.com/jbossas/jboss-modules/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildArch:      noarch

%description
Ths package contains A Modular Classloading System.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Conditionally remove dependency on apiviz
%pom_remove_plugin :maven-javadoc-plugin

# Unneeded task
%pom_remove_plugin :maven-source-plugin

# Compiles tests even though we disable them
%pom_remove_plugin :maven-compiler-plugin

# Use not available org.wildfly.checkstyle:wildfly-checkstyle-config:1.0.4.Final
%pom_remove_plugin :maven-checkstyle-plugin

# Tries to connect to remote host
rm src/test/java/org/jboss/modules/MavenResourceTest.java \
 src/test/java/org/jboss/modules/maven/MavenSettingsTest.java

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE.txt XPP3-LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt XPP3-LICENSE.txt

%changelog
