#
# spec file for package spec-version-maven-plugin
#
# Copyright (c) 2022 SUSE LLC
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


Name:           spec-version-maven-plugin
Version:        2.1
Release:        0
Summary:        Spec Version Maven Plugin
License:        EPL-2.0 OR GPL-2.0-with-classpath-exception
Group:          Development/Libraries/Java
URL:            https://github.com/eclipse-ee4j/glassfish-spec-version-maven-plugin
Source0:        https://github.com/eclipse-ee4j/glassfish-spec-version-maven-plugin/archive/%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.eclipse.ee4j:project:pom:)
BuildArch:      noarch

%description
Maven Plugin to configure APIs version and
specs in a MANIFEST.MF file.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n glassfish-%{name}-%{version}
chmod -x *.md

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-checkstyle-plugin
# This one is needed only to process test resources
%pom_remove_plugin :build-helper-maven-plugin

sed -i "s|mvn|mvn-rpmbuild|" src/main/resources/checkVersion.sh

%{mvn_file} :%{name} %{name}

%build

%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
