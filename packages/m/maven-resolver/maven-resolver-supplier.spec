#
# spec file for package maven-resolver-supplier
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global base_name maven-resolver
%define _buildshell /bin/bash
Name:           %{base_name}-supplier
Version:        1.9.27
Release:        0
Summary:        Apache Maven Artifact Resolver library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/resolver/
Source0:        https://archive.apache.org/dist/maven/resolver/%{base_name}-%{version}-source-release.zip
Source1:        %{base_name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  maven-lib
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-connector-basic
BuildRequires:  maven-resolver-impl
BuildRequires:  maven-resolver-named-locks
BuildRequires:  maven-resolver-spi
BuildRequires:  maven-resolver-transport-file
BuildRequires:  maven-resolver-transport-http
BuildRequires:  maven-resolver-util
BuildRequires:  sisu-inject
BuildRequires:  slf4j
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
A helper module to provide RepositorySystem instances.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n %{base_name}-%{version} -a1

# requires internet connection
rm maven-resolver-transport-http/src/test/java/org/eclipse/aether/transport/http/{HttpServer,HttpTransporterTest}.java
%pom_remove_dep org.eclipse.jetty: maven-resolver-transport-http

%pom_remove_plugin -r :bnd-maven-plugin
%pom_remove_plugin -r org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_remove_plugin -r :japicmp-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%pom_disable_module maven-resolver-demos
%pom_disable_module maven-resolver-named-locks-hazelcast
%pom_disable_module maven-resolver-named-locks-redisson
%pom_disable_module maven-resolver-transport-classpath

# generate OSGi manifests
for pom in $(find -mindepth 2 -name pom.xml) ; do
  %pom_add_plugin "org.apache.felix:maven-bundle-plugin" $pom \
  "<configuration>
    <instructions>
      <Bundle-SymbolicName>\${project.groupId}$(sed 's:./maven-resolver::;s:/pom.xml::;s:-:.:g' <<< $pom)</Bundle-SymbolicName>
      <Export-Package>!org.eclipse.aether.internal*,org.eclipse.aether*</Export-Package>
      <_nouses>true</_nouses>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>create-manifest</id>
      <phase>process-classes</phase>
      <goals><goal>manifest</goal></goals>
    </execution>
  </executions>"
done
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%{mvn_package} :maven-resolver __noinstall
%{mvn_alias} 'org.apache.maven.resolver:maven-resolver{*}' 'org.eclipse.aether:aether@1'
%{mvn_alias} 'org.apache.maven.resolver:maven-resolver-transport-wagon' 'org.eclipse.aether:aether-connector-wagon'
%{mvn_file} ':%{base_name}{*}' %{base_name}/%{base_name}@1 aether/aether@1

# Try to avoid sucking in dependencies on packages that are not built at this moment
%pom_remove_parent .
%pom_remove_plugin :maven-jar-plugin .

%build
mkdir -p lib
build-jar-repository -s lib \
  atinject \
  maven-resolver/maven-resolver-api \
  maven-resolver/maven-resolver-util \
  maven-resolver/maven-resolver-spi \
  maven-resolver/maven-resolver-named-locks \
  maven-resolver/maven-resolver-impl \
  maven-resolver/maven-resolver-connector-basic \
  maven-resolver/maven-resolver-transport-file \
  maven-resolver/maven-resolver-transport-http \
  maven/maven-resolver-provider \
  maven/maven-model-builder \
  org.eclipse.sisu.inject \
  slf4j/api
ant \
  -f %{name}/build.xml \
  -Dtest.skip=true \
  package javadoc

%{mvn_artifact} pom.xml

%{mvn_artifact} %{name}/pom.xml %{name}/target/%{name}-%{version}.jar

%install
%mvn_install -J %{name}/target/site/apidocs
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
