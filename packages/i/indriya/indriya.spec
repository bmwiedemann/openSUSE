#
# spec file for package indriya
#
# Copyright (c) 2022 SUSE LLC
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


Name:           indriya
Version:        1.3
Release:        0
Summary:        Next Generation Units of Measurement Implementation
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/unitsofmeasurement/%{name}
Source0:        https://github.com/unitsofmeasurement/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(javax.measure:unit-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(tech.uom.lib:uom-lib-common)
BuildRequires:  mvn(tech.uom:uom-parent:pom:)
BuildArch:      noarch

%description
Units of Measurement Libraries - JSR 385 Reference Implementation

%package common
Summary:        Java Units of Measurement Common Library
Group:          Development/Libraries/Java

%description common
Units of Measurement Common Library - extending and complementing JSR 363.

%package javadoc
Summary:        Javadoc for the Units of Measurement Libraries
Group:          Documentation/HTML

%description javadoc
%{summary}

%prep
%setup -q

%build
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-surefire-plugin
%pom_remove_plugin :maven-source-plugin

find . -name "*.java" | xargs sed -i s,'tec.uom.lib.common','tech.uom.lib.common',g

%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
