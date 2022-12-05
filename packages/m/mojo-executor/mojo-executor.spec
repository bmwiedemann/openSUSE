#
# spec file for package mojo-executor
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


Name:           mojo-executor
Version:        2.4.0
Release:        0
Summary:        Mojo Executor
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://mojo-executor.github.io/mojo-executor/
Source0:        https://github.com/mojo-executor/mojo-executor/archive/refs/tags/mojo-executor-parent-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0
Patch0:         mojo-executor-dependency.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
The Mojo Executor provides a way to to execute other Mojos (plugins) within a Maven plugin,
allowing to create Maven plugins that are composed of other plugins.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-parent-%{version}
%patch0 -p1
cp %{SOURCE1} .
%pom_disable_module %{name}-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin

perl -pi -e 's#org\.sonatype\.aether\.repository#org.eclipse.aether.repository#g' \
	mojo-executor/src/main/java/org/twdata/maven/mojoexecutor/MavenCompatibilityHelper.java

%build
%mvn_build -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=7
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE-2.0 LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0 LICENSE.txt

%changelog
