#
# spec file for package maven-enforcer
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


Name:           maven-enforcer
Version:        3.4.1
Release:        0
Summary:        A build rule execution framework
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/enforcer
Source0:        https://repo1.maven.org/maven2/org/apache/maven/enforcer/enforcer/%{version}/enforcer-%{version}-source-release.zip
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
Enforcer is a build rule execution framework.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%package api
Summary:        Enforcer API
Group:          Development/Libraries/Java

%description api
This component provides the generic interfaces needed to
implement custom rules for the maven-enforcer-plugin.

%package rules
Summary:        Enforcer Rules
Group:          Development/Libraries/Java

%description rules
This component contains the standard Enforcer Rules.

%package plugin
Summary:        Enforcer Rules
Group:          Development/Libraries/Java

%description plugin
The Enforcer plugin provides goals to control certain environmental
constraints such as Maven version, JDK version and OS family along
with many more built-in rules and user created rules.

%package extension
Summary:        Maven Enforcer Extension
Group:          Development/Libraries/Java

%description extension
The Enforcer Extension provides a way to globally define rules without
making use of pom inheritence. This way you don't have to adjust the
pom.xml, but you can enforce a set of rules.

%prep
%setup -q -n enforcer-%{version}

find -name '*.java' -exec sed -i 's/\r//' {} +

%pom_remove_dep org.junit:junit-bom

%pom_add_dep javax.annotation:javax.annotation-api maven-enforcer-plugin

%pom_add_plugin org.eclipse.sisu:sisu-maven-plugin maven-enforcer-plugin

%build
%{mvn_build} -s -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dversion.maven-enforcer-plugin=SYSTEM \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-enforcer
%license LICENSE
%doc NOTICE

%files api -f .mfiles-enforcer-api
%license LICENSE
%doc NOTICE

%files rules -f .mfiles-enforcer-rules

%files plugin -f .mfiles-maven-enforcer-plugin

%files extension -f .mfiles-maven-enforcer-extension

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
