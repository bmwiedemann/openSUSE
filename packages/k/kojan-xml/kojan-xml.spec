#
# spec file for package kojan-xml
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_with bootstrap
Name:           kojan-xml
Version:        1.0.1
Release:        0
Summary:        Java library for modeling data in XML format
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/mizdebsk/kojan-xml
Source0:        https://github.com/mizdebsk/kojan-xml/archive/refs/tags/1.0.1.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 11
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
The Kojan XML library is used to model data according to the
entity–relationship (ER) model and write and read data in XML
format. It allows you to define data entities with their properties,
such as attributes and relationships, and serialize and deserialize
data in XML format.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

%build
ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
