#
# spec file for package maven-plugin-testing
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           maven-plugin-testing
Version:        3.4.0
Release:        0
Summary:        Maven Plugin Testing
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugin-testing/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-testing/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  apiguardian
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  google-guice
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  junit5-minimal
BuildRequires:  maven-lib
BuildRequires:  maven-resolver-api
BuildRequires:  maven-wagon-provider-api
BuildRequires:  mockito
BuildRequires:  plexus-archiver
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-testing >= 2.0.0
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildArch:      noarch

%description
The Maven Plugin Testing contains the necessary modules
to be able to test Maven Plugins.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%package harness
Summary:        Maven Plugin Testing Mechanism
Group:          Development/Libraries/Java
Obsoletes:      %{name}-tools < %{version}
Obsoletes:      maven-test-tools < %{version}

%description harness
The Maven Plugin Testing Harness provides mechanisms to manage tests on Mojo.

%prep
%setup -q -a1

%pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0 maven-plugin-testing-harness

%{mvn_alias} : org.apache.maven.shared:

%{mvn_package} :{*} @1

%build
mkdir -p lib
build-jar-repository -s lib \
    apiguardian/apiguardian-api \
    atinject \
    google-guice \
    junit \
    junit5/junit-jupiter-api \
    junit5/junit-platform-commons \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model-builder \
    maven/maven-model \
    maven/maven-plugin-api \
    maven/maven-resolver-provider \
    maven-resolver/maven-resolver-api \
    maven-wagon/provider-api \
    mockito/mockito-core \
    org.eclipse.sisu.plexus \
    plexus/archiver \
    plexus-classworlds \
    plexus/testing \
    plexus/utils \
    plexus/xml \
    slf4j/api
%{ant} \
    -Dtest.skip=true \
    package javadoc

%{mvn_artifact} pom.xml
%{mvn_artifact} maven-plugin-testing-harness/pom.xml maven-plugin-testing-harness/target/maven-plugin-testing-harness-%{version}.jar

%install
%mvn_install -J maven-plugin-testing-harness/target/site/apidocs
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}
%license LICENSE
%doc NOTICE

%files harness -f .mfiles-%{name}-harness

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
