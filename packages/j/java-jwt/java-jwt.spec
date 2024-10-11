#
# spec file for package java-jwt
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           java-jwt
Version:        4.4.0
Release:        0
Summary:        Java JWT
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/auth0/%{name}
Source0:        https://github.com/auth0/%{name}/archive/%{version}.tar.gz
Source1:        %{name}-build.xml
Source2:        https://repo1.maven.org/maven2/com/auth0/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jackson-annotations
BuildRequires:  jackson-core
BuildRequires:  jackson-databind
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Java implementation of JSON Web Token (JWT)

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for the Logback library

%prep
%setup -q
cp %{SOURCE1} lib/build.xml

%build
mkdir -p lib/lib
build-jar-repository -s lib/lib jackson-annotations jackson-core jackson-databind
ant -f lib/build.xml jar javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 lib/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

install -dm 0755 %{buildroot}%{_javadocdir}
cp -r lib/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
