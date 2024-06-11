#
# spec file for package maven-artifact-transfer
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


Name:           maven-artifact-transfer
Version:        0.13.1
Release:        0
Summary:        Apache Maven Artifact Transfer
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/maven-artifact-transfer
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
Patch0:         0001-Compatibility-with-Maven-3.0.3-and-later.patch
Patch1:         0002-Remove-support-for-maven-3.0.X.patch
Patch2:         0003-Port-to-maven-3.8.1.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-common-artifact-filters
BuildRequires:  maven-lib
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-impl
BuildRequires:  maven-resolver-util
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  unzip
BuildArch:      noarch

%description
An API to either install or deploy artifacts with Maven 3.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q
cp %{SOURCE1} build.xml
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

# We don't want to support legacy Maven versions (older than 3.1)
%pom_remove_dep org.sonatype.aether:
find -name Maven30\*.java -delete

%build
mkdir -p lib
build-jar-repository -s lib \
    maven-common-artifact-filters/maven-common-artifact-filters \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-impl \
    maven-resolver/maven-resolver-util \
    org.eclipse.sisu.plexus \
    plexus-classworlds \
    plexus-containers/plexus-component-annotations \
    plexus/utils \
    plexus/xml \
    slf4j/api

%{ant} \
    package javadoc

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
