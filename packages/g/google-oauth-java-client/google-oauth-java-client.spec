#
# spec file for package google-oauth-java-client
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


%bcond_with dnplugin
Name:           google-oauth-java-client
Version:        1.22.0
Release:        0
Summary:        Google OAuth Client Library for Java
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/google-oauth-java-client
Source0:        https://github.com/google/google-oauth-java-client/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.http-client:google-http-client)
BuildRequires:  mvn(com.google.http-client:google-http-client-jdo)
BuildRequires:  mvn(javax.jdo:jdo2-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch
%if %{with dnplugin}
BuildRequires:  mvn(org.datanucleus:datanucleus-maven-plugin)
%endif

%description
Google OAuth Client Library for Java. Functionality that
works on all supported Java platforms, including Java 5
(or higher) desktop (SE) and web (EE), Android, and
Google App Engine.

%package java6
Summary:        Google OAuth Client Java 6 extensions
Group:          Development/Libraries/Java

%description java6
Java 6 (and higher) extensions to the
Google OAuth Client Library for Java.

%package parent
Summary:        Google OAuth Client Parent POM
Group:          Development/Libraries/Java

%description parent
Parent POM for the Google OAuth Client Library for Java.

%package servlet
Summary:        Google OAuth Client Servlet and JDO extensions
Group:          Development/Libraries/Java

%description servlet
Servlet and JDO extensions to the
Google OAuth Client Library for Java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :clirr-maven-plugin
%pom_remove_plugin -r :findbugs-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-source-plugin
# duplicate declaration
%pom_remove_plugin -r :maven-release-plugin

%pom_disable_module google-oauth-client-assembly
# com.google.appengine:appengine-{api-1.0-sdk,testing,api-stubs}:1.7.7
%pom_disable_module google-oauth-client-appengine

# org.mortbay.jetty:jetty
%pom_disable_module google-oauth-client-jetty

%pom_disable_module samples/dailymotion-cmdline-sample

%pom_change_dep -r :guava-jdk5 :guava
%pom_change_dep -r :servlet-api :javax.servlet-api:3.1.0

%if %{without dnplugin}
%pom_remove_plugin org.datanucleus:maven-datanucleus-plugin google-oauth-client-servlet
%else
# Generate:
# ENHANCED (PersistenceCapable) : com.google.api.client.extensions.auth.helpers.oauth.OAuthHmacThreeLeggedFlow
# ENHANCED (PersistenceCapable) : com.google.api.client.extensions.auth.helpers.oauth.OAuthHmacCredential
# Upgrade datanucleus-maven-plugin refs
%pom_xpath_set "pom:plugin[pom:groupId='org.datanucleus']/pom:artifactId" datanucleus-maven-plugin google-oauth-client-servlet
# Fix datanucleus-maven-plugin runtime deps
# Error: Could not find or load main class org.datanucleus.enhancer.DataNucleusEnhancer
%pom_xpath_inject "pom:plugin[pom:groupId='org.datanucleus']" "
<dependencies>
    <dependency>
      <groupId>org.datanucleus</groupId>
      <artifactId>datanucleus-core</artifactId>
      <version>3.2.9</version>
    </dependency>
    <dependency>
      <groupId>org.datanucleus</groupId>
      <artifactId>datanucleus-api-jdo</artifactId>
      <version>3.2.6</version>
    </dependency>
</dependencies>" google-oauth-client-servlet
# Class "com.google.api.client.extensions.auth.helpers.oauth.OAuthHmacThreeLeggedFlow"
# field "authorizationUrl" : marked as persistent yet is final so cannot be persisted
#sed -i "s|private final String authorizationUrl;|private String authorizationUrl;|" \
# google-oauth-client-servlet/src/main/java/com/google/api/client/extensions/auth/helpers/oauth/OAuthHmacThreeLeggedFlow.java
%endif

%pom_xpath_remove -r "pom:plugin[pom:artifactId ='maven-jar-plugin']/pom:executions"

%build

%{mvn_build} -s -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-google-oauth-client
%doc README.md
%license LICENSE

%files java6 -f .mfiles-google-oauth-client-java6

%files parent -f .mfiles-google-oauth-client-parent
%license LICENSE

%files servlet -f .mfiles-google-oauth-client-servlet

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
