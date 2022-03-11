#
# spec file for package jaxb-api
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


%global artifact_name jakarta.xml.bind-api
Name:           jaxb-api
Version:        4.0.0
Release:        0
Summary:        Jakarta XML Binding API
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-api
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jakarta-activation
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
The Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q

pushd api
cp %{SOURCE1} build.xml

%pom_remove_parent
%pom_xpath_inject pom:project "
    <groupId>jakarta.xml.bind</groupId>
    <version>%{version}</version>"
popd

%build
pushd api
mkdir -p lib
build-jar-repository -s lib jakarta-activation
%{ant} jar javadoc
popd

%install
# jar
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -m 644 api/target/%{artifact_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{artifact_name}.jar

#pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -m 644 api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifact_name}.pom
%add_maven_depmap %{name}/%{artifact_name}.pom %{name}/%{artifact_name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr api/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.md NOTICE.md

%changelog
