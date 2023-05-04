#
# spec file for package google-errorprone
#
# Copyright (c) 2023 SUSE LLC
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


%global source_name error-prone
Name:           google-errorprone
Version:        2.11.0
Release:        0
Summary:        Google Error Prone
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://errorprone.info
Source0:        %{source_name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.auto.service:auto-service)
BuildRequires:  mvn(com.google.auto.service:auto-service-annotations)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.errorprone:error_prone_annotations)
BuildRequires:  mvn(com.google.guava:guava)
BuildArch:      noarch

%description
Error Prone is a static analysis tool for Java that catches
common programming mistakes at compile-time.

%package annotation
Summary:        @BugPattern annotation
Group:          Development/Libraries/Java

%description annotation
@BugPattern annotation for Google Error Prone

%package docgen_processor
Summary:        @BugPattern annotation processor
Group:          Development/Libraries/Java

%description docgen_processor
JSR-269 annotation processor for @BugPattern annotation

%package type_annotations
Summary:        error-prone type annotations
Group:          Development/Libraries/Java

%description type_annotations
Google Error Prone type annotations

%package parent
Summary:        Error Prone parent POM
Group:          Development/Libraries/Java

%description parent
Error Prone is a static analysis tool for Java that catches
common programming mistakes at compile-time.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{source_name}-%{version}
# already built with different spec
%pom_disable_module annotations
# Disable modules that we cannot build because of dependencies
%pom_disable_module check_api
%pom_disable_module test_helpers
%pom_disable_module core
%pom_disable_module docgen
%pom_disable_module refaster

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin

%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:compilerArgs"
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 8
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 8

%{mvn_package} ":error_prone_{*}" @1
%{mvn_file} ":error_prone_{*}" %{name}/@1

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files annotation -f .mfiles-annotation
%license COPYING

%files docgen_processor -f .mfiles-docgen_processor
%license COPYING

%files type_annotations -f .mfiles-type_annotations
%license COPYING

%files parent -f .mfiles-parent
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING
%doc README.md

%changelog
