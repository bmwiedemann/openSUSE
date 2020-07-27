#
# spec file for package jnr-unixsocket
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


Name:           jnr-unixsocket
Version:        0.21
Release:        0
Summary:        Unix sockets for Java
License:        Apache-2.0
URL:            https://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-constants)
BuildRequires:  mvn(com.github.jnr:jnr-enxio)
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(com.github.jnr:jnr-posix)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Unix sockets for Java.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

# remove unnecessary wagon extension
%pom_xpath_remove pom:build/pom:extensions

# Unnecessary for RPM builds
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-javadoc-plugin

# Can't run integration tests
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :exec-maven-plugin

# Remove enxio classes to avoid OSGi split-package problems,
# see https://github.com/jnr/jnr-unixsocket/pull/41
rm -r src/main/java/jnr/enxio

# Fix jar plugin usage
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions"

%build
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
