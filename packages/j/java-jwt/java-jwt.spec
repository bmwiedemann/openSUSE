#
# spec file for package java-jwt
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


Name:           java-jwt
Version:        3.8.3
Release:        0
Summary:        Java JWT
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/auth0/%{name}
Source0:        https://github.com/auth0/%{name}/archive/%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/com/auth0/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(commons-codec:commons-codec)
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
cp %{SOURCE1} lib/pom.xml

%pom_xpath_remove pom:dependency/pom:scope lib

%build
pushd lib
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=7 \
%endif
	-Dmaven.compiler.source=7 -Dmaven.compiler.target=7 -Dsource=7
popd

%install
pushd lib
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f lib/.mfiles
%license LICENSE
%doc README.md

%files javadoc -f lib/.mfiles-javadoc
%license LICENSE

%changelog
