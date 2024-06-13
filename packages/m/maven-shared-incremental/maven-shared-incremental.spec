#
# spec file for package maven-shared-incremental
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


Name:           maven-shared-incremental
Version:        1.1
Release:        0
Summary:        Maven Incremental Build support utilities
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/maven-shared-incremental/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-lib
BuildRequires:  maven-shared-utils
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildArch:      noarch

%description
Various utility classes and plexus components for supporting
incremental build functionality in maven plugins.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q
cp %{SOURCE1} build.xml

%pom_change_dep :plexus-component-api org.eclipse.sisu:org.eclipse.sisu.plexus:0.9.0.M2

%build
mkdir -p lib
build-jar-repository -s lib \
  maven/maven-core \
  maven/maven-model \
  maven/maven-plugin-api \
  maven-shared-utils/maven-shared-utils \
  org.eclipse.sisu.plexus \
  plexus-containers/plexus-component-annotations

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
