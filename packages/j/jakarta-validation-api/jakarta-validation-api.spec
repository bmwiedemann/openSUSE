#
# spec file for package jakarta-validation-api
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


%global base_name validation
Name:           jakarta-%{base_name}-api
Version:        3.1.0
Release:        0
Summary:        Jakarta Validation API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://beanvalidation.org
Source0:        https://github.com/jakartaee/%{base_name}/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Jakarta Validation defines a metadata model and API for JavaBean and method validation.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{base_name}-%{version}
cp %{SOURCE1} build.xml

%build
ant package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/jakarta.validation-api-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license license.txt NOTICE.md
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license license.txt NOTICE.md

%changelog
