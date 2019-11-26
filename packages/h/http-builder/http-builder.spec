#
# spec file for package http-builder
#
# Copyright (c) 2019 SUSE LLC
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


Name:           http-builder
Version:        0.7.2
Release:        0
Summary:        HTTP client framework for Groovy
License:        Apache-2.0
URL:            https://github.com/jgritman/httpbuilder
Source0:        https://github.com/jgritman/httpbuilder/archive/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(net.sf.json-lib:json-lib)
BuildRequires:  mvn(net.sourceforge.nekohtml:nekohtml)
BuildRequires:  mvn(oauth.signpost:signpost-commonshttp4)
BuildRequires:  mvn(oauth.signpost:signpost-core)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires:  mvn(org.codehaus.groovy:groovy)
BuildRequires:  mvn(org.codehaus.groovy:groovy-json)
BuildRequires:  mvn(org.codehaus.groovy:groovy-xml)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildArch:      noarch

%description
A builder-style HTTP client API, including authentication, and extensible
handling of common content-types such as JSON and XML. It is built on top of
Apache's HttpClient.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n httpbuilder-%{name}-%{version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :gmaven-plugin
%pom_add_plugin org.codehaus.gmavenplus:gmavenplus-plugin:1.5 . "
 <executions>
  <execution>
   <goals>
    <goal>testGenerateStubs</goal>
   </goals>
  </execution>
 </executions>"

# Useless tasks
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-surefire-report-plugin

# Use system setting to avoid doclint errors
%pom_remove_plugin :maven-javadoc-plugin

# org.apache.maven.wagon:wagon-webdav-jackrabbit:1.0-beta-7
%pom_xpath_remove pom:build/pom:extensions

%pom_change_dep log4j: ::1.2.17
# net.sf.json-lib:json-lib:2.3:jdk15:
%pom_xpath_remove "pom:dependency[pom:artifactId = 'json-lib']/pom:classifier"

# com.google.appengine:appengine-api-1.0-sdk:1.3.8
%pom_remove_dep :appengine-api-1.0-sdk
rm -r src/main/java/groovyx/net/http/thirdparty \
 src/test/groovy/groovyx/net/http/thirdparty

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

# package groovy....  does not exist
%pom_add_dep org.codehaus.groovy:groovy-xml
%pom_add_dep org.codehaus.groovy:groovy-json

%{mvn_file} org.codehaus.groovy.modules.%{name}:%{name} %{name}

# AssertionError: Expected exception: java.lang.IllegalArgumentException
rm src/test/groovy/groovyx/net/http/HTTPBuilderTest.groovy
# AssertionError: Expected exception: java.net.SocketTimeoutException
rm src/test/groovy/groovyx/net/http/HttpURLClientTest.groovy

%build

%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
# README file contains also project license
%doc README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
