#
# spec file for package javaparser
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


Name:           javadoc-parser
Version:        0.3.1
Release:        0
Summary:        Java library for parsing information from a structured Javadoc string
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/chhorz/javadoc-parser
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
BuildRequires:  fdupes ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
This library provides a parsing mechanism for Javadoc comments
within java files.
To get the parsing mechanism work properly the Javadoc comment
has to follow a specific structure. The structure should be as
close as possible to the Writers Guide from Oracle.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} %{name}/build.xml

%build
pushd %{name}
%ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{name}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{name}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r %{name}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.adoc
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
