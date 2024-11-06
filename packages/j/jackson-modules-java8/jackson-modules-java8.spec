#
# spec file for package jackson-modules-java8
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


Name:           jackson-modules-java8
Version:        2.17.3
Release:        0
Summary:        Set of support modules for Java 8 datatypes
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/%{name}
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
BuildArch:      noarch

%description
This is a multi-module umbrella project for Jackson modules needed to support
Java 8 features, especially with Jackson 2.x that only requires Java 7 for
running (and until 2.7 only Java 6).

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin de.jjohannes:gradle-module-metadata-maven-plugin

%build
%{mvn_build} -f -- \
	-Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc {SECURITY,README}.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
