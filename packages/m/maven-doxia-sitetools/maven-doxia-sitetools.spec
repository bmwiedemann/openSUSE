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


Name:           maven-doxia-sitetools
Version:        2.0.0
Release:        0
Summary:        Doxia content generation framework
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/doxia/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.tar.xz
Patch1:         0001-Remove-dependency-on-velocity-tools.patch
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-doxia-core
BuildRequires:  maven-doxia-module-xhtml5
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-lib
BuildRequires:  maven-reporting-api
BuildRequires:  maven-resolver-api
BuildRequires:  modello
BuildRequires:  plexus-i18n
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  velocity-engine-core
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
%setup -q -a1
%patch -P 1 -p1

%pom_remove_dep -r :velocity-tools-generic

%build
mkdir -p lib
build-jar-repository -s lib \
    apache-commons-lang3 \
    atinject \
    commons-io \
    maven-doxia/doxia-core \
    maven-doxia/doxia-module-xhtml5 \
    maven-doxia/doxia-sink-api \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven-reporting-api/maven-reporting-api \
    maven-resolver/maven-resolver-api \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus-i18n/plexus-i18n \
    plexus/interpolation \
    plexus/utils \
    plexus-velocity/plexus-velocity \
    plexus/xml \
    slf4j/api \
    velocity-engine/velocity-engine-core

ant package javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for i in \
    doxia-site-model \
    doxia-skin-model \
    doxia-site-renderer \
    doxia-integration-tools; do
  install -pm 0644 ${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
  %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f ${i}
  if [ -d ${i}/target/site/apidocs ]; then
    cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
  fi
done
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-doxia-integration-tools -f .mfiles-doxia-site-model -f .mfiles-doxia-site-renderer -f .mfiles-doxia-skin-model

%files javadoc
%{_javadocdir}/%{name}

%changelog
