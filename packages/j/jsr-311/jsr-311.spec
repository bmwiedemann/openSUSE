#
# spec file for package jsr-311
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


%global oname jsr311-api
Name:           jsr-311
Version:        1.1.1
Release:        0
Summary:        JAX-RS: Java API for RESTful Web Services
License:        CDDL-1.0
Group:          Development/Libraries/Java
URL:            http://jsr311.java.net
Source0:        https://github.com/javaee/jsr311/archive/%{oname}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Provides:       javax.ws.rs
BuildArch:      noarch

%description
JAX-RS: Java API for RESTful Web Services

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jsr311-%{oname}-%{version}

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "///pom:extensions/pom:extension[pom:artifactId='wagon-svn']"

%build

%{mvn_file} :jsr311-api %{name} javax.ws.rs/%{name}
%{mvn_build} -f -- -Dproject.build.sourceEncoding=UTF-8 \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%dir %{_javadir}/javax.ws.rs/

%files javadoc -f .mfiles-javadoc

%changelog
