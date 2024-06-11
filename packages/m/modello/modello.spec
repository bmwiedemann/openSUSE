#
# spec file for package modello
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


Name:           modello
Version:        2.4.0
Release:        0
Summary:        Modello Data Model toolkit
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://codehaus-plexus.github.io/modello
Source0:        https://repo1.maven.org/maven2/org/codehaus/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source100:      %{name}-build.tar.xz
Patch0:         0001-Upgrade-to-SnakeYaml-2.2-439.patch
Patch1:         0002-Update-build-get-rid-of-legacy-fix-CLI-452.patch
Patch2:         0003-Add-support-for-domAsXpp3-and-fail-if-the-old-Java5-.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  guava
BuildRequires:  jackson-core
BuildRequires:  jakarta-inject
BuildRequires:  javadoc-parser
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsoup
BuildRequires:  junit
BuildRequires:  plexus-build-api >= 1.0
BuildRequires:  plexus-compiler
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  snakeyaml
BuildRequires:  unzip
BuildRequires:  velocity
Requires:       aopalliance
Requires:       atinject
Requires:       google-guice
Requires:       guava
Requires:       jackson-core
Requires:       jakarta-inject
Requires:       javadoc-parser
Requires:       javapackages-tools
Requires:       plexus-build-api
Requires:       plexus-build-api0
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-utils
Requires:       plexus-xml
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
Requires:       snakeyaml
Requires:       velocity
BuildArch:      noarch

%description
Modello is a Data Model toolkit in use by the Apache Maven Project.

Modello is a framework for code generation from a simple model.
Modello generates code from a simple model format based on a plugin
architecture, various types of code and descriptors can be generated
from the single model, including Java POJOs, XML
marshallers/unmarshallers, XSD and documentation.

%package test
Summary:        Modello Test Package
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description test
Modello Test Package contains the basis to create Modello generator
unit-tests, including sample models and xml files to test every
feature for every plugin.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -a100
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
cp -p %{SOURCE1} .

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :sisu-maven-plugin

%pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0 modello-core

# This builds correctly with the older velocity 1.x and avoids build cycles
%pom_change_dep -r :velocity-engine-core :velocity

%pom_remove_dep :jackson-bom

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    guava/guava \
    jackson-core \
    jakarta-inject \
    javadoc-parser \
    jsoup \
    junit \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus/cli \
    plexus-compiler \
    plexus/plexus-build-api \
    plexus/utils \
    plexus/xml \
    slf4j/api \
    snakeyaml \
    velocity

%{ant} \
  -Dtest.skip=true \
  package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}

for i in core test; do
  install -pm 0644 %{name}-${i}/target/%{name}-${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${i}.jar
  %{mvn_install_pom} %{name}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${i}.pom
  %add_maven_depmap %{name}/%{name}-${i}.pom %{name}/%{name}-${i}.jar -f ${i}
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}
  cp -pr %{name}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}/
done

for i in converters dom4j java jdom sax stax xdoc xml xpp3 xsd jackson jsonschema snakeyaml velocity; do
  install -pm 0644 %{name}-plugins/%{name}-plugin-${i}/target/%{name}-plugin-${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-plugin-${i}.jar
  %{mvn_install_pom} %{name}-plugins/%{name}-plugin-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-plugin-${i}.pom
  %add_maven_depmap %{name}/%{name}-plugin-${i}.pom %{name}/%{name}-plugin-${i}.jar
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/%{name}-plugin-${i}
  cp -pr %{name}-plugins/%{name}-plugin-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/%{name}-plugin-${i}/
done

%fdupes -s %{buildroot}%{_javadocdir}

# script
%jpackage_script org.codehaus.modello.ModelloCli "" "" modello:aopalliance:atinject:google-guice:guava:jackson-core:jakarta-inject:javadoc-parser:plexus/plexus-build-api:plexus/plexus-build-api0:plexus/classworlds:plexus-containers/plexus-component-annotations:plexus/utils:plexus/xml:org.eclipse.sisu.inject:org.eclipse.sisu.plexus:slf4j/api:slf4j/simple:snakeyaml:velocity %{name} true

%files -f .mfiles -f .mfiles-core
%license LICENSE.txt LICENSE-2.0.txt
%{_bindir}/*

%files test -f .mfiles-test
%license LICENSE.txt LICENSE-2.0.txt

%files javadoc
%license LICENSE.txt LICENSE-2.0.txt
%{_javadocdir}/%{name}

%changelog
