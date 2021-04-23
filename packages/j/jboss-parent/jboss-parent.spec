#
# spec file for package jboss-parent
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


Name:           jboss-parent
Version:        20
Release:        0
Summary:        JBoss Parent POM
License:        CC0-1.0
Group:          Development/Libraries/Java
URL:            http://www.jboss.org/
Source0:        https://github.com/jboss/jboss-parent-pom/archive/%{name}-%{version}.tar.gz
Source1:        http://repository.jboss.org/licenses/cc0-1.0.txt
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildArch:      noarch

%description
The Project Object Model files for JBoss packages.

%prep
%setup -q -n %{name}-pom-%{name}-%{version}

# NOT available plugins
%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :javancss-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :sonar-maven-plugin

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :buildnumber-maven-plugin

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%build
%{mvn_build}

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
