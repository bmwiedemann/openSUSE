#
# spec file for package jsoup
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


Name:           jsoup
Version:        1.15.3
Release:        0
Summary:        Java library for working with HTML
License:        MIT
Group:          Development/Libraries/Java
URL:            https://jsoup.org/
# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  jsr-305
BuildArch:      noarch

%description
jsoup is a Java library for working with HTML.
It provides an API for extracting and manipulating data,
using DOM, CSS, and jquery-like methods.

jsoup implements the WHATWG HTML5 specification.

 - scrapes and parses HTML from a URL, file, or string
 - finds and extracts data, using DOM traversal or CSS selectors
 - manipulates the HTML elements, attributes, and text
 - cleans user-submitted content against a safe white-list,
   to prevent XSS attacks
 - outputs tidied HTML

jsoup can deal with invalid HTML tag soup.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} .

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :maven-failsafe-plugin

%build
mkdir -p lib
build-jar-repository -s lib jsr-305
%{ant} -f %{name}-build.xml jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
install -pdm 0755 target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md CHANGES
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
