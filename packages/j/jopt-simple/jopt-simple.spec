#
# spec file for package jopt-simple
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


Name:           jopt-simple
Version:        5.0.4
Release:        0
Summary:        A Java command line parser
License:        MIT
URL:            https://jopt-simple.github.io/jopt-simple
Source0:        https://github.com/jopt-simple/jopt-simple/archive/jopt-simple-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
JOpt Simple is a Java library for parsing command line options, such as those
you might pass to an invocation of javac.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_dep org.infinitest:continuous-testing-toolkit
%pom_remove_plugin org.pitest:pitest-maven
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-source-plugin

%build
# Unit testing is disabled due to a missing dependency of continuous-testing-toolkit
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
