#
# spec file for package maven-dependency-analyzer
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


Name:           maven-dependency-analyzer
Version:        1.10
Release:        0
Summary:        Maven dependency analyzer
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/shared/maven-dependency-analyzer/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-lang3
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  google-guice
BuildRequires:  guava20
BuildRequires:  javapackages-local
BuildRequires:  jdom2
BuildRequires:  maven-lib
#BuildRequires:  maven-project
BuildRequires:  objectweb-asm
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-cli
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  qdox
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildRequires:  xbean
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
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

# Do not require maven2
%pom_change_dep :maven-project :maven-core

%build
mkdir -p lib
build-jar-repository -s lib \
	apache-commons-lang3 \
	atinject \
	commons-cli \
	guava20/guava-10.0 \
	guice/google-guice-no_aop \
	jdom2/jdom2 \
	maven/maven-artifact \
	maven/maven-core \
	maven/maven-model \
	objectweb-asm/asm \
	org.eclipse.sisu.inject \
	org.eclipse.sisu.plexus \
	plexus-classworlds \
	plexus/cli \
	plexus-containers/plexus-component-annotations \
	plexus-metadata-generator \
	plexus/utils \
	qdox \
	xbean/xbean-reflect

%{ant} \
	-Dtest.skip=true \
	jar javadoc

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
