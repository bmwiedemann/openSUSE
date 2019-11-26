#
# spec file for package gmetrics
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


%global oname GMetrics
Name:           gmetrics
Version:        1.0
Release:        0
Summary:        Groovy library that provides reports and metrics for Groovy code
License:        Apache-2.0
URL:            http://gmetrics.sourceforge.net/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires:  mvn(org.codehaus.groovy:groovy)
BuildRequires:  mvn(org.codehaus.groovy:groovy-ant)
BuildRequires:  mvn(org.codehaus.groovy:groovy-xml)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
GMetrics provides calculation and reporting of size and
complexity metrics for Groovy source code, by scanning the
code with an Ant Task, applying a set of metrics, and
generating an HTML or XML report of the results.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin

%pom_remove_plugin :gmaven-plugin
%pom_add_plugin org.codehaus.gmavenplus:gmavenplus-plugin:1.5 . "
 <executions>
  <execution>
   <goals>
    <goal>generateStubs</goal>
    <goal>testGenerateStubs</goal>
   </goals>
  </execution>
 </executions>"

%pom_remove_dep :CodeNarc
%pom_change_dep :log4j org.slf4j:slf4j-api:1.7.25

%pom_xpath_set pom:project/pom:version %{version}

# package org.apache.tools.ant does not exist
%pom_add_dep org.apache.ant:ant:1.9.6 . "<optional>true</optional>"

%{mvn_file} :%{oname} %{name} %{oname}

%build

# test skipped require Codenarc, circular deps
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGELOG.md README.md
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
