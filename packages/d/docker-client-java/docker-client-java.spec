#
# spec file for package docker-client-java
#
# Copyright (c) 2021 SUSE LLC
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


Name:           docker-client-java
Version:        8.11.7
Release:        0
Summary:        Docker Client
License:        Apache-2.0
URL:            https://github.com/spotify/docker-client
Source0:        https://github.com/spotify/docker-client/archive/v%{version}.tar.gz
Patch0:         0001-Port-to-latest-version-of-Google-AutoValue.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.datatype:jackson-datatype-guava)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
BuildRequires:  mvn(com.github.jnr:jnr-unixsocket)
BuildRequires:  mvn(com.google.auto.value:auto-value) >= 1.4.1
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.glassfish.hk2:hk2-api)
BuildRequires:  mvn(org.glassfish.jersey.connectors:jersey-apache-connector)
BuildRequires:  mvn(org.glassfish.jersey.core:jersey-client)
BuildRequires:  mvn(org.glassfish.jersey.media:jersey-media-json-jackson)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
The Docker Client is a Java API library for accessing a Docker daemon.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n docker-client-%{version}
%patch0 -p1

# The parent pom doen't add anything we can't live without
%pom_remove_parent
sed -i -e '/<packaging>/a<groupId>com.spotify</groupId>' pom.xml

# Plugins unnecessary for RPM builds
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :jacoco-maven-plugin

# Unnecessary static ananlysis stuff
%pom_remove_dep com.google.code.findbugs:annotations
sed -i -e '/SuppressFBWarnings/d' src/main/java/com/spotify/docker/client/DefaultDockerClient.java \
  src/main/java/com/spotify/docker/client/messages/{Host,Container}Config.java

# Missing dep for google cloud support
%pom_remove_dep :google-auth-library-oauth2-http
rm -rf src/{main,test}/java/com/spotify/docker/client/auth/gcr

# Add dep on hk2 api
%pom_add_dep org.glassfish.hk2:hk2-api

# Generate OSGi metadata
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" pom.xml \
"<configuration>
  <instructions>
    <Bundle-SymbolicName>\${project.groupId}.docker.client</Bundle-SymbolicName>
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
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
