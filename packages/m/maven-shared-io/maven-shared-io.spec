#
# spec file for package maven-shared-io
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


Name:           maven-shared-io
Version:        3.0.0
Release:        0
Summary:        API for I/O support like logging, download or file scanning
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/maven-shared-io
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
# Rejected upstream: https://issues.apache.org/jira/browse/MSHARED-490
Patch0:         0001-Fix-running-tests-with-Maven-3.3.9.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven-lib
BuildRequires:  maven-shared-utils
BuildRequires:  maven-wagon-provider-api
BuildRequires:  plexus-utils
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildArch:      noarch

%description
API for I/O support like logging, download or file scanning.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml
%patch -P 0 -p1

%pom_add_dep org.codehaus.plexus:plexus-container-default::provided

%build
mkdir -p lib
build-jar-repository -s lib \
  maven/maven-compat \
  maven/maven-core \
  maven/maven-artifact \
  maven/maven-plugin-api \
  maven-wagon/provider-api \
  maven-shared-utils/maven-shared-utils \
  org.eclipse.sisu.plexus \
  plexus/utils

# Some of the tests cannot run outside maven
%{ant} \
  -Dtest.skip=true \
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
