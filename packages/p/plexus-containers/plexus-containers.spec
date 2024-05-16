#
# spec file for package plexus-containers
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


%bcond_with tests
Name:           plexus-containers
Version:        2.2.0
Release:        0
Summary:        Containers for Plexus
# Most of the files are either under ASL 2.0 or MIT
# The following files are under xpp:
# plexus-component-metadata/src/main/java/org/codehaus/plexus/metadata/merge/Driver.java
# plexus-component-metadata/src/main/java/org/codehaus/plexus/metadata/merge/MXParser.java
License:        Apache-2.0 AND MIT AND xpp
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-containers
Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        LICENSE.MIT
Source100:      %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  guava
BuildRequires:  javapackages-local >= 6
BuildRequires:  junit
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  xbean
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
BuildRequires:  objectweb-asm
%endif

%description
Plexus contains end-to-end developer tools for writing applications.
At the core is the container, which can be embedded or for an
application server. There are many reusable components for hibernate,
form processing, jndi, i18n, velocity, etc. Plexus also includes an
application server which is like a J2EE application server.

%package component-annotations
Summary:        Component API from %{name}
Group:          Development/Libraries/Java

%description component-annotations
%{summary}.

%package javadoc
Summary:        API documentation for all plexus-containers packages
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version} -a100

mkdir -p lib
build-jar-repository -s lib plexus/classworlds plexus/utils plexus/xml guava/guava junit xbean/xbean-reflect
%if %{with tests}
build-jar-repository -s lib objectweb-asm/asm objectweb-asm/asm-commons hamcrest/core
%endif

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

%build
pushd plexus-component-annotations
  %{ant} \
%if %{without tests}
    -Dtest.skip=true \
%endif
    jar javadoc
popd

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 plexus-component-annotations/target/plexus-component-annotations-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}/plexus-component-annotations.jar

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} plexus-component-annotations/pom.xml \
    %{buildroot}%{_mavenpomdir}/%{name}/plexus-component-annotations.pom
%add_maven_depmap %{name}/plexus-component-annotations.pom %{name}/plexus-component-annotations.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr plexus-component-annotations/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/plexus-component-annotations
%fdupes -s %{buildroot}%{_javadocdir}

%files component-annotations -f .mfiles
%license LICENSE-2.0.txt LICENSE.MIT

%files javadoc
%license LICENSE-2.0.txt LICENSE.MIT
%{_javadocdir}/%{name}

%changelog
