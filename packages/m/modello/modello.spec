#
# spec file for package modello
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.0.0
Release:        0
Summary:        Modello Data Model toolkit
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://codehaus-plexus.github.io/modello
Source0:        https://repo1.maven.org/maven2/org/codehaus/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source100:      %{name}-build.tar.xz
Patch0:         modello-cli-domasxpp3.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  google-guice
BuildRequires:  guava
BuildRequires:  javapackages-local
BuildRequires:  jsoup
BuildRequires:  junit
BuildRequires:  plexus-build-api
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-compiler
BuildRequires:  plexus-utils
BuildRequires:  sisu-plexus
BuildRequires:  unzip
Requires:       guava
Requires:       javapackages-tools
Requires:       xbean
Requires:       mvn(org.codehaus.plexus:plexus-compiler-api)
Requires:       mvn(org.codehaus.plexus:plexus-compiler-javac)
Requires:       mvn(org.codehaus.plexus:plexus-utils)
Requires:       mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
Requires:       mvn(org.jsoup:jsoup)
Requires:       mvn(org.sonatype.plexus:plexus-build-api)
Requires:       mvn(org.sonatype.sisu:sisu-guice::no_aop:)
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
%patch0 -p1
cp -p %{SOURCE1} LICENSE

%pom_remove_plugin :maven-site-plugin

%pom_remove_dep :jackson-bom

%pom_disable_module modello-plugin-jackson modello-plugins
%pom_disable_module modello-plugin-jsonschema modello-plugins
%pom_disable_module modello-plugin-snakeyaml modello-plugins
%pom_remove_dep :modello-plugin-jackson modello-maven-plugin
%pom_remove_dep :modello-plugin-jsonschema modello-maven-plugin
%pom_remove_dep :modello-plugin-snakeyaml modello-maven-plugin

%build
mkdir -p lib
build-jar-repository -s lib plexus/classworlds plexus/utils plexus/plexus-build-api \
  plexus-compiler/plexus-compiler-api plexus-compiler/plexus-compiler-javac \
  jsoup guava/guava junit org.eclipse.sisu.plexus
# skip tests because we have too old xmlunit in openSUSE now (1.5)
%{ant} \
  -Dtest.skip=true \
  package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}

for i in core test; do
  install -pm 0644 %{name}-${i}/target/%{name}-${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${i}.jar
done

for i in converters dom4j java jdom sax stax xdoc xml xpp3 xsd; do
  install -pm 0644 %{name}-plugins/%{name}-plugin-${i}/target/%{name}-plugin-${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-plugin-${i}.jar
done

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}

install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom

install -pm 0644 %{name}-plugins/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-plugins.pom
%add_maven_depmap %{name}/%{name}-plugins.pom

for i in core test; do
  install -pm 0644 %{name}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${i}.pom
  %add_maven_depmap %{name}/%{name}-${i}.pom %{name}/%{name}-${i}.jar
done

for i in converters dom4j java jdom sax stax xdoc xml xpp3 xsd; do
  install -pm 0644 %{name}-plugins/%{name}-plugin-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-plugin-${i}.pom
  %add_maven_depmap %{name}/%{name}-plugin-${i}.pom %{name}/%{name}-plugin-${i}.jar
done

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}

for i in core test; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}
  cp -pr %{name}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}/
done

for i in converters dom4j java jdom sax stax xdoc xml xpp3 xsd; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/%{name}-plugin-${i}
  cp -pr %{name}-plugins/%{name}-plugin-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/%{name}-plugin-${i}/
done

%fdupes -s %{buildroot}%{_javadocdir}

# script
%jpackage_script org.codehaus.modello.ModelloCli "" "" modello:org.eclipse.sisu.plexus:org.eclipse.sisu.inject:google-guice-no_aop:atinject:plexus-containers/plexus-component-annotations:plexus/classworlds:plexus/utils:plexus/plexus-build-api:guava:plexus-compiler/plexus-compiler-api:plexus-compiler/plexus-compiler-javac %{name} true

%files -f .mfiles
%license LICENSE
%{_bindir}/*

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
