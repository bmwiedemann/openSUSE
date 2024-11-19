#
# spec file for package jcache
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


Name:           jcache
Version:        1.1.1
Release:        0
Summary:        JSR107 Cache Specification
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/jsr107/jsr107spec
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
JCache is the Java caching API. It was defined by JSR107. It defines a standard
Java Caching API for use by developers and a standard SPI (“Service Provider
Interface”) for use by implementers.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n jsr107spec-%{version}
%pom_xpath_set 'pom:plugin[pom:artifactId/text()="maven-compiler-plugin"]/pom:configuration/pom:source' '1.8'
%pom_xpath_set 'pom:plugin[pom:artifactId/text()="maven-compiler-plugin"]/pom:configuration/pom:target' '1.8'
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
