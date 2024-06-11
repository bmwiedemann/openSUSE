#
# spec file for package maven-javadoc-plugin
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global base_name maven-javadoc-plugin
Version:        3.6.0
Release:        0
Summary:        Maven plugin for creating javadocs
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugins/maven-javadoc-plugin
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{base_name}/%{version}/%{base_name}-%{version}-source-release.zip
Source1:        %{base_name}-build.xml
Patch0:         %{base_name}-bootstrap-resources.patch
Patch1:         stale-data-encoding.patch
Patch2:         no-override.patch
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-text
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  javapackages-local
BuildRequires:  maven-archiver
BuildRequires:  maven-common-artifact-filters
BuildRequires:  maven-doxia-core
BuildRequires:  maven-doxia-logging-api
BuildRequires:  maven-doxia-module-xhtml
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-invoker
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-reporting-api >= 3.1.0
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-util
BuildRequires:  maven-shared-utils
BuildRequires:  maven-wagon-provider-api
BuildRequires:  plexus-archiver
BuildRequires:  plexus-interactivity-api
BuildRequires:  plexus-io
BuildRequires:  plexus-languages
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  qdox
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{base_name}-bootstrap
BuildRequires:  ant
BuildRequires:  modello >= 2.0.0
%else
Name:           %{base_name}
BuildRequires:  xmvn
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:) >= 40
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
Obsoletes:      %{base_name}-bootstrap
#!BuildRequires: maven-compiler-plugin-bootstrap
#!BuildRequires: maven-jar-plugin-bootstrap
#!BuildRequires: maven-javadoc-plugin-bootstrap
#!BuildRequires: maven-plugin-plugin-bootstrap
#!BuildRequires: maven-resources-plugin-bootstrap
#!BuildRequires: maven-surefire-plugin-bootstrap
%endif

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
%setup -q -n %{base_name}-%{version}
%if %{with bootstrap}
cp %{SOURCE1} build.xml
%patch -P 0 -p1
%endif
%patch -P 1 -p1
%patch -P 2 -p1

%pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0

%pom_xpath_remove pom:project/pom:parent/pom:relativePath
%pom_remove_dep :::test:

%build
%if %{with bootstrap}
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
    maven-doxia/doxia-logging-api \
    maven-doxia/doxia-module-xhtml \
    maven-doxia/doxia-module-xhtml5 \
    maven-doxia/doxia-sink-api \
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
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus/archiver \
    plexus/interactivity-api \
    plexus/io \
    plexus-languages/plexus-java \
    plexus/utils \
    plexus/xml \
    qdox
%{ant} -Dtest.skip=true jar
%else
xmvn --batch-mode --offline \
    -Dmaven.test.skip=true -DmavenVersion=3.5.0 \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    package org.apache.maven.plugins:maven-javadoc-plugin:aggregate
%endif

%{mvn_artifact} pom.xml target/%{base_name}-%{version}.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc NOTICE

%if %{without bootstrap}
%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE
%endif

%changelog
