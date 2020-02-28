#
# spec file for package uima-parent-pom
#
# Copyright (c) 2020 SUSE LLC
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


Name:           uima-parent-pom
Version:        10
Release:        0
Summary:        Apache UIMA Parent POM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://uima.apache.org/
Source0:        https://github.com/apache/uima-build/archive/parent-pom-%{version}.tar.gz
# uima-parent-pom package don't include the license file
# reported @ https://issues.apache.org/jira/browse/UIMA-3575
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(jakarta-regexp:jakarta-regexp)
BuildRequires:  mvn(org.apache.ant:ant-apache-regexp)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildArch:      noarch

%description
UIMA (Unstructured Information Management Architecture).
UIMA promotes community development and reuse of annotators
that extract meta-data from unstructured information (text,
audio, video, etc.); it provides for externalized declaration of
type systems, component configuration, aggregation, and more,
supports scalablity, and provides tooling.

This package provides Parent for Apache UIMA Projects.

%prep
%setup -q -n uima-build-parent-pom-%{version}

%pom_xpath_remove pom:Embed-Dependency
%pom_xpath_remove pom:Embed-Directory
%pom_xpath_remove pom:Bundle-ClassPath
%pom_xpath_set pom:Include-Resource '{maven-resources}'
# Deprecated entry
%pom_xpath_remove pom:Bundle-RequiredExecutionEnvironment

%pom_remove_plugin org.apache.uima:uima-build-helper-maven-plugin
%pom_remove_plugin com.agilejava.docbkx:docbkx-maven-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-javadoc-plugin

# unavailable deps org.apache.uima:uima-docbook-olink:zip:olink:1-SNAPSHOT
# https://svn.apache.org/repos/asf/uima/build/trunk/uima-docbook-olink/
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'process-docbook']"
# Unavailable deps
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'build-eclipse-update-subsite']"
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'build distribution']"

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt README.txt

%build
%{mvn_build}

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%license LICENSE-2.0.txt

%changelog
