#
# spec file for package maven-surefire-provider-junit5
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


%global base_name maven-surefire
Name:           %{base_name}-provider-junit5
Version:        3.5.2
Release:        0
Summary:        JUnit 5 provider for Maven Surefire
License:        Apache-2.0 AND CPL-1.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/surefire/
Source0:        %{base_name}-%{version}.tar.xz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        https://www.eclipse.org/legal/cpl-v10.html
Patch0:         0001-Port-to-TestNG-7.4.0.patch
Patch1:         0002-Unshade-surefire.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.surefire:common-java5)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.junit.platform:junit-platform-engine)
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
# PpidChecker relies on /usr/bin/ps to check process uptime
Requires:       procps
BuildArch:      noarch

%description
JUnit 5 provider for Maven Surefire.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{base_name}-%{version}
cp -p %{SOURCE1} %{SOURCE2} .

%patch -P 0 -p1
%patch -P 1 -p1

# Disable strict doclint
sed -i /-Xdoclint:all/d pom.xml

# QA plugin useful only for upstream
%pom_remove_plugin -r :jacoco-maven-plugin
# Not wanted
%pom_remove_plugin -r :maven-shade-plugin
# Not packaged
%pom_remove_plugin -r :animal-sniffer-maven-plugin
# Complains
%pom_remove_plugin -r :apache-rat-plugin

%pom_disable_module surefire-shadefire
%pom_remove_dep -r :surefire-shadefire

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-its

# We don't need site-source
%pom_remove_plugin :maven-assembly-plugin maven-surefire-plugin

%build
pushd surefire-providers/surefire-junit-platform
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

popd

%install
pushd surefire-providers/surefire-junit-platform
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f surefire-providers/surefire-junit-platform/.mfiles
%doc README.md
%license LICENSE-2.0.txt cpl-v10.html

%files javadoc -f surefire-providers/surefire-junit-platform/.mfiles-javadoc
%license LICENSE-2.0.txt cpl-v10.html

%changelog
