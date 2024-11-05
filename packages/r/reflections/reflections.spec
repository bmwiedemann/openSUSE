#
# spec file for package reflections
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


Name:           reflections
Version:        0.10.2
Release:        0
Summary:        Java run-time meta-data analysis
License:        WTFPL
URL:            https://github.com/ronmamo/reflections
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.jboss:jboss-vfs)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildArch:      noarch

%description
A Java run-time meta-data analysis, in the spirit of Scannotations

Reflections scans your class-path, indexes the meta-data, allows you
to query it on run-time and may save and collect that information
for many modules within your project.

Using Reflections you can query your meta-data such as:
* get all sub types of some type
* get all types/methods/fields annotated with some annotation,
  w/o annotation parameters matching
* get all resources matching matching a regular expression

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p1

find -type f '(' -name '*.jar' -o -name '*.class' ')' -not -path './src/test/*' -print -delete

%build
%{mvn_build} -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license COPYING.txt

%files javadoc -f .mfiles-javadoc
%license COPYING.txt

%changelog
