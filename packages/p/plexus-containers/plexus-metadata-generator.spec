#
# spec file for package plexus-metadata-generator
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


%global base_name plexus-containers
%global comp_name component-metadata
%bcond_with tests
Name:           plexus-metadata-generator
Version:        2.2.0
Release:        0
Summary:        Component metadata from %{base_name}
# Most of the files are either under ASL 2.0 or MIT
# The following files are under xpp:
# plexus-component-metadata/src/main/java/org/codehaus/plexus/metadata/merge/Driver.java
# plexus-component-metadata/src/main/java/org/codehaus/plexus/metadata/merge/MXParser.java
License:        Apache-2.0 AND MIT AND xpp
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-containers
Source0:        https://github.com/codehaus-plexus/%{base_name}/archive/%{base_name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        LICENSE.MIT
Source100:      %{base_name}-build.tar.xz
Patch1:         plexus-metadata-generator-cli.patch
Patch1000:      %{name}-nomojo.patch
BuildRequires:  ant
BuildRequires:  apache-commons-cli
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  jdom2
BuildRequires:  junit
BuildRequires:  objectweb-asm >= 7
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-cli
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  qdox >= 2
BuildRequires:  sisu-plexus
BuildRequires:  xbean
Requires:       apache-commons-cli
Requires:       atinject
Requires:       google-guice
Requires:       guava
Requires:       jakarta-inject
Requires:       jdom2
Requires:       objectweb-asm >= 7
Requires:       plexus-cli
Requires:       plexus-containers-component-annotations = %{version}
Requires:       plexus-utils
Requires:       plexus-xml
Requires:       qdox >= 2
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       xbean
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
%endif

%description
Plexus contains end-to-end developer tools for writing applications.
At the core is the container, which can be embedded or for an
application server. There are many reusable components for hibernate,
form processing, jndi, i18n, velocity, etc. Plexus also includes an
application server which is like a J2EE application server.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n %{base_name}-%{base_name}-%{version} -a100

mkdir -p lib
build-jar-repository -s lib %{base_name} objectweb-asm/asm objectweb-asm/asm-commons org.eclipse.sisu.plexus plexus/classworlds plexus/utils plexus/xml jdom2/jdom2 commons-cli qdox plexus/cli
%if %{with tests}
build-jar-repository -s lib hamcrest/core xbean/xbean-reflect
%endif

%patch -P 1 -p1

%patch -P 1000 -p1

cp %{SOURCE1} .
cp %{SOURCE2} .

%pom_remove_plugin -r :maven-site-plugin

%pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0 plexus-component-metadata

# Generate OSGI info
%pom_xpath_inject "pom:project" "
    <packaging>bundle</packaging>
    <build>
      <plugins>
        <plugin>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <extensions>true</extensions>
          <configuration>
            <instructions>
              <_nouses>true</_nouses>
              <Export-Package>org.codehaus.plexus.component.annotations.*</Export-Package>
            </instructions>
          </configuration>
        </plugin>
      </plugins>
    </build>" plexus-component-annotations

# to prevent ant from failing
mkdir -p plexus-component-annotations/src/test/java

rm -rf plexus-%{comp_name}/src/main/java/org/codehaus/plexus/maven
rm -rf plexus-%{comp_name}/src/main/resources/META-INF/maven

%pom_remove_dep :maven-core plexus-%{comp_name}
%pom_remove_dep :maven-model plexus-%{comp_name}
%pom_remove_dep :maven-plugin-api plexus-%{comp_name}

%pom_xpath_set "pom:project/pom:artifactId" %{name} plexus-%{comp_name}

%build
pushd plexus-%{comp_name}
  ant \
     -f generator-build.xml \
%if %{without tests}
    -Dtest.skip=true \
%endif
    jar javadoc
popd

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 plexus-%{comp_name}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} plexus-%{comp_name}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr plexus-%{comp_name}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}
# script
%jpackage_script org.codehaus.plexus.metadata.PlexusMetadataGeneratorCli "" "" %{name}:atinject:jakarta-inject:org.eclipse.sisu.plexus:org.eclipse.sisu.inject:guice/google-guice:%{base_name}/plexus-component-annotations:objectweb-asm/asm:plexus-classworlds:plexus/utils:plexus/xml:jdom2/jdom2:commons-cli:qdox:plexus/cli:guava/guava:xbean/xbean-reflect %{name}

%files -f .mfiles
%license LICENSE-2.0.txt LICENSE.MIT
%{_bindir}/%{name}

%files javadoc
%license LICENSE-2.0.txt LICENSE.MIT
%{_javadocdir}/%{name}

%changelog
