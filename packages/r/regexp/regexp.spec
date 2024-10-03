#
# spec file for package regexp
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2000-2008, JPackage Project
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


%define full_name       jakarta-%{name}
Name:           regexp
Version:        1.5
Release:        0
Summary:        Simple regular expressions API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://jakarta.apache.org/%{name}/
Source0:        http://www.apache.org/dist/jakarta/regexp/jakarta-regexp-%{version}.tar.gz
Source1:        regexp-%{version}.pom
BuildRequires:  ant >= 1.6
BuildRequires:  java-devel
BuildRequires:  javapackages-local >= 6
BuildRequires:  xml-commons-apis-bootstrap
#!BuildIgnore:  xerces-j2
#!BuildIgnore:  xml-commons
#!BuildIgnore:  xml-commons-apis
#!BuildIgnore:  xml-commons-jaxp-1.3-apis
#!BuildIgnore:  xml-commons-resolver
BuildArch:      noarch

%description
Regexp is a 100% Pure Java Regular Expression package that was
graciously donated to the Apache Software Foundation by Jonathan Locke.
He originally wrote this software back in 1996 and it has stood up
quite well to the test of time. It includes complete Javadoc
documentation as well as a simple Applet for visual debugging and
testing suite for compatibility.

%prep
%setup -q -n %{full_name}-%{version}
# remove all binary libs
find . -type f -name "*.jar" | xargs -t rm

%build
mkdir lib
ant -Djakarta-site2.dir=. -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  jar

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 build/*.jar %{buildroot}%{_javadir}/%{name}.jar
[ -d docs/api ] && rm -rf docs/api
# pom
mkdir -p %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a %{full_name}:%{full_name}

%files -f .mfiles
%license LICENSE

%changelog
