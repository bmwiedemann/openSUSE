#
# spec file for package maven-compiler-plugin
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


Name:           maven-compiler-plugin
Version:        3.16.0
Release:        0
Summary:        Maven Compiler Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugins/maven-compiler-plugin
Source0:        https://archive.apache.org/dist/maven/plugins/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-util
BuildRequires:  maven-shared-incremental
BuildRequires:  maven-shared-utils
BuildRequires:  objectweb-asm
BuildRequires:  plexus-compiler >= 2.13
BuildRequires:  plexus-languages
BuildRequires:  plexus-utils
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-minimal
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
Obsoletes:      %{name}-bootstrap
BuildArch:      noarch

%description
The Compiler Plugin is used to compile the sources of your project.

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
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven/maven-plugin-api \
    maven-plugin-tools/maven-plugin-annotations \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-util \
    maven-shared-incremental/maven-shared-incremental \
    maven-shared-utils/maven-shared-utils \
    objectweb-asm/asm-all \
    plexus-compiler/plexus-compiler-api \
    plexus-compiler/plexus-compiler-manager \
    plexus-languages/plexus-java \
    plexus/utils
ant -Dtest.skip=true jar javadoc

%{mvn_artifact} pom.xml target/%{name}-%{version}.jar

%install
%mvn_install

%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
