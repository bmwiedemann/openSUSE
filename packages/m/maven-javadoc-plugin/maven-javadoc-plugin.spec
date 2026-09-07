#
# spec file for package maven-javadoc-plugin
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


Name:           maven-javadoc-plugin
Version:        3.12.0
Release:        0
Summary:        Maven plugin for creating javadocs
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugins/maven-javadoc-plugin
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Patch0:         0001-Consider-empty-release-and-source-strings-as-null.patch
Patch1:         expected-encoding.patch
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-text
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  javapackages-local
BuildRequires:  maven-archiver
BuildRequires:  maven-common-artifact-filters
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-invoker
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-reporting-api
BuildRequires:  maven-reporting-impl
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-impl
BuildRequires:  maven-resolver-util
BuildRequires:  maven-shared-utils
BuildRequires:  maven-wagon-provider-api
BuildRequires:  modello >= 2.0.0
BuildRequires:  objectweb-asm
BuildRequires:  plexus-archiver
BuildRequires:  plexus-interactivity-api
BuildRequires:  plexus-io
BuildRequires:  plexus-languages
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  qdox
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-minimal
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:) >= 40
Obsoletes:      %{name}-bootstrap
BuildArch:      noarch

%description
The Maven Javadoc Plugin is a plugin that uses the javadoc tool for
generating javadocs for the specified project.

%if %{without bootstrap}
%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.
%endif

%prep
%setup -q
cp %{SOURCE1} build.xml
%patch -P 0 -p1
%patch -P 1 -p1

%pom_remove_dep :::test:

%build
mkdir -p lib
build-jar-repository -s lib \
    apache-commons-lang3 \
    apache-commons-text \
    atinject \
    httpcomponents/httpclient \
    httpcomponents/httpcore \
    maven-archiver/maven-archiver \
    maven-common-artifact-filters/maven-common-artifact-filters \
    maven-doxia/doxia-core \
    maven-doxia/doxia-module-xhtml5 \
    maven-doxia/doxia-sink-api \
    maven-doxia-sitetools/doxia-integration-tools \
    maven-doxia-sitetools/doxia-site-renderer \
    maven-invoker/maven-invoker \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven/maven-model-builder \
    maven/maven-plugin-api \
    maven/maven-settings \
    maven-plugin-tools/maven-plugin-annotations \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-util \
    maven-reporting-api/maven-reporting-api \
    maven-shared-utils/maven-shared-utils \
    maven-wagon/provider-api \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus/archiver \
    plexus-classworlds \
    plexus/interactivity-api \
    plexus/io \
    plexus-languages/plexus-java \
    plexus/utils \
    plexus/xml \
    qdox \
    slf4j/api
ant -Dtest.skip=true jar javadoc

%{mvn_artifact} pom.xml target/%{name}-%{version}.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
