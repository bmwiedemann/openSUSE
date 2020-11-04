#
# spec file for package jettison
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


Name:           jettison
Version:        1.3.7
Release:        0
Summary:        A JSON StAX implementation
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://jettison.codehaus.org/
Source0:        https://github.com/codehaus/jettison/archive/%{name}-%{version}.tar.gz
# Change the POM to use the version of woodstox that we have available:
Patch0:         %{name}-update-woodstox-version.patch
Patch1:         %{name}-1.3.7-jdk10plus.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.codehaus:codehaus-parent:pom:)
BuildRequires:  mvn(stax:stax-api)
BuildArch:      noarch

%description
Jettison is a collection of Java APIs (like STaX and DOM) which read
and write JSON. This allows nearly transparent enablement of JSON based
web services in services frameworks like CXF or XML serialization
frameworks like XStream.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch1 -p1
chmod -x src/main/resources/META-INF/LICENSE
# We don't need wagon-webdav
%pom_xpath_remove pom:build/pom:extensions

%pom_remove_plugin :maven-release-plugin

# Confuses maven-bundle-plugin
%pom_xpath_remove pom:Private-Package

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license src/main/resources/META-INF/LICENSE

%files javadoc -f .mfiles-javadoc
%license src/main/resources/META-INF/LICENSE

%changelog
