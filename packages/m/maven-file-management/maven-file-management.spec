#
# spec file for package maven-file-management
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


Name:           maven-file-management
Version:        3.1.0
Release:        0
Summary:        Maven File Management API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/file-management
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/file-management/%{version}/file-management-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-lib
BuildRequires:  modello >= 2.0.0
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  slf4j
BuildRequires:  unzip
BuildArch:      noarch

%description
Provides a component for plugins to easily resolve project dependencies.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n file-management-%{version}
cp %{SOURCE1} build.xml

%pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0

%build
mkdir -p lib
build-jar-repository -s lib \
    commons-io \
    maven/maven-plugin-api \
    plexus/utils \
    plexus/xml \
    slf4j/api

%{ant} \
    jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/file-management-%{version}.jar %{buildroot}%{_javadir}/%{name}/file-management.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/file-management.pom
%add_maven_depmap %{name}/file-management.pom %{name}/file-management.jar
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
