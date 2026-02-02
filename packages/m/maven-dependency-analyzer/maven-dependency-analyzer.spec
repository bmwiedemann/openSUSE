#
# spec file for package maven-dependency-analyzer
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           maven-dependency-analyzer
Version:        1.17.0
Release:        0
Summary:        Maven dependency analyzer
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/maven-dependency-analyzer/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-lib
BuildRequires:  objectweb-asm
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  slf4j
BuildRequires:  unzip
BuildArch:      noarch

%description
Analyzes the dependencies of a project for undeclared or unused artifacts.

Warning: Analysis is not done at source but bytecode level, then some cases are
not detected (constants, annotations with source-only retention, links in
javadoc) which can lead to wrong result if they are the only use of a
dependency.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}

%prep
%setup -q
cp %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib \
    apache-commons-lang3 \
    atinject \
    commons-io \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    plexus/xml \
    slf4j/api

%{ant} \
    -Dtest.skip=true \
    jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE NOTICE

%changelog
