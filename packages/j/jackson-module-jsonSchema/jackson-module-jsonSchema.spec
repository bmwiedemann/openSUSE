#
# spec file for package jackson-module-jsonSchema
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


Name:           jackson-module-jsonSchema
Version:        2.17.3
Release:        0
Summary:        Jackson module for JSON Schema 3 generation
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/%{name}
Source0:        %{url}/archive/refs/tags/%{name}-parent-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires:  mvn(jakarta.validation:jakarta.validation-api)
BuildRequires:  mvn(javax.validation:validation-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
BuildArch:      noarch

%description
Add-on module for Jackson to support JSON Schema version 3 generation.

%package jakarta
Summary:        Jackson module for JSON Schema 3 generation (Jakarta APIs)

%description jakarta
Add-on module for Jackson to support JSON Schema version 3 generation.
This module contains the newer "jakarta" APIs

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{name}-parent-%{version}
cp %{SOURCE1} LICENSE

%pom_remove_plugin -r de.jjohannes:gradle-module-metadata-maven-plugin

%{mvn_file} :{*} jackson-modules/@1
%{mvn_package} :{*}-parent __noinstall
%{mvn_package} :{*}-jakarta jakarta

%build
%{mvn_build} -f -- \
	-Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc README.md

%files jakarta -f .mfiles-jakarta
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
