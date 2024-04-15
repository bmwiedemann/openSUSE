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
Version:        2.3.0
Release:        0
Summary:        Modello Data Model toolkit
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://codehaus-plexus.github.io/modello
Source0:        https://repo1.maven.org/maven2/org/codehaus/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source100:      %{name}-build.tar.xz
Patch0:         0001-Fix-ModelloCli-after-moving-from-Plexus-to-JSR330.patch
Patch1:         0002-Add-support-for-domAsXpp3-and-fail-if-the-old-Java5-.patch
Patch2:         0003-Revert-Switch-to-codehaus-plexus-build-api-1.2.0-345.patch
BuildRequires:  ant
BuildRequires:  aopalliance
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  google-guice
BuildRequires:  guava
BuildRequires:  javadoc-parser
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsoup
BuildRequires:  objectweb-asm
BuildRequires:  plexus-build-api
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  unzip
Requires:       aopalliance
Requires:       atinject
Requires:       google-guice
Requires:       guava
Requires:       javadoc-parser
Requires:       javapackages-tools
Requires:       plexus-build-api
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-utils
Requires:       plexus-xml
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
BuildArch:      noarch

%description
Modello is a Data Model toolkit in use by the Apache Maven Project.

Modello is a framework for code generation from a simple model.
Modello generates code from a simple model format based on a plugin
architecture, various types of code and descriptors can be generated
from the single model, including Java POJOs, XML
marshallers/unmarshallers, XSD and documentation.

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
cp -p %{SOURCE1} LICENSE

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_dep :sisu-guice modello-core
%pom_add_dep com.google.inject:guice modello-core

%pom_remove_dep :jackson-bom

%pom_disable_module modello-plugin-jackson modello-plugins
%pom_disable_module modello-plugin-jsonschema modello-plugins
%pom_disable_module modello-plugin-snakeyaml modello-plugins
%pom_disable_module modello-plugin-velocity modello-plugins
%pom_remove_dep :modello-plugin-jackson modello-maven-plugin
%pom_remove_dep :modello-plugin-jsonschema modello-maven-plugin
%pom_remove_dep :modello-plugin-snakeyaml modello-maven-plugin
%pom_remove_dep :modello-plugin-velocity modello-maven-plugin

rm -f modello-maven-plugin/src/main/java/org/codehaus/modello/maven/ModelloVelocityMojo.java

%pom_disable_module modello-test

%build
mkdir -p lib
build-jar-repository -s lib \
    aopalliance \
    atinject \
    guava/guava \
    guice/google-guice \
    javadoc-parser \
    jsoup \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus/classworlds \
    plexus/cli \
    plexus/plexus-build-api \
    plexus/utils \
    plexus/xml \
    plexus-containers/plexus-component-annotations \
    slf4j/api

%{ant} \
  -Dtest.skip=true \
  package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}

for i in core; do
  install -pm 0644 %{name}-${i}/target/%{name}-${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${i}.jar
done

for i in converters dom4j java jdom sax stax xdoc xml xpp3 xsd; do
  install -pm 0644 %{name}-plugins/%{name}-plugin-${i}/target/%{name}-plugin-${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-plugin-${i}.jar
done

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}

for i in core; do
  %{mvn_install_pom} %{name}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${i}.pom
  %add_maven_depmap %{name}/%{name}-${i}.pom %{name}/%{name}-${i}.jar
done

for i in converters dom4j java jdom sax stax xdoc xml xpp3 xsd; do
  %{mvn_install_pom} %{name}-plugins/%{name}-plugin-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-plugin-${i}.pom
  %add_maven_depmap %{name}/%{name}-plugin-${i}.pom %{name}/%{name}-plugin-${i}.jar
done

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}

for i in core; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}
  cp -pr %{name}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}/
done

for i in converters dom4j java jdom sax stax xdoc xml xpp3 xsd; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/%{name}-plugin-${i}
  cp -pr %{name}-plugins/%{name}-plugin-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/%{name}-plugin-${i}/
done

%fdupes -s %{buildroot}%{_javadocdir}

# script
%jpackage_script org.codehaus.modello.ModelloCli "" "" modello:objectweb-asm:org.eclipse.sisu.plexus:org.eclipse.sisu.inject:javadoc-parser:google-guice:aopalliance:atinject:plexus-containers/plexus-component-annotations:plexus/classworlds:plexus/utils:plexus/xml:plexus/plexus-build-api:guava:slf4j/api:slf4j/simple %{name} true

%files -f .mfiles
%license LICENSE
%{_bindir}/*

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
