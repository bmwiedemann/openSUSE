#
# spec file for package maven-filtering
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


Name:           maven-filtering
Version:        3.2.0
Release:        0
Summary:        Shared component providing resource filtering
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/%{name}/index.html
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-io
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  google-guice
BuildRequires:  guava
BuildRequires:  javapackages-local
BuildRequires:  jdom2
BuildRequires:  jsr-305
BuildRequires:  maven-lib
BuildRequires:  maven-shared-utils
BuildRequires:  objectweb-asm
BuildRequires:  plexus-build-api
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-cli
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  qdox
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildArch:      noarch

%description
These Plexus components have been built from the filtering process/code in
Maven Resources Plugin. The goal is to provide a shared component for all
plugins that needs to filter resources.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib \
    maven/maven-core \
    maven/maven-model \
    maven/maven-settings \
    org.eclipse.sisu.plexus \
    plexus-containers/plexus-component-annotations \
    maven-shared-utils/maven-shared-utils \
    plexus/utils \
    plexus/interpolation \
    plexus/plexus-build-api \
    commons-io \
    jsr-305 \
    \
    atinject \
    commons-cli \
    guava/guava \
    guice/google-guice-no_aop \
    jdom2/jdom2 \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    plexus-classworlds \
    plexus-metadata-generator \
    plexus/cli \
    qdox

# Tests use a package that is no longer present in plexus-build-api (v0.0.7)
%{ant} \
  jar javadoc

%{mvn_artifact} pom.xml target/%{name}-%{version}.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
