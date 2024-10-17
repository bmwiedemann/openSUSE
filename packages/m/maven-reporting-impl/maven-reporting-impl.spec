#
# spec file for package maven-reporting-impl
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


Name:           maven-reporting-impl
Version:        4.0.0
Release:        0
Summary:        Abstract classes to manage report generation
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-archiver
BuildRequires:  maven-doxia-core
BuildRequires:  maven-doxia-module-xhtml5
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-reporting-api >= 4
BuildRequires:  maven-resolver-api
BuildRequires:  maven-shared-utils
BuildRequires:  plexus-utils
BuildRequires:  sisu-plexus
BuildArch:      noarch

%description
Abstract classes to manage report generation, which can be run both:

* as part of a site generation (as a maven-reporting-api's MavenReport),
* or as a direct standalone invocation (as a maven-plugin-api's Mojo).

This is a replacement package for maven-shared-reporting-impl

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} LICENSE.txt
cp %{SOURCE2} build.xml

# integration tests try to download stuff from the internet
# and therefore they don't work in Build Service
%pom_remove_plugin :maven-invoker-plugin

%build
mkdir -p lib
build-jar-repository -s lib \
    maven-archiver/maven-archiver \
    maven-doxia/doxia-core \
    maven-doxia/doxia-module-xhtml5 \
    maven-doxia/doxia-sink-api \
    maven-doxia-sitetools/doxia-integration-tools \
    maven-doxia-sitetools/doxia-site-model \
    maven-doxia-sitetools/doxia-site-renderer \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven/maven-plugin-api \
    maven-plugin-tools/maven-plugin-annotations \
    maven-reporting-api/maven-reporting-api \
    maven-resolver/maven-resolver-api \
    maven-shared-utils/maven-shared-utils \
    org.eclipse.sisu.plexus \
    plexus/utils

ant jar javadoc

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
%license LICENSE.txt
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
