#
# spec file for package maven-filtering
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


Name:           maven-filtering
Version:        3.3.2
Release:        0
Summary:        Shared component providing resource filtering
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/%{name}/index.html
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-lib
BuildRequires:  plexus-build-api0
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-utils
BuildRequires:  sisu-inject
BuildRequires:  slf4j
BuildRequires:  unzip
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

%pom_xpath_remove pom:project/pom:parent/pom:relativePath

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    commons-io \
    commons-lang3 \
    maven/maven-core \
    maven/maven-model \
    maven/maven-settings \
    org.eclipse.sisu.inject \
    plexus/utils \
    plexus/interpolation \
    plexus/plexus-build-api0 \
    slf4j/api

%{ant} \
  jar javadoc

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
