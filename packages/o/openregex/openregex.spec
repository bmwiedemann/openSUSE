#
# spec file for package openregex
#
# Copyright (c) 2024 SUSE LLC
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           openregex
Version:        1.1.1
Release:        0
Summary:        OpenRegex regular expressions library
License:        LGPL-3.0-only
URL:            https://github.com/knowitall/%{name}
Source0:        https://github.com/knowitall/%{name}/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
OpenRegex is an efficient and flexible library for running regular expressions
over sequences of user-defined objects.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

# Needed only to build tests which we skip
%pom_remove_plugin :scala-maven-plugin

%build
%{mvn_build} -f -- \
	-Dmaven.compiler.release=8 \
	-Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
