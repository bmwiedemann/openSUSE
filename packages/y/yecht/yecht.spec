#
# spec file for package yecht
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


%global cluster jruby
Name:           yecht
Version:        1.1
Release:        0
Summary:        A YAML processor based on Syck
License:        MIT
URL:            https://github.com/%{cluster}/%{name}
Source0:        https://github.com/%{cluster}/%{name}/archive/%{name}-%{version}.zip
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Yecht is a Syck port, a YAML 1.0 processor for Ruby.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find ./ -name '*.jar' -exec rm -f '{}' \;
find ./ -name '*.class' -exec rm -f '{}' \;

%pom_remove_dep org.jruby:jruby-core

%pom_remove_plugin :build-helper-maven-plugin
%pom_xpath_remove pom:build/pom:resources

# With removal of the jruby dependency, the normal jar and the
# one with jruby classifier are identical. So don't build both,
# just alias one artifact to the other
%pom_remove_plugin :maven-jar-plugin
%{mvn_alias} :::: :::jruby:

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
