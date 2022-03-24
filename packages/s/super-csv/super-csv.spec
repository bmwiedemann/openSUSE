#
# spec file for package super-csv
#
# Copyright (c) 2022 SUSE LLC
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


Name:           super-csv
Version:        2.4.0
Release:        0
Summary:        A CSV library for Java
License:        Apache-2.0
URL:            https://super-csv.github.io/super-csv/
Source:         https://github.com/super-csv/super-csv/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/super-csv/super-csv/pull/169
Patch0:         jdk6.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
A library for reading and writing CSV files with Java.

It supports reading and writing with POJOs, Maps and Lists. It also
has support for deep-mapping and index-based mapping with POJOs.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%autosetup -p1

# Remove pre-built binaries
find -name '*.class' -print -delete
find -name '*.jar' -print -delete

# missing dependency
%pom_disable_module super-csv-dozer

# error: package org.joda.time does not exist even when supplied
%pom_disable_module super-csv-joda

# unavailable plugins
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :cobertura-maven-plugin
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-scm-publish-plugin
%pom_remove_plugin -r :maven-site-plugin

# Empty artifact, only for testing
%pom_disable_module %{name}-benchmark

%pom_disable_module %{name}-distribution

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
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
