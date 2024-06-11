#
# spec file for package maven-doxia-sitetools
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


%global parent maven-doxia
%global subproj sitetools
Name:           %{parent}-%{subproj}
Version:        1.11.1
Release:        0
Summary:        Doxia content generation framework
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/doxia/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia-sitetools/%{version}/doxia-%{subproj}-%{version}-source-release.zip
Source1:        %{name}-build.tar.xz
Patch1:         0002-Remove-dependency-on-velocity-tools.patch
BuildRequires:  ant
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-doxia-core
BuildRequires:  maven-doxia-logging-api
BuildRequires:  maven-doxia-module-fo
BuildRequires:  maven-doxia-module-xhtml
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-lib
BuildRequires:  maven-reporting-api
BuildRequires:  modello >= 2.0.0
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-i18n
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  plexus-xml
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildRequires:  velocity
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  xz
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-apt)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-fml)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xdoc)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xhtml5)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildArch:      noarch

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n doxia-%{subproj}-%{version} -a1
%patch -P 1 -p1

# migrate to maven 3
%pom_xpath_set //pom:mavenVersion 3.8.6 doxia-integration-tools
%pom_change_dep :maven-artifact-manager :maven-core doxia-integration-tools
%pom_change_dep :maven-project :maven-compat doxia-integration-tools

# complains
%pom_remove_plugin :apache-rat-plugin

%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_dep net.sourceforge.htmlunit:htmlunit doxia-site-renderer/pom.xml
%pom_remove_dep -r :velocity-tools

rm -rf $(find -type d -name itext)
%pom_remove_dep -r :doxia-module-itext

%pom_remove_dep -r :doxia-module-markdown

for i in doxia-decoration-model doxia-doc-renderer doxia-integration-tools doxia-site-renderer; do
  %pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0 ${i}
done

%{mvn_alias} :doxia-integration-tools org.apache.maven.shared:maven-doxia-tools

%build
mkdir -p lib
build-jar-repository -s lib \
    apache-commons-collections \
    apache-commons-lang3 \
    commons-io \
    maven-doxia/doxia-core \
    maven-doxia/doxia-logging-api \
    maven-doxia/doxia-module-fo \
    maven-doxia/doxia-module-xhtml \
    maven-doxia/doxia-module-xhtml5 \
    maven-doxia/doxia-sink-api \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-plugin-api \
    maven/maven-project \
    maven-reporting-api/maven-reporting-api \
    org.eclipse.sisu.plexus \
    plexus-containers/plexus-component-annotations \
    plexus-i18n/plexus-i18n \
    plexus/interpolation \
    plexus/utils \
    plexus/xml \
    plexus-velocity/plexus-velocity \
    velocity
# tests can't run because of missing deps
%{ant} -Dtest.skip=true package javadoc

mkdir -p target/site/apidocs
for i in \
    doxia-decoration-model \
    doxia-skin-model \
    doxia-integration-tools \
    doxia-site-renderer \
    doxia-doc-renderer; do
  %{mvn_artifact} ${i}/pom.xml ${i}/target/${i}-%{version}.jar
  if [ -d ${i}/target/site/apidocs ]; then
    cp -r ${i}/target/site/apidocs target/site/apidocs/${i}
  fi
done

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
