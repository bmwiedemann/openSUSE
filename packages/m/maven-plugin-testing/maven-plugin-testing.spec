#
# spec file for package maven-plugin-testing
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


Name:           maven-plugin-testing
Version:        3.3.0
Release:        0
Summary:        Maven Plugin Testing
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugin-testing/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-testing/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.tar.xz
Patch0:         0001-Port-to-plexus-utils-3.0.21.patch
Patch1:         0002-Port-to-current-maven-artifact.patch
Patch2:         %{name}-blocked.patch
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  easymock
BuildRequires:  fdupes
BuildRequires:  google-guice
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  maven-invoker
BuildRequires:  maven-lib
BuildRequires:  maven-resolver-api
BuildRequires:  maven-wagon-provider-api
BuildRequires:  plexus-archiver
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-plexus
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

%description harness
The Maven Plugin Testing Harness provides mechanisms to manage tests on Mojo.

%package tools
Summary:        Maven Plugin Testing Tools
Group:          Development/Libraries/Java

%description tools
A set of useful tools to help the Maven Plugin testing.

%package -n maven-test-tools
Summary:        Maven Testing Tool
Group:          Development/Libraries/Java

%description -n maven-test-tools
Framework to test Maven Plugins with Easymock objects.

%prep
%setup -q -a1

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin

for i in maven-plugin-testing-harness maven-plugin-testing-tools; do
  %pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0 ${i}
done

sed -i -e "s/MockControl/IMocksControl/g" maven-test-tools/src/main/java/org/apache/maven/shared/tools/easymock/MockManager.java

# needs network for some reason
rm maven-plugin-testing-tools/src/test/java/org/apache/maven/shared/test/plugin/ProjectToolTest.java

%{mvn_alias} : org.apache.maven.shared:

%{mvn_package} :{*} @1

%build
mkdir -p lib
build-jar-repository -s lib \
    commons-io \
    easymock \
    google-guice \
    junit \
    maven-invoker/maven-invoker \
    maven/maven-artifact \
    maven/maven-compat \
    maven/maven-core \
    maven/maven-model-builder \
    maven/maven-model \
    maven/maven-plugin-api \
    maven/maven-resolver-provider \
    maven/maven-settings \
    maven-resolver/maven-resolver-api \
    maven-shared-utils/maven-shared-utils \
    maven-wagon/provider-api \
    org.eclipse.sisu.plexus \
    plexus/archiver \
    plexus-classworlds \
    plexus-containers/plexus-component-annotations \
    plexus/utils \
    plexus/xml
%{ant} \
    -Dtest.skip=true \
    package javadoc

%{mvn_artifact} pom.xml
mkdir -p target/site/apidocs
for i in maven-plugin-testing-harness maven-plugin-testing-tools maven-test-tools; do
  cp -r ${i}/target/site/apidocs target/site/apidocs/${i}
  %{mvn_artifact} ${i}/pom.xml ${i}/target/${i}-%{version}.jar
done

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}
%license LICENSE
%doc NOTICE

%files harness -f .mfiles-%{name}-harness

%files tools -f .mfiles-%{name}-tools

%files -n maven-test-tools -f .mfiles-maven-test-tools

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
