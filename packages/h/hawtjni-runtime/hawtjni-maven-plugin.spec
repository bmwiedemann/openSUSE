#
# spec file for package hawtjni-maven-plugin
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


%global base_name hawtjni
# That is the maven-release-plugin generated commit, but it's not tagged for some reason
# https://github.com/fusesource/hawtjni/issues/46
%global commit    fa1fd5dfdd0a1a5a67b61fa7d7ee7126b300c8f0
Name:           hawtjni-maven-plugin
Version:        1.16
Release:        0
Summary:        Use HawtJNI from a maven plugin
License:        Apache-2.0 AND EPL-1.0 AND BSD-3-Clause
URL:            https://github.com/fusesource/hawtjni
Source0:        https://github.com/fusesource/hawtjni/archive/%{commit}/hawtjni-%{commit}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-generator) >= %{version}
BuildRequires:  mvn(org.fusesource:fusesource-pom:pom:)
BuildArch:      noarch

%description
HawtJNI is a code generator that produces the JNI code needed to
implement java native methods. It is based on the jnigen code generator
that is part of the SWT Tools project which is used to generate all the
JNI code which powers the eclipse platform.

This package allows to use HawtJNI from a maven plugin.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n hawtjni-%{commit}

# We build only the maven plugin in this one
%pom_disable_module hawtjni-example
%pom_disable_module hawtjni-generator
%pom_disable_module hawtjni-runtime

%pom_remove_plugin -r :maven-eclipse-plugin

%{mvn_package} :hawtjni-project __noinstall

%{mvn_alias} :hawtjni-maven-plugin :maven-hawtjni-plugin

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license license.txt
%doc readme.md changelog.md

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
