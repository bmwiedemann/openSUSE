#
# spec file for package jsonp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jsonp
Version:        1.0.4
Release:        0
Summary:        JSR 353 (JSON Processing) RI
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://github.com/javaee/%{name}
Source0:        https://github.com/javaee/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/javaee/%{name}/master/LICENSE.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(javax.ws.rs:javax.ws.rs-api)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
BuildArch:      noarch

%description
JSR 353: Java API for Processing JSON RI.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} .
find . -name '*.jar' -delete
find . -name '*.class' -delete
# Unwanted old apis
%pom_disable_module bundles
%pom_disable_module demos
%pom_disable_module gf
%pom_disable_module tests

%pom_remove_dep javax:javaee-web-api

%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin org.codehaus.mojo:wagon-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-dependency-plugin impl

# disabled source and javadoc jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-jar-plugin impl
%pom_remove_plugin :maven-javadoc-plugin impl
%pom_remove_plugin :maven-source-plugin impl
%pom_remove_plugin :maven-javadoc-plugin jaxrs

sed -i '/check-module/d' api/pom.xml impl/pom.xml

# disable apis copy
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-bundle-plugin']/pom:configuration/pom:instructions/pom:Export-Package"  impl
# Make the api dependency non-optional
%pom_xpath_remove "pom:dependency/pom:optional" impl

%pom_xpath_set "pom:parent/pom:version" %{version} api
%pom_xpath_set "pom:parent/pom:version" %{version} jaxrs

%{mvn_file} :javax.json-api %{name}/%{name}-api
%{mvn_file} :javax.json %{name}/%{name}
%{mvn_file} :%{name}-jaxrs %{name}/%{name}-jaxrs

%build

%{mvn_build} -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
