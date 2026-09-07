#
# spec file for package maven-jar-plugin
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


Name:           maven-jar-plugin
Version:        3.5.1
Release:        0
Summary:        Maven JAR Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugins/maven-jar-plugin/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  maven-archiver >= 3.5.0
BuildRequires:  maven-file-management
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  objectweb-asm
BuildRequires:  plexus-archiver >= 4.2.0
BuildRequires:  sisu-inject
BuildRequires:  slf4j
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-minimal
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
Obsoletes:      %{name}-bootstrap
BuildArch:      noarch

%description
Builds a Java Archive (JAR) file from the compiled
project classes and resources.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

# Remove all dependencies with scope test, since a raw xmvn does not hide them
%pom_remove_dep -r :::test:

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    maven-file-management/file-management \
    maven-archiver/maven-archiver \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-plugin-api \
    maven-plugin-tools/maven-plugin-annotations \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    plexus/archiver \
    plexus/utils \
    slf4j/api
ant -Dtest.skip=true jar javadoc

%{mvn_artifact} pom.xml target/%{name}-%{version}.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%dir %{_javadir}/%{name}
%license LICENSE
%doc NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
