#
# spec file for package glassfish-websocket-api
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


%global base_name websocket-api
Name:           glassfish-%{base_name}
Version:        1.1
Release:        0
Summary:        JSR 356: Java API for WebSocket
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://github.com/javaee/websocket-spec/
Source0:        %{base_name}-%{version}.tar.xz
Source1:        https://raw.githubusercontent.com/javaee/websocket-spec/master/LICENSE
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  xz
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
Conflicts:      jboss-websocket-1.0-api
BuildArch:      noarch

%description
Java API for WebSocket JSR will define a standard API for
creating web socket applications.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n websocket-api-%{version}

cp %{SOURCE1} .

find  -name "*.class"  -print -delete
find  -name "*.jar"  -print -delete

%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-release-plugin

%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-dependency-plugin server
%pom_remove_plugin :maven-jar-plugin server

%pom_xpath_set "pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.8
%pom_xpath_set "pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.8

%pom_xpath_set "pom:packaging" bundle client
%pom_xpath_inject "pom:project" "<version>%{version}</version>" client
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 client '
<extensions>true</extensions>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

chmod 644 etc/config/copyright.txt

sed -i '/check-module/d' server/pom.xml

%{mvn_file} :javax.websocket-api %{name}
%{mvn_file} :javax.websocket-client-api glassfish-websocket-client-api

%build

%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
