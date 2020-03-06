#
# spec file for package uom-lib
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


Name:           uom-lib
Version:        1.2
Release:        0
Summary:        Java Unit of Measurement Libraries (JSR 363)
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/unitsofmeasurement/uom-lib
Source0:        https://github.com/unitsofmeasurement/uom-lib/archive/%{version}/uom-lib-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  mvn(javax.measure:unit-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(tech.uom:uom-parent:pom:)
#!BuildIgnore:  java-1_7_0-openjdk
#!BuildIgnore:  java-1_7_0-openjdk-devel
#!BuildIgnore:  java-1_7_0-openjdk-headless
#!BuildIgnore:  java-1_8_0-openjdk
#!BuildIgnore:  java-1_8_0-openjdk-devel
#!BuildIgnore:  java-1_8_0-openjdk-headless
BuildArch:      noarch

%description
Units of Measurement Libraries - extending and complementing JSR 363.

%package assertj
Summary:        Java Units of Measurement AssertJ Library
Group:          Development/Libraries/Java

%description assertj
Units of Measurement AssertJ Library - extending and complementing JSR 363.

%package common
Summary:        Java Units of Measurement Common Library
Group:          Development/Libraries/Java

%description common
Units of Measurement Common Library - extending and complementing JSR 363.

%package jackson
Summary:        Java Units of Measurement Jackson Library
Group:          Development/Libraries/Java

%description jackson
Units of Measurement Jackson Library - extending and complementing JSR 363.

%package javadoc
Summary:        Javadoc for the Units of Measurement Libraries
Group:          Documentation/HTML

%description javadoc
This package contains documentation for the Units of Measurement
Libraries (JSR 363).

%prep
%setup -q
# we don't have all dependencies to build this module
%pom_disable_module jackson

%build
%{mvn_build} -f -s \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=8
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-uom-lib
%license LICENSE

%files assertj -f .mfiles-uom-lib-assertj
%license LICENSE

%files common -f .mfiles-uom-lib-common
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
