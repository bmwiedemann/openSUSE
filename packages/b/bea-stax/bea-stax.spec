#
# spec file for package bea-stax
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


%global apiver  1.0.1
Name:           bea-stax
Version:        1.2.0
Release:        0
Summary:        Streaming API for XML
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://stax.codehaus.org/Home
Source0:        https://repo.maven.apache.org/maven2/stax/stax-src/%{version}/stax-src-%{version}.distribution-zip#/stax-src-%{version}.zip
Source1:        https://repo.maven.apache.org/maven2/stax/stax/%{version}/stax-%{version}.pom
Source2:        https://repo.maven.apache.org/maven2/stax/stax-api/%{apiver}/stax-api-%{apiver}.pom
Patch0:         bea-stax-target8.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
BuildRequires:  xml-apis
BuildRequires:  xml-resolver
#!BuildIgnore:  antlr
#!BuildIgnore:  antlr-java
Requires:       %{name}-api = %{version}-%{release}
BuildArch:      noarch

%description
The Streaming API for XML (StAX) is Java API for
parsing and writing XML easily and efficiently.

%package api
Summary:        The StAX API
Group:          Development/Libraries/Java

%description api
The Streaming API for XML (StAX) is Java API for
parsing and writing XML easily and efficiently.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
%{name} API documentation.

%prep
%setup -q -c
%patch -P 0

%build
ant all javadoc

%install
# jar
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 build/stax-api-%{apiver}.jar %{buildroot}%{_javadir}/%{name}-api.jar
install -p -m 0644 build/stax-%{version}-dev.jar %{buildroot}%{_javadir}/%{name}-ri.jar
# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}-ri.pom
%add_maven_depmap %{name}-ri.pom %{name}-ri.jar
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}-api.pom
%add_maven_depmap %{name}-api.pom %{name}-api.jar -f api -a javax.xml.stream:stax-api
# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r build/javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license ASF2.0.txt

%files api -f .mfiles-api
%license ASF2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%license ASF2.0.txt

%changelog
