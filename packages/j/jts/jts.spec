#
# spec file for package jts
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


Name:           jts
Version:        1.20.0
Release:        0
Summary:        Java Topology Suite
License:        EPL-1.0
Group:          Development/Libraries/Java
URL:            https://projects.eclipse.org/projects/locationtech.%{name}
Source0:        https://github.com/locationtech/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.googlecode.json-simple:json-simple)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.jdom:jdom2)
BuildArch:      noarch

%description
The LocationTech JTS Topology Suite (JTS) is an open source Java software
library that provides an object model for planar geometry together with a
set of fundamental geometric functions. JTS conforms to the Simple Features
Specification for SQL published by the Open GIS Consortium.  JTS is designed
to be used as a core component of vector-based geomatics software such as
geographical information systems. It can also be used as a general-purpose
library providing algorithms in computational geometry.

%package app
Summary:        JTS Applications & tools
Group:          Development/Libraries/Java

%description app
Applications & tools for working with JTS.

%package example
Summary:        JTS Examples
Group:          Development/Libraries/Java

%description example
Examples of working JTS code.

%package io
Summary:        JTS IO
Group:          Development/Libraries/Java

%description io
Extension to assist in read / write operations.

%package parent
Summary:        JTS Parent POMs
Group:          Development/Libraries/Java

%description parent
Maven POMs for project inheritance.

%package lab
Summary:        JTS Lab
Group:          Development/Libraries/Java

%description lab
Algorithms for JTS which are exploratory or in-progress

%package build-tools
Summary:        JTS Build Tools
Group:          Development/Libraries/Java

%description build-tools
JTS Topology Suite Build Configuration

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains API documentation for %{name}.

%package doc
Summary:        Documentation for %{name}
Group:          Development/Libraries/Java

%description doc
This package contains documentation for %{name}.

%prep
%setup -q

# Uneeded plugins for RPM builds
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-site-plugin

# Don't bundle deps
%pom_remove_plugin :maven-assembly-plugin modules/tests modules/app

# Backward compatibility aliases
%{mvn_alias} org.locationtech.jts:jts-core com.vividsolutions:jts-core com.vividsolutions:jts
%{mvn_alias} org.locationtech.jts.io:jts-io-common com.vividsolutions:jts-io

%{mvn_package} ":jts-io*" jts-io
%{mvn_package} ":jts-lab*" jts-lab
%{mvn_package} ":jts{,-modules}" jts-parent
%{mvn_package} ":jts-tests" jts-app

%build
%{mvn_build} -sfj -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8 org.apache.maven.plugins:maven-javadoc-plugin:aggregate

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
install -dm0755 %{buildroot}%{_defaultdocdir}/%{name}
cp README.md USING.md MIGRATION.md doc/* %{buildroot}%{_defaultdocdir}/%{name}

%files -f .mfiles-%{name}-core
%license LICENSE*

%files app -f .mfiles-%{name}-app

%files example -f .mfiles-%{name}-example

%files io -f .mfiles-%{name}-io

%files lab -f .mfiles-%{name}-lab

%files build-tools -f .mfiles-build-tools

%files parent -f .mfiles-%{name}-parent
%license LICENSE*

%files javadoc -f .mfiles-javadoc
%license LICENSE*

%files doc
%license LICENSE*
%{_defaultdocdir}/%{name}

%changelog
