#
# spec file for package apache-logging-parent
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


%global short_name logging-parent
Name:           apache-%{short_name}
Version:        12.1.1
Release:        0
Summary:        Parent pom for Apache Logging Services projects
License:        Apache-2.0
URL:            https://logging.apache.org/
Source0:        https://archive.apache.org/dist/logging/%{short_name}/%{version}/%{name}-%{version}-src.zip
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildArch:      noarch

%description
Parent pom for Apache Logging Services projects.

%prep
%setup -q -c
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :xml-maven-plugin
%pom_remove_plugin :flatten-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin
%pom_remove_plugin :maven-clean-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :spotless-maven-plugin
%pom_remove_plugin :apache-rat-plugin

# We don't have com.google.errorprone:error_prone_core and we don't
# need static analysis checks running during the compilation phase
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:compilerArgs"
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:annotationProcessorPaths"

%pom_xpath_set pom:project/pom:version %{version}

%build
%{mvn_build} -jf

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%changelog
