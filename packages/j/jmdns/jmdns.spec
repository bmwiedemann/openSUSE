#
# spec file for package jmdns
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           jmdns
Version:        3.5.7
Release:        0
Summary:        Java implementation of multi-cast DNS
License:        Apache-2.0
URL:            https://github.com/jmdns/jmdns
Source0:        https://github.com/jmdns/jmdns/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
JmDNS is a Java implementation of multi-cast DNS
and can be used for service registration and discovery
in local area networks. JmDNS is fully compatible
with Apple's Bonjour.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
%{summary}.

%prep
%setup -q
chmod -x README.md

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:executions'

%{mvn_alias} :jmdns javax.jmdns:

%build
# Tests are disabled because they try to use network
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
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
